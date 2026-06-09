#!/usr/bin/env python3
"""
Esempio semplice: misurare il tempo di esecuzione con il modulo time
"""

import time


# Esempio 1: Misura base
print("Esempio 1: Misura base")
print("-" * 40)

start = time.time()

# Codice da misurare
somma = 0
for i in range(1000000):
    somma += i

end = time.time()
tempo_impiegato = end - start

print(f"Risultato: {somma}")
print(f"Tempo impiegato: {tempo_impiegato:.6f} secondi")


# Esempio 2: Misurare più segmenti
print("\n\nEsempio 2: Confrontare due implementazioni")
print("-" * 40)

# Implementazione 1: loop
start1 = time.time()
somma1 = sum(range(1000000))
end1 = time.time()
tempo1 = end1 - start1

# Implementazione 2: formula
start2 = time.time()
n = 1000000 - 1
somma2 = n * (n + 1) // 2
end2 = time.time()
tempo2 = end2 - start2

print(f"Loop:    {tempo1:.6f} secondi")
print(f"Formula: {tempo2:.6f} secondi")
print(f"Speedup: {tempo1/tempo2:.2f}x")


# Esempio 3: time.perf_counter() - più preciso
print("\n\nEsempio 3: Usando perf_counter (più preciso)")
print("-" * 40)

start = time.perf_counter()

# Operazione veloce
risultato = [x**2 for x in range(10000)]

end = time.perf_counter()

print(f"Tempo: {(end - start)*1000:.3f} millisecondi")


# Esempio 4: Misurare con context manager (opzionale)
print("\n\nEsempio 4: Funzione helper per misurare")
print("-" * 40)

def misura_tempo(descrizione):
    """Helper per misurare facilmente"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            risultato = func(*args, **kwargs)
            end = time.perf_counter()
            print(f"{descrizione}: {(end - start)*1000:.3f} ms")
            return risultato
        return wrapper
    return decorator

@misura_tempo("Calcolo fattoriale")
def calcola_fattoriale(n):
    if n <= 1:
        return 1
    return n * calcola_fattoriale(n - 1)

risultato = calcola_fattoriale(100)
print(f"Risultato: {risultato}")
