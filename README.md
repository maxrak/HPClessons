# HPC Lessons - Quantum Computation Module

This repository contains materials and code examples for the **High Performance Computing (HPC) module** of the Quantum Computation course. It focuses on HPC architectures and parallel programming models, providing practical implementations and exercises.

## 📁 Repository Structure

### `CUDA/`
**GPU Programming with CUDA**
- CUDA runtime API examples
- GPU acceleration techniques
- Parallel computation on NVIDIA GPUs

### `MPI/`
**Message Passing Interface**
- Distributed memory parallel programming in C
- Point-to-point communication (Send/Recv)
- Collective operations (Broadcast, Scatter, Gather, Reduce, AllGather, All2All)
- Synchronization primitives (Barrier)
- Ring communication patterns
- SLURM job submission scripts

### `openMP/`
**Shared Memory Parallelism with OpenMP**
- Multi-threading in C using OpenMP directives
- Parallel loops and reductions
- Matrix multiplication examples
- Performance benchmarking scripts
- Results visualization

### `HPCpython/`
**HPC Programming in Python**
Python implementations of parallel algorithms using multiple approaches:
- **MPI** (mpi4py): Distributed computing
- **OpenMP** (via external libraries): Shared memory parallelism
- **Numba**: JIT compilation for GPU/CPU acceleration
- **Threading**: Multi-threaded implementations

Includes exercises on:
- Vector operations (dot product, L2 norm, matrix-vector multiplication)
- Numerical integration (2D integration, Monte Carlo π estimation)
- Cellular automata (Game of Life)

### `Profiling/`
**Performance Analysis Tools**
Documentation and examples for Python profiling:
- **cProfile**: Standard profiling tool
- **line_profiler**: Line-by-line performance analysis
- **memory_profiler**: Memory usage tracking
- Performance optimization techniques
- Pareto analysis for bottleneck identification

## 🎯 Learning Objectives

- Understand different HPC architectures and their programming models
- Compare shared memory vs. distributed memory paradigms
- Master GPU programming fundamentals
- Optimize code for performance and scalability
- Profile and analyze parallel applications

## 🚀 Getting Started

Each directory contains self-contained examples and exercises. Refer to individual folders for specific compilation and execution instructions.

### Prerequisites
- C compiler (gcc) with MPI and OpenMP support
- Python 3.x with HPC libraries (mpi4py, numba)
- CUDA toolkit (for GPU examples)
- SLURM (for cluster job submission)

## 📚 Course Context

This repository is part of the **Quantum Computation** curriculum, providing foundational knowledge in high-performance computing essential for quantum simulation and computational physics applications.

---

*Maintained for educational purposes*
