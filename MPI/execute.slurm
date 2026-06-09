#!/bin/bash

#SBATCH --job-name=testMPI

#SBATCH --nodes=2

#SBATCH --ntasks-per-node=2

#SBATCH --time=00:10:00

#SBATCH --partition=parallel

mpirun -np 4 $1