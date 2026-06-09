from time import perf_counter
import numpy as np
import math
from numba import njit, prange

@njit(parallel=True)
def norm_l2(x):
    """Calculate L2 norm with Numba parallelization"""
    sum_sq = 0.0
    for i in prange(len(x)):
        sum_sq += x[i] * x[i]
    return math.sqrt(sum_sq)

# Create random vector
n = 100_000_000
x = np.random.rand(n)

# Warm-up compilation
_ = norm_l2(x[:100])

starttime = perf_counter()
norm = norm_l2(x)
endtime = perf_counter()

print("Numba parallel version")
print("L2 norm: %.6f" % norm)
print("Time spent: %.4f sec" % (endtime - starttime))
