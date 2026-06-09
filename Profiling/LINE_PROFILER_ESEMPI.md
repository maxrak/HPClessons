# Line Profiler - Guida Rapida agli Esempi

Questi esempi sono **pronti per line_profiler** e usano le funzioni da `funzioni_test.py`.

## 🚀 Come Eseguire

### Metodo 1: Script Helper (raccomandato)

```bash
# Esempio 1: Analisi base
./run_line_profiler.sh lp_esempio1_base.py esegui_operazioni_miste elabora_numeri

# Esempio 2: Identificare bottleneck (Fibonacci ricorsivo vs iterativo)
./run_line_profiler.sh lp_esempio2_bottleneck.py calcola_fibonacci_multipli calcola_fibonacci_multipli_veloce

# Esempio 3: Confronto implementazioni (loop separati vs unico vs builtin)
./run_line_profiler.sh lp_esempio3_confronto.py metodo_con_loop_separati metodo_con_loop_unico metodo_con_builtin

# Esempio 4: Ottimizzazione algoritmica (O(n²) vs O(n))
./run_line_profiler.sh lp_esempio4_algoritmi.py trova_duplicati_lento trova_duplicati_veloce
```

### Metodo 2: Manuale (aggiungi @profile)

1. Apri il file (es. `lp_esempio1_base.py`)
2. Aggiungi `@profile` prima delle funzioni:
   ```python
   @profile  # ← Aggiungi questa linea
   def esegui_operazioni_miste():
       # ...
   ```
3. Esegui:
   ```bash
   kernprof -l -v lp_esempio1_base.py
   ```

---

## 📚 Cosa Mostra Ogni Esempio

### 1️⃣ `lp_esempio1_base.py` - Analisi Base
**Funzioni da profilare:**
- `esegui_operazioni_miste` - chiama `funzione_veloce()`, `funzione_lenta()`, `funzione_con_sleep()`
- `elabora_numeri` - loop con calcoli

**Mostra:** Come line_profiler identifica quale chiamata è lenta

**Comando:**
```bash
./run_line_profiler.sh lp_esempio1_base.py esegui_operazioni_miste elabora_numeri
```

---

### 2️⃣ `lp_esempio2_bottleneck.py` - Identificare Bottleneck
**Funzioni da profilare:**
- `calcola_fibonacci_multipli` - usa `fibonacci_ricorsivo()` 🐌 LENTO
- `calcola_fibonacci_multipli_veloce` - usa `fibonacci_iterativo()` ⚡ VELOCE
- `operazione_mista` - combina tutto

**Mostra:** Differenza drammatica tra algoritmo ricorsivo e iterativo

**Comando:**
```bash
./run_line_profiler.sh lp_esempio2_bottleneck.py calcola_fibonacci_multipli calcola_fibonacci_multipli_veloce operazione_mista
```

**Risultato atteso:** La linea con `fibonacci_ricorsivo()` avrà % Time molto alto!

---

### 3️⃣ `lp_esempio3_confronto.py` - Confronto Implementazioni
**Funzioni da profilare:**
- `metodo_con_loop_separati` - 3 loop separati
- `metodo_con_loop_unico` - 1 solo loop
- `metodo_con_builtin` - usa `sum()` e generator
- `test_con_funzioni_esterne` - chiama `operazione_complessa()`

**Mostra:** Quale approccio è più veloce linea per linea

**Comando:**
```bash
./run_line_profiler.sh lp_esempio3_confronto.py metodo_con_loop_separati metodo_con_loop_unico metodo_con_builtin
```

**Risultato atteso:** 
- Loop separati: più lento (più passaggi)
- Loop unico: medio
- Built-in: più veloce (ottimizzato in C)

---

### 4️⃣ `lp_esempio4_algoritmi.py` - Ottimizzazione Algoritmica
**Funzioni da profilare:**
- `trova_duplicati_lento` - O(n²) con loop annidati 🐌
- `trova_duplicati_veloce` - O(n) con set ⚡
- `cerca_elementi_lento` - O(n*m) 🐌
- `cerca_elementi_veloce` - O(n+m) ⚡

**Mostra:** Impatto della complessità algoritmica

**Comando:**
```bash
./run_line_profiler.sh lp_esempio4_algoritmi.py trova_duplicati_lento trova_duplicati_veloce
```

**Risultato atteso:** La versione "lenta" avrà loop annidati con % Time altissimo

---

## 📊 Interpretare i Risultati

```
Line #  Hits    Time     Per Hit  % Time  Line Contents
========================================================
15      5       1000     200.0    5.0%    for _ in range(5):
16      5       500      100.0    2.5%        funzione_veloce()
19      1       18000    18000.0  90.0%   funzione_lenta()  ← BOTTLENECK!
22      1       500      500.0    2.5%    funzione_con_sleep()
```

**Interpretazione:**
- 🔥 **% Time = 90%**: Questa linea è il bottleneck!
- 🔢 **Hits = 5**: Eseguita 5 volte
- ⏱️ **Time**: Tempo totale in microsecondi
- 📈 **Per Hit**: Tempo medio per esecuzione

**Azione:** Ottimizza le linee con % Time > 10%

---

## 💡 Tips

1. **Non profilare tutte le funzioni** - solo quelle sospette identificate con cProfile
2. **Confronta sempre** prima/dopo ottimizzazione
3. **Focus sui loop** - spesso sono i bottleneck
4. **Attenzione all'overhead** - line_profiler rallenta l'esecuzione

---

## 🎯 Workflow Ottimizzazione

1. **cProfile** → Trova funzione lenta
2. **line_profiler** → Trova linea lenta in quella funzione
3. **Ottimizza** quella linea specifica
4. **Ri-profila** per verificare miglioramento
5. **Ripeti** se necessario

---

## ✅ Checklist Rapida

```bash
# 1. Test base
./run_line_profiler.sh lp_esempio1_base.py esegui_operazioni_miste

# 2. Confronto algoritmi
./run_line_profiler.sh lp_esempio2_bottleneck.py calcola_fibonacci_multipli calcola_fibonacci_multipli_veloce

# 3. Ottimizzazione
./run_line_profiler.sh lp_esempio4_algoritmi.py trova_duplicati_lento trova_duplicati_veloce
```

**Buon profiling! 🎯**
