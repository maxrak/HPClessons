from time import perf_counter
import numpy as np

def count_neighbors(grid, i, j):
    """Count living neighbors for cell (i,j)"""
    rows, cols = grid.shape
    count = 0
    
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if di == 0 and dj == 0:
                continue
            ni = (i + di) % rows  # Periodic boundaries
            nj = (j + dj) % cols
            count += grid[ni, nj]
    
    return count

def game_of_life_step(grid):
    """Compute one generation of Conway's Game of Life"""
    rows, cols = grid.shape
    new_grid = np.zeros_like(grid)
    
    for i in range(rows):
        for j in range(cols):
            neighbors = count_neighbors(grid, i, j)
            
            if grid[i, j] == 1:  # Cell is alive
                if neighbors == 2 or neighbors == 3:
                    new_grid[i, j] = 1
            else:  # Cell is dead
                if neighbors == 3:
                    new_grid[i, j] = 1
    
    return new_grid

def simulate(grid, generations):
    """Run the Game of Life for multiple generations"""
    for gen in range(generations):
        grid = game_of_life_step(grid)
    return grid

# Initialize random grid
n = 2000
generations = 100
np.random.seed(42)
grid = np.random.randint(0, 2, (n, n))

initial_alive = np.sum(grid)

starttime = perf_counter()
final_grid = simulate(grid, generations)
endtime = perf_counter()

final_alive = np.sum(final_grid)

print("Serial version")
print("Grid size: %d x %d" % (n, n))
print("Generations: %d" % generations)
print("Initial alive cells: %d" % initial_alive)
print("Final alive cells: %d" % final_alive)
print("Time spent: %.4f sec" % (endtime - starttime))
