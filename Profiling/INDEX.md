# 📊 Tutorial Completo - Python Profiling

Guida completa al profiling e ottimizzazione del codice Python con esempi pratici e progressivi.

---

## 🎯 Panoramica

Questa raccolta contiene **tutorial completi** per 3 strumenti essenziali di profiling Python:

1. **cProfile** - Analisi tempo di esecuzione per funzione
2. **line_profiler** - Analisi tempo linea per linea
3. **memory_profiler** - Analisi uso memoria linea per linea

Ogni tool include:
- ✅ Esempi progressivi (da base ad avanzato)
- ✅ Script helper per esecuzione semplificata
- ✅ Documentazione dettagliata
- ✅ Dimostrazione del Principio di Pareto (80/20)

---

## 🚀 Quick Start

### Installazione
```bash
# line_profiler
pip install line-profiler

# memory_profiler
pip install memory_profiler

# cProfile è già incluso in Python!
```

### Primi Test (5 minuti)
```bash
# cProfile - tempo per funzione
python esempio1_base.py

# line_profiler - tempo per linea
kernprof -l -v demo_line_profiler.py

# memory_profiler - memoria per linea
./run_memory_profiler.sh mp_esempio1_base.py crea_lista_grande
```

---

## 📚 Struttura del Tutorial

### 1️⃣ cProfile - Profiling per Funzione

**File:** 14 esempi + funzioni_test.py

**Esempi Base:**
- `esempio1_base.py` - Uso base di cProfile.run()
- `esempio2_statistiche.py` - Ordinamento statistiche (TIME, CUMULATIVE, CALLS)
- `esempio3_salvataggio.py` - Salvare e caricare profili .prof
- `esempio4_confronto.py` - Confronto algoritmi (ricorsivo vs iterativo)
- `esempio5_contesto.py` - Profiling selettivo con enable/disable

**Principio di Pareto:**
- `esempio_pareto.py` - Identificare il 20% critico del codice
- `confronto_pareto.py` - Dimostrazione 6955x speedup ottimizzando solo il bottleneck

**Time Module:**
- `esempio_time.py` - Misurazioni semplici con time.time() e time.perf_counter()

**Funzioni Condivise:**
- `funzioni_test.py` - Modulo con funzioni di test usate in tutti gli esempi

**📖 Documentazione:** [`README.md`](README.md)

---

### 2️⃣ line_profiler - Tempo per Linea

**File:** 9 esempi + script helper

**Esempi Self-Contained (senza import):**
- `line_profiler_1_base.py` - Analisi base
- `line_profiler_2_bottleneck.py` - Identificare bottleneck
- `line_profiler_3_confronto.py` - Confronto implementazioni
- `line_profiler_4_algoritmi.py` - O(n²) vs O(n)

**Esempi con funzioni_test.py:**
- `lp_esempio1_base.py` - Operazioni miste (veloce/lenta/I-O)
- `lp_esempio2_bottleneck.py` - Fibonacci ricorsivo vs iterativo (2000x diff!)
- `lp_esempio3_confronto.py` - Loop separati vs unico vs builtin
- `lp_esempio4_algoritmi.py` - Ottimizzazione algoritmica

**Demo Pronto:**
- `demo_line_profiler.py` - Eseguibile direttamente con kernprof

**Script Helper:**
- `run_line_profiler.sh` - Aggiunge @profile automaticamente

**📖 Documentazione:** [`LINE_PROFILER_README.md`](LINE_PROFILER_README.md), [`LINE_PROFILER_ESEMPI.md`](LINE_PROFILER_ESEMPI.md)

---

### 3️⃣ memory_profiler - Memoria per Linea

**File:** 4 esempi + script helper

**Esempi:**
- `mp_esempio1_base.py` - Uso base, allocazione liste
- `mp_esempio2_liste_vs_generatori.py` - Liste vs generatori (9x differenza!)
- `mp_esempio3_memory_leak.py` - Identificare e risolvere memory leak
- `mp_esempio4_strutture_dati.py` - Liste vs array.array vs strutture efficienti

**Script Helper:**
- `run_memory_profiler.sh` - Aggiunge @profile automaticamente

**📖 Documentazione:** [`MEMORY_PROFILER_README.md`](MEMORY_PROFILER_README.md)

