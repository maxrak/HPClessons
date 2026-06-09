#!/usr/bin/env python3
"""
Line Profiler - Esempio 3: Confronto implementazioni
=====================================================
Confronta diverse implementazioni linea per linea.
"""

from funzioni_test import funzione_veloce, funzione_lenta, operazione_complessa


def metodo_con_loop_separati(n):
    """Usa loop separati - meno efficiente."""
    # Primo loop: crea lista
    numeri = []
    for i in range(n):
        numeri.append(i)
    
    # Secondo loop: eleva al quadrato
    quadrati = []
    for num in numeri:
        quadrati.append(num ** 2)
    
    # Terzo loop: somma
    somma = 0
    for q in quadrati:
        somma += q
    
    return somma


def metodo_con_loop_unico(n):
    """Usa un solo loop - più efficiente."""
    somma = 0
    for i in range(n):
        quadrato = i ** 2
        somma += quadrato
    return somma


def metodo_con_builtin(n):
    """Usa funzioni built-in - più veloce."""
    return sum(i ** 2 for i in range(n))


def test_con_funzioni_esterne():
    """Usa funzioni dal modulo funzioni_test."""
    risultati = []
    
    # Chiama funzione veloce
    for _ in range(5):
        funzione_veloce()
        risultati.append(1)
    
    # Chiama operazione complessa
    risultato_complesso = operazione_complessa()
    risultati.append(risultato_complesso)
    
    # Chiama funzione lenta
    funzione_lenta()
    risultati.append(2)
    
    return sum(risultati)


def main():
    """Funzione principale."""
    print("Line Profiler - Esempio 3: Confronto implementazioni\n")
    
    n = 50000
    
    r1 = metodo_con_loop_separati(n)
    print(f"Loop separati: {r1}")
    
    r2 = metodo_con_loop_unico(n)
    print(f"Loop unico: {r2}")
    
    r3 = metodo_con_builtin(n)
    print(f"Built-in: {r3}")
    
    r4 = test_con_funzioni_esterne()
    print(f"Funzioni esterne: {r4}")
    
    print("\n✓ Completato!")


if __name__ == "__main__":
    main()
