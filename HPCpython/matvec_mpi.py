from time import perf_counter
import numpy as np
from mpi4py import MPI

def matvec_partial(A, x, start_row, end_row):
    """Compute matrix-vector multiplication for a subset of rows"""
    m = end_row - start_row
    n = A.shape[1]
    y_partial = np.zeros(m)
    
    for i in range(m):
        for j in range(n):
            y_partial[i] += A[start_row + i, j] * x[j]
    
    return y_partial

if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    
    n = 10_000
    
    # Only rank 0 creates the matrix and vector
    if rank == 0:
        A = np.random.rand(n, n)
        x = np.random.rand(n)
    else:
        A = None
        x = None
    
    # Broadcast matrix and vector to all processes
    A = comm.bcast(A, root=0)
    x = comm.bcast(x, root=0)
    
    # Calculate row distribution
    m = A.shape[0]
    chunk_size = m // size
    remainder = m % size
    
    if rank < remainder:
        start_row = rank * (chunk_size + 1)
        end_row = start_row + chunk_size + 1
    else:
        start_row = rank * chunk_size + remainder
        end_row = start_row + chunk_size
    
    # Synchronize and start timing
    comm.Barrier()
    starttime = perf_counter()
    
    # Each process computes its portion
    y_partial = matvec_partial(A, x, start_row, end_row)
    
    # Gather all partial results at rank 0
    y_list = comm.gather(y_partial, root=0)
    
    endtime = perf_counter()
    
    # Only rank 0 assembles and prints the result
    if rank == 0:
        y = np.concatenate(y_list)
        print("MPI version")
        print("Result vector norm: %.6f" % np.linalg.norm(y))
        print("Time spent: %.4f sec" % (endtime - starttime))
        print("Number of MPI processes: %d" % size)
