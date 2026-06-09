#!/usr/bin/env python3
"""
Memory Profiler - Esempio 4: NumPy vs Liste
============================================
Confronta uso memoria tra liste Python e array NumPy.
"""

import sys


def usa_liste_python(n):
    """Usa liste Python native - PIÙ MEMORIA."""
    # Lista di interi Python (ogni int è un oggetto)
    lista = [i for i in range(n)]
    
    # Lista di float
    lista_float = [float(i) for i in range(n)]
    
    # Calcolo
    risultato = sum(lista) + sum(lista_float)
    
    return risultato


def usa_array_efficiente(n):
    """Usa array.array - MENO MEMORIA di liste."""
    import array
    
    # Array di interi (tipo 'i')
    arr_int = array.array('i', range(n))
    
    # Array di float (tipo 'd')
    arr_float = array.array('d', (float(i) for i in range(n)))
    
    # Calcolo
    risultato = sum(arr_int) + sum(arr_float)
    
    return risultato


def calcola_dimensioni():
    """Mostra differenze di dimensione tra strutture."""
    n = 1000
    
    # Lista Python
    lista = list(range(n))
    dim_lista = sys.getsizeof(lista) + sum(sys.getsizeof(i) for i in lista[:100])
    
    # Array
    import array
    arr = array.array('i', range(n))
    dim_array = sys.getsizeof(arr)
    
    print(f"\nDimensioni per {n} elementi:")
    print(f"  Lista Python: ~{dim_lista} bytes")
    print(f"  Array:        {dim_array} bytes")
    print(f"  Rapporto:     {dim_lista/dim_array:.1f}x")


def processa_matrice_liste():
    """Matrice con liste - MOLTA MEMORIA."""
    # Matrice 100x100 con liste
    matrice = [[i + j for j in range(100)] for i in range(100)]
    
    # Somma tutti gli elementi
    totale = sum(sum(riga) for riga in matrice)
    
    return totale


def processa_matrice_flat():
    """Matrice "flat" - MENO MEMORIA."""
    # Singola lista rappresenta matrice 100x100
    dimensione = 100
    matrice_flat = [i + j for i in range(dimensione) for j in range(dimensione)]
    
    # Somma
    totale = sum(matrice_flat)
    
    return totale


def main():
    """Funzione principale."""
    print("Memory Profiler - Esempio 4: Strutture Dati Efficienti\n")
    
    n = 100000
    
    r1 = usa_liste_python(n)
    print(f"Liste Python: {r1}")
    
    r2 = usa_array_efficiente(n)
    print(f"Array: {r2}")
    
    calcola_dimensioni()
    
    r3 = processa_matrice_liste()
    print(f"\nMatrice con liste: {r3}")
    
    r4 = processa_matrice_flat()
    print(f"Matrice flat: {r4}")
    
    print("\n✓ Completato!")


if __name__ == "__main__":
    main()
