Description:
- 20231109-111039-pr
Torch version: 2.2.0a0+gita310cc8
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
                                                                                                          |  Eager (2.2.0a0+gita310cc8) PR  |  Eager (2.2.0a0+git3ca81ae) nightly  |  Speed-up PR vs Nightly
1 threads: -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      Input: (1, 3, 500, 400) torch.float32, torch.contiguous_format, align_corners=True, mode=nearest    |        631.287 (+-5.513)        |         1196.590 (+-16.223)          |     1.895 (+-0.000)    
      Input: (1, 3, 500, 400) torch.float64, torch.contiguous_format, align_corners=True, mode=nearest    |       1421.300 (+-66.202)       |         2658.933 (+-62.208)          |     1.871 (+-0.000)    
      Input: (1, 3, 500, 400) torch.float32, torch.channels_last, align_corners=True, mode=nearest        |        534.609 (+-3.975)        |         1166.259 (+-13.349)          |     2.182 (+-0.000)    
      Input: (1, 3, 500, 400) torch.float64, torch.channels_last, align_corners=True, mode=nearest        |       1121.308 (+-47.820)       |         2472.511 (+-37.322)          |     2.205 (+-0.000)    
      Input: (1, 3, 500, 400) torch.float32, torch.contiguous_format, align_corners=False, mode=nearest   |        647.366 (+-4.091)        |         1211.040 (+-15.933)          |     1.871 (+-0.000)    
      Input: (1, 3, 500, 400) torch.float64, torch.contiguous_format, align_corners=False, mode=nearest   |       1384.886 (+-79.936)       |         2680.096 (+-72.214)          |     1.935 (+-0.000)    
      Input: (1, 3, 500, 400) torch.float32, torch.channels_last, align_corners=False, mode=nearest       |        552.036 (+-4.704)        |         1165.713 (+-13.829)          |     2.112 (+-0.000)    
      Input: (1, 3, 500, 400) torch.float64, torch.channels_last, align_corners=False, mode=nearest       |       1169.958 (+-51.045)       |         2479.525 (+-37.279)          |     2.119 (+-0.000)    
      Input: (1, 3, 500, 400) torch.float32, torch.contiguous_format, align_corners=True, mode=bilinear   |       1351.042 (+-20.562)       |         3713.318 (+-53.087)          |     2.748 (+-0.000)    
      Input: (1, 3, 500, 400) torch.float64, torch.contiguous_format, align_corners=True, mode=bilinear   |       2564.684 (+-68.066)       |         6266.618 (+-70.403)          |     2.443 (+-0.000)    
      Input: (1, 3, 500, 400) torch.float32, torch.channels_last, align_corners=True, mode=bilinear       |       1084.460 (+-18.702)       |         3689.232 (+-35.200)          |     3.402 (+-0.000)    
      Input: (1, 3, 500, 400) torch.float64, torch.channels_last, align_corners=True, mode=bilinear       |       2176.147 (+-55.133)       |         6053.448 (+-43.859)          |     2.782 (+-0.000)    
      Input: (1, 3, 500, 400) torch.float32, torch.contiguous_format, align_corners=False, mode=bilinear  |       1378.859 (+-16.401)       |         3695.113 (+-48.203)          |     2.680 (+-0.000)    
      Input: (1, 3, 500, 400) torch.float64, torch.contiguous_format, align_corners=False, mode=bilinear  |       2612.592 (+-70.854)       |         6244.574 (+-66.058)          |     2.390 (+-0.000)    
      Input: (1, 3, 500, 400) torch.float32, torch.channels_last, align_corners=False, mode=bilinear      |       1130.353 (+-15.661)       |         3680.292 (+-35.145)          |     3.256 (+-0.000)    
      Input: (1, 3, 500, 400) torch.float64, torch.channels_last, align_corners=False, mode=bilinear      |       2186.742 (+-60.633)       |         6073.101 (+-99.366)          |     2.777 (+-0.000)    
      Input: (1, 3, 500, 400) torch.float32, torch.contiguous_format, align_corners=True, mode=bicubic    |       4966.612 (+-58.559)       |        14703.326 (+-564.378)         |     2.960 (+-0.000)    
      Input: (1, 3, 500, 400) torch.float64, torch.contiguous_format, align_corners=True, mode=bicubic    |      29693.948 (+-671.345)      |        38338.429 (+-768.288)         |     1.291 (+-0.000)    
      Input: (1, 3, 500, 400) torch.float32, torch.channels_last, align_corners=True, mode=bicubic        |       4514.567 (+-67.148)       |        14766.649 (+-260.509)         |     3.271 (+-0.000)    
      Input: (1, 3, 500, 400) torch.float64, torch.channels_last, align_corners=True, mode=bicubic        |      29042.242 (+-1716.618)     |        37420.822 (+-785.526)         |     1.288 (+-0.000)    
      Input: (1, 3, 500, 400) torch.float32, torch.contiguous_format, align_corners=False, mode=bicubic   |       4989.461 (+-53.598)       |        14704.016 (+-330.618)         |     2.947 (+-0.000)    
      Input: (1, 3, 500, 400) torch.float64, torch.contiguous_format, align_corners=False, mode=bicubic   |      29907.569 (+-680.919)      |        38409.600 (+-691.079)         |     1.284 (+-0.000)    
      Input: (1, 3, 500, 400) torch.float32, torch.channels_last, align_corners=False, mode=bicubic       |       4526.322 (+-50.505)       |        14756.324 (+-236.034)         |     3.260 (+-0.000)    
      Input: (1, 3, 500, 400) torch.float64, torch.channels_last, align_corners=False, mode=bicubic       |      29087.928 (+-605.207)      |        37389.990 (+-663.702)         |     1.285 (+-0.000)    
      Input: (8, 3, 500, 400) torch.float32, torch.contiguous_format, align_corners=True, mode=nearest    |       9701.365 (+-91.253)       |        13726.028 (+-112.412)         |     1.415 (+-0.000)    
      Input: (8, 3, 500, 400) torch.float64, torch.contiguous_format, align_corners=True, mode=nearest    |      32915.423 (+-294.043)      |        41501.452 (+-327.186)         |     1.261 (+-0.000)    
      Input: (8, 3, 500, 400) torch.float32, torch.channels_last, align_corners=True, mode=nearest        |       7547.142 (+-49.234)       |         10839.269 (+-93.029)         |     1.436 (+-0.000)    
      Input: (8, 3, 500, 400) torch.float64, torch.channels_last, align_corners=True, mode=nearest        |       15215.403 (+-99.483)      |        34985.201 (+-350.970)         |     2.299 (+-0.000)    
      Input: (8, 3, 500, 400) torch.float32, torch.contiguous_format, align_corners=False, mode=nearest   |       9654.002 (+-97.579)       |        13858.466 (+-128.411)         |     1.436 (+-0.000)    
      Input: (8, 3, 500, 400) torch.float64, torch.contiguous_format, align_corners=False, mode=nearest   |      33171.633 (+-202.875)      |        41104.817 (+-433.195)         |     1.239 (+-0.000)    
      Input: (8, 3, 500, 400) torch.float32, torch.channels_last, align_corners=False, mode=nearest       |       7565.635 (+-51.029)       |         10916.952 (+-96.023)         |     1.443 (+-0.000)    
      Input: (8, 3, 500, 400) torch.float64, torch.channels_last, align_corners=False, mode=nearest       |      27745.697 (+-185.644)      |        34851.453 (+-260.788)         |     1.256 (+-0.000)    
      Input: (8, 3, 500, 400) torch.float32, torch.contiguous_format, align_corners=True, mode=bilinear   |      14466.361 (+-121.156)      |        36243.299 (+-350.811)         |     2.505 (+-0.000)    
      Input: (8, 3, 500, 400) torch.float64, torch.contiguous_format, align_corners=True, mode=bilinear   |      39935.914 (+-229.508)      |        68053.260 (+-1057.869)        |     1.704 (+-0.000)    
      Input: (8, 3, 500, 400) torch.float32, torch.channels_last, align_corners=True, mode=bilinear       |      11332.998 (+-118.720)      |        30729.080 (+-381.639)         |     2.711 (+-0.000)    
      Input: (8, 3, 500, 400) torch.float64, torch.channels_last, align_corners=True, mode=bilinear       |      21425.783 (+-173.883)      |        63030.143 (+-390.692)         |     2.942 (+-0.000)    
      Input: (8, 3, 500, 400) torch.float32, torch.contiguous_format, align_corners=False, mode=bilinear  |      14916.502 (+-134.419)      |        36150.986 (+-293.416)         |     2.424 (+-0.000)    
      Input: (8, 3, 500, 400) torch.float64, torch.contiguous_format, align_corners=False, mode=bilinear  |      40509.286 (+-226.356)      |        67757.076 (+-991.072)         |     1.673 (+-0.000)    
      Input: (8, 3, 500, 400) torch.float32, torch.channels_last, align_corners=False, mode=bilinear      |      11991.997 (+-118.332)      |        30465.192 (+-282.936)         |     2.540 (+-0.000)    
      Input: (8, 3, 500, 400) torch.float64, torch.channels_last, align_corners=False, mode=bilinear      |      35531.845 (+-322.375)      |        63729.695 (+-678.976)         |     1.794 (+-0.000)    
      Input: (8, 3, 500, 400) torch.float32, torch.contiguous_format, align_corners=True, mode=bicubic    |      48899.091 (+-298.459)      |       129854.028 (+-1635.314)        |     2.656 (+-0.000)    
      Input: (8, 3, 500, 400) torch.float64, torch.contiguous_format, align_corners=True, mode=bicubic    |     281653.903 (+-2543.997)     |       352072.211 (+-3178.250)        |     1.250 (+-0.000)    
      Input: (8, 3, 500, 400) torch.float32, torch.channels_last, align_corners=True, mode=bicubic        |      41144.817 (+-265.546)      |       126762.714 (+-1740.266)        |     3.081 (+-0.000)    
      Input: (8, 3, 500, 400) torch.float64, torch.channels_last, align_corners=True, mode=bicubic        |     274124.393 (+-2777.655)     |       341804.886 (+-2974.238)        |     1.247 (+-0.000)    
      Input: (8, 3, 500, 400) torch.float32, torch.contiguous_format, align_corners=False, mode=bicubic   |      48553.607 (+-220.137)      |       130436.644 (+-3081.411)        |     2.686 (+-0.000)    
      Input: (8, 3, 500, 400) torch.float64, torch.contiguous_format, align_corners=False, mode=bicubic   |     281025.314 (+-2349.876)     |       353432.316 (+-3600.725)        |     1.258 (+-0.000)    
      Input: (8, 3, 500, 400) torch.float32, torch.channels_last, align_corners=False, mode=bicubic       |      41116.567 (+-327.711)      |       126884.936 (+-1718.414)        |     3.086 (+-0.000)    
      Input: (8, 3, 500, 400) torch.float64, torch.channels_last, align_corners=False, mode=bicubic       |     275067.863 (+-2265.981)     |       326207.948 (+-2578.309)        |     1.186 (+-0.000)    

Times are in microseconds (us).
