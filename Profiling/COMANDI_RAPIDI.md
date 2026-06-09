# 🚀 Comandi Rapidi - Profiling Python

Riferimento veloce per tutti gli strumenti di profiling disponibili.

---

## 📊 cProfile - Profiling per Funzione

### Esempi Base
```bash
# Esempio 1: Uso base
python esempio1_base.py

# Esempio 2: Statistiche ordinate
python esempio2_statistiche.py

# Esempio 3: Salvataggio risultati
python esempio3_salvataggio.py

# Esempio 4: Confronto algoritmi
python esempio4_confronto.py

# Esempio 5: Profiling selettivo
python esempio5_contesto.py
```

### Esempi Principio di Pareto
```bash
# Identificare bottleneck (Principio 80/20)
python esempio_pareto.py

# Confronto prima/dopo ottimizzazione
python confronto_pareto.py
```

### Esempio Time
```bash
# Misurazioni tempo semplici
python esempio_time.py
```

**📖 Documentazione**: `README.md`

---

## ⏱️ line_profiler - Profiling per Linea (TEMPO)

### Esempi Self-Contained (senza funzioni_test.py)
```bash
# Esempio 1: Base
kernprof -l -v line_profiler_1_base.py

# Esempio 2: Bottleneck
kernprof -l -v line_profiler_2_bottleneck.py

# Esempio 3: Confronto
kernprof -l -v line_profiler_3_confronto.py

# Esempio 4: Algoritmi
kernprof -l -v line_profiler_4_algoritmi.py
```

### Esempi con funzioni_test.py (usa script helper)
```bash
# Esempio 1: Base
./run_line_profiler.sh lp_esempio1_base.py esegui_operazioni_miste elabora_numeri

# Esempio 2: Bottleneck Fibonacci
./run_line_profiler.sh lp_esempio2_bottleneck.py calcola_fibonacci_multipli calcola_fibonacci_multipli_veloce

# Esempio 3: Confronto metodi
./run_line_profiler.sh lp_esempio3_confronto.py metodo_con_loop_separati metodo_con_loop_unico metodo_con_builtin

# Esempio 4: Algoritmi O(n²) vs O(n)
./run_line_profiler.sh lp_esempio4_algoritmi.py trova_duplicati_lento trova_duplicati_veloce
```

### Demo Pronto all'Uso
```bash
# Demo con @profile già inserito
kernprof -l -v demo_line_profiler.py
```

**📖 Documentazione**: `LINE_PROFILER_README.md`, `LINE_PROFILER_ESEMPI.md`

---

## 💾 memory_profiler - Profiling per Linea (MEMORIA)

### Tutti gli Esempi (usa script helper)
```bash
# Esempio 1: Uso base
./run_memory_profiler.sh mp_esempio1_base.py crea_lista_grande crea_piu_liste elabora_stringhe

# Esempio 2: Liste vs Generatori ⭐
./run_memory_profiler.sh mp_esempio2_liste_vs_generatori.py usa_lista usa_generatore

# Esempio 3: Memory Leak ⚠️
./run_memory_profiler.sh mp_esempio3_memory_leak.py memory_leak_accumulo no_memory_leak_processa

# Esempio 4: Strutture Dati Efficienti
./run_memory_profiler.sh mp_esempio4_strutture_dati.py usa_liste_python usa_array_efficiente

# Tutte le funzioni di un esempio
./run_memory_profiler.sh mp_esempio2_liste_vs_generatori.py usa_lista usa_generatore concatena_stringhe_male concatena_stringhe_bene
```

### Profiling con Grafico Temporale
```bash
# Registra profilo memoria nel tempo
mprof run mp_esempio1_base.py

# Visualizza grafico
mprof plot
```

**📖 Documentazione**: `MEMORY_PROFILER_README.md`

---

## 🎯 Workflow Ottimizzazione Completo

### 1. Identificare Bottleneck Generale (cProfile)
```bash
python esempio_pareto.py
```
→ Identifica quali funzioni consumano più tempo

### 2. Analizzare Linee Specifiche (line_profiler)
```bash
./run_line_profiler.sh lp_esempio2_bottleneck.py calcola_fibonacci_multipli
```
→ Trova esattamente quali linee sono lente

### 3. Verificare Uso Memoria (memory_profiler)
```bash
./run_memory_profiler.sh mp_esempio2_liste_vs_generatori.py usa_lista
```
→ Controlla se ci sono problemi di memoria

