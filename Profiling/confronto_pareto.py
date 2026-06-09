#!/usr/bin/env python3
"""
CONFRONTO: Prima e Dopo l'Ottimizzazione basata su Pareto
===========================================================

Questo script confronta le prestazioni PRIMA e DOPO l'ottimizzazione
della funzione identificata come bottleneck dal profiling.

Dimostra l'impatto pratico del Principio di Pareto:
ottimizzare il 20% del codice critico porta all'80% del miglioramento!
"""

import cProfile
import pstats
from pstats import SortKey
import time


# ============================================================================
# VERSIONE ORIGINALE (NON OTTIMIZZATA)
# ============================================================================

def process_data_original():
    """Versione originale - loop Python puro (LENTO)."""
    total = 0
    for i in range(10000000):
        total += i
    return total


def print_report():
    """Funzione veloce - non ottimizzata."""
    print("Analysis completed")


def initialize():
    """Funzione veloce - non ottimizzata."""
    config = {'name': 'Test', 'version': '1.0'}
    return config


def validate_data():
    """Funzione veloce - non ottimizzata."""
    return True


def main_original():
    """Programma originale."""
    config = initialize()
    is_valid = validate_data()
    result = process_data_original()  # BOTTLENECK!
    print_report()
    return result


# ============================================================================
# VERSIONE OTTIMIZZATA (focus sul bottleneck)
# ============================================================================

def process_data_optimized():
    """Versione ottimizzata - usa la formula di Gauss (VELOCE!)."""
    # Formula di Gauss: somma(0..n) = n * (n+1) / 2
    n = 10000000 - 1
    total = n * (n + 1) // 2
    return total


def main_optimized():
    """Programma ottimizzato - SOLO process_data è cambiato!"""
    config = initialize()
    is_valid = validate_data()
    result = process_data_optimized()  # OTTIMIZZATO!
    print_report()
    return result


# ============================================================================
# CONFRONTO E ANALISI
# ============================================================================

def profila_versione(nome, func):
    """Profila una versione e ritorna le statistiche."""
    print(f"\n{'='*70}")
    print(f"Profiling: {nome}")
    print('='*70)
    
    profiler = cProfile.Profile()
    
    # Misura anche il tempo totale
    start_time = time.time()
    
    profiler.enable()
    result = func()
    profiler.disable()
    
    end_time = time.time()
    tempo_totale = end_time - start_time
    
    # Statistiche
    stats = pstats.Stats(profiler)
    stats.strip_dirs()
    stats.sort_stats(SortKey.CUMULATIVE)
    stats.print_stats(10)
    
    return stats, tempo_totale, result


def confronta_risultati(tempo_orig, tempo_opt):
    """Confronta i risultati e mostra il miglioramento."""
    print("\n" + "="*70)
    print("CONFRONTO PRESTAZIONI")
    print("="*70)
    
    speedup = tempo_orig / tempo_opt
    riduzione_percentuale = ((tempo_orig - tempo_opt) / tempo_orig) * 100
    
    print(f"\n⏱️  TEMPI DI ESECUZIONE:")
    print(f"   Versione Originale:  {tempo_orig:.4f} secondi")
    print(f"   Versione Ottimizzata: {tempo_opt:.4f} secondi")
    
    print(f"\n🚀 MIGLIORAMENTO:")
    print(f"   Speedup: {speedup:.2f}x più veloce")
    print(f"   Riduzione tempo: {riduzione_percentuale:.1f}%")
    
    # Visualizzazione grafica
    print(f"\n📊 VISUALIZZAZIONE:")
    
    lunghezza_orig = 50
    lunghezza_opt = int(lunghezza_orig / speedup)
    
    print(f"   Originale:   [{'█' * lunghezza_orig}] {tempo_orig:.4f}s")
    print(f"   Ottimizzata: [{'█' * lunghezza_opt}] {tempo_opt:.4f}s")
    
    print(f"\n💡 PRINCIPIO DI PARETO IN AZIONE:")
    print(f"   ✓ Modificata SOLO 1 funzione su 5 (20% del codice)")
    print(f"   ✓ Ottenuto {riduzione_percentuale:.1f}% di miglioramento")
    print(f"   ✓ Le altre 4 funzioni veloci non sono state toccate")
    
    if riduzione_percentuale > 70:
        print(f"\n   🎯 Questo dimostra il Principio di Pareto:")
        print(f"      Ottimizzando il 20% giusto del codice")
        print(f"      otteniamo la maggior parte dei benefici!")


