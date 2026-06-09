# Memory Profiler - Guida agli Esempi

Questi esempi mostrano come usare **memory_profiler** per analizzare l'uso della memoria linea per linea.

## 📦 Installazione

```bash
pip install memory_profiler
```

## 🎯 Cos'è memory_profiler?

**memory_profiler** analizza l'uso della memoria **LINEA PER LINEA**, mostrando:
- 💾 Quanta memoria usa ogni linea
- 📈 Incremento/decremento di memoria
- 🔍 Memory leak e sprechi

---

## 🚀 Come Usare

### Metodo 1: Script Helper (raccomandato)

```bash
# Esempio 1: Uso base
./run_memory_profiler.sh mp_esempio1_base.py crea_lista_grande crea_piu_liste

# Esempio 2: Liste vs Generatori
./run_memory_profiler.sh mp_esempio2_liste_vs_generatori.py usa_lista usa_generatore

# Esempio 3: Memory Leak
./run_memory_profiler.sh mp_esempio3_memory_leak.py memory_leak_accumulo no_memory_leak_processa

# Esempio 4: Strutture Dati
./run_memory_profiler.sh mp_esempio4_strutture_dati.py usa_liste_python usa_array_efficiente
```

### Metodo 2: Manuale

1. Aggiungi `@profile` alle funzioni:
   ```python
   @profile
   def mia_funzione():
       # ...
   ```

2. Esegui:
   ```bash
   python -m memory_profiler script.py
   ```

### Metodo 3: Profilo nel tempo con grafico

```bash
# Registra uso memoria nel tempo
mprof run script.py

# Visualizza grafico
mprof plot
```

---

## 📚 Esempi Disponibili

### 1️⃣ `mp_esempio1_base.py` - Uso Base
**Cosa mostra:** Come memory_profiler traccia l'allocazione di memoria

**Funzioni:**
- `crea_lista_grande` - Alloca 1 milione di numeri
- `crea_piu_liste` - Alloca più liste (memoria si somma)
- `elabora_stringhe` - Operazioni su stringhe

**Comando:**
```bash
./run_memory_profiler.sh mp_esempio1_base.py crea_lista_grande crea_piu_liste
```

**Cosa aspettarsi:** Vedrai picchi di memoria quando le liste vengono create.

---

### 2️⃣ `mp_esempio2_liste_vs_generatori.py` - Liste vs Generatori
**Cosa mostra:** Differenza drammatica nell'uso di memoria

**Confronta:**
- `usa_lista` - Lista completa in memoria 💥
- `usa_generatore` - Calcolo on-demand, memoria costante ✅
- `concatena_stringhe_male` - Concatenazione inefficiente
- `concatena_stringhe_bene` - Uso di join()

**Comando:**
```bash
./run_memory_profiler.sh mp_esempio2_liste_vs_generatori.py usa_lista usa_generatore
```

**Risultato atteso:**
- Lista: ~40 MB per 1 milione di numeri
- Generatore: ~0.1 MB (memoria costante!)

---

### 3️⃣ `mp_esempio3_memory_leak.py` - Memory Leak e Ottimizzazione
**Cosa mostra:** Come identificare e risolvere memory leak

**Confronta:**
- `memory_leak_accumulo` - Accumula dati continuamente 🐛
- `no_memory_leak_processa` - Processa e libera ✅
- `duplica_dati_inutilmente` - Copie inutili
- `usa_dati_direttamente` - Nessuna copia

**Comando:**
```bash
./run_memory_profiler.sh mp_esempio3_memory_leak.py memory_leak_accumulo no_memory_leak_processa
```

**Lezione:** Evita di accumulare dati se non necessario!

---

### 4️⃣ `mp_esempio4_strutture_dati.py` - Strutture Dati Efficienti
**Cosa mostra:** Scelta della struttura dati impatta la memoria

**Confronta:**
- `usa_liste_python` - Liste Python native (ogni int è un oggetto)
- `usa_array_efficiente` - array.array (memoria compatta)
- `processa_matrice_liste` - Matrice con liste annidate
- `processa_matrice_flat` - Matrice "flat" (più efficiente)

**Comando:**
```bash
./run_memory_profiler.sh mp_esempio4_strutture_dati.py usa_liste_python usa_array_efficiente
```

