from time import perf_counter
from mpi4py import MPI

def calc_pi_mpi(num_steps, start, end):
    """Calculate pi for a subset of iterations"""
    step = 1.0 / num_steps
    partial_sum = 0.0
    
    for j in range(start, end):
        x = ((j - 1) - 0.5) * step
        partial_sum += 4.0 / (1.0 + x * x)
    
    return partial_sum


if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    
    num_steps = 100000000
    
    # Calculate iteration distribution
    chunk_size = num_steps // size
    remainder = num_steps % size
    
    # Distribute iterations
    if rank < remainder:
        start = rank * (chunk_size + 1)
        end = start + chunk_size + 1
    else:
        start = rank * chunk_size + remainder
        end = start + chunk_size
    
    # Synchronize and start timing
    comm.Barrier()
    starttime = perf_counter()
    
    # Each process calculates its portion
    partial_sum = calc_pi_mpi(num_steps, start, end)
    
    # Reduce: sum all partial results
    total_sum = comm.reduce(partial_sum, op=MPI.SUM, root=0)
    
    endtime = perf_counter()
    
    # Only rank 0 computes and prints the final result
    if rank == 0:
        step = 1.0 / num_steps
        pi = step * total_sum
        print("Pi value is %e" % pi)
        print("Time spent: %.2f sec" % (endtime - starttime))
        print("Number of MPI processes: %d" % size)
