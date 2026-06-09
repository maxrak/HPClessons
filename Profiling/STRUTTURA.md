# 📁 Struttura Completa - Directory Profiling

Mappa completa di tutti i file disponibili con descrizioni.

---

## 📚 Documentazione (6 file)

```
📖 INDEX.md                          ← INIZIA QUI! Panoramica completa
📖 COMANDI_RAPIDI.md                ← Quick reference tutti i comandi
📖 README.md                        ← Guida completa cProfile
📖 LINE_PROFILER_README.md          ← Guida completa line_profiler
📖 LINE_PROFILER_ESEMPI.md          ← Dettagli esempi lp_esempio*.py
📖 MEMORY_PROFILER_README.md        ← Guida completa memory_profiler
📖 STRUTTURA.md                     ← Questo file
```

**Ordine di lettura consigliato:**
1. INDEX.md (panoramica)
2. COMANDI_RAPIDI.md (reference)
3. README specifici per ogni tool quando ne usi gli esempi

---

## 🎯 cProfile - Profiling per Funzione (10 file)

### Modulo Condiviso
```python
📦 funzioni_test.py                 # Funzioni di test comuni
   ├─ funzione_veloce()             # O(1000) - veloce
   ├─ funzione_lenta()              # O(1M) - lenta
   ├─ funzione_con_sleep()          # 0.5s I/O
   ├─ calcolo_fattoriale(n)         # n!
   ├─ fibonacci_ricorsivo(n)        # Fibonacci ricorsivo (lento!)
   ├─ fibonacci_iterativo(n)        # Fibonacci iterativo (veloce!)
   └─ operazione_complessa()        # Operazioni miste
```

### Esempi Base (5 file)
```python
🟢 esempio1_base.py                 # cProfile.run() - uso base
   └─ Comando: python esempio1_base.py

🟢 esempio2_statistiche.py          # pstats con ordinamenti diversi
   ├─ SortKey.TIME                  # Ordina per tempo
   ├─ SortKey.CUMULATIVE            # Ordina per tempo cumulativo
   └─ SortKey.CALLS                 # Ordina per numero chiamate
   └─ Comando: python esempio2_statistiche.py

🟡 esempio3_salvataggio.py          # Salva/carica profili .prof
   ├─ cProfile.run(..., 'output.prof')
   └─ pstats.Stats('output.prof')
   └─ Comando: python esempio3_salvataggio.py

🟡 esempio4_confronto.py            # Confronto algoritmi
   ├─ fibonacci_ricorsivo vs iterativo
   └─ Speedup: ~2000x
   └─ Comando: python esempio4_confronto.py

🔴 esempio5_contesto.py             # Profiling selettivo
   ├─ profiler.enable()
   ├─ profiler.disable()
   └─ profiler.runcall()
   └─ Comando: python esempio5_contesto.py
```

### Principio di Pareto (2 file)
```python
⭐ esempio_pareto.py                # Identifica 20% critico
   ├─ Analizza distribuzione tempo
   ├─ Mostra funzioni che consumano 80%+ tempo
   └─ Visualizzazione con barre
   └─ Comando: python esempio_pareto.py

⭐ confronto_pareto.py              # Demo 80/20
   ├─ Versione originale (lenta)
   ├─ Versione ottimizzata (veloce)
   ├─ Confronto e speedup
   └─ Speedup: 6955x (0.27s → 0.00004s)
   └─ Comando: python confronto_pareto.py
```

### Time Module (1 file)
```python
🟢 esempio_time.py                  # Misurazioni semplici
   ├─ time.time()                   # Tempo wall-clock
   ├─ time.perf_counter()           # Tempo preciso
   ├─ Confronto implementazioni
   └─ Decorator per timing
   └─ Comando: python esempio_time.py
```

### Legacy (1 file)
```python
📝 cprofile_demo.py                 # Demo originale (non usato)
```

---

## ⏱️ line_profiler - Tempo per Linea (10 file)

### Esempi Self-Contained (4 file)
Eseguibili direttamente con kernprof (nessun import esterno).

