#!/usr/bin/env python3
"""
DIMOSTRAZIONE DEL PRINCIPIO DI PARETO CON cProfile
===================================================

Il Principio di Pareto (regola 80/20) nel contesto del profiling significa:
"L'80% del tempo di esecuzione è speso nel 20% del codice"

Questo esempio profila il codice di pareto_principle.py e dimostra
visivamente come una piccola parte del codice consuma la maggior parte del tempo.
"""

import cProfile
import pstats
from pstats import SortKey
import sys
import os

# Aggiungi il percorso parent alla path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def process_data():
    """Funzione LENTA - elabora molti dati (simula il 20% del codice)."""
    total = 0
    for i in range(10000000):
        total += i
    return total


def print_report():
    """Funzione VELOCE - stampa solo un messaggio."""
    print("Analysis completed")


def initialize():
    """Funzione VELOCE - inizializzazione rapida."""
    config = {
        'name': 'Pareto Demo',
        'version': '1.0',
        'debug': False
    }
    return config


def validate_data():
    """Funzione VELOCE - validazione semplice."""
    data = [1, 2, 3, 4, 5]
    return all(x > 0 for x in data)


def save_results(result):
    """Funzione VELOCE - salvataggio rapido."""
    filename = "results.txt"
    # Simula solo, non salva davvero
    return filename


def main():
    """Funzione principale che chiama tutte le altre."""
    print("Inizio elaborazione...\n")
    
    # Fase 1: Inizializzazione (veloce)
    config = initialize()
    
    # Fase 2: Validazione (veloce)
    is_valid = validate_data()
    
    # Fase 3: Elaborazione INTENSIVA (lenta - qui si concentra il tempo!)
    result = process_data()
    
    # Fase 4: Salvataggio (veloce)
    filename = save_results(result)
    
    # Fase 5: Report (veloce)
    print_report()
    
    return result


def analizza_pareto(stats):
    """
    Analizza le statistiche e calcola la distribuzione secondo Pareto.
    """
    print("\n" + "="*70)
    print("ANALISI PRINCIPIO DI PARETO")
    print("="*70)
    
    # Ottieni tutte le statistiche
    stats_dict = stats.stats
    
    # Crea lista di (funzione, tempo_cumulativo)
    funzioni_tempo = []
    tempo_totale = 0
    
    for func, (cc, nc, tt, ct, callers) in stats_dict.items():
        if 'esempio_pareto.py' in str(func[0]) or 'pareto_principle.py' in str(func[0]):
            funzione_nome = func[2]
            funzioni_tempo.append((funzione_nome, ct))
            tempo_totale += ct
    
    # Ordina per tempo decrescente
    funzioni_tempo.sort(key=lambda x: x[1], reverse=True)
    
    print(f"\nTempo totale di esecuzione: {tempo_totale:.4f} secondi")
    print(f"Numero di funzioni analizzate: {len(funzioni_tempo)}\n")
    
    # Calcola percentuali cumulative
    print("Funzione" + " "*30 + "Tempo (s)  % Tempo  % Cumulativa")
    print("-" * 70)
    
    tempo_cumulativo = 0
    for i, (funzione, tempo) in enumerate(funzioni_tempo):
        tempo_cumulativo += tempo
        percentuale = (tempo / tempo_totale) * 100
        percentuale_cum = (tempo_cumulativo / tempo_totale) * 100
        
        # Evidenzia la funzione più lenta
        marker = " 🔥" if i == 0 else ""
        print(f"{funzione:<35} {tempo:>8.4f}  {percentuale:>6.1f}%    {percentuale_cum:>6.1f}%{marker}")
    
    # Analisi Pareto
    print("\n" + "="*70)
    print("VERIFICA PRINCIPIO DI PARETO")
    print("="*70)
    
    # Calcola quale percentuale di funzioni produce 80% del tempo
    tempo_target = tempo_totale * 0.8
    tempo_accumulato = 0
    num_funzioni_80 = 0
    
    for funzione, tempo in funzioni_tempo:
        tempo_accumulato += tempo
        num_funzioni_80 += 1
        if tempo_accumulato >= tempo_target:
            break
    
    percentuale_funzioni = (num_funzioni_80 / len(funzioni_tempo)) * 100
    percentuale_tempo = (tempo_accumulato / tempo_totale) * 100
    
    print(f"\n📊 RISULTATO:")
    print(f"   {num_funzioni_80} funzione(i) su {len(funzioni_tempo)} ({percentuale_funzioni:.1f}%)")
    print(f"   consumano il {percentuale_tempo:.1f}% del tempo totale")
    
    print(f"\n🎯 PRINCIPIO DI PARETO:")
    if percentuale_funzioni <= 30:
        print(f"   ✓ VERIFICATO! Circa il {percentuale_funzioni:.0f}% delle funzioni")
        print(f"     consumano l'80% del tempo di esecuzione")
    else:
        print(f"   ⚠ In questo caso specifico la distribuzione è diversa")
    
    print(f"\n💡 IMPLICAZIONE:")
    print(f"   Ottimizzando '{funzioni_tempo[0][0]}' (la funzione più lenta)")
    print(f"   otterrai il massimo miglioramento delle prestazioni!")
    print(f"   Ignorare le altre funzioni veloci è OK in questo caso.")