---

## 🎓 Percorsi di Apprendimento

### 🟢 Principiante (30 minuti)

Obiettivo: Capire i concetti base di profiling

1. **cProfile Base**
   ```bash
   python esempio1_base.py
   ```
   → Capire output cProfile

2. **Principio di Pareto**
   ```bash
   python esempio_pareto.py
   ```
   → Identificare il 20% critico

3. **line_profiler Demo**
   ```bash
   kernprof -l -v demo_line_profiler.py
   ```
   → Vedere tempo per linea

4. **memory_profiler Base**
   ```bash
   ./run_memory_profiler.sh mp_esempio1_base.py crea_lista_grande
   ```
   → Vedere allocazione memoria

**Concetti appresi:** ncalls, tottime, cumtime, % Time, Mem usage, Increment

---

### 🟡 Intermedio (1-2 ore)

Obiettivo: Usare tutti gli strumenti autonomamente

1. **cProfile - Tutti gli esempi**
   ```bash
   python esempio2_statistiche.py
   python esempio3_salvataggio.py
   python esempio4_confronto.py
   python esempio5_contesto.py
   ```

2. **Confronti Impressionanti**
   ```bash
   python confronto_pareto.py  # 6955x speedup!
   ./run_line_profiler.sh lp_esempio2_bottleneck.py calcola_fibonacci_multipli calcola_fibonacci_multipli_veloce  # 2000x
   ./run_line_profiler.sh lp_esempio4_algoritmi.py trova_duplicati_lento trova_duplicati_veloce  # 340x
   ```

3. **memory_profiler - Tutti gli esempi**
   ```bash
   ./run_memory_profiler.sh mp_esempio2_liste_vs_generatori.py usa_lista usa_generatore
   ./run_memory_profiler.sh mp_esempio3_memory_leak.py memory_leak_accumulo no_memory_leak_processa
   ./run_memory_profiler.sh mp_esempio4_strutture_dati.py usa_liste_python usa_array_efficiente
   ```

4. **Leggere documentazione**
   - [`README.md`](README.md)
   - [`LINE_PROFILER_README.md`](LINE_PROFILER_README.md)
   - [`MEMORY_PROFILER_README.md`](MEMORY_PROFILER_README.md)

**Concetti appresi:** Ordinamento statistiche, confronti algoritmi, generatori, memory leak, complessità O(n)

---

### 🔴 Avanzato (2+ ore)

Obiettivo: Applicare al codice reale

1. **Profila il tuo codice**
   ```bash
   # cProfile
   python -m cProfile -s cumulative tuo_script.py
   
   # line_profiler (aggiungi @profile alle funzioni lente)
   kernprof -l -v tuo_script.py
   
   # memory_profiler
   python -m memory_profiler tuo_script.py
   ```

2. **Workflow completo di ottimizzazione**
   - Profila con cProfile → identifica funzione lenta
   - Profila con line_profiler → identifica linea specifica
   - Profila con memory_profiler → verifica uso memoria
   - Ottimizza
   - Ri-profila per confermare miglioramento
   - Documenta speedup ottenuto

3. **Creazione confronti personalizzati**
   - Usa `esempio4_confronto.py` come template
   - Confronta versioni originale vs ottimizzata
   - Calcola e documenta speedup

4. **Analisi avanzata**
   - Usa `mprof` per grafici memoria nel tempo
   - Combina cProfile con line_profiler per analisi completa
   - Esporta e condividi risultati

**Concetti appresi:** Workflow professionale, decisioni di ottimizzazione basate su dati, documentazione miglioramenti

---

## 🔥 Demo Impressionanti

### 🎯 Principio di Pareto in Azione
```bash
python confronto_pareto.py
```
**Risultato:** Modificando **SOLO 1 funzione su 5 (20%)** ottieni **6955x speedup** (0.27s → 0.00004s)

### 🐢 Fibonacci: Ricorsivo vs Iterativo
```bash
./run_line_profiler.sh lp_esempio2_bottleneck.py calcola_fibonacci_multipli calcola_fibonacci_multipli_veloce
```
**Risultato:** Versione iterativa **2000x più veloce** (0.19s → 0.0001s)

