import time
import random

class GraphSorter:
    def __init__(self, n, edges, representation_type):
        self.n = n
        self.type = representation_type # 'ms', 'ln', 'lk'
        self.data = self._build_data(edges)

    def _build_data(self, edges):
        # Tutaj budujesz odpowiednią strukturę na podstawie list krawędzi
        pass

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

#aa