#!/usr/bin/env python3
"""
ESEMPIO 2: Profiling con statistiche dettagliate
=================================================

Questo esempio mostra come usare cProfile.Profile() per avere
un controllo maggiore sul profiling e come ordinare/filtrare
le statistiche in modi diversi.
"""

import cProfile
import pstats
from pstats import SortKey
from funzioni_test import (funzione_veloce, funzione_lenta, 
                           calcolo_fattoriale, operazione_complessa)


def main():
    """Funzione principale."""
    print("Esecuzione operazioni complesse...")
    
    # Operazioni multiple
    for _ in range(5):
        funzione_veloce()
    
    funzione_lenta()
    
    for i in range(5, 12):
        calcolo_fattoriale(i)
    
    operazione_complessa()
    
    print("Operazioni completate!")


if __name__ == "__main__":
    print("="*70)
    print("ESEMPIO 2: Profiling con controllo delle statistiche")
    print("="*70)
    
    # Crea un oggetto profiler
    profiler = cProfile.Profile()
    
    # Avvia il profiling
    profiler.enable()
    main()
    profiler.disable()
    
    # Crea oggetto statistiche
    stats = pstats.Stats(profiler)
    stats.strip_dirs()  # Rimuove percorsi completi dei file
    
    # STATISTICHE ORDINATE PER TEMPO TOTALE
    print("\n" + "="*70)
    print("1. ORDINATE PER TEMPO TOTALE (tottime)")
    print("="*70)
    print("Mostra quali funzioni consumano più tempo ESCLUDENDO le chiamate interne")
    stats.sort_stats(SortKey.TIME)
    stats.print_stats(8)
    
    # STATISTICHE ORDINATE PER TEMPO CUMULATIVO
    print("\n" + "="*70)
    print("2. ORDINATE PER TEMPO CUMULATIVO (cumtime)")
    print("="*70)
    print("Mostra quali funzioni consumano più tempo INCLUDENDO le chiamate interne")
    stats.sort_stats(SortKey.CUMULATIVE)
    stats.print_stats(8)
    
    # STATISTICHE ORDINATE PER NUMERO DI CHIAMATE
    print("\n" + "="*70)
    print("3. ORDINATE PER NUMERO DI CHIAMATE (ncalls)")
    print("="*70)
    print("Mostra quali funzioni vengono chiamate più spesso")
    stats.sort_stats(SortKey.CALLS)
    stats.print_stats(8)
    
    # FILTRARE PER NOME FILE
    print("\n" + "="*70)
    print("4. FILTRATE PER FILE (solo funzioni_test.py)")
    print("="*70)
    print("Mostra solo le funzioni del nostro modulo")
    stats.sort_stats(SortKey.TIME)
    stats.print_stats('funzioni_test')
    
    print("\n" + "="*70)
    print("SUGGERIMENTI:")
    print("="*70)
    print("""
- Usa TIME per trovare hotspot nel codice stesso
- Usa CUMULATIVE per trovare funzioni che chiamano operazioni lente
- Usa CALLS per trovare funzioni chiamate troppo spesso
- Usa print_stats(n) per limitare l'output alle prime n righe
- Usa print_stats('pattern') per filtrare per nome file/funzione
    """)