### 4. Ottimizzare e Ricontrollare
```bash
# Confronta versioni ottimizzate
python confronto_pareto.py
./run_line_profiler.sh lp_esempio2_bottleneck.py calcola_fibonacci_multipli_veloce
./run_memory_profiler.sh mp_esempio2_liste_vs_generatori.py usa_generatore
```

---

## 📋 Cheat Sheet

| Tool | Analizza | Comando Tipico | Output |
|------|----------|----------------|--------|
| **cProfile** | Tempo per funzione | `python script.py` | Funzioni + tempo totale |
| **line_profiler** | Tempo per linea | `./run_line_profiler.sh script.py func1` | Tempo ogni linea |
| **memory_profiler** | Memoria per linea | `./run_memory_profiler.sh script.py func1` | Memoria ogni linea |
| **time** | Tempo totale | `time python script.py` | Secondi totali |

---

## 🔥 Esempi Pronti da Eseguire

### Quick Start - Test Veloce di Tutto
```bash
# Test cProfile (2 secondi)
python esempio1_base.py

# Test line_profiler (3 secondi)
kernprof -l -v demo_line_profiler.py

# Test memory_profiler (10 secondi)
./run_memory_profiler.sh mp_esempio1_base.py crea_lista_grande
```

### Confronti Impressionanti
```bash
# 6955x speedup con ottimizzazione!
python confronto_pareto.py

# Fibonacci: ricorsivo vs iterativo (2000x)
./run_line_profiler.sh lp_esempio2_bottleneck.py calcola_fibonacci_multipli calcola_fibonacci_multipli_veloce

# O(n²) vs O(n) - 340x più veloce!
./run_line_profiler.sh lp_esempio4_algoritmi.py trova_duplicati_lento trova_duplicati_veloce

# Liste vs Generatori - 9x meno memoria!
./run_memory_profiler.sh mp_esempio4_strutture_dati.py usa_liste_python usa_array_efficiente
```

### Principio di Pareto in Azione
```bash
# Identifica il 20% critico
python esempio_pareto.py

# Verifica l'80% di miglioramento
python confronto_pareto.py
```

---

## 🛠️ Script Helper

### run_line_profiler.sh
Aggiunge automaticamente `@profile` e esegue kernprof:
```bash
./run_line_profiler.sh <script.py> <funzione1> [funzione2] ...
```

### run_memory_profiler.sh
Aggiunge automaticamente `@profile` e esegue memory_profiler:
```bash
./run_memory_profiler.sh <script.py> <funzione1> [funzione2] ...
```

---

## 📚 Documentazione Completa

| File | Contenuto |
|------|-----------|
| `README.md` | Guida completa cProfile + esempi 1-5 |
| `LINE_PROFILER_README.md` | Guida completa line_profiler |
| `LINE_PROFILER_ESEMPI.md` | Dettagli esempi lp_esempio*.py |
| `MEMORY_PROFILER_README.md` | Guida completa memory_profiler |
| `COMANDI_RAPIDI.md` | Questo file - quick reference |

---

## ⚡ Tips Veloci

### Quando usare cosa?
- 🤔 **Non so dove sia il problema** → `python esempio_pareto.py`
- 🐌 **So quale funzione è lenta** → `./run_line_profiler.sh`
- 💾 **Problemi di memoria** → `./run_memory_profiler.sh`
- ⏱️ **Solo tempo totale** → `python esempio_time.py`

### Pattern Comuni da Cercare

**line_profiler**:
- ⚠️ Una linea con >50% del tempo → bottleneck!
- 🔁 Loop con Time elevato → candidato per ottimizzazione
- 🐢 Chiamate ricorsive → considera versione iterativa

**memory_profiler**:
- 📈 Increment positivo crescente → possibile memory leak
- 💥 Increment alto in una linea → alloca troppa memoria
- 🔄 Liste grandi in loop → considera generatori

---

## 🎓 Tutorial Step-by-Step

### Principiante (30 min)
1. `python esempio1_base.py` - Capire cProfile
2. `python esempio_pareto.py` - Principio 80/20
3. `kernprof -l -v demo_line_profiler.py` - Line profiling
4. `./run_memory_profiler.sh mp_esempio1_base.py crea_lista_grande` - Memory profiling

### Intermedio (1 ora)
1. Esempi 2-5 di cProfile
2. Tutti gli esempi line_profiler_*.py
3. Esempi mp_esempio 1-4 con memory_profiler
4. Leggi README completi

### Avanzato (2 ore)
1. Applica al tuo codice
2. Crea confronti prima/dopo
3. Combina i 3 strumenti per analisi completa
4. Misura speedup ottenuti

---

**Buon profiling! 🚀**

_Ricorda: Profila sempre prima di ottimizzare!_