def visualizza_grafico_ascii(stats):
    """Crea un semplice grafico ASCII per visualizzare la distribuzione."""
    print("\n" + "="*70)
    print("VISUALIZZAZIONE DISTRIBUZIONE TEMPO")
    print("="*70)
    
    stats_dict = stats.stats
    funzioni_tempo = []
    
    for func, (cc, nc, tt, ct, callers) in stats_dict.items():
        if 'esempio_pareto.py' in str(func[0]) or 'pareto_principle.py' in str(func[0]):
            funzione_nome = func[2]
            funzioni_tempo.append((funzione_nome, ct))
    
    funzioni_tempo.sort(key=lambda x: x[1], reverse=True)
    
    if not funzioni_tempo:
        return
    
    tempo_max = funzioni_tempo[0][1]
    
    print("\nTempo di esecuzione per funzione (barre proporzionali):\n")
    
    for funzione, tempo in funzioni_tempo:
        barra_lunghezza = int((tempo / tempo_max) * 50)
        barra = "█" * barra_lunghezza
        percentuale = (tempo / sum(t for _, t in funzioni_tempo)) * 100
        print(f"{funzione:<25} {barra} {percentuale:.1f}%")


if __name__ == "__main__":
    print("="*70)
    print("PRINCIPIO DI PARETO E PROFILING")
    print("="*70)
    print("""
Il Principio di Pareto nel software dice che:

    📊 L'80% del tempo di esecuzione
       è consumato dal 20% del codice

Questo significa che per ottimizzare efficacemente:
✓ Trova il 20% del codice che è lento (bottleneck)
✓ Concentra gli sforzi di ottimizzazione su quello
✗ Non perdere tempo a ottimizzare codice già veloce

Useremo cProfile per identificare questo 20% critico!
    """)
    
    input("Premi INVIO per iniziare il profiling...\n")
    
    # Crea profiler
    profiler = cProfile.Profile()
    
    # Esegui il profiling
    profiler.enable()
    result = main()
    profiler.disable()
    
    # Analizza risultati
    stats = pstats.Stats(profiler)
    stats.strip_dirs()
    
    print("\n" + "="*70)
    print("STATISTICHE COMPLETE (Top 10)")
    print("="*70)
    stats.sort_stats(SortKey.CUMULATIVE)
    stats.print_stats(10)
    
    # Analisi Pareto personalizzata
    analizza_pareto(stats)
    
    # Visualizzazione grafica
    visualizza_grafico_ascii(stats)
    
    # Conclusioni
    print("\n" + "="*70)
    print("CONCLUSIONI E RACCOMANDAZIONI")
    print("="*70)
    print("""
🎯 COSA OTTIMIZZARE:
   1. Concentrati su 'process_data' - è il chiaro bottleneck
   2. Considera: vectorizzazione (NumPy), compilazione (Numba), 
      parallelizzazione, algoritmi più efficienti
   
❌ COSA NON OTTIMIZZARE:
   - Le funzioni veloci (initialize, validate_data, print_report, ecc.)
   - Ottimizzarle non darebbe benefici significativi
   
📈 IMPATTO STIMATO:
   - Ridurre del 50% il tempo di process_data → ~50% più veloce tutto il programma
   - Ottimizzare tutte le altre funzioni → impatto trascurabile (<1%)

💰 RITORNO SULL'INVESTIMENTO:
   - Ore spese su process_data: alto ritorno
   - Ore spese su altre funzioni: basso ritorno
   
Questo è il potere del Principio di Pareto nel profiling! 🚀
    """)
    
    print("\n✓ Analisi completata!")
    print(f"✓ Risultato elaborazione: {result}")
