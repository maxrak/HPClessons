#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Leggi il CSV
df = pd.read_csv('result.csv')

# Filtra solo le linee che ci interessano: sequenziale e parallelo con K=1, K=2, K=5
df_filtered = df[
    (df['tipo'] == 'sequenziale') | 
    ((df['tipo'] == 'parallelo') & (df['K'].isin([1, 2, 5])))
]

# Crea una figura
plt.figure(figsize=(12, 8))

# Raggruppa per combinazioni di tipo e K
for (tipo, K), group in df_filtered.groupby(['tipo', 'K']):
    # Ordina per dimensione per avere linee continue
    group = group.sort_values('dimensione')
    
    # Crea label per la legenda
    if K == 'N/A':
        label = f'{tipo}'
    else:
        label = f'{tipo} (K={K})'
    
    # Plot della linea
    plt.plot(group['dimensione'], group['tempo_somma_sec'], 
             marker='o', label=label, linewidth=2, markersize=6)

# Configura il grafico
plt.xlabel('Dimensione', fontsize=12)
plt.ylabel('Tempo Somma (secondi)', fontsize=12)
plt.title('Tempo di Esecuzione per Dimensione della Matrice', fontsize=14, fontweight='bold')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=9)
plt.grid(True, alpha=0.3)

# Regola il layout per non tagliare la legenda
plt.tight_layout()

# Salva il grafico
plt.savefig('plot_results.png', dpi=300, bbox_inches='tight')
print("Grafico salvato come 'plot_results.png'")

# Mostra il grafico
plt.show()
