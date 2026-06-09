#!/usr/bin/env python3
"""
Line Profiler - Esempio 4: Ottimizzazione algoritmica
======================================================
Confronta algoritmi O(n²) vs O(n).
"""


def trova_duplicati_lento(lista):
    """Trova duplicati con loop annidati - O(n²) - LENTO!"""
    duplicati = []
    
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j]:
                if lista[i] not in duplicati:
                    duplicati.append(lista[i])
    
    return duplicati


def trova_duplicati_veloce(lista):
    """Trova duplicati con set - O(n) - VELOCE!"""
    visti = set()
    duplicati = set()
    
    for elemento in lista:
        if elemento in visti:
            duplicati.add(elemento)
        else:
            visti.add(elemento)
    
    return list(duplicati)


def cerca_elementi_lento(lista, targets):
    """Ricerca multipla lineare - O(n*m) - LENTO!"""
    trovati = []
    
    for target in targets:
        for elemento in lista:
            if elemento == target:
                trovati.append(target)
                break
    
    return trovati


def cerca_elementi_veloce(lista, targets):
    """Ricerca con set - O(n+m) - VELOCE!"""
    set_lista = set(lista)
    trovati = []
    
    for target in targets:
        if target in set_lista:
            trovati.append(target)
    
    return trovati


def main():
    """Funzione principale."""
    print("Line Profiler - Esempio 4: Ottimizzazione algoritmica\n")
    
    # Test duplicati
    dati = [1, 2, 3, 4, 5] * 100 + [6, 7, 8, 9, 10] * 100
    
    dup1 = trova_duplicati_lento(dati)
    print(f"Duplicati (lento): {len(dup1)} trovati")
    
    dup2 = trova_duplicati_veloce(dati)
    print(f"Duplicati (veloce): {len(dup2)} trovati")
    
    # Test ricerca
    numeri = list(range(5000))
    targets = [100, 500, 1000, 2000, 3000, 4500]
    
    trov1 = cerca_elementi_lento(numeri, targets)
    print(f"Ricerca (lenta): {len(trov1)} trovati")
    
    trov2 = cerca_elementi_veloce(numeri, targets)
    print(f"Ricerca (veloce): {len(trov2)} trovati")
    
    print("\n✓ Completato!")


if __name__ == "__main__":
    main()
