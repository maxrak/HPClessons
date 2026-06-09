from mpi4py import MPI
import math
from time import perf_counter

# grid size
n = 10000

def integration2d_mpi(n, start_i, end_i):
    # interval size (same for X and Y)
    h = math.pi / float(n)
    # cummulative variable
    mysum = 0.0

    # regular integration in the X axis (partial range)
    for i in range(start_i, end_i):
        x = h * (i + 0.5)
        # regular integration in the Y axis
        for j in range(n):
            y = h * (j + 0.5)
            mysum += math.sin(x + y)
    
    partial_integral = h**2 * mysum
    return partial_integral


if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    
    # Calcola il range di iterazioni per ogni processo
    chunk_size = n // size
    remainder = n % size
    
    # Distribuzione del lavoro
    if rank < remainder:
        start_i = rank * (chunk_size + 1)
        end_i = start_i + chunk_size + 1
    else:
        start_i = rank * chunk_size + remainder
        end_i = start_i + chunk_size
    
    # Sincronizza tutti i processi prima di iniziare
    comm.Barrier()
    starttime = perf_counter()
    
    # Ogni processo calcola la sua parte
    partial_integral = integration2d_mpi(n, start_i, end_i)
    
    # Riduzione: somma tutti i risultati parziali
    integral = comm.reduce(partial_integral, op=MPI.SUM, root=0)
    
    endtime = perf_counter()
    
    # Solo il processo 0 stampa il risultato
    if rank == 0:
        print("Integral value is %e, Error is %e" % (integral, abs(integral - 0.0)))
        print("Time spent: %.2f sec" % (endtime - starttime))
        print("Number of MPI processes: %d" % size)
