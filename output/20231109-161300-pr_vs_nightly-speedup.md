Description:
- 20231109-155929-pr
Torch version: 2.2.0a0+git971a50e
Torch config: PyTorch built with:
  - GCC 9.4
  - C++ Version: 201703
  - OpenMP 201511 (a.k.a. OpenMP 4.5)
  - CPU capability usage: AVX2
  - CUDA Runtime 12.1
  - NVCC architecture flags: -gencode;arch=compute_61,code=sm_61;-gencode;arch=compute_75,code=sm_75;-gencode;arch=compute_89,code=sm_89
  - CuDNN 8.9
  - Build settings: BUILD_TYPE=Release, CUDA_VERSION=12.1, CUDNN_VERSION=8.9.0, CXX_COMPILER=/usr/bin/c++, CXX_FLAGS= -D_GLIBCXX_USE_CXX11_ABI=1 -fvisibility-inlines-hidden -DUSE_PTHREADPOOL -DNDEBUG -DUSE_PYTORCH_QNNPACK -DSYMBOLICATE_MOBILE_DEBUG_HANDLE -O2 -fPIC -Wall -Wextra -Werror=return-type -Werror=non-virtual-dtor -Werror=bool-operation -Wnarrowing -Wno-missing-field-initializers -Wno-type-limits -Wno-array-bounds -Wno-unknown-pragmas -Wno-unused-parameter -Wno-unused-function -Wno-unused-result -Wno-strict-overflow -Wno-strict-aliasing -Wno-stringop-overflow -Wno-psabi -Wno-error=pedantic -Wno-error=old-style-cast -Wno-missing-braces -fdiagnostics-color=always -faligned-new -Wno-unused-but-set-variable -Wno-maybe-uninitialized -fno-math-errno -fno-trapping-math -Werror=format -Wno-stringop-overflow, PERF_WITH_AVX=1, PERF_WITH_AVX2=1, PERF_WITH_AVX512=1, TORCH_DISABLE_GPU_ASSERTS=ON, TORCH_VERSION=2.2.0, USE_CUDA=1, USE_CUDNN=1, USE_EIGEN_FOR_BLAS=ON, USE_EXCEPTION_PTR=1, USE_GFLAGS=OFF, USE_GLOG=OFF, USE_MKL=OFF, USE_MKLDNN=0, USE_MPI=OFF, USE_NCCL=0, USE_NNPACK=0, USE_OPENMP=ON, USE_ROCM=OFF, 


- 20231109-110115-nightly
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



[--------------------------------------------------------------------------------------- Affine grid sampling, cpu ----------------------------------------------------------------------------------------]
                                                                                                          |  Eager (2.2.0a0+git971a50e) PR  |  Eager (2.2.0a0+git3ca81ae) nightly  |  Speed-up PR vs Nightly
