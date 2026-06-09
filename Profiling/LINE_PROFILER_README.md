# Tutorial line_profiler - Guida Completa

## 📦 Installazione

```bash
pip install line_profiler
```

## 🎯 Cos'è line_profiler?

**line_profiler** analizza il codice **LINEA PER LINEA**, mostrando:
- ⏱️ Quanto tempo impiega ogni singola linea
- 🔢 Quante volte ogni linea è eseguita
- 📊 Percentuale del tempo totale per linea

**Differenza con cProfile:**
- **cProfile**: analizza per funzione (quale funzione è lenta)
- **line_profiler**: analizza per linea (quale linea dentro la funzione è lenta)

---

## 🚀 Come Usare line_profiler

### Passo 1: Aggiungi il decoratore `@profile`

```python
@profile  # ← Aggiungi questo
def mia_funzione():
    somma = 0
    for i in range(1000000):
        somma += i
    return somma
```

**NOTA:** NON importare `profile` - è fornito automaticamente da `kernprof`

### Passo 2: Esegui con `kernprof`

```bash
kernprof -l -v script.py
```

**Opzioni:**
- `-l`: line-by-line profiling
- `-v`: verbose, mostra output subito
- `-o nome.lprof`: salva in file specifico

---

## 📚 Esempi nella Directory

### 1️⃣ `line_profiler_1_base.py`
**Cosa mostra:** Uso base di line_profiler

**Come eseguire:**
```bash
# ATTENZIONE: Devi modificare il file e aggiungere @profile prima di eseguire!
# Vedi sotto per istruzioni

kernprof -l -v line_profiler_1_base.py
```

**Funzioni da profilare:**
- `calcola_somma_quadrati()`
- `processa_lista()`

---

### 2️⃣ `line_profiler_2_bottleneck.py`
**Cosa mostra:** Identifica esattamente quali linee sono lente

**Funzioni da profilare:**
- `metodo_inefficiente()` - mostra operazioni costose
- `metodo_efficiente()` - versione ottimizzata
- `analizza_testo()` - trova loop costosi

---

### 3️⃣ `line_profiler_3_confronto.py`
**Cosa mostra:** Loop vs List Comprehension vs Built-in

**Confronta:**
- Loop tradizionale vs `sum()`
- Loop vs list comprehension
- Loop vs `map()`

---

### 4️⃣ `line_profiler_4_algoritmi.py`
**Cosa mostra:** Complessità algoritmica in azione

**Confronta:**
- O(n²) vs O(n) - ricerca duplicati
- O(n) vs O(log n) - ricerca lineare vs binaria
- O(n*m) vs O(n+m) - intersezione liste

---

## 🔧 Preparare gli Esempi per l'Esecuzione

Gli esempi **NON** hanno il decoratore `@profile` di default perché causerebbero errori in esecuzione normale.

### Metodo 1: Aggiungi @profile manualmente

Apri il file e aggiungi `@profile` prima delle funzioni che vuoi analizzare:

```python
@profile  # ← Aggiungi questa linea
def calcola_somma_quadrati(n):
    totale = 0
    for i in range(n):
        quadrato = i ** 2
        totale += quadrato
    return totale

@profile  # ← E questa
def processa_lista(numeri):
    # ...
```

Poi esegui:
```bash
kernprof -l -v line_profiler_1_base.py
```

---

### Metodo 2: Usa uno script helper

Creerò uno script che aggiunge automaticamente `@profile`:

```bash
# Vedi run_line_profiler.sh più avanti
./run_line_profiler.sh line_profiler_1_base.py calcola_somma_quadrati processa_lista
```

---

## 📊 Interpretare l'Output

```
Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     8                                           @profile
     9                                           def calcola_somma_quadrati(n):
    10         1          2.0      2.0      0.0      totale = 0
    11     10001       4523.0      0.5      8.5      for i in range(n):
    12     10000       5234.0      0.5      9.8          quadrato = i ** 2
    13     10000      43521.0      4.4     81.7          totale += quadrato
    14         1          1.0      1.0      0.0      return totale
```

**Colonne:**
- **Line #**: Numero di linea
- **Hits**: Quante volte è stata eseguita
- **Time**: Tempo totale (microsecondi)
- **Per Hit**: Tempo medio per esecuzione
- **% Time**: Percentuale del tempo totale
- **Line Contents**: Codice della linea

**Cosa cercare:**
- 🔥 **% Time alto**: questa linea è il bottleneck!
- 🔢 **Hits alto con Time alto**: operazione ripetuta molte volte
- 🎯 **Focus**: concentrati sulle linee con % Time > 10%

---

## 💡 Esempio Pratico Completo

### 1. Crea file `esempio_test.py`:

```python
def calcola_fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for i in range(n - 1):
        a, b = b, a + b
    return b

def main():
    for i in range(30):
        risultato = calcola_fibonacci(i)
    print("Completato!")

if __name__ == "__main__":
    main()
```

### 2. Aggiungi `@profile`:

```python
@profile  # ← Aggiungi qui
def calcola_fibonacci(n):
    # ...

@profile  # ← E qui se vuoi profilare anche main
def main():
    # ...
```

### 3. Esegui:

```bash
kernprof -l -v esempio_test.py
```

### 4. Analizza output e ottimizza le linee lente!

---

## 🆚 Quando Usare Cosa?

| Strumento | Quando Usare | Output |
|-----------|--------------|--------|
| **time.time()** | Misura veloce di un blocco | Tempo totale |
| **cProfile** | Trova quale funzione è lenta | Per funzione |
| **line_profiler** | Trova quale linea è lenta | Per linea |
| **memory_profiler** | Analizza uso memoria | Memoria per linea |

**Workflow tipico:**
1. ⏱️ `time.time()` - "Il programma è lento?"
2. 🔍 `cProfile` - "Quale funzione è il problema?"
3. 🎯 `line_profiler` - "Quale linea dentro quella funzione?"
4. 🔧 Ottimizza quella linea specifica!

---

## 🚀 Tips & Tricks

### 1. Profila solo le funzioni sospette
Non mettere `@profile` ovunque - rallenta l'esecuzione. Usa cProfile prima per identificare le funzioni lente.

### 2. Salva i risultati
```bash
kernprof -l -o risultato.lprof script.py
python -m line_profiler risultato.lprof
```

### 3. Confronta prima/dopo
Salva il profiling prima dell'ottimizzazione, ottimizza, ri-profila e confronta!

### 4. Attenzione ai loop
Una linea con 1.000.000 di hits può essere lenta solo perché ripetuta, non perché inefficiente.

---

## 🔗 Risorse

- [Documentazione ufficiale](https://github.com/pyutils/line_profiler)
- [Memory Profiler](https://pypi.org/project/memory-profiler/) - per memoria
- [py-spy](https://github.com/benfred/py-spy) - profiler senza modificare codice

---

## ✅ Checklist Ottimizzazione

1. ✓ Esegui cProfile per trovare funzione lenta
2. ✓ Aggiungi `@profile` a quella funzione
3. ✓ Esegui `kernprof -l -v script.py`
4. ✓ Identifica linee con % Time > 10%
5. ✓ Ottimizza quelle linee specifiche
6. ✓ Ri-profila per verificare miglioramento
7. ✓ Ripeti se necessario

**Buon profiling linea per linea! 🎯**
