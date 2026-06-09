from time import perf_counter
import numpy as np
import math
from numba.openmp import njit
from numba.openmp import openmp_context as openmp

@njit
def norm_l2(x):
    """Calculate L2 norm with OpenMP parallelization"""
    sum_sq = 0.0
    with openmp("parallel for reduction(+:sum_sq)"):
        for i in range(len(x)):
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

print("OpenMP version")
print("L2 norm: %.6f" % norm)
print("Time spent: %.4f sec" % (endtime - starttime))
