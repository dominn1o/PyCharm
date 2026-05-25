import time

class Hamilton:
    def __init__(self, n, edges, is_directed, matrix):
        self.n = n
        self.edges = edges
        self.is_directed = is_directed
        self.matrix = matrix

    def has_edge(self, u, v):
        """Uniwersalna metoda sprawdzająca krawędź u -> v """
        if not self.is_directed:
            return self.matrix[u][v] == 1
        else:
            val = self.matrix[u][v]
            return (0 <= val <= self.n) or (2 * self.n + 1 <= val <= 3 * self.n)

    def dhc(self):
        """Wersja decyzyjna (sprawdzenie warunków) """
        start_time = time.perf_counter()
        if self.n < 3: return False, time.perf_counter() - start_time

        if not self.is_directed:
            # Twierdzenie Orego
            for u in range(self.n):
                for v in range(u + 1, self.n):
                    if not self.has_edge(u, v):
                        deg_u = sum(1 for i in range(self.n) if self.has_edge(u, i))
                        deg_v = sum(1 for i in range(self.n) if self.has_edge(v, i))
                        if deg_u + deg_v < self.n:
                            return False, time.perf_counter() - start_time # Brak pewności
        else:
            # Twierdzenie Woodalla
            for u in range(self.n):
                for v in range(self.n):
                    if u != v and not self.has_edge(u, v):
                        out_u = sum(1 for i in range(self.n) if self.has_edge(u, i))
                        in_v = sum(1 for i in range(self.n) if self.has_edge(i, v))
                        if out_u + in_v < self.n:
                            return False, time.perf_counter() - start_time # Brak pewności

        return True, time.perf_counter() - start_time

    def shc(self):
        """Wersja przeszukiwania (Roberts-Flores) [cite: 65]"""
        start_time = time.perf_counter()
        self.backtracks = 0
        self.cycle = []
        visited = [False] * self.n

        def backtrack(u, depth):
            visited[u] = True
            self.cycle.append(u)

            if depth == self.n:
                start_vertex = self.cycle[0]
                if self.has_edge(u, start_vertex):
                    self.cycle.append(start_vertex)
                    return True
            else:
                for v in range(self.n):
                    if self.has_edge(u, v) and not visited[v]:
                        if backtrack(v, depth + 1):
                            return True

            self.backtracks += 1
            visited[u] = False
            self.cycle.pop()
            return False

        found = backtrack(0, 1)
        return found, time.perf_counter() - start_time, self.backtracks