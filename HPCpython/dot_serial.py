from time import perf_counter
import numpy as np

def dot_product_serial(A, B):
    """Matrix multiplication with pure Python loops (no optimization)"""
    m, n = A.shape
    p = B.shape[1]
    
    C = np.zeros((m, p))
    
    for i in range(m):
        for j in range(p):
            temp = 0.0
            for k in range(n):
                temp += A[i, k] * B[k, j]
            C[i, j] = temp
    
    return C

# Create random matrix (800x800 same as other versions)
A = np.random.rand(800, 800)

starttime = perf_counter()
B = dot_product_serial(A, A)
endtime = perf_counter()

print("Serial version (no optimization)")
print("Time spent: %.2f sec" % (endtime - starttime))
