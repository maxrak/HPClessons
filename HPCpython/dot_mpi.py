from time import perf_counter
import numpy as np
from mpi4py import MPI

def dot_product_rows(A, B, start_row, end_row):
    """Compute matrix multiplication for a subset of rows"""
    m = end_row - start_row
    n = A.shape[1]
    p = B.shape[1]
    
    C_partial = np.zeros((m, p))
    
    for i in range(m):
        for j in range(p):
            temp = 0.0
            for k in range(n):
                temp += A[start_row + i, k] * B[k, j]
            C_partial[i, j] = temp
    
    return C_partial

if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    
    # Only rank 0 creates the matrix
    if rank == 0:
        A = np.random.rand(3000, 3000)
    else:
        A = None
    
    # Broadcast matrix A to all processes
    A = comm.bcast(A, root=0)
    
    # Calculate row distribution
    m = A.shape[0]
    chunk_size = m // size
    remainder = m % size
    
    # Distribute rows
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
    C_partial = dot_product_rows(A, A, start_row, end_row)
    
    # Gather all partial results at rank 0
    C_list = comm.gather(C_partial, root=0)
    
    endtime = perf_counter()
    
    # Only rank 0 assembles and prints the result
    if rank == 0:
        C = np.vstack(C_list)
        print("MPI version")
        print("Time spent: %.2f sec" % (endtime - starttime))
        print("Number of MPI processes: %d" % size)
