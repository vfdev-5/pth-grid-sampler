# Notes on CPU Grid Sampler implementation

Problems:
- perfs with 1 thread on CPU for torchvision
- precision: unitary mask is transformed with values around 1
```
Unique: tensor([0.0000000000000000, 0.0155006768015857, 0.0155006768015866,
        0.0350042421037449, 0.0350042421037458, 0.0545078074058989,
        0.0545078074059049, 0.0740113727080580, 0.0740113727080640,
        0.0935149380102089, 0.0935149380102120, 0.2853453458858832,
        0.2853453458858866, 0.3048489111880373, 0.3048489111880386,
        0.3243524764901964, 0.3243524764901977, 0.3438560417923426,
        0.3438560417923504, 0.3633596070945018, 0.3633596070945095,
        0.5551900149701723, 0.5551900149701756, 0.5746935802723314,
        0.5746935802723322, 0.5941971455744888, 0.5941971455744905,
        0.6137007108766479, 0.6137007108766497, 0.6332042761788017,
        0.6332042761788019, 0.6527078414809608, 0.6527078414809611,
        0.8445382493566242, 0.8445382493566271, 0.8640418146587834,
        0.8640418146587836, 0.8640418146587863, 0.8835453799609403,
        0.8835453799609425, 0.8835453799609428, 0.9030489452630994,
        0.9030489452631016, 0.9225525105652534, 0.9225525105652537,
        0.9225525105652560, 0.9225525105652608, 0.9999999999999999,
        1.0000000000000000], dtype=torch.float64)
```




## Perfs PR vs Nightly

### On nightly
```
python -u run_bench_grid_sampler.py "output/$(date "+%Y%m%d-%H%M%S")-nightly.pkl" --tag=nightly
```


### On PR
```
python -u run_bench_grid_sampler.py "output/$(date "+%Y%m%d-%H%M%S")-pr.pkl" --tag=PR

python -u make_results_table_from_pickles.py output/$(date "+%Y%m%d-%H%M%S")-pr_vs_nightly.md output/XYZ-pr.pkl output/ABC-nightly.pkl

python -u perf_results_compute_speedup_v2.py output/test-multicols_pr_vs_nightly-speedup.md 'output/20230327-114043-pr.pkl' 'output/20230327-111746-nightly.pkl' --compare "torch (2.1.0a0+git90861e5) PR;torch (2.1.0a0+git2b75955) nightly;speed-up PR vs Nightly" --compare "Pillow (9.0.0.post1);torch (2.1.0a0+git90861e5) PR"
```

```
python -u run_bench_interp.py "output/$(date "+%Y%m%d-%H%M%S")-pr.pkl" --tag=PR --with-torchvision
```

