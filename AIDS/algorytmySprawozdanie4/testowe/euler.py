import time
import sys

# Zwiększenie limitu rekurencji dla backtracking'u
sys.setrecursionlimit(50000)


class Euler:
    def __init__(self, n, edges, is_directed, matrix):
        self.n = n
        self.edges = edges
        self.is_directed = is_directed
        self.matrix = matrix
        self.m = len(edges)

    def has_edge(self, u, v):
        """Uniwersalna metoda sprawdzająca krawędź u -> v """
        if not self.is_directed:
            return self.matrix[u][v] == 1
        else:
            val = self.matrix[u][v]
            return (0 <= val <= self.n) or (2 * self.n + 1 <= val <= 3 * self.n)

    def dec(self):
        """Wersja decyzyjna (sprawdzenie warunków) [cite: 62]"""
        start_time = time.perf_counter()

        # 1. Warunek stopni
        if not self.is_directed:
            for i in range(self.n):
                degree = sum(1 for j in range(self.n) if self.has_edge(i, j))
                if degree % 2 != 0: return False, time.perf_counter() - start_time
        else:
            for i in range(self.n):
                out_deg = sum(1 for j in range(self.n) if self.has_edge(i, j))
                in_deg = sum(1 for j in range(self.n) if self.has_edge(j, i))
                if out_deg != in_deg: return False, time.perf_counter() - start_time

        # 2. Spójność (BFS)
        start_node = next((i for i in range(self.n) if any(self.has_edge(i, j) for j in range(self.n))), -1)
        if start_node != -1:
            visited = [False] * self.n
            queue = [start_node]
            visited[start_node] = True
            while queue:
                u = queue.pop(0)
                for v in range(self.n):
                    if self.has_edge(u, v) and not visited[v]:
                        visited[v] = True
                        queue.append(v)

            for i in range(self.n):
                if any(self.has_edge(i, j) for j in range(self.n)) and not visited[i]:
                    return False, time.perf_counter() - start_time

        return True, time.perf_counter() - start_time

    def sec(self):
        """Wersja przeszukiwania (backtracking) [cite: 64]"""
        start_time = time.perf_counter()
        self.backtracks = 0
        self.cycle = []

        # Macierz pomocnicza dla zużytych krawędzi (nie modyfikujemy struktury wejściowej)
        self.used_edges = [[False] * self.n for _ in range(self.n)]

        def backtrack(u, edges_left):
            if edges_left == 0:
                self.cycle.append(u)
                return True

            for v in range(self.n):
                if self.has_edge(u, v) and not self.used_edges[u][v]:
                    # Zaznacz jako zużytą
                    self.used_edges[u][v] = True
                    if not self.is_directed: self.used_edges[v][u] = True

                    if backtrack(v, edges_left - 1):
                        self.cycle.append(u)
                        return True

                    # Backtrack [cite: 64]
                    self.used_edges[u][v] = False
                    if not self.is_directed: self.used_edges[v][u] = False
                    self.backtracks += 1
            return False

        found = backtrack(0, self.m)
        if found: self.cycle.reverse()

        return found, time.perf_counter() - start_time, self.backtracks