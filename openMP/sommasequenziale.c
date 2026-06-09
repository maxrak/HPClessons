#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define RIGHE   10000
#define COLONNE   10000

// Funzione per allocare una matrice dinamicamente
double** allocaMatrice(int righe, int colonne) {
    double** matrice = (double**)malloc(righe * sizeof(double*));
    if (matrice == NULL) {
        fprintf(stderr, "Errore: allocazione memoria fallita\n");
        exit(1);
    }
    
    for (int i = 0; i < righe; i++) {
        matrice[i] = (double*)malloc(colonne * sizeof(double));
        if (matrice[i] == NULL) {
            fprintf(stderr, "Errore: allocazione memoria fallita\n");
            exit(1);
        }
    }
    
    return matrice;
}

// Funzione per liberare una matrice allocata dinamicamente
void liberaMatrice(double** matrice, int righe) {
    for (int i = 0; i < righe; i++) {
        free(matrice[i]);
    }
    free(matrice);
}

// Funzione per stampare una matrice (limitata ai primi elementi per matrici grandi)
void stampaMatrice(double** matrice, int righe, int colonne, const char* nome) {
    printf("\n%s (%dx%d):\n", nome, righe, colonne);
    
    int max_stampa_righe = (righe > 10) ? 10 : righe;
    int max_stampa_colonne = (colonne > 10) ? 10 : colonne;
    
    for (int i = 0; i < max_stampa_righe; i++) {
        for (int j = 0; j < max_stampa_colonne; j++) {
            printf("%8.2f ", matrice[i][j]);
        }
        if (colonne > 10) printf("...");
        printf("\n");
    }
    if (righe > 10) printf("...\n");
}

// Funzione per sommare due matrici
void sommaMatrici(double** matrice1, double** matrice2, double** risultato, int righe, int colonne) {
    for (int i = 0; i < righe; i++) {
        for (int j = 0; j < colonne; j++) {
            risultato[i][j] = matrice1[i][j] + matrice2[i][j];
        }
    }
}

// Funzione per inizializzare una matrice con valori casuali
void inizializzaMatrice(double** matrice, int righe, int colonne) {
    for (int i = 0; i < righe; i++) {
        for (int j = 0; j < colonne; j++) {
            matrice[i][j] = (double)(rand() % 100) / 10.0; // Valori tra 0.0 e 9.9
        }
    }
}

int main() {
    int righe=RIGHE, colonne=COLONNE;
    
    //printf("=== SOMMA DI DUE MATRICI (ALLOCAZIONE DINAMICA) ===\n\n");
    
    // Input delle dimensioni
    // printf("Inserisci il numero di righe: ");
    // if (scanf("%d", &righe) != 1 || righe <= 0) {
    //     fprintf(stderr, "Errore: numero di righe non valido\n");
    //     return 1;
    // }
    
    // printf("Inserisci il numero di colonne: ");
    // if (scanf("%d", &colonne) != 1 || colonne <= 0) {
    //     fprintf(stderr, "Errore: numero di colonne non valido\n");
    //     return 1;
    // }
    
    printf("\nDimensioni matrici: %dx%d\n", righe, colonne);
    printf("Memoria allocata: %.2f MB per matrice\n", 
           (righe * colonne * sizeof(double)) / (1024.0 * 1024.0));
    
    // Inizializzazione del generatore casuale
    srand(time(NULL));
    
    // Allocazione delle matrici
//    printf("\nAllocazione matrici in corso...\n");
    double** matrice1 = allocaMatrice(righe, colonne);
    double** matrice2 = allocaMatrice(righe, colonne);
    double** risultato = allocaMatrice(righe, colonne);
//    printf("Allocazione completata!\n");
    
    // Inizializzazione delle matrici con valori casuali
//    printf("Inizializzazione matrici...\n");
    inizializzaMatrice(matrice1, righe, colonne);
    inizializzaMatrice(matrice2, righe, colonne);
    
    // Stampa delle matrici di input (solo preview per matrici grandi)
    //stampaMatrice(matrice1, righe, colonne, "Matrice 1");
    //stampaMatrice(matrice2, righe, colonne, "Matrice 2");
    
    // Calcolo della somma
    printf("\nCalcolo della somma in corso...\n");
    clock_t inizio = clock();
    sommaMatrici(matrice1, matrice2, risultato, righe, colonne);
    clock_t fine = clock();
    double tempo = ((double)(fine - inizio)) / CLOCKS_PER_SEC;
    
    printf("Somma completata in %.6f secondi\n", tempo);
    
    // Stampa del risultato
    //stampaMatrice(risultato, righe, colonne, "Risultato (Matrice 1 + Matrice 2)");
    
    // Liberazione della memoria
    //printf("\nLiberazione memoria...\n");
    liberaMatrice(matrice1, righe);
    liberaMatrice(matrice2, righe);
    liberaMatrice(risultato, righe);
    //printf("Memoria liberata con successo!\n\n");
    
    return 0;
}
