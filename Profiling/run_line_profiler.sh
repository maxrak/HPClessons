#!/bin/bash
#
# Script helper per eseguire line_profiler sugli esempi
# Uso: ./run_line_profiler.sh <script.py> <funzione1> <funzione2> ...
#
# Esempio:
#   ./run_line_profiler.sh line_profiler_1_base.py calcola_somma_quadrati processa_lista
#

if [ $# -lt 2 ]; then
    echo "Uso: $0 <script.py> <funzione1> [funzione2] ..."
    echo ""
    echo "Esempi disponibili:"
    echo "  $0 line_profiler_1_base.py calcola_somma_quadrati processa_lista"
    echo "  $0 line_profiler_2_bottleneck.py metodo_inefficiente analizza_testo"
    echo "  $0 line_profiler_3_confronto.py somma_con_loop somma_con_builtin"
    echo "  $0 line_profiler_4_algoritmi.py trova_duplicati_lento trova_duplicati_veloce"
    exit 1
fi

SCRIPT=$1
shift
FUNZIONI=("$@")

if [ ! -f "$SCRIPT" ]; then
    echo "Errore: file $SCRIPT non trovato!"
    exit 1
fi

# Crea file temporaneo nella directory corrente (per mantenere gli import)
TEMP_SCRIPT=".temp_profiler_$(basename $SCRIPT)"

echo "Preparazione script per profiling..."
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

echo "Esecuzione kernprof..."
echo "===================="
echo ""

# Esegui kernprof
kernprof -l -v "$TEMP_SCRIPT"

# Pulizia
rm -f "$TEMP_SCRIPT"
rm -f "${TEMP_SCRIPT}.lprof"

echo ""
echo "✓ Profiling completato!"
echo ""
echo "NOTA: Se vuoi mantenere i risultati, usa direttamente:"
echo "  kernprof -l -v $SCRIPT"