def mostra_cosa_e_cambiato():
    """Mostra esattamente cosa è stato ottimizzato."""
    print("\n" + "="*70)
    print("COSA È STATO OTTIMIZZATO?")
    print("="*70)
    
    print("""
❌ VERSIONE ORIGINALE (process_data_original):
    def process_data_original():
        total = 0
        for i in range(10000000):  # ← 10 milioni di iterazioni!
            total += i
        return total
    
    Problema: Loop Python puro è lento per operazioni ripetitive

✅ VERSIONE OTTIMIZZATA (process_data_optimized):
    def process_data_optimized():
        n = 10000000 - 1
        total = n * (n + 1) // 2  # ← Formula di Gauss: O(1)!
        return total
    
    Soluzione: Formula matematica diretta, nessun loop

🔍 ALTRE FUNZIONI:
    ✓ initialize() - NON modificata (già veloce)
    ✓ validate_data() - NON modificata (già veloce)
    ✓ print_report() - NON modificata (già veloce)
    
    Perché? Il profiling ha mostrato che sono irrilevanti!

📈 STRATEGIA:
    1. Profiling identifica bottleneck (process_data)
    2. Ottimizza SOLO quello (Principio di Pareto)
    3. Ignora le funzioni già veloci (non vale la pena)
    4. Risultato: massimo guadagno con minimo sforzo!
    """)


if __name__ == "__main__":
    print("="*70)
    print("DIMOSTRAZIONE PRINCIPIO DI PARETO")
    print("Confronto: Originale vs Ottimizzato")
    print("="*70)
    
    print("""
Passi di questa dimostrazione:

1. Profilare versione ORIGINALE (non ottimizzata)
2. Profilare versione OTTIMIZZATA (solo bottleneck modificato)
3. Confrontare i risultati
4. Vedere l'impatto del Principio di Pareto

Questo dimostra che:
📊 Ottimizzare il 20% giusto → 80% del beneficio
⚠️  Ottimizzare tutto il resto → impatto minimo
    """)
    
    input("\nPremi INVIO per iniziare...\n")
    
    # Profila versione originale
    stats_orig, tempo_orig, result_orig = profila_versione(
        "VERSIONE ORIGINALE (non ottimizzata)",
        main_original
    )
    
    print("\n" + "⏳ Attendere analisi versione ottimizzata...\n")
    time.sleep(1)
    
    # Profila versione ottimizzata
    stats_opt, tempo_opt, result_opt = profila_versione(
        "VERSIONE OTTIMIZZATA (solo bottleneck)",
        main_optimized
    )
    
    # Verifica correttezza
    if result_orig != result_opt:
        print(f"\n⚠️  ATTENZIONE: I risultati sono diversi!")
        print(f"   Originale: {result_orig}")
        print(f"   Ottimizzata: {result_opt}")
    else:
        print(f"\n✓ Risultati identici: {result_orig}")
    
    # Confronta e mostra miglioramenti
    confronta_risultati(tempo_orig, tempo_opt)
    
    # Spiega cosa è cambiato
    mostra_cosa_e_cambiato()
    
    # Conclusioni finali
    print("\n" + "="*70)
    print("CONCLUSIONI FINALI")
    print("="*70)
    print("""
🎓 LEZIONI APPRESE:

1. IL PROFILING È ESSENZIALE
   → Senza cProfile non avresti saputo dove ottimizzare
   → Potresti aver perso tempo su funzioni già veloci

2. PRINCIPIO DI PARETO FUNZIONA
   → Una piccola modifica → grande impatto
   → Focus selettivo è più efficace dello sforzo uniforme

3. MISURA SEMPRE
   → Le intuizioni possono sbagliare
   → Il profiling fornisce dati oggettivi
   → Confronta sempre prima e dopo

4. OTTIMIZZA STRATEGICAMENTE
   → Identifica bottleneck con profiling
   → Ottimizza solo quello
   → Ri-profila per verificare
   → Ripeti se necessario

🚀 PROSSIMI PASSI:
   - Applica questo processo al tuo codice
   - Profila prima di ottimizzare
   - Concentrati sui veri bottleneck
   - Misura i risultati

Buon profiling e ottimizzazione! 🎯
    """)
