#!/usr/bin/env python3
"""
Dimostrazione dell'uso di cProfile per il profiling di codice Python.
cProfile è un modulo built-in che analizza le prestazioni del programma.
"""

import cProfile
import pstats
from pstats import SortKey
import time


def funzione_veloce():
    """Funzione che esegue rapidamente."""
    somma = 0
    for i in range(1000):
        somma += i
    return somma


def funzione_lenta():
    """Funzione che richiede più tempo."""
    somma = 0
    for i in range(1000000):
        somma += i
    return somma


def funzione_con_sleep():
    """Funzione che simula operazioni I/O."""
    time.sleep(0.5)
    return "Completato"


def calcolo_fattoriale(n):
    """Calcola il fattoriale ricorsivamente."""
    if n <= 1:
        return 1
    return n * calcolo_fattoriale(n - 1)


def funzione_principale():
    """Funzione principale che chiama tutte le altre."""
    print("Inizio esecuzione...")
    
    # Chiama funzione veloce multiple volte
    for _ in range(10):
        funzione_veloce()
    
    # Chiama funzione lenta
    risultato_lento = funzione_lenta()
    
    # Chiama funzione con sleep
    risultato_sleep = funzione_con_sleep()
    
    # Calcola alcuni fattoriali
    for i in range(5, 10):
        calcolo_fattoriale(i)
    
    print("Esecuzione completata!")
    return risultato_lento


def esempio_base():
    """Esempio 1: Uso base di cProfile."""
    print("\n" + "="*60)
    print("ESEMPIO 1: Uso base di cProfile")
    print("="*60)
    
    # Profiling diretto con cProfile.run()
    cProfile.run('funzione_principale()')


def esempio_con_statistiche():
    """Esempio 2: Profiling con analisi dettagliata delle statistiche."""
    print("\n" + "="*60)
    print("ESEMPIO 2: Profiling con statistiche dettagliate")
    print("="*60)
    
    # Crea un profiler
    profiler = cProfile.Profile()
    
    # Avvia il profiling
    profiler.enable()
    funzione_principale()
    profiler.disable()
    
    # Analizza le statistiche
    stats = pstats.Stats(profiler)
    
    print("\n--- Ordinate per tempo totale ---")
    stats.sort_stats(SortKey.TIME)
    stats.print_stats(10)  # Mostra le prime 10 funzioni
    
    print("\n--- Ordinate per tempo cumulativo ---")
    stats.sort_stats(SortKey.CUMULATIVE)
    stats.print_stats(10)
    
    print("\n--- Ordinate per numero di chiamate ---")
    stats.sort_stats(SortKey.CALLS)
    stats.print_stats(10)


def esempio_salvataggio_risultati():
    """Esempio 3: Salvataggio dei risultati in un file."""
    print("\n" + "="*60)
    print("ESEMPIO 3: Salvataggio risultati in file")
    print("="*60)
    
    output_file = 'profile_results.prof'
    
    # Profiling e salvataggio in file
    cProfile.run('funzione_principale()', output_file)
    
    print(f"\nRisultati salvati in: {output_file}")
    print("Per visualizzarli successivamente, usa:")
    print(f"  python -m pstats {output_file}")
    
    # Carica e visualizza le statistiche dal file
    stats = pstats.Stats(output_file)
    stats.strip_dirs()  # Rimuove i percorsi dei file
    stats.sort_stats(SortKey.TIME)
    print("\n--- Prime 5 funzioni più lente ---")
    stats.print_stats(5)


def spiegazione_output():
    """Spiega come interpretare l'output di cProfile."""
    print("\n" + "="*60)
    print("INTERPRETAZIONE OUTPUT cProfile")
    print("="*60)
    print("""
Le colonne nell'output di cProfile significano:

- ncalls:     Numero di chiamate alla funzione
- tottime:    Tempo totale NELLA funzione (escludendo sottochiamate)
- percall:    tottime / ncalls
- cumtime:    Tempo cumulativo (incluse tutte le sottochiamate)
- percall:    cumtime / ncalls (chiamate primitive)
- filename:lineno(function): Posizione della funzione

Ordinamenti utili:
- SortKey.TIME:       Per trovare le funzioni più lente
- SortKey.CUMULATIVE: Per trovare le funzioni con più tempo totale
- SortKey.CALLS:      Per trovare le funzioni più chiamate
- SortKey.NAME:       Ordine alfabetico
    """)


if __name__ == "__main__":
    print("DIMOSTRAZIONE DI cProfile IN PYTHON")
    print("="*60)
    
    # Mostra spiegazione
    spiegazione_output()
    
    # Esegui gli esempi
    esempio_base()
    
    esempio_con_statistiche()
    
    esempio_salvataggio_risultati()
    
    print("\n" + "="*60)
    print("SUGGERIMENTI:")
    print("="*60)
    print("""
1. Per profilare uno script esistente:
   python -m cProfile -o output.prof mio_script.py

2. Per analizzare i risultati salvati:
   python -m pstats output.prof
   
3. Per visualizzazione grafica, installa snakeviz:
   pip install snakeviz
   snakeviz output.prof

4. Per linea per linea, usa line_profiler:
   pip install line_profiler
    """)
