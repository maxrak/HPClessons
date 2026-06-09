#include <iostream>
#include <cuda_runtime.h>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cstdio>
#include <algorithm>

__global__
void matrixMul(float* A, float* B, float* C, int n)
{
    int row = blockIdx.y * blockDim.y + threadIdx.y;
    int col = blockIdx.x * blockDim.x + threadIdx.x;

    if (row < n && col < n)
    {
        float sum = 0.0f;

        for (int k = 0; k < n; k++)
        {
            sum += A[row * n + k] * B[k * n + col];
        }

        C[row * n + col] = sum;
    }
}

// Function to fill matrix with random values
void fillRandomMatrix(float* mat, int rows, int cols)
{
    for(int i = 0; i < rows * cols; i++)
    {
        mat[i] = static_cast<float>(rand()) / static_cast<float>(RAND_MAX) * 10.0f;
    }
}

// Print usage information
void printUsage(const char* progName)
{
    std::cerr << "Usage: " << progName << " <matrix_size>\n"
              << "\nMatrix multiplication on GPU using CUDA (C = A * B)\n"
              << "\nArguments:\n"
              << "  matrix_size    Dimension of square matrices (NxN, positive integer)\n"
              << "\nOptions:\n"
              << "  -h, --help     Display this help message and exit\n"
              << "\nExample:\n"
              << "  " << progName << " 512    # Multiplies two 512x512 matrices\n"
              << std::endl;
}

// Print a small portion of the matrix
void printMatrixSample(const char* name, float* mat, int n, int maxPrint = 4)
{
    int printSize = std::min(maxPrint, n);
    std::cout << "\n" << name << " (showing " << printSize << "x" << printSize 
              << " corner of " << n << "x" << n << " matrix):\n";
    
    for(int i = 0; i < printSize; i++)
    {
        for(int j = 0; j < printSize; j++)
        {
            printf("%8.2f ", mat[i * n + j]);
        }
        std::cout << std::endl;
    }
}

int main(int argc, char* argv[])
{
    // Handle command line arguments
    if (argc < 2 || strcmp(argv[1], "-h") == 0 || strcmp(argv[1], "--help") == 0)
    {
        printUsage(argv[0]);
        return (argc < 2) ? 1 : 0;
    }

    // Parse matrix size
    int N = atoi(argv[1]);
    
    if (N <= 0)
    {
        std::cerr << "Error: matrix_size must be a positive integer\n" << std::endl;
        printUsage(argv[0]);
        return 1;
    }

    std::cout << "Matrix multiplication: C(" << N << "x" << N << ") = "
              << "A(" << N << "x" << N << ") * B(" << N << "x" << N << ")\n";

    // Seed random number generator
    srand(static_cast<unsigned>(time(NULL)));

    size_t size = N * N * sizeof(float);

    // Host memory (CPU)
    float *h_A = new float[N * N];
    float *h_B = new float[N * N];
    float *h_C = new float[N * N];

    // Fill matrices with random values
    fillRandomMatrix(h_A, N, N);
    fillRandomMatrix(h_B, N, N);

    // Print samples of input matrices
    if (N <= 16)
    {
        printMatrixSample("Matrix A", h_A, N);
        printMatrixSample("Matrix B", h_B, N);
    }

    // Device memory (GPU)
    float *d_A, *d_B, *d_C;

    cudaMalloc(&d_A, size);
    cudaMalloc(&d_B, size);
    cudaMalloc(&d_C, size);

    // Copy CPU -> GPU
    cudaMemcpy(d_A, h_A, size, cudaMemcpyHostToDevice);
    cudaMemcpy(d_B, h_B, size, cudaMemcpyHostToDevice);

    // Launch kernel
    dim3 threadsPerBlock(16, 16);
    dim3 blocksPerGrid(
        (N + threadsPerBlock.x - 1) / threadsPerBlock.x,
        (N + threadsPerBlock.y - 1) / threadsPerBlock.y
    );

    std::cout << "\nLaunching kernel with:" << std::endl;
    std::cout << "  Blocks per grid: (" << blocksPerGrid.x << ", " 
              << blocksPerGrid.y << ")" << std::endl;
    std::cout << "  Threads per block: (" << threadsPerBlock.x << ", " 
              << threadsPerBlock.y << ")" << std::endl;

    matrixMul<<<blocksPerGrid, threadsPerBlock>>>(d_A, d_B, d_C, N);

    // Wait for GPU to finish
    cudaDeviceSynchronize();

    // Copy GPU -> CPU
    cudaMemcpy(h_C, d_C, size, cudaMemcpyDeviceToHost);

    // Print result sample
    printMatrixSample("Matrix C (Result)", h_C, N);

    // Verify one element manually (optional)
    if (N <= 16)
    {
        float expected = 0.0f;
        for(int k = 0; k < N; k++)
        {
            expected += h_A[k] * h_B[k * N];
        }
        std::cout << "\nVerification: C[0][0] = " << h_C[0] 
                  << " (CPU check: " << expected << ")" << std::endl;
    }
    else
    {
        std::cout << "\nC[0][0] = " << h_C[0] << std::endl;
    }

    std::cout << "\nMatrix multiplication completed successfully!" << std::endl;

    // Cleanup
    cudaFree(d_A);
    cudaFree(d_B);
    cudaFree(d_C);

    delete[] h_A;
    delete[] h_B;
    delete[] h_C;

    return 0;
}
