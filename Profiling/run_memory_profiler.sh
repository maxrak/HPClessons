#!/bin/bash
#
# Script helper per eseguire memory_profiler sugli esempi
# Uso: ./run_memory_profiler.sh <script.py> <funzione1> <funzione2> ...
#
# Esempio:
#   ./run_memory_profiler.sh mp_esempio1_base.py crea_lista_grande crea_piu_liste
#

if [ $# -lt 2 ]; then
    echo "Uso: $0 <script.py> <funzione1> [funzione2] ..."
    echo ""
    echo "Esempi disponibili:"
    echo "  $0 mp_esempio1_base.py crea_lista_grande crea_piu_liste"
    echo "  $0 mp_esempio2_liste_vs_generatori.py usa_lista usa_generatore"
    echo "  $0 mp_esempio3_memory_leak.py memory_leak_accumulo no_memory_leak_processa"
    echo "  $0 mp_esempio4_strutture_dati.py usa_liste_python usa_array_efficiente"
    exit 1
fi

SCRIPT=$1
shift
FUNZIONI=("$@")

if [ ! -f "$SCRIPT" ]; then
    echo "Errore: file $SCRIPT non trovato!"
    exit 1
fi

# Crea file temporaneo nella directory corrente
TEMP_SCRIPT=".temp_memory_$(basename $SCRIPT)"

echo "Preparazione script per memory profiling..."
echo "Script: $SCRIPT"
echo "Funzioni: ${FUNZIONI[*]}"
echo ""

# Copia il contenuto originale
cp "$SCRIPT" "$TEMP_SCRIPT"

# Aggiungi @profile prima di ogni funzione specificata
for func in "${FUNZIONI[@]}"; do
    # Cerca "def funzione(" e aggiungi @profile sulla linea precedente
    sed -i.bak "/def $func(/i\\
@profile
" "$TEMP_SCRIPT"
done

# Rimuovi file backup
rm -f "${TEMP_SCRIPT}.bak"

echo "Esecuzione memory_profiler..."
echo "==============================="
echo ""

# Esegui memory_profiler
python -m memory_profiler "$TEMP_SCRIPT"

# Pulizia
rm -f "$TEMP_SCRIPT"

echo ""
echo "✓ Memory profiling completato!"
echo ""
echo "NOTA: Per grafico nel tempo, usa:"
echo "  mprof run $SCRIPT"
echo "  mprof plot"
