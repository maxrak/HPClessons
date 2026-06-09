#!/usr/bin/env python3
"""
Funzioni di test comuni utilizzate negli esempi di profiling.
Questo modulo contiene diverse funzioni con caratteristiche diverse
per illustrare il comportamento di cProfile.
"""

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


def fibonacci_ricorsivo(n):
    """Calcola Fibonacci in modo ricorsivo (inefficiente)."""
    if n <= 1:
        return n
    return fibonacci_ricorsivo(n - 1) + fibonacci_ricorsivo(n - 2)


def fibonacci_iterativo(n):
    """Calcola Fibonacci in modo iterativo (efficiente)."""
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b


def operazione_complessa():
    """Combina più operazioni."""
    risultati = []
    
    # Operazioni veloci
    for _ in range(5):
        risultati.append(funzione_veloce())
    
    # Operazione lenta
    risultati.append(funzione_lenta())
    
    # Calcoli
    for i in range(5, 8):
        risultati.append(calcolo_fattoriale(i))
    
    return sum(risultati)
