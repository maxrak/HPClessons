from time import perf_counter
import numpy as np
from numba.openmp import njit
from numba.openmp import openmp_context as openmp

@njit
def matvec(A, x):
    """Matrix-vector multiplication with OpenMP parallelization"""
    m, n = A.shape
    y = np.zeros(m)
    
    with openmp("parallel for"):
        for i in range(m):
            temp = 0.0
            for j in range(n):
                temp += A[i, j] * x[j]
            y[i] = temp
    
    return y

# Create random matrix and vector
n = 10_000
A = np.random.rand(n, n)
x = np.random.rand(n)

# Warm-up compilation
_ = matvec(A[:10, :10], x[:10])

starttime = perf_counter()
y = matvec(A, x)
endtime = perf_counter()

print("OpenMP version")
print("Result vector norm: %.6f" % np.linalg.norm(y))
print("Time spent: %.4f sec" % (endtime - starttime))