## Perf tests
- Baseline:
```
python perf_affine_grid_sampler_custom_cases.py


Datetime: 20231108-214452
Torch version: 2.2.0a0+git3ca81ae
Torch config: PyTorch built with:
  - GCC 9.4
  - C++ Version: 201703
  - OpenMP 201511 (a.k.a. OpenMP 4.5)
  - CPU capability usage: AVX2
  - CUDA Runtime 12.1
  - NVCC architecture flags: -gencode;arch=compute_61,code=sm_61;-gencode;arch=compute_75,code=sm_75;-gencode;arch=compute_89,code=sm_89
  - CuDNN 8.9
  - Build settings: BUILD_TYPE=Release, CUDA_VERSION=12.1, CUDNN_VERSION=8.9.0, CXX_COMPILER=/usr/bin/c++, CXX_FLAGS= -D_GLIBCXX_USE_CXX11_ABI=1 -fvisibility-inlines-hidden -DUSE_PTHREADPOOL -DNDEBUG -DUSE_PYTORCH_QNNPACK -DSYMBOLICATE_MOBILE_DEBUG_HANDLE -O2 -fPIC -Wall -Wextra -Werror=return-type -Werror=non-virtual-dtor -Werror=bool-operation -Wnarrowing -Wno-missing-field-initializers -Wno-type-limits -Wno-array-bounds -Wno-unknown-pragmas -Wno-unused-parameter -Wno-unused-function -Wno-unused-result -Wno-strict-overflow -Wno-strict-aliasing -Wno-stringop-overflow -Wno-psabi -Wno-error=pedantic -Wno-error=old-style-cast -Wno-missing-braces -fdiagnostics-color=always -faligned-new -Wno-unused-but-set-variable -Wno-maybe-uninitialized -fno-math-errno -fno-trapping-math -Werror=format -Wno-stringop-overflow, PERF_WITH_AVX=1, PERF_WITH_AVX2=1, PERF_WITH_AVX512=1, TORCH_DISABLE_GPU_ASSERTS=ON, TORCH_VERSION=2.2.0, USE_CUDA=1, USE_CUDNN=1, USE_EIGEN_FOR_BLAS=ON, USE_EXCEPTION_PTR=1, USE_GFLAGS=OFF, USE_GLOG=OFF, USE_MKL=OFF, USE_MKLDNN=0, USE_MPI=OFF, USE_NCCL=0, USE_NNPACK=0, USE_OPENMP=ON, USE_ROCM=OFF,

Num threads: 1

[----------------------------------------------------- Affine grid sampling, cpu ------------------------------------------------------]
                                                                                                          |  Eager (2.2.0a0+git3ca81ae)
1 threads: -----------------------------------------------------------------------------------------------------------------------------
      Input: (8, 3, 345, 456) torch.float32, torch.contiguous_format, align_corners=False, mode=nearest   |        13.779 (+-0.062)
      Input: (8, 3, 345, 456) torch.float32, torch.channels_last, align_corners=False, mode=nearest       |        9.609 (+-0.037)
      Input: (8, 3, 345, 456) torch.float32, torch.contiguous_format, align_corners=False, mode=bilinear  |        23.348 (+-0.129)
      Input: (8, 3, 345, 456) torch.float32, torch.channels_last, align_corners=False, mode=bilinear      |        23.374 (+-0.089)
      Input: (8, 3, 345, 456) torch.float32, torch.contiguous_format, align_corners=False, mode=bicubic   |       100.529 (+-0.749)
      Input: (8, 3, 345, 456) torch.float32, torch.channels_last, align_corners=False, mode=bicubic       |       102.068 (+-0.460)

      Input: (8, 3, 345, 456) torch.float64, torch.contiguous_format, align_corners=False, mode=nearest   |        23.038 (+-0.089)
      Input: (8, 3, 345, 456) torch.float64, torch.channels_last, align_corners=False, mode=nearest       |        17.959 (+-0.073)
      Input: (8, 3, 345, 456) torch.float64, torch.contiguous_format, align_corners=False, mode=bilinear  |        40.003 (+-0.183)
      Input: (8, 3, 345, 456) torch.float64, torch.channels_last, align_corners=False, mode=bilinear      |        40.249 (+-0.131)
      Input: (8, 3, 345, 456) torch.float64, torch.contiguous_format, align_corners=False, mode=bicubic   |       255.375 (+-1.988)
      Input: (8, 3, 345, 456) torch.float64, torch.channels_last, align_corners=False, mode=bicubic       |       260.071 (+-1.858)

Times are in milliseconds (ms)
```

- Use vectorized `mask_gather` and `cast`
```
Num threads: 1

[----------------------------------------------------- Affine grid sampling, cpu ------------------------------------------------------]
                                                                                                          |  Eager (2.2.0a0+gita310cc8)
1 threads: -----------------------------------------------------------------------------------------------------------------------------
      Input: (8, 3, 345, 456) torch.float32, torch.contiguous_format, align_corners=False, mode=nearest   |        8.831 (+-0.035)
      Input: (8, 3, 345, 456) torch.float32, torch.channels_last, align_corners=False, mode=nearest       |        6.226 (+-0.009)
      Input: (8, 3, 345, 456) torch.float32, torch.contiguous_format, align_corners=False, mode=bilinear  |        11.261 (+-0.032)
      Input: (8, 3, 345, 456) torch.float32, torch.channels_last, align_corners=False, mode=bilinear      |        10.337 (+-0.039)
      Input: (8, 3, 345, 456) torch.float32, torch.contiguous_format, align_corners=False, mode=bicubic   |        40.563 (+-0.072)
      Input: (8, 3, 345, 456) torch.float32, torch.channels_last, align_corners=False, mode=bicubic       |        36.392 (+-0.084)

      Input: (8, 3, 345, 456) torch.float64, torch.contiguous_format, align_corners=False, mode=nearest   |        16.214 (+-0.052)
      Input: (8, 3, 345, 456) torch.float64, torch.channels_last, align_corners=False, mode=nearest       |        13.157 (+-0.039)
      Input: (8, 3, 345, 456) torch.float64, torch.contiguous_format, align_corners=False, mode=bilinear  |        18.343 (+-0.062)
      Input: (8, 3, 345, 456) torch.float64, torch.channels_last, align_corners=False, mode=bilinear      |        18.100 (+-0.077)
      Input: (8, 3, 345, 456) torch.float64, torch.contiguous_format, align_corners=False, mode=bicubic   |       199.438 (+-1.837)
      Input: (8, 3, 345, 456) torch.float64, torch.channels_last, align_corners=False, mode=bicubic       |       206.403 (+-2.081)

Times are in milliseconds (ms).
```

