from time import perf_counter
import numpy as np
import math

def norm_l2(x):
    """Calculate L2 norm (Euclidean norm) of a vector"""
    sum_sq = 0.0
    for i in range(len(x)):
        sum_sq += x[i] * x[i]
    return math.sqrt(sum_sq)

# Create random vector
n = 100_000_000
x = np.random.rand(n)

starttime = perf_counter()
norm = norm_l2(x)
endtime = perf_counter()

print("Serial version")
print("L2 norm: %.6f" % norm)
print("Time spent: %.4f sec" % (endtime - starttime))
