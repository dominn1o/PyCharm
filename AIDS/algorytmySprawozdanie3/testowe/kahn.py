import time
import random
import sys
import random


class kahn:
    def __init__(self, n, edges, mode):
        self.n = n
        self.mode = mode
        self.data = self.build_data(edges)

    def build_matrix(self, edges):
        matrix = [["00"] * self.n for _ in range(self.n)]
        for u, v in edges:
            matrix[u - 1][v - 1] = "+1"
            matrix[v - 1][u - 1] = "-1"
        return matrix

    def build_nastepniki(self, edges):
        nastepniki = {i: [] for i in range(self.n)}
        for u, v in edges:
            nastepniki[u - 1].append(v - 1)
        return nastepniki

    def build_krawedzie(self, edges):
        krawedzie = []
        for u, v in edges:
            krawedzie.append((u - 1, v - 1))
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
            return [v for v, val in enumerate(self.data[u]) if val == "+1"]
        elif self.mode == 'ln':
            return self.data[u]
        elif self.mode == 'lk':
            return [v for start, v in self.data if start == u]

    def kahn_sort(self):
        start_perf = time.perf_counter()

        # Obliczanie początkowych stopni wejściowych na podstawie danych 
        # bez modyfikowania lub niszczenia wejściowego grafu
        in_deg = {i: 0 for i in range(self.n)}
        for u in range(self.n):
            for v in self.get_neighbors(u):
                in_deg[v] += 1

        zero_deg = [i for i in range(self.n) if in_deg[i] == 0]
        result = []

        while zero_deg:
            # Słownik printowany jako 1-indeksowany, aby być przyjaznym dla użytkownika
            display_in_deg = {k + 1: v for k, v in in_deg.items()}

            u = zero_deg.pop(0)
            result.append(u + 1)

            for v in self.get_neighbors(u):
                in_deg[v] -= 1
                if in_deg[v] == 0:
                    zero_deg.append(v)

        end_perf = time.perf_counter()

        # Wykrywanie cykli - jeśli wynik ma mniej elementów niż n
        if len(result) != self.n:
            cycle_nodes = [v + 1 for v in range(self.n) if in_deg[v] > 0]
            sys.exit()

        display_in_deg = {k + 1: v for k, v in in_deg.items()}
        return result



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
        nazwa_pliku = f"wyniki/eksperyment1_kahn_{typReprezentacji}.txt"
    elif eksperyment == 2:
        nazwa_pliku = f"wyniki/eksperyment2_kahn_{typReprezentacji}.txt"

    with open(nazwa_pliku, "a", encoding="utf-8") as f:
        f.write(f"Operacja: sortowanie; Typ: {nazwa_typu}; n: {n}; Nasycenie: {nasycenie:.2f}; Czas: {czas_ms:.4f} ms;\n")


def wykonaj_pomiary(typReprezentacji, n, eksperyment, nasycenie=None):
    """
    Funkcja główna wykonująca pomiary algorytmu Kahna.
    - typReprezentacji: 1 (ms), 2 (ln), 3 (lk)
    - n: liczba wierzchołków
    - eksperyment: 1 lub 2
    - nasycenie: używane tylko w eksperymencie 2 (np. podawane w pętli 9 razy)
    """
    # Mapowanie wyboru użytkownika na argument trybu klasy kahn
    mapa_reprezentacji = {1: 'ms', 2: 'ln', 3: 'lk'}
    mode = mapa_reprezentacji.get(typReprezentacji, 'ms')

    if eksperyment == 1:
        # 3 poziomy nasycenia zgodnie z instrukcją
        poziomy_nasycenia = [0.1, 0.5, 0.9]

        for s in poziomy_nasycenia:
            # Generujemy DAG na bazie 'n' i konkretnego nasycenia 's'
            _, edges = generate_random_dag(n, s)

            # Inicjalizacja grafu (zmienione na kahn)
            graf = kahn(n, edges, mode)

            # Pomiar czasu sortowania
            start = time.perf_counter()
            graf.kahn_sort()  # Kahn nie wymaga wierzchołka startowego
            stop = time.perf_counter()

            czas_sortowania_ms = (stop - start) * 1000
            zapisz_wynik(eksperyment, mode, n, s, czas_sortowania_ms)

    elif eksperyment == 2:
        # Dla eksperymentu 2 nasycenie przekazujemy z zewnątrz
        if nasycenie is None:
            raise ValueError("Dla eksperymentu 2 wymagane jest podanie argumentu 'nasycenie'.")

        _, edges = generate_random_dag(n, nasycenie)
        graf = kahn(n, edges, mode)

        start = time.perf_counter()
        graf.kahn_sort()  # Kahn nie wymaga wierzchołka startowego
        stop = time.perf_counter()

        czas_sortowania_ms = (stop - start) * 1000
        zapisz_wynik(eksperyment, mode, n, nasycenie, czas_sortowania_ms)