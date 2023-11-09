
import pickle
from pathlib import Path
import unittest.mock


import torch
import torch.utils.benchmark as benchmark

from torch.nn.functional import grid_sample, affine_grid

import fire


def transform(img, grid, mode, align_corners):
    output = grid_sample(img, grid, align_corners=align_corners, mode=mode)
    return output


def patched_as_column_strings(self):
    concrete_results = [r for r in self._results if r is not None]
    env = f"({concrete_results[0].env})" if self._render_env else ""
    env = env.ljust(self._env_str_len + 4)
    output = ["  " + env + concrete_results[0].as_row_name]
    for m, col in zip(self._results, self._columns or ()):
        if m is None:
            output.append(col.num_to_str(None, 1, None))
        else:
            if len(m.times) == 1:
                spread = 0
            else:
                spread = float(torch.tensor(m.times, dtype=torch.float64).std(unbiased=len(m.times) > 1))
                if col._trim_significant_figures:
                    spread = benchmark.utils.common.trim_sigfig(spread, m.significant_figures)
            output.append(f"{m.median / self._time_scale:>3.3f} (+-{spread / self._time_scale:>3.3f})")
    return output


def run_benchmark(mode, align_corners, memory_format, dtype, device, tag="", min_run_time=10.0, n=2):
    results = []
    torch.manual_seed(12)

    a = torch.deg2rad(torch.tensor(53.0))
    ca, sa = torch.cos(a), torch.sin(a)
    s1 = 1.23
    s2 = 1.34

    c, h, w = 3, 500, 400

    theta = torch.tensor([[
        [ca / s1, sa, 0.123],
        [-sa, ca / s2, 0.234],
    ]])
    theta = theta.expand(n, 2, 3).contiguous()

    x = torch.arange(n * c * h * w, device=device).reshape(n, c, h, w).to(torch.uint8)
    x = x.to(dtype=dtype)
    x = x.contiguous(memory_format=memory_format)

    theta = theta.to(device=device, dtype=dtype)

    n, c, h, w = x.shape
    grid = affine_grid(theta, size=(n, c, h, w), align_corners=align_corners)

    results.append(
        benchmark.Timer(
            stmt=f"fn(x, grid, mode, align_corners)",
            globals={
                "fn": transform,
                "x": x,
                "grid": grid,
                "mode": mode,
                "align_corners": align_corners,
            },
            num_threads=torch.get_num_threads(),
            label=f"Affine grid sampling, {device}",
            sub_label=f"Input: {tuple(x.shape)} {x.dtype}, {memory_format}, align_corners={align_corners}, mode={mode}",
            description=f"Eager ({torch.__version__}) {tag}",
        ).blocked_autorange(min_run_time=min_run_time)
    )

    return results


def main(
    output_filepath: str,
    min_run_time: float = 10.0,
    tag: str = "",
    display: bool = True,
    num_threads: int = 1,
):
    torch.set_num_threads(num_threads)
    output_filepath = Path(output_filepath)

    from datetime import datetime

    now = datetime.now().strftime('%Y%m%d-%H%M%S')

    print(f"Datetime: {now}")
    print(f"Torch version: {torch.__version__}")
    print(f"Torch config: {torch.__config__.show()}")
    print(f"Num threads: {torch.get_num_threads()}")
    print("")

    test_results = []

    for n in [1, 8]:
        for device in ["cpu", ]:
            for mode in ["nearest", "bilinear", "bicubic"]:
                for align_corners in [True, False]:
                    for memory_format in [torch.contiguous_format, torch.channels_last]:
                        for dtype in [torch.float32, torch.float64]:

                            test_results += run_benchmark(
                                mode, align_corners, memory_format, dtype, device, tag, min_run_time, n=n
                            )

    with open(output_filepath, "wb") as handler:
        output = {
            "torch_version": torch.__version__,
            "torch_config": torch.__config__.show(),
            "num_threads": torch.get_num_threads(),
            "test_results": test_results,
        }
        pickle.dump(output, handler)

    if display:
        with unittest.mock.patch(
            "torch.utils.benchmark.utils.compare._Row.as_column_strings", patched_as_column_strings
        ):
            compare = benchmark.Compare(test_results)
            compare.print()


if __name__ == "__main__":
    fire.Fire(main)
