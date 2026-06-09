#!/usr/bin/env python3
"""
ESEMPIO 5: Profiling selettivo con context manager
===================================================

Questo esempio mostra come profilare solo sezioni specifiche
del codice usando il profiler come context manager.
"""

import cProfile
import pstats
from pstats import SortKey
from funzioni_test import (funzione_veloce, funzione_lenta, 
                           calcolo_fattoriale, operazione_complessa)


def fase_inizializzazione():
    """Fase di inizializzazione (NON profilata)."""
    print("Fase 1: Inizializzazione...")
    for _ in range(1000):
        _ = [i**2 for i in range(100)]
    print("✓ Inizializzazione completata")


def fase_elaborazione():
    """Fase di elaborazione (DA PROFILARE)."""
    print("\nFase 2: Elaborazione...")
    
    # Operazioni varie
    for _ in range(5):
        funzione_veloce()
    
    funzione_lenta()
    
    for i in range(8, 12):
        calcolo_fattoriale(i)
    
    print("✓ Elaborazione completata")


def fase_finalizzazione():
    """Fase di finalizzazione (NON profilata)."""
    print("\nFase 3: Finalizzazione...")
    for _ in range(500):
        _ = sum(range(100))
    print("✓ Finalizzazione completata")


if __name__ == "__main__":
    print("="*70)
    print("ESEMPIO 5: Profiling selettivo con context manager")
    print("="*70)
    print("\nProfilando SOLO la fase di elaborazione\n")
    
    profiler = cProfile.Profile()
    
    # Fase 1: NON profilata
    fase_inizializzazione()
    
    # Fase 2: PROFILATA usando enable/disable
    print("\n[Avvio profiling...]")
    profiler.enable()
    fase_elaborazione()
    profiler.disable()
    print("[Profiling terminato]")
    
    # Fase 3: NON profilata
    fase_finalizzazione()
    
    # Analisi risultati
    print("\n" + "="*70)
    print("RISULTATI DEL PROFILING (solo fase 2)")
    print("="*70)
    
    stats = pstats.Stats(profiler)
    stats.strip_dirs()
    stats.sort_stats(SortKey.CUMULATIVE)
    stats.print_stats(10)
    
    # Esempio con runcall
    print("\n" + "="*70)
    print("ALTERNATIVA: usando runcall()")
    print("="*70)
    
    profiler2 = cProfile.Profile()
    profiler2.runcall(operazione_complessa)
    
    stats2 = pstats.Stats(profiler2)
    stats2.strip_dirs()
    stats2.sort_stats(SortKey.TIME)
    print("\nProfiling di operazione_complessa():")
    stats2.print_stats(8)
    
    # Conclusioni
    print("\n" + "="*70)
    print("CONCLUSIONI")
    print("="*70)
    print("""
Profiling selettivo è utile quando:

1. Vuoi profilare solo parti specifiche del codice
2. Hai fasi di inizializzazione/cleanup che non ti interessano
3. Vuoi ridurre l'overhead del profiling
4. Vuoi confrontare diverse sezioni del programma

METODI:
- enable()/disable(): per blocchi di codice
- runcall(func, *args): per singole funzioni
- Context manager: più pythonic (richiede wrapper)

VANTAGGI:
- Output più pulito e focalizzato
- Meno overhead di profiling
- Più facile trovare i bottleneck
    """)
    
    print("\n✓ Esempio completato!")
