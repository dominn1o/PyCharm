import time
import random
import numpy as np

class tarjan:
    def __init__(self, n, edges, representation_type):
        self.n = n # l. wierzcholkow
        self.type = representation_type # 'ms', 'ln', 'lk'
        self.data = self._build_data(edges)

    def _build_data(self, edges):

        def build_matrix(n, edges):
            matrix = np.zeros((n,n), dtype=int)
            for u, v in edges:
                matrix[u-1][v-1] = 1
            return matrix

        def build_nastepniki(n, edges):
            nastepniki = {}
            for i in range(1, n+1):
                nastepniki = {i: [] for i in range(1, n + 1)}
            for u,v in edges:
                nastepniki[u].append(v)
            return nastepniki

        def build_krawedzie(n, edges):
            krawedzie = []
            for u,v in edges:
                krawedzie.append((u,v))
            return krawedzie

        if self.type == 'ms':
            print(build_matrix(self.n, edges))
        elif self.type == 'ln':
            print(build_nastepniki(self.n, edges))
        elif self.type == 'lk':
            print(build_krawedzie(self.n,edges))


    def get_neighbors(self, u):
        # KLUCZ ZADANIA: Ta funkcja musi działać inaczej dla każdej reprezentacji
        if self.type == 'ms':
            return [v for v, val in enumerate(self.data[u]) if val == 1]
        elif self.type == 'ln':
            return self.data[u]
        elif self.type == 'lk':
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
tarjan(n_vertices,sample_edges, 'lk')