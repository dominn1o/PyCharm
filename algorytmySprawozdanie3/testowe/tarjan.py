import time
import random
import sys

# Zwiększenie limitu rekurencji dla głębokich grafów
sys.setrecursionlimit(50000)

class tarjan:
    def __init__(self, n, edges, mode):
        self.n = n
        self.mode = mode
        self.data = self.build_data(edges)

    def build_matrix(self, edges):
        matrix = [["00"] * self.n for _ in range(self.n)]
        for u, v in edges:
            matrix[u-1][v-1] = "+1"
            matrix[v-1][u-1] = "-1"
        return matrix

    def build_nastepniki(self, edges):
        nastepniki = {i: [] for i in range(self.n)}
        for u, v in edges:
            nastepniki[u-1].append(v-1)
        return nastepniki

    def build_krawedzie(self, edges):
        krawedzie = []
        for u, v in edges:
            krawedzie.append((u-1, v-1))
        return krawedzie

    def build_data(self, edges):
        if self.mode == 'ms':
            return self.build_matrix(edges)
        elif self.mode == 'ln':
            return self.build_nastepniki(edges)
        elif self.mode == 'lk':
            return self.build_krawedzie(edges)

    def get_neighbors(self, u):
        if self.mode == 'ms':
            # w macierzy sąsiedztwa sprawdzamy cały wiersz u dla v ("+1").
            return [v for v, val in enumerate(self.data[u]) if val == "+1"]
        elif self.mode == 'ln':
            # w liście następników zwracamy listę pod indeksem u.
            return self.data[u]
        elif self.mode == 'lk':
            # w liście krawędzi przechodzimy przez wszystkie pary.
            return [v for start, v in self.data if start == u]

    def tarjan_sort(self, start_node):
        # 0 - biały, 1 - szary, 2 - czarny
        colors = [0] * self.n
        entry_times = [0] * self.n  # moment wejścia do wierzchołka
        exit_times = [0] * self.n  # moment wyjścia z wierzchołka
        self.timer = 0  # licznik kroków
        stack = []
        recursion_stack = []

        def dfs(u):
            # oznaczamy jako szary
            colors[u] = 1
            recursion_stack.append(u)
            self.timer += 1
            entry_times[u] = self.timer

            # przeszukujemy sąsiadów
            for v in self.get_neighbors(u):
                if colors[v] == 1:  # nastepnik jest szary
                    cycle_idx = recursion_stack.index(v)
                    cycle_nodes = [node + 1 for node in recursion_stack[cycle_idx:]]
                    sys.exit()

                if colors[v] == 0:
                    dfs(v)

            # oznaczamy jako czarny
            colors[u] = 2
            self.timer += 1
            exit_times[u] = self.timer

            # dodajemy do wyniku po przetworzeniu sąsiadów
            stack.append(u + 1)
            recursion_stack.pop()

        s = start_node - 1
        if colors[s] == 0:
            dfs(s)

        for i in range(self.n):
            if colors[i] == 0:
                dfs(i)

        result = stack[::-1]

        return result


import random


def generate_random_dag(n, s):
    edges = []

    # Przechodzimy przez wszystkie dozwolone pary w DAG-u (u < v)
    for u in range(1, n):
        for v in range(u + 1, n + 1):
            # random.random() losuje ułamek od 0.0 do 1.0.
            # Jeśli s=0.9, warunek spełni się w ~90% przypadków.
            if random.random() < s:
                edges.append((u, v))

    return n, edges


def generate_random_graph(n_nodes, edge_probability=0.3, is_dag=True):
    temp_edges = []

    for i in range(1, n_nodes + 1):
        for j in range(1, n_nodes + 1):
            if i == j:
                continue

            if is_dag:
                # tylko DAG (brak cykli) - wymuszony kierunek i < j
                if i < j:
                    if random.random() < edge_probability:
                        temp_edges.append((i, j))
            else:
                # może zawierać cykle
                if random.random() < edge_probability:
                    temp_edges.append((i, j))

    # mapowanie dla losowości (aby ukryć trywialne u < v w DAGu)
    mapping = list(range(1, n_nodes + 1))
    random.shuffle(mapping)

    random_edges = []
    for u, v in temp_edges:
        new_u = mapping[u - 1]
        new_v = mapping[v - 1]
        random_edges.append((new_u, new_v))

    return n_nodes, random_edges


# ==========================================
# FUNKCJE DO TESTÓW EKSPERYMENTALNYCH
# ==========================================

def zapisz_wynik(eksperyment, typReprezentacji, n, nasycenie, czas_ms):
    """Zapisuje wyniki do odpowiedniego pliku z dopiskiem nasycenia."""
    # Tłumaczenie trybu na przyjazną nazwę dla logów
    nazwy_reprezentacji = {'ms': 'Macierz Sasiedztwa', 'ln': 'Lista Nastepnikow', 'lk': 'Lista Krawedzi'}
    nazwa_typu = nazwy_reprezentacji.get(typReprezentacji, typReprezentacji)

    if eksperyment == 1:
        nazwa_pliku = f"wyniki/eksperyment1_tarjan_{typReprezentacji}.txt"
    elif eksperyment == 2:
        nazwa_pliku = f"wyniki/eksperyment2_tarjan_{typReprezentacji}.txt"

    with open(nazwa_pliku, "a", encoding="utf-8") as f:
        f.write(
            f"Operacja: sortowanie; Typ: {nazwa_typu}; n: {n}; Nasycenie: {nasycenie:.2f}; Czas: {czas_ms:.4f} ms;\n")


def wykonaj_pomiary(typReprezentacji, n, eksperyment, nasycenie=None):
    """
    Funkcja główna wykonująca pomiary algorytmu Tarjana.
    - typReprezentacji: 1 (ms), 2 (ln), 3 (lk)
    - n: liczba wierzchołków
    - eksperyment: 1 lub 2
    - nasycenie: używane tylko w eksperymencie 2 (np. podawane w pętli 9 razy)
    """
    # Mapowanie wyboru użytkownika na argument trybu klasy tarjan
    mapa_reprezentacji = {1: 'ms', 2: 'ln', 3: 'lk'}
    mode = mapa_reprezentacji.get(typReprezentacji, 'ms')

    if eksperyment == 1:
        # 3 poziomy nasycenia zgodnie z instrukcją
        poziomy_nasycenia = [0.1, 0.5, 0.9]

        for s in poziomy_nasycenia:
            # Generujemy DAG na bazie 'n' i konkretnego nasycenia 's'
            _, edges = generate_random_dag(n, s)

            # Inicjalizacja grafu
            graf = tarjan(n, edges, mode)

            # Pomiar czasu sortowania
            start = time.perf_counter()
            graf.tarjan_sort(1)  # start z wierzchołka 1
            stop = time.perf_counter()

            czas_sortowania_ms = (stop - start) * 1000
            nasycenie = s
            zapisz_wynik(eksperyment, mode, n, nasycenie, czas_sortowania_ms)

    elif eksperyment == 2:
        # Dla eksperymentu 2 nasycenie przekazujemy z zewnątrz
        if nasycenie is None:
            raise ValueError("Dla eksperymentu 2 wymagane jest podanie argumentu 'nasycenie'.")

        _, edges = generate_random_dag(n, nasycenie)
        graf = tarjan(n, edges, mode)

        start = time.perf_counter()
        graf.tarjan_sort(1)
        stop = time.perf_counter()

        czas_sortowania_ms = (stop - start) * 1000
        zapisz_wynik(eksperyment, mode, n, nasycenie, czas_sortowania_ms)