from pathlib import Path

import torch
from torch.nn.functional import grid_sample, affine_grid

import fire


def transform(img, grid, mode, align_corners):
    return grid_sample(img, grid, align_corners=align_corners, mode=mode)


def store_expected(tensor, output, output_path, seed, mf, c, dtype, size, grid, mode, ac, non_contig):
    if not output_path.exists():
        output_path.mkdir(parents=True)
    bs = len(tensor)
    filepath = output_path / f"{seed}_{bs}_{mf}_{c}_{dtype}_{size[0]}_{size[1]}_{mode}_{ac}_{non_contig}.pt"
    torch.save(
        {"input": tensor, "output": output, "torch_version": torch.__version__},
        filepath
    )


def get_expected(tensor, output_path, seed, mf, c, dtype, size, grid, mode, ac, non_contig):
    bs = len(tensor)
    filepath = output_path / f"{seed}_{bs}_{mf}_{c}_{dtype}_{size[0]}_{size[1]}_{mode}_{ac}_{non_contig}.pt"
    obj = torch.load(filepath)
    inpt = obj["input"]
    torch.testing.assert_close(inpt, tensor)
    return obj["output"]


def test_consistency_or_record(
    tensor, c, size, mf, dtype, grid, mode, ac, is_ref, output_path, seed,
    exact_match=True,
    record_path={
        torch.float32: "native",
        torch.float64: "native",
    },
    non_contig=False,
):
    # Tested op -> output
    if is_ref:

        if non_contig is not False:
            assert tensor.ndim == 4, tensor.ndim
            if mf == "channels_first":
                tensor = tensor.contiguous()
            elif mf == "channels_last":
                tensor = tensor.contiguous(memory_format=torch.channels_last)
            else:
                raise RuntimeError(
                    "Unknown mf:", mf, " | ",
                    c, size, mf, dtype, mode, ac, is_ref, output_path, seed
                )

        # When there is no reference code, we can use float32 intermediate dtype
        code_path = record_path.get(dtype, "force_float")
        if code_path == "native":
            print("take 'native' code path", end=" ")
            output = transform(tensor, grid, mode, ac)
        else:
            raise ValueError(f"Unknown value for record_path on {code_path}, record_path={record_path}")
    else:
        output = transform(tensor, grid, mode, ac)

    # Expected result:
    if is_ref:
        if output is not None:
            print(" -> store output")
            store_expected(tensor, output, output_path, seed, mf, c, dtype, size, grid, mode, ac, non_contig)
        else:
            print("")
        return

    print(" -> get expected from file")
    expected_ten = get_expected(tensor, output_path, seed, mf, c, dtype, size, grid, mode, ac, non_contig)
    print("---")

    expected_mf = torch.channels_last if expected_ten.is_contiguous(memory_format=torch.channels_last) else torch.contiguous_format
    output_mf = torch.channels_last if output.is_contiguous(memory_format=torch.channels_last) else torch.contiguous_format
    assert expected_mf == output_mf, (expected_mf, output_mf)

    abs_diff = torch.abs(expected_ten.float() - output.float())
    mae = torch.mean(abs_diff)
    max_abs_err = torch.max(abs_diff)

    if mode == "bilinear":

        if exact_match:
            torch.testing.assert_close(expected_ten, output)
        else:
            assert mae.item() < 1.0, mae.item()
            max_abs_err_tol = 2.0
            m = abs_diff > 1.5
            assert max_abs_err.item() < max_abs_err_tol + 1e-5, \
                (max_abs_err.item(), expected_ten.float()[m], output.float()[m])


def main(output_path: str, is_ref: bool = False):

    output_path = Path(output_path)

    if is_ref and output_path.exists():
        raise RuntimeError("Please provide non-exising folder if --is_ref flag is used")

    a = torch.deg2rad(torch.tensor(45.0))
    ca, sa = torch.cos(a), torch.sin(a)
    s1 = 1.23
    s2 = 1.34

    theta = torch.tensor([[
        [ca / s1, sa, 0.12],
        [-sa, ca / s2, 0.23],
    ]])

    seed = 115

    for batch_size in [1, 5]:
        theta = theta.expand(batch_size, 2, 3).contiguous()
        for non_contig in [False, "sliced", "restrided"]:
            for ac in [True, False]:
                for mf in ["channels_last", "channels_first", ]:
                    for c, dtype in [
                        (1, torch.float32),
                        (3, torch.float32),

                        (1, torch.float64),
                        (3, torch.float64),
                    ]:
                        for size in [256, (256, 299), (299, 321)]:
                            if isinstance(size, int):
                                size = [size, size]

                            if non_contig is not False:
                                if non_contig == "sliced":
                                    size = [size[0] + 50, size[1] + 50]
                                elif non_contig == "restrided":
                                    size = [size[0] * 2, size[1] * 2]
                                else:
                                    raise ValueError("Unknown non_contig value '{non_contig}'")

                            grid = affine_grid(theta.to(dtype), size=(batch_size, c, size[0], size[1]), align_corners=ac)

                            for mode in ["nearest", "bilinear", "bicubic"]:

                                print("batch_size/non_contig/mf/size/dtype/c/osize/aa/mode/ac : ", batch_size, non_contig, mf, size, dtype, c, mode, ac, end=" ")

                                torch.manual_seed(seed)

                                if dtype == torch.bool:
                                    tensor = torch.randint(0, 2, size=(c, size[0], size[1]), dtype=dtype)
                                elif dtype == torch.complex64:
                                    real = torch.randint(0, 256, size=(c, size[0], size[1]), dtype=torch.float32)
                                    imag = torch.randint(0, 256, size=(c, size[0], size[1]), dtype=torch.float32)
                                    tensor = torch.complex(real, imag)
                                elif dtype == torch.int8:
                                    tensor = torch.randint(-127, 127, size=(c, size[0], size[1]), dtype=dtype)
                                else:
                                    tensor = torch.randint(0, 256, size=(c, size[0], size[1]), dtype=dtype)

                                if non_contig is not False:
                                    if non_contig == "sliced":
                                        tensor = tensor[:, 25:-25, 25:-25]
                                    elif non_contig == "restrided":
                                        tensor = tensor[:, ::2, ::2]
                                    else:
                                        raise ValueError("Unknown non_contig value '{non_contig}'")

                                memory_format = torch.channels_last if mf == "channels_last" else torch.contiguous_format

                                if batch_size == 1:
                                    tensor = tensor[None, ...].contiguous(memory_format=memory_format)
                                else:
                                    new_shape = (batch_size, ) + tensor.shape
                                    tensor = tensor[None, ...].expand(new_shape).contiguous(memory_format=memory_format)

                                print(".", end=" ")
                                test_consistency_or_record(
                                    tensor, c, size, mf, dtype, grid, mode, ac, is_ref, output_path, seed,
                                    exact_match=True, non_contig=non_contig
                                )


if __name__ == "__main__":

    import os
    if not ("OMP_NUM_THREADS" in os.environ):
        torch.set_num_threads(1)

    print("")
    print(f"Torch version: {torch.__version__}")
    print(f"Torch config: {torch.__config__.show()}")
    print(f"Num threads: {torch.get_num_threads()}")
    print("")

    fire.Fire(main)
