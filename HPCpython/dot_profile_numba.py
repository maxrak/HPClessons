import cProfile
import pstats
import numpy as np
from numba import njit, prange

#@njit(parallel=True, fastmath=True)
def dot_product_numba(A, B):
    """Matrix multiplication with Numba parallelization"""
    m, n = A.shape
    p = B.shape[1]
    
    C = np.zeros((m, p))
    
    # Parallel outer loop
    for i in prange(m):
        for j in range(p):
            temp = 0.0
            for k in range(n):
                temp += A[i, k] * B[k, j]
            C[i, j] = temp
    
    return C

# Create random matrix (800x800 for reasonable execution time)
A = np.random.rand(800, 800)

# First call to compile the function
_ = dot_product_numba(A[:2, :2], A[:2, :2])
profiler = cProfile.Profile()

profiler.enable
B = dot_product_numba(A, A)
profiler.disable

stats = pstats.Stats(profiler)
stats.print_stats(100)

