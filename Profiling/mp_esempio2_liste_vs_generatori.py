#!/usr/bin/env python3
"""
Memory Profiler - Esempio 2: Liste vs Generatori
=================================================
Confronta l'uso di memoria tra liste e generatori.
"""


def usa_lista(n):
    """Usa una lista - CONSUMA MOLTA MEMORIA."""
    # Crea lista completa in memoria
    numeri = [i ** 2 for i in range(n)]
    
    # Somma tutti gli elementi
    totale = 0
    for num in numeri:
        totale += num
    
    return totale


def usa_generatore(n):
    """Usa un generatore - USA POCA MEMORIA."""
    # Generatore: calcola on-demand, non memorizza tutto
    numeri = (i ** 2 for i in range(n))
    
    # Somma tutti gli elementi
    totale = 0
    for num in numeri:
        totale += num
    
    return totale


def concatena_stringhe_male(n):
    """Concatena stringhe in modo inefficiente - MOLTA MEMORIA."""
    risultato = ""
    
    # Ogni += crea una nuova stringa in memoria!
    for i in range(n):
        risultato += str(i) + " "
    
    return risultato


def concatena_stringhe_bene(n):
    """Concatena stringhe in modo efficiente - POCA MEMORIA."""
    # Lista usa meno memoria di concatenazione ripetuta
    parti = []
    
    for i in range(n):
        parti.append(str(i))
    
    # Join è più efficiente
    risultato = " ".join(parti)
    
    return risultato


def copia_lista_male(lista):
    """Copia lista in modo inefficiente."""
    # Crea nuova lista elemento per elemento
    nuova_lista = []
    for elemento in lista:
        nuova_lista.append(elemento)
    
    return nuova_lista


def copia_lista_bene(lista):
    """Copia lista in modo efficiente."""
    # list() è ottimizzato e usa meno memoria temporanea
    return list(lista)


def main():
    """Funzione principale."""
    print("Memory Profiler - Esempio 2: Liste vs Generatori\n")
    
    n = 1000000
    
    r1 = usa_lista(n)
    print(f"Lista: {r1}")
    
    r2 = usa_generatore(n)
    print(f"Generatore: {r2}")
    
    r3 = len(concatena_stringhe_male(10000))
    print(f"Concatenazione inefficiente: {r3} caratteri")
    
    r4 = len(concatena_stringhe_bene(10000))
    print(f"Concatenazione efficiente: {r4} caratteri")
    
    dati = list(range(100000))
    r5 = len(copia_lista_male(dati))
    print(f"Copia inefficiente: {r5} elementi")
    
    r6 = len(copia_lista_bene(dati))
    print(f"Copia efficiente: {r6} elementi")
    
    print("\n✓ Completato!")


if __name__ == "__main__":
    main()
