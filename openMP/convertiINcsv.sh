#!/bin/bash

# Script per convertire risultati_benchmark.txt in formato CSV

INPUT_FILE="risultati_benchmark.txt"
OUTPUT_FILE="risultati_benchmark.csv"

# Verifica che il file di input esista
if [ ! -f "$INPUT_FILE" ]; then
    echo "Errore: file $INPUT_FILE non trovato"
    exit 1
fi

echo "Conversione di $INPUT_FILE in formato CSV..."

# Crea l'header del CSV
echo "tipo,dimensione,K,chunk,memoria_MB,tempo_somma_sec,tempo_real_sec,tempo_user_sec,tempo_sys_sec" > "$OUTPUT_FILE"

# Variabili temporanee
tipo=""
dimensione=""
chunk=""
k=""
memoria=""
tempo_somma=""
tempo_real=""
tempo_user=""
tempo_sys=""

# Funzione per convertire il formato tempo (es. "0m0.001s" -> "0.001")
convert_time() {
    local time_str="$1"
    # Estrai minuti e secondi
    if [[ $time_str =~ ([0-9]+)m([0-9.]+)s ]]; then
        local minutes="${BASH_REMATCH[1]}"
        local seconds="${BASH_REMATCH[2]}"
        # Converti in secondi totali usando awk
        echo "$minutes $seconds" | awk '{printf "%.6f", $1 * 60 + $2}'
    else
        echo "0"
    fi
}

# Funzione per scrivere una riga nel CSV
write_row() {
    if [ -n "$tipo" ] && [ -n "$dimensione" ]; then
        # Per la versione sequenziale, chunk e K sono N/A
        if [ "$tipo" == "sequenziale" ]; then
            k="N/A"
            chunk="N/A"
        fi
        echo "$tipo,$dimensione,$k,$chunk,$memoria,$tempo_somma,$tempo_real,$tempo_user,$tempo_sys" >> "$OUTPUT_FILE"
    fi
}

# Leggi il file riga per riga
while IFS= read -r line; do
    
    # Identifica la dimensione
    if [[ $line =~ DIMENSIONE:\ ([0-9]+)x([0-9]+) ]]; then
        dimensione="${BASH_REMATCH[1]}"
    fi
    
    # Identifica il tipo di versione
    if [[ $line =~ ---\ VERSIONE\ SEQUENZIALE\ --- ]]; then
        # Se c'era una riga precedente, scrivila
        write_row
        # Resetta le variabili
        tipo="sequenziale"
        k=""
        chunk=""
        memoria=""
        tempo_somma=""
        tempo_real=""
        tempo_user=""
        tempo_sys=""
    fi
    
    if [[ $line =~ ---\ VERSIONE\ PARALLELA\ \(K=([0-9]+),\ CHUNK=([0-9]+)\)\ --- ]]; then
        # Se c'era una riga precedente, scrivila
        write_row
        # Resetta le variabili
        tipo="parallelo"
        k="${BASH_REMATCH[1]}"
        chunk="${BASH_REMATCH[2]}"
        memoria=""
        tempo_somma=""
        tempo_real=""
        tempo_user=""
        tempo_sys=""
    fi
    
    # Estrai la memoria allocata
    if [[ $line =~ Memoria\ allocata:\ ([0-9.]+)\ MB ]]; then
        memoria="${BASH_REMATCH[1]}"
    fi
    
    # Estrai il tempo di somma
    if [[ $line =~ Somma\ completata\ in\ ([0-9.]+)\ secondi ]]; then
        tempo_somma="${BASH_REMATCH[1]}"
    fi
    
    # Estrai il tempo real
    if [[ $line =~ ^real[[:space:]]+(.+)$ ]]; then
        tempo_real=$(convert_time "${BASH_REMATCH[1]}")
    fi
    
    # Estrai il tempo user
    if [[ $line =~ ^user[[:space:]]+(.+)$ ]]; then
        tempo_user=$(convert_time "${BASH_REMATCH[1]}")
    fi
    
    # Estrai il tempo sys
    if [[ $line =~ ^sys[[:space:]]+(.+)$ ]]; then
        tempo_sys=$(convert_time "${BASH_REMATCH[1]}")
    fi
    
done < "$INPUT_FILE"

# Scrivi l'ultima riga se presente
write_row

echo "Conversione completata!"
echo "File CSV creato: $OUTPUT_FILE"
echo ""

# Mostra un'anteprima
echo "=== ANTEPRIMA (prime 10 righe) ==="
head -n 10 "$OUTPUT_FILE" | column -t -s ','
echo ""

# Conta le righe
total_rows=$(($(wc -l < "$OUTPUT_FILE") - 1))
echo "Totale esecuzioni registrate: $total_rows"
echo ""
