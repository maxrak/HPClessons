#!/usr/bin/env python3
"""
Line Profiler - Esempio 1: Analisi base
========================================
Usa line_profiler per vedere quanto tempo impiega ogni linea.
"""

from funzioni_test import funzione_veloce, funzione_lenta, funzione_con_sleep


def esegui_operazioni_miste():
    """Esegue operazioni con tempi diversi."""
    # Operazioni veloci
    for _ in range(10):
        funzione_veloce()
    
    # Operazione lenta
    funzione_lenta()
    
    # Operazione I/O
    funzione_con_sleep()
    
    return "completato"


def elabora_numeri(n):
    """Elabora una lista di numeri."""
    risultati = []
    
    for i in range(n):
        quadrato = i ** 2
        risultati.append(quadrato)
    
    somma = sum(risultati)
    return somma


def main():
    """Funzione principale."""
    print("Line Profiler - Esempio 1: Analisi base\n")
    
    risultato1 = esegui_operazioni_miste()
    print(f"Operazioni: {risultato1}")
    
    risultato2 = elabora_numeri(10000)
    print(f"Somma quadrati: {risultato2}")
    
    print("\n✓ Completato!")


if __name__ == "__main__":
    main()
