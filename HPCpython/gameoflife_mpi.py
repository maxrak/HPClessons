from time import perf_counter
import numpy as np
from mpi4py import MPI

def count_neighbors(grid, i, j):
    """Count living neighbors for cell (i,j) - includes ghost rows"""
    rows, cols = grid.shape
    count = 0
    
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if di == 0 and dj == 0:
                continue
            ni = i + di
            nj = (j + dj) % cols  # Periodic in columns
            if 0 <= ni < rows:
                count += grid[ni, nj]
    
    return count

def game_of_life_step_local(grid_with_ghosts, start_row, end_row):
    """Compute one generation for local rows (excluding ghost rows)"""
    rows, cols = grid_with_ghosts.shape
    new_grid = np.zeros((end_row - start_row, cols), dtype=np.int32)
    
    for i in range(end_row - start_row):
        for j in range(cols):
            # i+1 because of ghost row at top
            neighbors = count_neighbors(grid_with_ghosts, i + 1, j)
            
            if grid_with_ghosts[i + 1, j] == 1:  # Cell is alive
                if neighbors == 2 or neighbors == 3:
                    new_grid[i, j] = 1
            else:  # Cell is dead
                if neighbors == 3:
                    new_grid[i, j] = 1
    
    return new_grid

if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    
    n = 2000
    generations = 100
    
    # Only rank 0 creates the full grid
    if rank == 0:
        np.random.seed(42)
        full_grid = np.random.randint(0, 2, (n, n), dtype=np.int32)
        initial_alive = np.sum(full_grid)
    else:
        full_grid = None
        initial_alive = 0
    
    # Broadcast initial alive count
    initial_alive = comm.bcast(initial_alive, root=0)
    
    # Calculate row distribution
    chunk_size = n // size
    remainder = n % size
    
    if rank < remainder:
        start_row = rank * (chunk_size + 1)
        end_row = start_row + chunk_size + 1
    else:
        start_row = rank * chunk_size + remainder
        end_row = start_row + chunk_size
    
    local_rows = end_row - start_row
    
    # Scatter the grid rows to all processes
    if rank == 0:
        send_data = []
        for r in range(size):
            if r < remainder:
                s = r * (chunk_size + 1)
                e = s + chunk_size + 1
            else:
                s = r * chunk_size + remainder
                e = s + chunk_size
            send_data.append(full_grid[s:e, :])
        local_grid = send_data[rank]
    else:
        local_grid = None
    
    local_grid = comm.scatter(send_data if rank == 0 else None, root=0)
    
    # Determine neighbors for communication
    rank_above = (rank - 1) % size
    rank_below = (rank + 1) % size
    
    # Synchronize and start timing
    comm.Barrier()
    starttime = perf_counter()
    
    # Simulation loop
    for gen in range(generations):
        # Exchange ghost rows with neighbors
        # Send top row to above, receive from below
        top_row = local_grid[0, :].copy()
        bottom_row = local_grid[-1, :].copy()
        
        ghost_top = comm.sendrecv(top_row, dest=rank_above, source=rank_below)
        ghost_bottom = comm.sendrecv(bottom_row, dest=rank_below, source=rank_above)
        
        # Create grid with ghost rows
        grid_with_ghosts = np.vstack([ghost_top, local_grid, ghost_bottom])
        
        # Compute next generation for local rows
        local_grid = game_of_life_step_local(grid_with_ghosts, start_row, end_row)
    
    # Gather final grid at rank 0
    final_parts = comm.gather(local_grid, root=0)
    
    endtime = perf_counter()
    
    # Only rank 0 assembles and prints the result
    if rank == 0:
        final_grid = np.vstack(final_parts)
        final_alive = np.sum(final_grid)
        
        print("MPI version")
        print("Grid size: %d x %d" % (n, n))
        print("Generations: %d" % generations)
        print("Initial alive cells: %d" % initial_alive)
        print("Final alive cells: %d" % final_alive)
        print("Time spent: %.4f sec" % (endtime - starttime))
        print("Number of MPI processes: %d" % size)
