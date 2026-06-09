#!/usr/bin/env python3
"""
Memory Profiler - Esempio 3: Memory Leak e Ottimizzazione
==========================================================
Identifica problemi di memoria e come risolverli.
"""


def memory_leak_accumulo():
    """Accumula dati senza liberarli - MEMORY LEAK!"""
    # Lista che cresce continuamente
    accumulatore = []
    
    for i in range(10):
        # Crea lista grande ogni volta
        dati_temporanei = [j for j in range(100000)]
        
        # Accumula TUTTO (memoria cresce!)
        accumulatore.extend(dati_temporanei)
    
    return len(accumulatore)


def no_memory_leak_processa():
    """Processa dati senza accumularli - NESSUN LEAK."""
    # Non accumula, solo processa
    totale = 0
    
    for i in range(10):
        # Crea lista temporanea
        dati_temporanei = [j for j in range(100000)]
        
        # Processa (la lista viene liberata dopo)
        totale += sum(dati_temporanei)
    
    return totale


def duplica_dati_inutilmente():
    """Duplica dati inutilmente - SPRECO MEMORIA."""
    # Lista originale
    originale = list(range(500000))
    
    # Copia inutile
    copia1 = originale.copy()
    
    # Altra copia inutile
    copia2 = originale.copy()
    
    # Elabora su copia (spreco!)
    risultato = [x * 2 for x in copia1]
    
    return sum(risultato)


def usa_dati_direttamente():
    """Usa dati direttamente senza copie - EFFICIENTE."""
    # Lista originale
    originale = list(range(500000))
    
    # Elabora direttamente (nessuna copia!)
    risultato = sum(x * 2 for x in originale)
    
    return risultato


def crea_dizionario_grande():
    """Crea dizionario che usa molta memoria."""
    # Dizionario con molte chiavi
    dati = {}
    
    for i in range(100000):
        # Chiave stringa (usa più memoria di int)
        chiave = f"elemento_{i}"
        dati[chiave] = i * 2
    
    return len(dati)


def crea_dizionario_ottimizzato():
    """Usa __slots__ o strutture più efficienti."""
    # Lista di tuple usa meno memoria di dizionario
    dati = [(i, i * 2) for i in range(100000)]
    
    return len(dati)


def main():
    """Funzione principale."""
    print("Memory Profiler - Esempio 3: Memory Leak e Ottimizzazione\n")
    
    r1 = memory_leak_accumulo()
    print(f"Con accumulo (leak): {r1} elementi")
    
    r2 = no_memory_leak_processa()
    print(f"Senza accumulo: {r2}")
    
    r3 = duplica_dati_inutilmente()
    print(f"Con duplicazioni: {r3}")
    
    r4 = usa_dati_direttamente()
    print(f"Senza duplicazioni: {r4}")
    
    r5 = crea_dizionario_grande()
    print(f"Dizionario: {r5} elementi")
    
    r6 = crea_dizionario_ottimizzato()
    print(f"Lista tuple: {r6} elementi")
    
    print("\n✓ Completato!")


if __name__ == "__main__":
    main()
