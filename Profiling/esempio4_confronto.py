#!/usr/bin/env python3
"""
ESEMPIO 4: Confronto tra implementazioni diverse
=================================================

Questo esempio mostra come usare cProfile per confrontare
diverse implementazioni dello stesso algoritmo e identificare
quale è più efficiente.
"""

import cProfile
import pstats
from pstats import SortKey
from io import StringIO
from funzioni_test import fibonacci_ricorsivo, fibonacci_iterativo


def test_fibonacci_ricorsivo():
    """Test dell'implementazione ricorsiva di Fibonacci."""
    print("Fibonacci ricorsivo...")
    risultati = []
    for i in range(15, 25):
        risultati.append(fibonacci_ricorsivo(i))
    print(f"Completato: {risultati[-1]}")
    return risultati


def test_fibonacci_iterativo():
    """Test dell'implementazione iterativa di Fibonacci."""
    print("Fibonacci iterativo...")
    risultati = []
    for i in range(15, 25):
        risultati.append(fibonacci_iterativo(i))
    print(f"Completato: {risultati[-1]}")
    return risultati


def profila_funzione(func_name, func):
    """Profila una funzione e ritorna le statistiche."""
    profiler = cProfile.Profile()
    
    profiler.enable()
    func()
    profiler.disable()
    
    # Cattura l'output in una stringa
    stream = StringIO()
    stats = pstats.Stats(profiler, stream=stream)
    stats.strip_dirs()
    stats.sort_stats(SortKey.CUMULATIVE)
    stats.print_stats(10)
    
    return stats, stream.getvalue()


if __name__ == "__main__":
    print("="*70)
    print("ESEMPIO 4: Confronto tra implementazioni")
    print("="*70)
    print("\nConfronto: Fibonacci ricorsivo vs iterativo")
    print("Calcoleremo Fibonacci per i numeri da 15 a 24\n")
    
    # Profila implementazione ricorsiva
    print("\n" + "="*70)
    print("IMPLEMENTAZIONE RICORSIVA")
    print("="*70)
    stats_ric, output_ric = profila_funzione("ricorsivo", test_fibonacci_ricorsivo)
    print(output_ric)
    
    # Profila implementazione iterativa
    print("\n" + "="*70)
    print("IMPLEMENTAZIONE ITERATIVA")
    print("="*70)
    stats_iter, output_iter = profila_funzione("iterativo", test_fibonacci_iterativo)
    print(output_iter)
    
    # Confronto diretto
    print("\n" + "="*70)
    print("CONFRONTO DIRETTO")
    print("="*70)
    
    # Estrai statistiche chiave
    stats_ric.sort_stats(SortKey.CUMULATIVE)
    stats_iter.sort_stats(SortKey.CUMULATIVE)
    
    print("\nStatistiche ricorsive (fibonacci_ricorsivo):")
    stats_ric.print_stats('fibonacci_ricorsivo', 1)
    
    print("\nStatistiche iterative (fibonacci_iterativo):")
    stats_iter.print_stats('fibonacci_iterativo', 1)
    
    # Conclusioni
    print("\n" + "="*70)
    print("CONCLUSIONI")
    print("="*70)
    print("""
Osservazioni chiave:

1. NUMERO DI CHIAMATE (ncalls):
   - Ricorsivo: migliaia/milioni di chiamate ricorsive
   - Iterativo: solo 10 chiamate (una per ogni numero)

2. TEMPO DI ESECUZIONE:
   - Ricorsivo: molto più lento (crescita esponenziale)
   - Iterativo: molto più veloce (crescita lineare)

3. PERCHÉ LA DIFFERENZA?
   - Ricorsivo: ricalcola gli stessi valori molte volte
   - Iterativo: calcola ogni valore una sola volta

LEZIONE: cProfile aiuta a identificare algoritmi inefficienti!

OTTIMIZZAZIONI POSSIBILI:
- Usare memoization per la versione ricorsiva
- Preferire implementazioni iterative quando possibile
- Identificare funzioni chiamate troppe volte
    """)
    
    print("\n✓ Esempio completato!")
