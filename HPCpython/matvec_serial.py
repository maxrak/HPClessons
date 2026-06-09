from time import perf_counter
import numpy as np

def matvec(A, x):
    """Matrix-vector multiplication y = A * x"""
    m, n = A.shape
    y = np.zeros(m)
    
    for i in range(m):
        for j in range(n):
            y[i] += A[i, j] * x[j]
    
    return y

# Create random matrix and vector
n = 10_000
A = np.random.rand(n, n)
x = np.random.rand(n)

starttime = perf_counter()
y = matvec(A, x)
endtime = perf_counter()

print("Serial version")
print("Result vector norm: %.6f" % np.linalg.norm(y))
print("Time spent: %.4f sec" % (endtime - starttime))
