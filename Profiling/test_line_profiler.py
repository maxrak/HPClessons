#!/usr/bin/env python3
"""
Esempio semplice per line_profiler
Aggiungi @profile alle funzioni che vuoi profilare
"""

import time
from funzioni_test import funzione_veloce, funzione_lenta


def elabora_dati(n):
    """Elabora una lista di numeri."""
    risultati = []
    
    # Loop con operazioni
    for i in range(n):
        valore = i ** 2
        risultati.append(valore)
    
    # Filtra numeri pari
    pari = [r for r in risultati if r % 2 == 0]
    
    return sum(pari)


def chiama_funzioni_test():
    """Chiama funzioni dal modulo funzioni_test."""
    # Chiama funzione veloce più volte
    for _ in range(5):
        funzione_veloce()
    
    # Chiama funzione lenta
    funzione_lenta()


def main():
    """Funzione principale."""
    print("Test line_profiler con funzioni esterne\n")
    
    risultato1 = elabora_dati(5000)
    print(f"Risultato elaborazione: {risultato1}")
    
    chiama_funzioni_test()
    
    print("\n✓ Completato!")


if __name__ == "__main__":
    main()
