from time import perf_counter
import numpy as np
import math
from mpi4py import MPI

def norm_l2_partial(x, start, end):
    """Calculate partial sum of squares"""
    sum_sq = 0.0
    for i in range(start, end):
        sum_sq += x[i] * x[i]
    return sum_sq

if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    
    n = 100_000_000
    
    # Only rank 0 creates the vector
    if rank == 0:
        x = np.random.rand(n)
    else:
        x = None
    
    # Broadcast vector to all processes
    x = comm.bcast(x, root=0)
    
    # Calculate chunk distribution
    chunk_size = n // size
    remainder = n % size
    
    if rank < remainder:
        start = rank * (chunk_size + 1)
        end = start + chunk_size + 1
    else:
        start = rank * chunk_size + remainder
        end = start + chunk_size
    
    # Synchronize and start timing
    comm.Barrier()
    starttime = perf_counter()
    
    # Each process computes partial sum
    partial_sum = norm_l2_partial(x, start, end)
    
    # Reduce: sum all partial results
    total_sum = comm.reduce(partial_sum, op=MPI.SUM, root=0)
    
    endtime = perf_counter()
    
    # Only rank 0 computes and prints final result
    if rank == 0:
        norm = math.sqrt(total_sum)
        print("MPI version")
        print("L2 norm: %.6f" % norm)
        print("Time spent: %.4f sec" % (endtime - starttime))
        print("Number of MPI processes: %d" % size)
