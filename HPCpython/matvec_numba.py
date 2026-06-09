from time import perf_counter
import numpy as np
from numba import njit, prange

@njit(parallel=True)
def matvec(A, x):
    """Matrix-vector multiplication with Numba parallelization"""
    m, n = A.shape
    y = np.zeros(m)
    
    for i in prange(m):
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

print("Numba parallel version")
print("Result vector norm: %.6f" % np.linalg.norm(y))
print("Time spent: %.4f sec" % (endtime - starttime))
