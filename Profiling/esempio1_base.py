#!/usr/bin/env python3
"""
ESEMPIO 1: Uso base di cProfile
================================

Questo esempio mostra il modo più semplice di usare cProfile:
utilizzando cProfile.run() per profilare una singola funzione.
"""

import cProfile
from funzioni_test import funzione_veloce, funzione_lenta, funzione_con_sleep


def main():
    """Funzione principale che esegue diverse operazioni."""
    print("Esecuzione di operazioni diverse...")
    
    # Chiama funzione veloce
    for _ in range(10):
        funzione_veloce()
    
    # Chiama funzione lenta
    funzione_lenta()
    
    # Chiama funzione con I/O
    funzione_con_sleep()
    
    print("Operazioni completate!")


if __name__ == "__main__":
    print("="*70)
    print("ESEMPIO 1: Uso base di cProfile")
    print("="*70)
    print("\nUtilizzo: cProfile.run('funzione()')")
    print("\nQuesto è il modo più semplice per profilare il tuo codice.")
    print("cProfile mostrerà tutte le funzioni chiamate e il loro tempo di esecuzione.\n")
    
    # Profiling base - passa la funzione come stringa
    cProfile.run('main()')
    
    print("\n" + "="*70)
    print("LEGGERE L'OUTPUT:")
    print("="*70)
    print("""
Colonne importanti:
- ncalls:  Numero di volte che la funzione è stata chiamata
- tottime: Tempo totale NELLA funzione (escluse le chiamate ad altre funzioni)
- cumtime: Tempo cumulativo (incluse tutte le sottofunzioni)

Nota: funzione_con_sleep() avrà un cumtime alto perché include time.sleep()!
    """)
