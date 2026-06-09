#include <iostream>
#include <cuda_runtime.h>

__global__
void vectorAdd(float* A,
               float* B,
               float* C,
               int N)
{
    int i = blockIdx.x * blockDim.x + threadIdx.x;

    if (i < N)
        C[i] = A[i] + B[i];
}

int main()
{
    const int N = 1024;

    size_t size = N * sizeof(float);

    // Host memory (CPU)

    float *h_A = new float[N];
    float *h_B = new float[N];
    float *h_C = new float[N];

    for(int i=0;i<N;i++)
    {
        h_A[i] = i;
        h_B[i] = 2*i;
    }

    // Device memory (GPU)

    float *d_A;
    float *d_B;
    float *d_C;

    cudaMalloc(&d_A,size);
    cudaMalloc(&d_B,size);
    cudaMalloc(&d_C,size);

    // Copy CPU -> GPU

    cudaMemcpy(d_A,h_A,size,cudaMemcpyHostToDevice);
    cudaMemcpy(d_B,h_B,size,cudaMemcpyHostToDevice);

    // Launch kernel

    int threadsPerBlock = 256;
    int blocksPerGrid =
        (N + threadsPerBlock - 1) / threadsPerBlock;

    vectorAdd<<<blocksPerGrid,
                threadsPerBlock>>>(
                    d_A,d_B,d_C,N);

    // Copy GPU -> CPU

    cudaMemcpy(h_C,d_C,size,cudaMemcpyDeviceToHost);

    // Check result

    for(int i=0;i<N;i++)
    {
        std::cout
            << h_A[i]
            << " + "
            << h_B[i]
            << " = "
            << h_C[i]
            << std::endl;
    }

    // Cleanup

    cudaFree(d_A);
    cudaFree(d_B);
    cudaFree(d_C);

    delete[] h_A;
    delete[] h_B;
    delete[] h_C;

    return 0;
}