# Esercizi HPC in Python

## Esempi Introduttivi

### Esempio 1: Calcolo di Pi (Monte Carlo)

**Obiettivo**: Calcolare il valore di π usando l'integrazione numerica: `π = ∫[0,1] 4/(1+x²) dx`

**Dimensione del problema**: 1.000.000 di passi

**Concetti**:
- Riduzione semplice (somma)
- Parallelizzazione di un singolo loop
- Pattern di base per HPC

**File disponibili**:
- `pi.py` - Versione seriale
- `piOMP.py` - Versione OpenMP
- `pi_mpi.py` - Versione MPI

---

### Esempio 2: Prodotto Matrice-Matrice (Dot Product)

**Obiettivo**: Calcolare `C = A * A` dove A è una matrice quadrata

**Dimensione del problema**: Matrice 800×800 (per versioni parallele con cicli for)

**Concetti**:
- Parallelizzazione di cicli annidati
- Distribuzione del lavoro per righe
- Confronto con librerie ottimizzate (BLAS)

**File disponibili**:
- `dot.py` - Versione con `np.dot()` (ottimizzata BLAS)
- `dot_serial.py` - Versione seriale con cicli for
- `dot_numba.py` - Versione Numba con `prange`
- `dot_OMP.py` - Versione OpenMP
- `dot_mpi.py` - Versione MPI con distribuzione righe

**Nota**: `np.dot()` usa librerie BLAS ottimizzate ed è molto più veloce dei cicli for. Le versioni parallele dimostrano le tecniche ma non battono BLAS.

---

### Esempio 3: Integrazione 2D

**Obiettivo**: Calcolare l'integrale doppio: `∫∫ sin(x+y) dx dy` su [0,π]×[0,π]

**Dimensione del problema**: Griglia 10000×10000

**Concetti**:
- Parallelizzazione di cicli annidati
- Riduzione su doppio loop
- Distribuzione del lavoro in 2D

**File disponibili**:
- `integration2d_serial_initial.py` - Versione seriale Python puro
- `integration2d_serial_numba.py` - Versione seriale con Numba
- `integration2d_OMP.py` - Versione OpenMP
- `integration2d_mpi.py` - Versione MPI
- `integration2d_threading.py` - Versione con Python threading

---

## Esercizi da Completare

## Esercizio 1 (Facile): Calcolo della Norma L2 di un Vettore

**Obiettivo**: Calcolare la norma L2 (euclidea) di un vettore: `norm = sqrt(sum(x[i]^2))`

**Dimensione del problema**: Vettore di 100.000.000 elementi

**Concetti da apprendere**:
- Operazione di riduzione (somma)
- Parallelizzazione su singolo loop
- Pattern base di parallelizzazione

**File da completare**:
- `norm_l2_serial.py` - Versione seriale di riferimento
- `norm_l2_numba.py` - Usare `@njit(parallel=True)` con `prange`
- `norm_l2_OMP.py` - Usare `with openmp("parallel for reduction(+:sum)")`
- `norm_l2_mpi.py` - Distribuire il vettore, `reduce` con `MPI.SUM`

---

## Esercizio 2 (Medio): Moltiplicazione Matrice-Vettore

**Obiettivo**: Calcolare `y = A * x` dove A è una matrice (n×m) e x è un vettore (m)

**Dimensione del problema**: Matrice 10000×10000, vettore 10000 elementi

**Concetti da apprendere**:
- Distribuzione di righe della matrice
- Ogni processo/thread calcola parte del vettore risultato
- Operazione di gather per raccogliere i risultati

**File da completare**:
- `matvec_serial.py` - Doppio loop (righe e colonne)
- `matvec_numba.py` - Parallelizzazione sul loop esterno (righe)
- `matvec_OMP.py` - `parallel for` sul loop delle righe
- `matvec_mpi.py` - Ogni processo calcola un blocco di righe, poi `gather`

---

## Esercizio 3 (Difficile): Conway's Game of Life

**Obiettivo**: Simulare l'automa cellulare di Conway su una griglia 2D

**Regole del gioco**:
1. Una cella viva con 2 o 3 vicini vivi rimane viva
2. Una cella morta con esattamente 3 vicini vivi diventa viva
3. In tutti gli altri casi, la cella muore (o rimane morta)

**Dimensione del problema**: Griglia 2000×2000, 100 generazioni

**Concetti da apprendere**:
- Stencil computation 3×3 (conta 8 vicini)
- Iterazioni temporali multiple (generazioni)
- Double buffering (griglia corrente e griglia successiva)
- **MPI**: Decomposizione del dominio + halo exchange (scambio righe di bordo)

**File da completare**:
- `gameoflife_serial.py` - Doppio loop su griglia, conta vicini, applica regole
- `gameoflife_numba.py` - `@njit(parallel=True)` con `prange` sulle righe
- `gameoflife_OMP.py` - `parallel for` sulle righe della griglia
- `gameoflife_mpi.py` - Ogni processo gestisce un blocco di righe + `Sendrecv` per ghost rows

**Sfide dell'esercizio 3**:
- Gestione corretta dei bordi (periodici o fissi)
- Comunicazione efficiente delle righe fantasma (ghost rows) in MPI
- Sincronizzazione tra generazioni

---

## Esecuzione

### Versioni seriali, Numba e OpenMP:
```bash
python <nome_file>.py
```

### Versione MPI:
```bash
mpiexec -np 4 python <nome_file>_mpi.py
```

## Metriche di Performance

Per ogni esercizio, confrontare:
1. Tempo di esecuzione
2. Speedup: `T_serial / T_parallel`
3. Efficienza: `Speedup / N_processes`

## Progressione didattica

**Esempi introduttivi** (già implementati):
- **Pi**: Riduzione semplice, primo approccio alla parallelizzazione
- **Dot**: Cicli annidati, confronto con librerie ottimizzate
- **Integration2D**: Riduzione su griglia 2D

**Esercizi da completare**:
1. **Norma L2**: Pattern di riduzione con quadrati
2. **Matrice-Vettore**: Distribuzione righe e gather
3. **Game of Life**: Stencil 2D, comunicazioni punto-a-punto, halo exchange