1 threads: -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      Input: (1, 3, 500, 400) torch.float32, torch.contiguous_format, align_corners=True, mode=nearest    |        698.871 (+-42.998)       |         1196.590 (+-16.223)          |     1.712 (+-0.000)    
      Input: (1, 3, 500, 400) torch.float64, torch.contiguous_format, align_corners=True, mode=nearest    |       1363.909 (+-49.798)       |         2658.933 (+-62.208)          |     1.949 (+-0.000)    
      Input: (1, 3, 500, 400) torch.float32, torch.channels_last, align_corners=True, mode=nearest        |        542.857 (+-3.547)        |         1166.259 (+-13.349)          |     2.148 (+-0.000)    
      Input: (1, 3, 500, 400) torch.float64, torch.channels_last, align_corners=True, mode=nearest        |       1110.957 (+-173.044)      |         2472.511 (+-37.322)          |     2.226 (+-0.000)    
      Input: (1, 3, 500, 400) torch.float32, torch.contiguous_format, align_corners=False, mode=nearest   |        666.702 (+-3.624)        |         1211.040 (+-15.933)          |     1.816 (+-0.000)    
      Input: (1, 3, 500, 400) torch.float64, torch.contiguous_format, align_corners=False, mode=nearest   |       1383.907 (+-52.735)       |         2680.096 (+-72.214)          |     1.937 (+-0.000)    
      Input: (1, 3, 500, 400) torch.float32, torch.channels_last, align_corners=False, mode=nearest       |        552.020 (+-4.574)        |         1165.713 (+-13.829)          |     2.112 (+-0.000)    
      Input: (1, 3, 500, 400) torch.float64, torch.channels_last, align_corners=False, mode=nearest       |       1195.561 (+-43.627)       |         2479.525 (+-37.279)          |     2.074 (+-0.000)    
      Input: (1, 3, 500, 400) torch.float32, torch.contiguous_format, align_corners=True, mode=bilinear   |       1434.594 (+-18.829)       |         3713.318 (+-53.087)          |     2.588 (+-0.000)    
      Input: (1, 3, 500, 400) torch.float64, torch.contiguous_format, align_corners=True, mode=bilinear   |       2584.424 (+-61.646)       |         6266.618 (+-70.403)          |     2.425 (+-0.000)    
      Input: (1, 3, 500, 400) torch.float32, torch.channels_last, align_corners=True, mode=bilinear       |       1064.318 (+-17.605)       |         3689.232 (+-35.200)          |     3.466 (+-0.000)    
      Input: (1, 3, 500, 400) torch.float64, torch.channels_last, align_corners=True, mode=bilinear       |       2227.200 (+-46.111)       |         6053.448 (+-43.859)          |     2.718 (+-0.000)    
      Input: (1, 3, 500, 400) torch.float32, torch.contiguous_format, align_corners=False, mode=bilinear  |       1479.566 (+-23.023)       |         3695.113 (+-48.203)          |     2.497 (+-0.000)    
      Input: (1, 3, 500, 400) torch.float64, torch.contiguous_format, align_corners=False, mode=bilinear  |       2551.005 (+-58.898)       |         6244.574 (+-66.058)          |     2.448 (+-0.000)    
      Input: (1, 3, 500, 400) torch.float32, torch.channels_last, align_corners=False, mode=bilinear      |       1081.029 (+-13.911)       |         3680.292 (+-35.145)          |     3.404 (+-0.000)    
      Input: (1, 3, 500, 400) torch.float64, torch.channels_last, align_corners=False, mode=bilinear      |       2209.528 (+-61.779)       |         6073.101 (+-99.366)          |     2.749 (+-0.000)    
      Input: (1, 3, 500, 400) torch.float32, torch.contiguous_format, align_corners=True, mode=bicubic    |       4607.162 (+-40.688)       |        14703.326 (+-564.378)         |     3.191 (+-0.000)    
      Input: (1, 3, 500, 400) torch.float64, torch.contiguous_format, align_corners=True, mode=bicubic    |      30132.017 (+-679.033)      |        38338.429 (+-768.288)         |     1.272 (+-0.000)    
      Input: (1, 3, 500, 400) torch.float32, torch.channels_last, align_corners=True, mode=bicubic        |       4274.459 (+-33.603)       |        14766.649 (+-260.509)         |     3.455 (+-0.000)    
      Input: (1, 3, 500, 400) torch.float64, torch.channels_last, align_corners=True, mode=bicubic        |      29137.615 (+-617.591)      |        37420.822 (+-785.526)         |     1.284 (+-0.000)    
      Input: (1, 3, 500, 400) torch.float32, torch.contiguous_format, align_corners=False, mode=bicubic   |       4954.048 (+-79.199)       |        14704.016 (+-330.618)         |     2.968 (+-0.000)    
      Input: (1, 3, 500, 400) torch.float64, torch.contiguous_format, align_corners=False, mode=bicubic   |      30068.414 (+-792.686)      |        38409.600 (+-691.079)         |     1.277 (+-0.000)    
      Input: (1, 3, 500, 400) torch.float32, torch.channels_last, align_corners=False, mode=bicubic       |       4274.381 (+-35.679)       |        14756.324 (+-236.034)         |     3.452 (+-0.000)    
      Input: (1, 3, 500, 400) torch.float64, torch.channels_last, align_corners=False, mode=bicubic       |      29148.286 (+-780.277)      |        37389.990 (+-663.702)         |     1.283 (+-0.000)    
      Input: (8, 3, 500, 400) torch.float32, torch.contiguous_format, align_corners=True, mode=nearest    |       9656.722 (+-66.127)       |        13726.028 (+-112.412)         |     1.421 (+-0.000)    
      Input: (8, 3, 500, 400) torch.float64, torch.contiguous_format, align_corners=True, mode=nearest    |      19947.575 (+-108.492)      |        41501.452 (+-327.186)         |     2.081 (+-0.000)    
      Input: (8, 3, 500, 400) torch.float32, torch.channels_last, align_corners=True, mode=nearest        |       7597.021 (+-52.866)       |         10839.269 (+-93.029)         |     1.427 (+-0.000)    
      Input: (8, 3, 500, 400) torch.float64, torch.channels_last, align_corners=True, mode=nearest        |      28164.663 (+-179.955)      |        34985.201 (+-350.970)         |     1.242 (+-0.000)    
      Input: (8, 3, 500, 400) torch.float32, torch.contiguous_format, align_corners=False, mode=nearest   |       9703.983 (+-154.907)      |        13858.466 (+-128.411)         |     1.428 (+-0.000)    
      Input: (8, 3, 500, 400) torch.float64, torch.contiguous_format, align_corners=False, mode=nearest   |      34086.142 (+-212.213)      |        41104.817 (+-433.195)         |     1.206 (+-0.000)    
      Input: (8, 3, 500, 400) torch.float32, torch.channels_last, align_corners=False, mode=nearest       |       7626.922 (+-56.371)       |         10916.952 (+-96.023)         |     1.431 (+-0.000)    
      Input: (8, 3, 500, 400) torch.float64, torch.channels_last, align_corners=False, mode=nearest       |      28277.855 (+-228.616)      |        34851.453 (+-260.788)         |     1.232 (+-0.000)    
      Input: (8, 3, 500, 400) torch.float32, torch.contiguous_format, align_corners=True, mode=bilinear   |      14180.691 (+-184.150)      |        36243.299 (+-350.811)         |     2.556 (+-0.000)    
      Input: (8, 3, 500, 400) torch.float64, torch.contiguous_format, align_corners=True, mode=bilinear   |      40699.798 (+-234.600)      |        68053.260 (+-1057.869)        |     1.672 (+-0.000)    
      Input: (8, 3, 500, 400) torch.float32, torch.channels_last, align_corners=True, mode=bilinear       |      11190.905 (+-103.419)      |        30729.080 (+-381.639)         |     2.746 (+-0.000)    
      Input: (8, 3, 500, 400) torch.float64, torch.channels_last, align_corners=True, mode=bilinear       |      35965.958 (+-298.474)      |        63030.143 (+-390.692)         |     1.752 (+-0.000)    
      Input: (8, 3, 500, 400) torch.float32, torch.contiguous_format, align_corners=False, mode=bilinear  |      14461.459 (+-120.555)      |        36150.986 (+-293.416)         |     2.500 (+-0.000)    
      Input: (8, 3, 500, 400) torch.float64, torch.contiguous_format, align_corners=False, mode=bilinear  |      40891.653 (+-195.887)      |        67757.076 (+-991.072)         |     1.657 (+-0.000)    
      Input: (8, 3, 500, 400) torch.float32, torch.channels_last, align_corners=False, mode=bilinear      |      11437.092 (+-100.145)      |        30465.192 (+-282.936)         |     2.664 (+-0.000)    
      Input: (8, 3, 500, 400) torch.float64, torch.channels_last, align_corners=False, mode=bilinear      |      36112.937 (+-306.527)      |        63729.695 (+-678.976)         |     1.765 (+-0.000)    
      Input: (8, 3, 500, 400) torch.float32, torch.contiguous_format, align_corners=True, mode=bicubic    |      39512.380 (+-368.172)      |       129854.028 (+-1635.314)        |     3.286 (+-0.000)    
      Input: (8, 3, 500, 400) torch.float64, torch.contiguous_format, align_corners=True, mode=bicubic    |     283835.203 (+-2166.425)     |       352072.211 (+-3178.250)        |     1.240 (+-0.000)    
      Input: (8, 3, 500, 400) torch.float32, torch.channels_last, align_corners=True, mode=bicubic        |      35804.934 (+-341.254)      |       126762.714 (+-1740.266)        |     3.540 (+-0.000)    
      Input: (8, 3, 500, 400) torch.float64, torch.channels_last, align_corners=True, mode=bicubic        |     275862.511 (+-2549.251)     |       341804.886 (+-2974.238)        |     1.239 (+-0.000)    
      Input: (8, 3, 500, 400) torch.float32, torch.contiguous_format, align_corners=False, mode=bicubic   |      39514.504 (+-307.814)      |       130436.644 (+-3081.411)        |     3.301 (+-0.000)    
      Input: (8, 3, 500, 400) torch.float64, torch.contiguous_format, align_corners=False, mode=bicubic   |     283929.198 (+-2373.485)     |       353432.316 (+-3600.725)        |     1.245 (+-0.000)    
      Input: (8, 3, 500, 400) torch.float32, torch.channels_last, align_corners=False, mode=bicubic       |      35776.293 (+-267.109)      |       126884.936 (+-1718.414)        |     3.547 (+-0.000)    
      Input: (8, 3, 500, 400) torch.float64, torch.channels_last, align_corners=False, mode=bicubic       |     276278.294 (+-2150.899)     |       326207.948 (+-2578.309)        |     1.181 (+-0.000)    

Times are in microseconds (us).
