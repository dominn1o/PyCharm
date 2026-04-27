import time
import random
import numpy as np # Upewnij się, że możesz używać numpy, jeśli nie - użyj list list.

class kahn:
    def __init__(self, n, edges, mode):
        self.n = n          # liczba wierzchołków
        self.mode = mode    # 'ms', 'ln', 'lk'
        # Wywołujemy budowanie danych i przypisujemy do self.data
        self.data = self._build_data(edges)

    def _build_data(self, edges):
        """Wybiera odpowiednią funkcję budującą na podstawie trybu."""
        if self.mode == 'ms':
            return self._build_matrix(edges)
        elif self.mode == 'ln':
            return self._build_nastepniki(edges)
        elif self.mode == 'lk':
            return self._build_krawedzie(edges)

    def _build_matrix(self, edges):
        # Macierz sąsiedztwa n x n
        matrix = np.zeros((self.n, self.n), dtype=int)
        for u, v in edges:
            # u-1, v-1 bo w pliku są od 1, a w macierzy indeksujemy od 0
            matrix[u+1][v+1] = 1
        return matrix

    def _build_nastepniki(self, edges):
        # Słownik/Lista list. Klucze to wierzchołki (0 do n-1)
        nastepniki = {i: [] for i in range(self.n)}
        for u, v in edges:
            nastepniki[u+1].append(v+1)
        return nastepniki

    def _build_krawedzie(self, edges):
        # Prosta lista krotek
        krawedzie = []
        for u, v in edges:
            krawedzie.append((u+1, v+1))
        return krawedzie


    def display(self, mode):
        if mode == 'ms':
            print(self.build_matrix)
        elif mode == 'ln':
            print(self.build_nastepniki())
        elif mode == 'lk':
            print(self.build_krawedzie())


    def get_neighbors(self, u):
        # KLUCZ ZADANIA: Ta funkcja musi działać inaczej dla każdej reprezentacji
        if self.mode == 'ms':
            return [v for v, val in enumerate(self.data[u]) if val == 1]
        elif self.mode == 'ln':
            return self.data[u]
        elif self.mode == 'lk':
            return [v for start, v in self.data if start == u]

    def kahn_sort(self):
        # Oblicz stopnie wejściowe OPERUJĄC BEZPOŚREDNIO na self.data
        # Jeśli 'ms', sumuj kolumny macierzy.
        # Jeśli 'lk', iteruj po całej liście krawędzi i zliczaj wystąpienia celów (v).
        pass

    def tarjan_sort(self):
        # Implementacja DFS z kolorami
        pass

n_vertices = 4
sample_edges = [
    (1, 2),  # Krawędź z 1 do 2
    (1, 4),
    (1, 3),  # Krawędź z 1 do 3
    (3, 4)   # Krawędź z 3 do 4
]
kahn(n_vertices,sample_edges, 'ms')
kahn.display('ms')