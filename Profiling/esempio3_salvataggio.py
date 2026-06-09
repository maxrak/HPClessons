#!/usr/bin/env python3
"""
ESEMPIO 3: Salvataggio e caricamento risultati
===============================================

Questo esempio mostra come salvare i risultati del profiling
in un file per analisi successive e come caricarli.
"""

import cProfile
import pstats
from pstats import SortKey
import os
from funzioni_test import operazione_complessa, calcolo_fattoriale


def calcoli_pesanti():
    """Esegue calcoli intensivi."""
    print("Esecuzione calcoli pesanti...")
    
    risultati = []
    for i in range(10, 15):
        risultati.append(calcolo_fattoriale(i))
    
    for _ in range(3):
        risultati.append(operazione_complessa())
    
    print(f"Completato! Totale: {sum(risultati)}")
    return risultati


if __name__ == "__main__":
    print("="*70)
    print("ESEMPIO 3: Salvataggio risultati profiling")
    print("="*70)
    
    output_file = 'profile_results.prof'
    
    # METODO 1: Salvataggio diretto con cProfile.run()
    print(f"\n1. Salvataggio in {output_file}...")
    cProfile.run('calcoli_pesanti()', output_file)
    print(f"✓ Risultati salvati!")
    
    # Verifica che il file esista
    if os.path.exists(output_file):
        print(f"✓ File {output_file} creato ({os.path.getsize(output_file)} bytes)")
    
    # METODO 2: Caricamento e analisi dal file
    print("\n" + "="*70)
    print("2. Caricamento e analisi risultati")
    print("="*70)
    
    stats = pstats.Stats(output_file)
    stats.strip_dirs()
    
    print("\n--- Top 5 funzioni per tempo totale ---")
    stats.sort_stats(SortKey.TIME)
    stats.print_stats(5)
    
    print("\n--- Top 5 funzioni per tempo cumulativo ---")
    stats.sort_stats(SortKey.CUMULATIVE)
    stats.print_stats(5)
    
    # METODO 3: Uso da linea di comando
    print("\n" + "="*70)
    print("3. Analisi da linea di comando")
    print("="*70)
    print(f"""
Puoi anche analizzare il file {output_file} dalla shell:

    python -m pstats {output_file}

Questo apre una shell interattiva dove puoi:
    - sort time      # Ordina per tempo
    - sort cumulative # Ordina per tempo cumulativo
    - stats 10       # Mostra top 10
    - stats pattern  # Filtra per pattern
    - help           # Mostra tutti i comandi
    """)
    
    # METODO 4: Profiling di script esistenti
    print("\n" + "="*70)
    print("4. Profilare script esistenti")
    print("="*70)
    print("""
Per profilare un qualsiasi script Python:

    python -m cProfile -o output.prof mio_script.py

Questo esegue mio_script.py e salva il profiling in output.prof
    """)
    
    # BONUS: Visualizzazione grafica
    print("\n" + "="*70)
    print("BONUS: Visualizzazione grafica con SnakeViz")
    print("="*70)
    print(f"""
Installa SnakeViz per visualizzare i risultati graficamente:

    pip install snakeviz
    snakeviz {output_file}

Questo aprirà un browser con una visualizzazione interattiva!
    """)
    
    print("\n✓ Esempio completato!")
    print(f"✓ File {output_file} disponibile per analisi")