### 🔍 Algoritmi: O(n²) vs O(n)
```bash
./run_line_profiler.sh lp_esempio4_algoritmi.py trova_duplicati_lento trova_duplicati_veloce
```
**Risultato:** Algoritmo O(n) **340x più veloce** (0.178s → 0.0005s)

### 💾 Liste vs Generatori
```bash
./run_memory_profiler.sh mp_esempio2_liste_vs_generatori.py usa_lista usa_generatore
```
**Risultato:** Generatore usa **9x meno memoria** (38 MiB vs costante)

### 🏗️ Liste vs Array
```bash
./run_memory_profiler.sh mp_esempio4_strutture_dati.py usa_liste_python usa_array_efficiente
```
**Risultato:** array.array usa **3-5x meno memoria** delle liste Python

---

## 📖 Documentazione Completa

| File | Contenuto | Quando Leggere |
|------|-----------|----------------|
| **INDEX.md** | Questo file - panoramica generale | Inizio |
| **COMANDI_RAPIDI.md** | Quick reference di tutti i comandi | Reference continuo |
| **README.md** | Guida completa cProfile | Dopo esempi cProfile |
| **LINE_PROFILER_README.md** | Guida completa line_profiler | Dopo esempi line_profiler |
| **LINE_PROFILER_ESEMPI.md** | Dettagli lp_esempio*.py | Quando usi lp_esempio |
| **MEMORY_PROFILER_README.md** | Guida completa memory_profiler | Dopo esempi memory |

---

## 🛠️ Script Helper

### run_line_profiler.sh
```bash
./run_line_profiler.sh <script.py> <funzione1> [funzione2] ...
```
Aggiunge automaticamente `@profile` alle funzioni specificate ed esegue `kernprof`.

**Esempio:**
```bash
./run_line_profiler.sh lp_esempio2_bottleneck.py calcola_fibonacci_multipli
```

### run_memory_profiler.sh
```bash
./run_memory_profiler.sh <script.py> <funzione1> [funzione2] ...
```
Aggiunge automaticamente `@profile` alle funzioni specificate ed esegue `memory_profiler`.

**Esempio:**
```bash
./run_memory_profiler.sh mp_esempio1_base.py crea_lista_grande
```

---

## 💡 Quando Usare Cosa?

### Decision Tree

```
Ho un problema di performance?
│
├─ Non so dove sia il problema
│  └─ USA: python esempio_pareto.py (cProfile)
│     → Identifica funzioni lente
│
├─ So quale funzione è lenta
│  └─ USA: ./run_line_profiler.sh script.py funzione
│     → Trova linea specifica lenta
│
├─ Il programma consuma troppa memoria
│  └─ USA: ./run_memory_profiler.sh script.py funzione
│     → Identifica allocazioni grosse
│
└─ Voglio solo sapere quanto tempo impiega
   └─ USA: python esempio_time.py
      → Misura semplice
```

### Tabella Comparativa

| Situazione | Tool | Comando |
|------------|------|---------|
| "Il programma è lento ma non so perché" | cProfile | `python esempio_pareto.py` |
| "Questa funzione è lenta, quale linea?" | line_profiler | `./run_line_profiler.sh` |
| "Il programma usa troppa RAM" | memory_profiler | `./run_memory_profiler.sh` |
| "Memory leak? Memoria cresce sempre" | memory_profiler | `mprof run script.py && mprof plot` |
| "Voglio confrontare 2 algoritmi" | cProfile + line_profiler | `python esempio4_confronto.py` |
| "Voglio misura veloce del tempo" | time | `python esempio_time.py` |

---

## 🎯 Principio di Pareto (80/20)

**Regola d'oro dell'ottimizzazione:**

> 📊 **L'80% del tempo di esecuzione**  
> **è consumato dal 20% del codice**

**Implicazioni:**
- ✅ Profila PRIMA di ottimizzare (identifica il 20%)
- ✅ Concentrati sul bottleneck reale (massimo impatto)
- ❌ NON ottimizzare codice già veloce (spreco di tempo)

**Demo:**
```bash
python confronto_pareto.py
```
Mostra come ottimizzare **1 funzione su 5** (20%) produce **100% del beneficio**.

---