- Use vectorized `mask_gather` and `cast` + no mask copy
```
[----------------------------------------------------- Affine grid sampling, cpu ------------------------------------------------------]
                                                                                                          |  Eager (2.2.0a0+gita310cc8)
1 threads: -----------------------------------------------------------------------------------------------------------------------------
      Input: (8, 3, 345, 456) torch.float32, torch.contiguous_format, align_corners=False, mode=nearest   |        8.800 (+-0.062)
      Input: (8, 3, 345, 456) torch.float32, torch.channels_last, align_corners=False, mode=nearest       |        7.335 (+-0.026)
      Input: (8, 3, 345, 456) torch.float32, torch.contiguous_format, align_corners=False, mode=bilinear  |        12.711 (+-0.033)
      Input: (8, 3, 345, 456) torch.float32, torch.channels_last, align_corners=False, mode=bilinear      |        10.988 (+-0.194)
      Input: (8, 3, 345, 456) torch.float32, torch.contiguous_format, align_corners=False, mode=bicubic   |        42.871 (+-0.097)
      Input: (8, 3, 345, 456) torch.float32, torch.channels_last, align_corners=False, mode=bicubic       |        36.406 (+-0.087)

      Input: (8, 3, 345, 456) torch.float64, torch.contiguous_format, align_corners=False, mode=nearest   |        16.710 (+-0.044)
      Input: (8, 3, 345, 456) torch.float64, torch.channels_last, align_corners=False, mode=nearest       |        15.029 (+-0.060)
      Input: (8, 3, 345, 456) torch.float64, torch.contiguous_format, align_corners=False, mode=bilinear  |        22.294 (+-0.064)
      Input: (8, 3, 345, 456) torch.float64, torch.channels_last, align_corners=False, mode=bilinear      |        20.022 (+-0.055)
      Input: (8, 3, 345, 456) torch.float64, torch.contiguous_format, align_corners=False, mode=bicubic   |       199.580 (+-1.053)
      Input: (8, 3, 345, 456) torch.float64, torch.channels_last, align_corners=False, mode=bicubic       |       203.661 (+-0.790)


Times are in milliseconds (ms).
```


- Use previous + `auto interpolated = fmadd(nw_val, nw, fmadd(ne_val, ne, fmadd(sw_val, sw, fmadd(se_val, se, Vec(0)))));`
```
Num threads: 1

[----------------------------------------------------- Affine grid sampling, cpu ------------------------------------------------------]
                                                                                                          |  Eager (2.2.0a0+gitf47f047)
1 threads: -----------------------------------------------------------------------------------------------------------------------------
      Input: (8, 3, 345, 456) torch.float32, torch.contiguous_format, align_corners=False, mode=bilinear  |        35.451 (+-1.306)
      Input: (8, 3, 345, 456) torch.float32, torch.channels_last, align_corners=False, mode=bilinear      |        35.714 (+-0.375)

Times are in milliseconds (ms).
```

- Previous + `use fmadd in unnormalize and define scaling_factor as Vec`
```
Num threads: 1

[----------------------------------------------------- Affine grid sampling, cpu ------------------------------------------------------]
                                                                                                          |  Eager (2.2.0a0+gitf47f047)
1 threads: -----------------------------------------------------------------------------------------------------------------------------
      Input: (8, 3, 345, 456) torch.float32, torch.contiguous_format, align_corners=False, mode=bilinear  |        35.389 (+-0.750)
      Input: (8, 3, 345, 456) torch.float32, torch.channels_last, align_corners=False, mode=bilinear      |        35.695 (+-0.265)

Times are in milliseconds (ms).
```