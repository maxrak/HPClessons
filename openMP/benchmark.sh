#!/bin/bash

# Script per testare somma matrici con diverse dimensioni e chunk size

echo "=========================================="
echo "BENCHMARK SOMMA MATRICI"
echo "=========================================="
echo ""

# Ottieni il numero di thread (da OMP_NUM_THREADS o usa nproc)
if [ -z "$OMP_NUM_THREADS" ]; then
    num_threads=$(nproc)
    echo "OMP_NUM_THREADS non impostato, uso: $num_threads thread (da nproc)"
else
    num_threads=$OMP_NUM_THREADS
    echo "Usando OMP_NUM_THREADS: $num_threads thread"
fi
echo ""

# Array delle dimensioni da testare
dimensioni=(100 200 300 400 500 600 700 800 900 1000)

# Valori di K da testare
valori_k=(1 2 5)

# File di output per i risultati
output_file="risultati_benchmark.txt"
echo "RISULTATI BENCHMARK - $(date)" > "$output_file"
echo "Numero di thread: $num_threads" >> "$output_file"
echo "=========================================" >> "$output_file"
echo "" >> "$output_file"

# Ciclo su tutte le dimensioni
for dim in "${dimensioni[@]}"
do
    echo "=========================================="
    echo "Testing con dimensione: ${dim}x${dim}"
    echo "=========================================="
    
    # Salva i risultati nel file
    echo "=========================================" >> "$output_file"
    echo "DIMENSIONE: ${dim}x${dim}" >> "$output_file"
    echo "=========================================" >> "$output_file"
    
    # Modifica il file sommasequenziale.c
    sed -i "s/#define RIGHE.*/#define RIGHE   ${dim}/" sommasequenziale.c
    sed -i "s/#define COLONNE.*/#define COLONNE   ${dim}/" sommasequenziale.c
    
    echo ""
    echo "--- VERSIONE SEQUENZIALE ---"
    echo "--- VERSIONE SEQUENZIALE ---" >> "$output_file"
    
    # Compila ed esegue versione sequenziale
    gcc -o sommas sommasequenziale.c -lm
    if [ $? -eq 0 ]; then
        echo "Compilazione sequenziale: OK"
        echo "Esecuzione in corso..."
        { time ./sommas ; } 2>&1 | tee -a "$output_file"
    else
        echo "ERRORE: Compilazione sequenziale fallita" | tee -a "$output_file"
    fi
    
    echo ""
    
    # Ciclo sui valori di K per la versione parallela
    for k in "${valori_k[@]}"
    do
        # Calcola chunk size: dimensione / (k * num_threads)
        chunk=$((dim / (k * num_threads)))
        
        # Assicurati che chunk sia almeno 1
        if [ $chunk -lt 1 ]; then
            chunk=1
        fi
        
        echo "--- VERSIONE PARALLELA (K=${k}, CHUNK=${chunk}) ---"
        echo "--- VERSIONE PARALLELA (K=${k}, CHUNK=${chunk}) ---" >> "$output_file"
        
        # Modifica il file sommaparallelo.c
        sed -i "s/#define RIGHE.*/#define RIGHE   ${dim}/" sommaparallelo.c
        sed -i "s/#define COLONNE.*/#define COLONNE   ${dim}/" sommaparallelo.c
        sed -i "s/#define CHUNK.*/#define CHUNK   ${chunk}/" sommaparallelo.c
        
        # Compila ed esegue versione parallela
        gcc -o sommap sommaparallelo.c -fopenmp -lm
        if [ $? -eq 0 ]; then
            echo "Compilazione parallela: OK"
            echo "Esecuzione in corso... (dim=${dim}, k=${k}, chunk=${chunk}, threads=${num_threads})"
            { time ./sommap ; } 2>&1 | tee -a "$output_file"
        else
            echo "ERRORE: Compilazione parallela fallita" | tee -a "$output_file"
        fi
        
        echo "" >> "$output_file"
        echo ""
    done
    
done

echo "=========================================="
echo "BENCHMARK COMPLETATO!"
echo "=========================================="
echo "Risultati salvati in: $output_file"
echo ""

# Mostra un riepilogo
echo "=== RIEPILOGO ==="
echo "File testati:"
echo "  - sommasequenziale.c"
echo "  - sommaparallelo.c"
echo ""
echo "Dimensioni testate: ${dimensioni[@]}"
echo "Valori K testati: ${valori_k[@]}"
echo "Numero di thread: $num_threads"
echo ""
echo "Formula chunk size: dimensione / (K × num_threads)"
echo ""
