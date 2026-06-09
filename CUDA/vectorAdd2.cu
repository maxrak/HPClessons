#include <iostream>
#include <cuda_runtime.h>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <algorithm>

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

// Function to fill vector with random values
void fillRandomVector(float* vec, int N)
{
    for(int i = 0; i < N; i++)
    {
        vec[i] = static_cast<float>(rand()) / static_cast<float>(RAND_MAX) * 100.0f;
    }
}

// Print usage information
void printUsage(const char* progName)
{
    std::cerr << "Usage: " << progName << " <vector_size>\n"
              << "\nVector addition on GPU using CUDA\n"
              << "\nArguments:\n"
              << "  vector_size    Number of elements in vectors (positive integer)\n"
              << "\nOptions:\n"
              << "  -h, --help     Display this help message and exit\n"
              << "\nExample:\n"
              << "  " << progName << " 1024\n"
              << std::endl;
}

int main(int argc, char* argv[])
{
    // Handle command line arguments
    if (argc < 2 || strcmp(argv[1], "-h") == 0 || strcmp(argv[1], "--help") == 0)
    {
        printUsage(argv[0]);
        return (argc < 2) ? 1 : 0;
    }

    // Parse vector size
    int N = atoi(argv[1]);
    
    if (N <= 0)
    {
        std::cerr << "Error: vector_size must be a positive integer\n" << std::endl;
        printUsage(argv[0]);
        return 1;
    }

    // Seed random number generator
    srand(static_cast<unsigned>(time(nullptr)));

    size_t size = N * sizeof(float);

    // Host memory (CPU)

    float *h_A = new float[N];
    float *h_B = new float[N];
    float *h_C = new float[N];

    // Fill vectors with random values
    fillRandomVector(h_A, N);
    fillRandomVector(h_B, N);

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

    // Check result (print first 5 elements)
    
    std::cout << "\nVector addition completed for N = " << N << " elements\n";
    std::cout << "Showing first " << std::min(5, N) << " results:\n\n";

    for(int i = 0; i < std::min(5, N); i++)
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