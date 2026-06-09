#!/usr/bin/env python3
"""
Demo completa di line_profiler - pronta all'uso
Questo file ha già i decoratori @profile inseriti
"""


@profile
def calcola_somma_quadrati(n):
    """Calcola la somma dei quadrati da 1 a n."""
    totale = 0
    for i in range(n):
        quadrato = i ** 2
        totale += quadrato
    return totale


@profile
def processa_lista(numeri):
    """Processa una lista di numeri."""
    risultati = []
    
    # Operazione 1: eleva al quadrato
    for num in numeri:
        risultati.append(num ** 2)
    
    # Operazione 2: filtra numeri pari
    pari = []
    for r in risultati:
        if r % 2 == 0:
            pari.append(r)
    
    # Operazione 3: calcola somma
    somma = 0
    for p in pari:
        somma += p
    
    return somma


def main():
    """Funzione principale."""
    print("Demo line_profiler - Analisi linea per linea\n")
    
    # Test 1
    risultato1 = calcola_somma_quadrati(10000)
    print(f"Somma quadrati: {risultato1}")
    
    # Test 2
    numeri = list(range(5000))
    risultato2 = processa_lista(numeri)
    print(f"Risultato processamento: {risultato2}")
    
    print("\n✓ Esecuzione completata!")


if __name__ == "__main__":
    main()