```python
🟢 line_profiler_1_base.py          # Analisi base
   ├─ calcola_somma_quadrati()
   └─ processa_lista()
   └─ Comando: kernprof -l -v line_profiler_1_base.py

🟡 line_profiler_2_bottleneck.py    # Identificare bottleneck
   ├─ metodo_inefficiente()         # Operazioni ripetute
   └─ analizza_testo()              # Loop annidati
   └─ Comando: kernprof -l -v line_profiler_2_bottleneck.py

🟡 line_profiler_3_confronto.py     # Confronto stili
   ├─ loop vs comprehension vs builtin
   └─ Mostra differenze performance
   └─ Comando: kernprof -l -v line_profiler_3_confronto.py

🔴 line_profiler_4_algoritmi.py     # O(n²) vs O(n)
   ├─ trova_duplicati: loop annidati vs set
   ├─ cerca_elemento: loop vs "in" operator
   └─ trova_intersezione: double loop vs set
   └─ Comando: kernprof -l -v line_profiler_4_algoritmi.py
```

### Esempi con funzioni_test.py (4 file)
Usano funzioni da funzioni_test.py, richiedono run_line_profiler.sh.

```python
🟢 lp_esempio1_base.py              # Operazioni miste
   ├─ esegui_operazioni_miste()     # Chiama funzione_veloce/lenta/con_sleep
   └─ elabora_numeri(n)             # Loop con append
   └─ Comando: ./run_line_profiler.sh lp_esempio1_base.py esegui_operazioni_miste elabora_numeri

🟡 lp_esempio2_bottleneck.py        # Fibonacci confronto
   ├─ calcola_fibonacci_multipli()  # Usa fibonacci_ricorsivo (LENTO!)
   ├─ calcola_fibonacci_multipli_veloce()  # Usa fibonacci_iterativo
   └─ Speedup: 2000x
   └─ Comando: ./run_line_profiler.sh lp_esempio2_bottleneck.py calcola_fibonacci_multipli calcola_fibonacci_multipli_veloce

🟡 lp_esempio3_confronto.py         # Stili loop
   ├─ metodo_con_loop_separati()
   ├─ metodo_con_loop_unico()
   ├─ metodo_con_builtin()
   └─ test_con_funzioni_esterne()   # Usa operazione_complessa()
   └─ Comando: ./run_line_profiler.sh lp_esempio3_confronto.py metodo_con_loop_separati metodo_con_loop_unico metodo_con_builtin

🔴 lp_esempio4_algoritmi.py         # Ottimizzazione algoritmica
   ├─ trova_duplicati_lento()       # O(n²) loop annidati
   ├─ trova_duplicati_veloce()      # O(n) con set
   └─ Speedup: 340x (0.178s vs 0.0005s)
   └─ Comando: ./run_line_profiler.sh lp_esempio4_algoritmi.py trova_duplicati_lento trova_duplicati_veloce
```

### Demo e Test (2 file)
```python
⭐ demo_line_profiler.py            # Demo pronto con @profile
   ├─ Già ha @profile decorator
   └─ Eseguibile direttamente
   └─ Comando: kernprof -l -v demo_line_profiler.py

🔧 test_line_profiler.py            # Test import funzioni_test
   ├─ Verifica import funzionano
   └─ Comando: ./run_line_profiler.sh test_line_profiler.py elabora_dati chiama_funzioni_test
```

---

## 💾 memory_profiler - Memoria per Linea (4 file)

```python
🟢 mp_esempio1_base.py              # Uso base
   ├─ crea_lista_grande()           # Alloca 1M numeri (~38 MiB)
   ├─ crea_piu_liste()              # Alloca 3 liste progressivamente
   └─ elabora_stringhe()            # Operazioni su stringhe
   └─ Comando: ./run_memory_profiler.sh mp_esempio1_base.py crea_lista_grande crea_piu_liste

⭐ mp_esempio2_liste_vs_generatori.py  # Liste vs Generatori
   ├─ usa_lista()                   # Lista completa in memoria (+38 MiB)
   ├─ usa_generatore()              # Memoria costante (no picchi)
   ├─ concatena_stringhe_male()     # += ripetuto (inefficiente)
   ├─ concatena_stringhe_bene()     # str.join() (efficiente)
   ├─ copia_lista_male()            # Loop append
   └─ copia_lista_bene()            # list() ottimizzato
   └─ Comando: ./run_memory_profiler.sh mp_esempio2_liste_vs_generatori.py usa_lista usa_generatore

⚠️  mp_esempio3_memory_leak.py      # Memory Leak Detection
   ├─ memory_leak_accumulo()        # Accumula dati (leak! +43 MiB)
   ├─ no_memory_leak_processa()     # Processa e libera (costante)
   ├─ duplica_dati_inutilmente()    # Copie multiple inutili
   ├─ usa_dati_direttamente()       # Nessuna copia
   ├─ crea_dizionario_grande()      # dict con chiavi stringa
   └─ crea_dizionario_ottimizzato() # lista tuple (più efficiente)
   └─ Comando: ./run_memory_profiler.sh mp_esempio3_memory_leak.py memory_leak_accumulo no_memory_leak_processa

🔴 mp_esempio4_strutture_dati.py    # Strutture Efficienti
   ├─ usa_liste_python()            # Liste native (~7.5 MiB)
   ├─ usa_array_efficiente()        # array.array (~0.8 MiB)
   ├─ calcola_dimensioni()          # Confronto sys.getsizeof
   ├─ processa_matrice_liste()      # Matrice con liste annidate
   └─ processa_matrice_flat()       # Matrice "flat" (più efficiente)
   └─ Rapporto: 9x meno memoria con array!
   └─ Comando: ./run_memory_profiler.sh mp_esempio4_strutture_dati.py usa_liste_python usa_array_efficiente
```