## 📊 Pattern Comuni e Soluzioni

### ⚡ Ottimizzazioni Tempo

| Problema | Soluzione | Speedup Tipico | Esempio |
|----------|-----------|----------------|---------|
| Fibonacci ricorsivo | Versione iterativa | 100-1000x | lp_esempio2 |
| Loop O(n²) | Algoritmo O(n) con set | 100-1000x | lp_esempio4 |
| Lista comprehension | Built-in functions | 2-5x | lp_esempio3 |
| Calcoli ripetuti | Caching/memoization | 10-100x | - |

### 💾 Ottimizzazioni Memoria

| Problema | Soluzione | Risparmio | Esempio |
|----------|-----------|-----------|---------|
| Liste grandi | Generatori | 10-100x | mp_esempio2 |
| Concatenazione stringhe | str.join() | 5-10x | mp_esempio2 |
| Liste di numeri | array.array | 3-5x | mp_esempio4 |
| Accumulo continuo | Processamento streaming | Evita leak | mp_esempio3 |

---

## 🚦 Best Practices

### ✅ DO - Fai Sempre
1. **Profila prima di ottimizzare** - Mai ottimizzare a intuito
2. **Misura il before/after** - Documenta miglioramenti
3. **Concentrati sul bottleneck** - Principio 80/20
4. **Usa il tool giusto** - cProfile → line_profiler → memory_profiler
5. **Verifica correttezza** - Ottimizzazione non deve introdurre bug

### ❌ DON'T - Non Fare Mai
1. **Ottimizzare senza profilare** - Probabile spreco di tempo
2. **Ottimizzare tutto** - Focalizzati sul 20% critico
3. **Ignorare la complessità algoritmica** - O(n²) resterà lento anche ottimizzato
4. **Sacrificare leggibilità per micro-ottimizzazioni** - Solo su bottleneck dimostrati
5. **Dimenticare di ri-profilare** - Verifica sempre l'impatto

---

## 📈 Workflow Professionale

```
1. BASELINE
   └─ Profila codice attuale (cProfile)
   └─ Documenta tempo/memoria

2. IDENTIFICA
   └─ Trova bottleneck con esempio_pareto.py
   └─ Nota funzioni con >50% tempo

3. ANALIZZA
   └─ Profila bottleneck con line_profiler
   └─ Trova linea/linee specifiche lente
   └─ Verifica memoria con memory_profiler

4. OTTIMIZZA
   └─ Cambia algoritmo (O(n²) → O(n))
   └─ Usa strutture dati efficienti
   └─ Considera generatori/lazy evaluation

5. VERIFICA
   └─ Ri-profila codice ottimizzato
   └─ Calcola speedup
   └─ Verifica correttezza

6. DOCUMENTA
   └─ Before/After con numeri
   └─ Speedup ottenuto
   └─ Decisioni prese
```

---

## 🎓 Risorse Aggiuntive

### Python Official Docs
- [cProfile](https://docs.python.org/3/library/profile.html)
- [pstats](https://docs.python.org/3/library/profile.html#module-pstats)
- [time](https://docs.python.org/3/library/time.html)
- [tracemalloc](https://docs.python.org/3/library/tracemalloc.html)

### External Tools
- [line_profiler](https://github.com/pyutils/line_profiler)
- [memory_profiler](https://github.com/pythonprofilers/memory_profiler)

### Performance Books
- "High Performance Python" - Micha Gorelick & Ian Ozsvald
- "Python Performance" - Anthony Shaw

---

## 🏁 Conclusione

Questo tutorial ti fornisce **tutto il necessario** per:
- ✅ Profilare codice Python professionalmente
- ✅ Identificare bottleneck reali (non immaginari)
- ✅ Ottimizzare con impatto misurabile
- ✅ Applicare il Principio di Pareto all'ottimizzazione

**Prossimi passi:**
1. Completa il percorso Principiante (30 min)
2. Prova gli esempi Intermedi (1-2 ore)
3. Applica al tuo codice reale
4. Condividi i tuoi risultati!

---

**Buon profiling e buone ottimizzazioni! 🚀**

_"Premature optimization is the root of all evil." - Donald Knuth_  
_"But measured, targeted optimization is pure gold!" - Ogni profiler esperto_
