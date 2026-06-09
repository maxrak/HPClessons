#!/usr/bin/env python3
"""
Memory Profiler - Esempio 1: Uso base
======================================
Analizza l'uso della memoria linea per linea.
"""


def crea_lista_grande():
    """Crea una lista grande che consuma molta memoria."""
    # Alloca memoria per lista
    lista = []
    
    # Riempie con 1 milione di numeri
    for i in range(1000000):
        lista.append(i)
    
    # Calcola somma (non usa memoria extra)
    somma = sum(lista)
    
    return somma


def crea_piu_liste():
    """Crea più liste che consumano memoria."""
    # Prima lista
    lista1 = [i for i in range(500000)]
    
    # Seconda lista (raddoppia memoria)
    lista2 = [i * 2 for i in range(500000)]
    
    # Terza lista (triplica memoria)
    lista3 = [i * 3 for i in range(500000)]
    
    # Combina (usa ancora più memoria)
    risultato = lista1 + lista2 + lista3
    
    return len(risultato)


def elabora_stringhe():
    """Elabora stringhe che consumano memoria."""
    # Stringa base
    testo = "Python " * 10000
    
    # Crea lista di parole (duplica memoria)
    parole = testo.split()
    
    # Modifica parole (usa più memoria)
    parole_maiuscole = [p.upper() for p in parole]
    
    # Unisce di nuovo (ancora più memoria)
    risultato = " ".join(parole_maiuscole)
    
    return len(risultato)


def main():
    """Funzione principale."""
    print("Memory Profiler - Esempio 1: Uso base\n")
    
    r1 = crea_lista_grande()
    print(f"Somma lista grande: {r1}")
    
    r2 = crea_piu_liste()
    print(f"Elementi totali: {r2}")
    
    r3 = elabora_stringhe()
    print(f"Lunghezza risultato: {r3}")
    
    print("\n✓ Completato!")


if __name__ == "__main__":
    main()