---

## 🛠️ Script Helper (2 file)

```bash
⚡ run_line_profiler.sh             # Helper per line_profiler
   ├─ Copia script in .temp_profiler_*.py
   ├─ Aggiunge @profile alle funzioni specificate
   ├─ Esegue: kernprof -l -v
   └─ Pulisce file temporanei
   └─ Uso: ./run_line_profiler.sh <script.py> <func1> [func2] ...

⚡ run_memory_profiler.sh           # Helper per memory_profiler
   ├─ Copia script in .temp_memory_*.py
   ├─ Aggiunge @profile alle funzioni specificate
   ├─ Esegue: python -m memory_profiler
   └─ Pulisce file temporanei
   └─ Uso: ./run_memory_profiler.sh <script.py> <func1> [func2] ...
```

**Perché usare gli helper?**
- ✅ Non devi modificare i file originali
- ✅ Aggiungono @profile automaticamente
- ✅ Gestiscono import correttamente
- ✅ Puliscono file temporanei

---

## 📊 File Generati (ignorabili)

```
🗑️  *.lprof                         # Output line_profiler
🗑️  .temp_profiler_*.py             # File temporanei run_line_profiler.sh
🗑️  .temp_memory_*.py               # File temporanei run_memory_profiler.sh
🗑️  __pycache__/                    # Cache Python
🗑️  .venv/                          # Virtual environment (se presente)
```

---

## 🎯 Quick Reference per Livello

### 🟢 Principiante
Inizia con questi file (esecuzione diretta):
```bash
python esempio1_base.py                          # cProfile base
python esempio_pareto.py                         # Principio 80/20
kernprof -l -v demo_line_profiler.py            # line_profiler demo
./run_memory_profiler.sh mp_esempio1_base.py crea_lista_grande  # memory_profiler
```

### 🟡 Intermedio
Esplora questi file (confronti e ottimizzazioni):
```bash
python esempio4_confronto.py                     # Confronto algoritmi
python confronto_pareto.py                       # 6955x speedup!
./run_line_profiler.sh lp_esempio2_bottleneck.py calcola_fibonacci_multipli calcola_fibonacci_multipli_veloce
./run_memory_profiler.sh mp_esempio2_liste_vs_generatori.py usa_lista usa_generatore
```

### 🔴 Avanzato
Usa questi per analisi approfondite:
```bash
python esempio5_contesto.py                      # Profiling selettivo
./run_line_profiler.sh lp_esempio4_algoritmi.py trova_duplicati_lento trova_duplicati_veloce
./run_memory_profiler.sh mp_esempio3_memory_leak.py memory_leak_accumulo no_memory_leak_processa
mprof run mp_esempio1_base.py && mprof plot    # Grafico memoria
```

---

## 📈 Statistiche

```
📚 Totale File:        37
   ├─ Documentazione:   7 (INDEX, README, guide)
   ├─ cProfile:        10 (esempi + funzioni_test)
   ├─ line_profiler:   10 (esempi + helper + demo)
   ├─ memory_profiler:  4 (esempi)
   ├─ Script helper:    2 (run_*.sh)
   └─ Generati:         4 (*.lprof, temp, cache)

🎓 Livelli Difficoltà:
   🟢 Principiante:     6 esempi
   🟡 Intermedio:       9 esempi
   🔴 Avanzato:         5 esempi
   ⭐ Demo/Speciali:    4 esempi

⏱️  Tempo Tutorial:
   🟢 Quick Start:     5 minuti
   🟡 Base:           30 minuti
   🔴 Completo:     1-2 ore
   🚀 Master:         2+ ore

📊 Confronti Impressionanti:
   🏆 confronto_pareto.py:           6955x speedup
   🏆 lp_esempio2:                   2000x speedup (Fibonacci)
   🏆 lp_esempio4:                    340x speedup (O(n²)→O(n))
   🏆 mp_esempio4:                      9x memoria (array vs list)
```

