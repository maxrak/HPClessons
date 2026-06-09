from time import perf_counter
import numpy as np
from numba.openmp import njit
from numba.openmp import openmp_context as openmp

@njit
def dot_product_omp(A, B):
    """Matrix multiplication using OpenMP parallelization"""
    m, n = A.shape
    p = B.shape[1]
    
    C = np.zeros((m, p))
    
    # Parallel outer loop with OpenMP
    with openmp("parallel for"):
        for i in range(m):
            for j in range(p):
                temp = 0.0
                for k in range(n):
                    temp += A[i, k] * B[k, j]
                C[i, j] = temp
    
    return C

# Create random matrix (800x800 for reasonable execution time)
A = np.random.rand(800, 800)

# First call to compile the function
_ = dot_product_omp(A[:2, :2], A[:2, :2])

starttime = perf_counter()
B = dot_product_omp(A, A)
endtime = perf_counter()

print("OpenMP version")
print("Time spent: %.2f sec" % (endtime - starttime))
