# Tutorial cProfile - Guida agli Esempi

Questa directory contiene una serie di esempi progressivi per imparare a usare **cProfile** per il profiling di codice Python.

## 📚 Struttura degli Esempi

Esegui gli esempi in ordine numerico per un apprendimento progressivo:

### 🔧 File di supporto

- **`funzioni_test.py`** - Funzioni comuni usate negli esempi

### 📖 Esempi da eseguire in ordine:

#### 1️⃣ `esempio1_base.py` - Introduzione a cProfile
**Cosa impari:**
- Uso base di `cProfile.run()`
- Come interpretare l'output base
- Differenza tra `tottime` e `cumtime`

**Esegui:**
```bash
python esempio1_base.py
```

---

#### 2️⃣ `esempio2_statistiche.py` - Analisi dettagliata
**Cosa impari:**
- Creare un oggetto `Profile()` per controllo avanzato
- Ordinare statistiche per tempo, chiamate, ecc.
- Filtrare risultati per file/funzione
- Usare `pstats.Stats()` per analisi personalizzata

**Esegui:**
```bash
python esempio2_statistiche.py
```

---

#### 3️⃣ `esempio3_salvataggio.py` - Persistenza dei risultati
**Cosa impari:**
- Salvare risultati profiling in file `.prof`
- Caricare e analizzare risultati salvati
- Usare cProfile da linea di comando
- Visualizzazione con SnakeViz

**Esegui:**
```bash
python esempio3_salvataggio.py
```

---

#### 4️⃣ `esempio4_confronto.py` - Confronto implementazioni
**Cosa impari:**
- Confrontare diverse implementazioni dello stesso algoritmo
- Identificare algoritmi inefficienti
- Usare cProfile per decisioni di ottimizzazione
- Caso pratico: Fibonacci ricorsivo vs iterativo

**Esegui:**
```bash
python esempio4_confronto.py
```

---

#### 5️⃣ `esempio5_contesto.py` - Profiling selettivo
**Cosa impari:**
- Profilare solo sezioni specifiche del codice
- Usare `enable()`/`disable()`
- Usare `runcall()` per singole funzioni
- Ridurre l'overhead del profiling

**Esegui:**
```bash
python esempio5_contesto.py
```

---

#### 🎯 `esempio_pareto.py` - PRINCIPIO DI PARETO (BONUS)
**Cosa impari:**
- Come il profiling dimostra il Principio di Pareto (regola 80/20)
- Identificare il 20% del codice che consuma l'80% del tempo
- Analisi della distribuzione del tempo di esecuzione
- Dove concentrare gli sforzi di ottimizzazione

**Esegui:**
```bash
python esempio_pareto.py
```

---

#### 🚀 `confronto_pareto.py` - PRIMA/DOPO OTTIMIZZAZIONE (BONUS)
**Cosa impari:**
- Confronto prestazioni prima e dopo l'ottimizzazione
- Misurare l'impatto reale delle ottimizzazioni
- Dimostrazione pratica del Principio di Pareto
- Strategia di ottimizzazione mirata

**Esegui:**
```bash
python confronto_pareto.py
```

---

## 🎯 Guida Rapida ai Comandi

### Profiling base
```python
import cProfile
cProfile.run('mia_funzione()')
```

### Profiling con analisi
```python
import cProfile
import pstats

profiler = cProfile.Profile()
profiler.enable()
# ... tuo codice ...
profiler.disable()

stats = pstats.Stats(profiler)
stats.sort_stats('time')
stats.print_stats(10)
```

### Da linea di comando
```bash
# Esegui e salva
python -m cProfile -o output.prof script.py

# Analizza risultati
python -m pstats output.prof
```

### Con SnakeViz (visualizzazione grafica)
```bash
pip install snakeviz
snakeviz output.prof
```

---

## 📊 Interpretare l'Output

| Colonna | Significato |
|---------|-------------|
| `ncalls` | Numero di chiamate alla funzione |
| `tottime` | Tempo NELLA funzione (escluse chiamate interne) |
| `percall` | `tottime / ncalls` |
| `cumtime` | Tempo TOTALE incluse tutte le chiamate interne |
| `percall` | `cumtime / ncalls` |
| `filename:lineno(function)` | Dove si trova la funzione |

**Regola pratica:**
- **Alto `tottime`** → La funzione stessa è lenta
- **Alto `cumtime`** ma basso `tottime` → La funzione chiama altre funzioni lente
- **Alto `ncalls`** → La funzione è chiamata troppo spesso

---

## 🎯 Il Principio di Pareto nel Profiling

**Regola 80/20:** L'80% del tempo di esecuzione è consumato dal 20% del codice

**Implicazioni pratiche:**
- 🔍 Usa il profiling per identificare il 20% critico
- ⚡ Ottimizza SOLO quel 20% per massimo impatto
- ⏱️ Non perdere tempo su codice già veloce
- 📊 Misura sempre prima e dopo l'ottimizzazione

Gli esempi `esempio_pareto.py` e `confronto_pareto.py` dimostrano questo concetto!

---

## 🔍 Quando Usare cProfile

✅ **Usa cProfile per:**
- Trovare bottleneck nelle prestazioni
- Confrontare implementazioni alternative
- Ottimizzare codice lento
- Analizzare tempo di esecuzione di funzioni
- Applicare il Principio di Pareto

❌ **Non usare cProfile per:**
- Profiling linea per linea (usa `line_profiler`)
- Analisi uso memoria (usa `memory_profiler`)
- Debug di errori logici
- Code coverage (usa `coverage.py`)

---

## 🚀 Prossimi Passi

Dopo aver completato tutti gli esempi, prova a:
1. Profilare il tuo codice esistente
2. Identificare le 3 funzioni più lente
3. Ottimizzarle e riprofilare per confrontare
4. Usare SnakeViz per visualizzazione grafica

---

## 📚 Risorse Aggiuntive

- [Documentazione ufficiale cProfile](https://docs.python.org/3/library/profile.html)
- [SnakeViz - Visualizzatore grafico](https://jiffyclub.github.io/snakeviz/)
- [line_profiler - Profiling linea per linea](https://github.com/pyutils/line_profiler)
- [memory_profiler - Analisi memoria](https://pypi.org/project/memory-profiler/)

---

**Buon profiling! 🎯**