---

## 🔍 Trova File per Scopo

### Voglio imparare...
```
cProfile base           → esempio1_base.py
Ordinamento risultati   → esempio2_statistiche.py
Salvare profili         → esempio3_salvataggio.py
Confrontare algoritmi   → esempio4_confronto.py
Profiling selettivo     → esempio5_contesto.py
Principio di Pareto     → esempio_pareto.py
Speedup impressionanti  → confronto_pareto.py
Misure tempo semplici   → esempio_time.py
```

### Voglio profilare tempo linea per linea...
```
Senza import            → line_profiler_1-4.py (kernprof -l -v)
Con funzioni_test       → lp_esempio1-4.py (./run_line_profiler.sh)
Demo veloce             → demo_line_profiler.py
```

### Voglio profilare memoria...
```
Allocazioni base        → mp_esempio1_base.py
Liste vs generatori     → mp_esempio2_liste_vs_generatori.py
Memory leak             → mp_esempio3_memory_leak.py
Strutture efficienti    → mp_esempio4_strutture_dati.py
```

### Voglio vedere risultati impressionanti...
```
6955x speedup           → confronto_pareto.py
2000x speedup           → lp_esempio2 (Fibonacci)
340x speedup            → lp_esempio4 (O(n²)→O(n))
9x memoria risparmiata  → mp_esempio4 (array vs list)
```

---

## 📖 Ordine di Studio Consigliato

### Percorso Lineare (2 ore)
```
1. INDEX.md                          # Panoramica (5 min)
2. python esempio1_base.py           # cProfile (5 min)
3. python esempio_pareto.py          # Principio 80/20 (5 min)
4. README.md                         # Guida cProfile (15 min)
5. esempio2-5.py                     # Altri esempi cProfile (20 min)
6. kernprof demo_line_profiler.py    # line_profiler (5 min)
7. LINE_PROFILER_README.md           # Guida line_profiler (15 min)
8. lp_esempio1-4.py                  # Esempi line_profiler (20 min)
9. mp_esempio1_base.py               # memory_profiler (5 min)
10. MEMORY_PROFILER_README.md        # Guida memory_profiler (15 min)
11. mp_esempio2-4.py                 # Altri esempi memory (15 min)
12. COMANDI_RAPIDI.md                # Reference (5 min)
```

### Percorso Rapido (30 min)
```
1. INDEX.md                          # Overview
2. python esempio1_base.py           # cProfile
3. python esempio_pareto.py          # 80/20
4. kernprof demo_line_profiler.py    # line_profiler
5. ./run_memory_profiler.sh mp_esempio1_base.py crea_lista_grande
6. COMANDI_RAPIDI.md                 # Reference
```

---

## ✅ Checklist Completamento

### Principiante
- [ ] Letto INDEX.md
- [ ] Eseguito esempio1_base.py
- [ ] Eseguito esempio_pareto.py
- [ ] Eseguito demo_line_profiler.py
- [ ] Eseguito mp_esempio1_base.py
- [ ] Capito ncalls, tottime, cumtime
- [ ] Capito Mem usage, Increment

### Intermedio
- [ ] Letti tutti i README
- [ ] Eseguiti tutti gli esempi cProfile
- [ ] Eseguiti tutti gli esempi line_profiler
- [ ] Eseguiti tutti gli esempi memory_profiler
- [ ] Visto confronto_pareto.py (6955x)
- [ ] Visto lp_esempio2 (Fibonacci 2000x)
- [ ] Visto lp_esempio4 (O(n²)→O(n) 340x)
- [ ] Capito SortKey, @profile, generatori

### Avanzato
- [ ] Profilato il mio codice con cProfile
- [ ] Usato line_profiler sul mio bottleneck
- [ ] Verificato memoria con memory_profiler
- [ ] Creato confronto prima/dopo
- [ ] Calcolato e documentato speedup
- [ ] Usato mprof per grafici temporali
- [ ] Applicato workflow completo

---

**Struttura chiara, esempi pronti, documentazione completa. Tutto pronto per diventare un profiler expert! 🚀**