**Risultato atteso:** array.array usa 3-5x meno memoria!

---

## 📊 Interpretare l'Output

```
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     5     38.5 MiB     38.5 MiB           1   @profile
     6                                         def crea_lista_grande():
     7     38.5 MiB      0.0 MiB           1       lista = []
     8                                         
     9     76.8 MiB     38.3 MiB      1000001       for i in range(1000000):
    10     76.8 MiB      0.0 MiB      1000000           lista.append(i)
    11                                         
    12     76.8 MiB      0.0 MiB           1       somma = sum(lista)
    13                                         
    14     76.8 MiB      0.0 MiB           1       return somma
```

**Colonne:**
- **Mem usage**: Memoria totale usata
- **Increment**: Memoria allocata/liberata in quella linea
- **Occurrences**: Quante volte eseguita
- **Line Contents**: Codice

**Cosa cercare:**
- 📈 **Increment alto**: Quella linea alloca molta memoria
- 📉 **Increment negativo**: Memoria liberata
- 🔥 **Crescita continua**: Possibile memory leak

---

## 🆚 Differenze tra Tools

| Tool | Analizza | Quando Usare |
|------|----------|--------------|
| **time** | Tempo totale | Quick check velocità |
| **cProfile** | Tempo per funzione | Trova funzioni lente |
| **line_profiler** | Tempo per linea | Trova linee lente |
| **memory_profiler** | Memoria per linea | Trova problemi memoria |
| **tracemalloc** | Tracciamento memoria | Memory leak complessi |

---

## 💡 Pattern Comuni

### ✅ BUONO: Generator invece di Lista
```python
# Male: carica tutto in memoria
numeri = [i ** 2 for i in range(1000000)]

# Bene: genera on-demand
numeri = (i ** 2 for i in range(1000000))
```

### ✅ BUONO: Join invece di Concatenazione
```python
# Male: crea nuova stringa ogni volta
risultato = ""
for s in stringhe:
    risultato += s

# Bene: join è ottimizzato
risultato = "".join(stringhe)
```

### ✅ BUONO: Del per Liberare Memoria
```python
dati_grandi = elabora_dati()
risultato = analizza(dati_grandi)
del dati_grandi  # Libera subito la memoria
```

### ✅ BUONO: Processa in Chunk
```python
# Male: carica tutto
with open('huge_file.txt') as f:
    contenuto = f.read()  # ❌ Tutto in memoria!

# Bene: processa riga per riga
with open('huge_file.txt') as f:
    for riga in f:  # ✅ Una riga alla volta
        processa(riga)
```

---

## 🎯 Workflow Ottimizzazione Memoria

1. **Profila** con memory_profiler
2. **Identifica** picchi di memoria
3. **Considera:**
   - Posso usare generatori invece di liste?
   - Posso processare in chunk invece di tutto insieme?
   - Posso usare strutture più compatte (array, numpy)?
   - Posso liberare memoria prima (del)?
4. **Ri-profila** per verificare miglioramento

---

## 🔧 Tips Avanzati

### Profilo grafico con mprof

```bash
# Registra profilo
mprof run --python python script.py

# Visualizza grafico
mprof plot
```

### Usa con IPython/Jupyter

```python
%load_ext memory_profiler
%memit funzione()
%mprun -f funzione funzione()
```

### Traccia allocazioni specifiche

```python
import tracemalloc

tracemalloc.start()
# ... tuo codice ...
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')

for stat in top_stats[:10]:
    print(stat)
```

---

## 📚 Risorse

- [Memory Profiler GitHub](https://github.com/pythonprofilers/memory_profiler)
- [Documentazione ufficiale](https://pypi.org/project/memory-profiler/)
- [tracemalloc](https://docs.python.org/3/library/tracemalloc.html) - Built-in Python

---

## ✅ Checklist

```bash
# 1. Test liste vs generatori
./run_memory_profiler.sh mp_esempio2_liste_vs_generatori.py usa_lista usa_generatore

# 2. Identifica memory leak
./run_memory_profiler.sh mp_esempio3_memory_leak.py memory_leak_accumulo no_memory_leak_processa

# 3. Ottimizza strutture dati
./run_memory_profiler.sh mp_esempio4_strutture_dati.py usa_liste_python usa_array_efficiente
```

**Buon memory profiling! 💾**
