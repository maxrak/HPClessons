#!/usr/bin/env python3
"""
Line Profiler - Esempio 2: Identificare bottleneck
===================================================
Trova esattamente quale linea è lenta.
"""

from funzioni_test import calcolo_fattoriale, fibonacci_ricorsivo, fibonacci_iterativo


def calcola_fibonacci_multipli():
    """Calcola più valori Fibonacci - versione ricorsiva (lenta!)."""
    risultati = []
    
    for i in range(10, 25):
        valore = fibonacci_ricorsivo(i)
        risultati.append(valore)
    
    return risultati


def calcola_fibonacci_multipli_veloce():
    """Calcola più valori Fibonacci - versione iterativa (veloce!)."""
    risultati = []
    
    for i in range(10, 25):
        valore = fibonacci_iterativo(i)
        risultati.append(valore)
    
    return risultati


def calcola_fattoriali():
    """Calcola più fattoriali."""
    risultati = []
    
    for i in range(5, 15):
        fatto = calcolo_fattoriale(i)
        risultati.append(fatto)
    
    return risultati


def operazione_mista():
    """Combina diverse operazioni."""
    # Fattoriali (medio)
    fatt = calcola_fattoriali()
    
    # Fibonacci iterativo (veloce)
    fib = calcola_fibonacci_multipli_veloce()
    
    # Fibonacci ricorsivo (lento!)
    fib_rec = calcola_fibonacci_multipli()
    
    return len(fatt) + len(fib) + len(fib_rec)


def main():
    """Funzione principale."""
    print("Line Profiler - Esempio 2: Identificare bottleneck\n")
    
    risultato = operazione_mista()
    print(f"Totale operazioni: {risultato}")
    
    print("\n✓ Completato!")


if __name__ == "__main__":
    main()
