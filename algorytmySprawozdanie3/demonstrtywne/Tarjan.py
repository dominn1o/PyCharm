import time
import random
import sys


class tarjan:
    def __init__(self, n, edges, mode):
        self.n = n
        self.mode = mode
        self.data = self.build_data(edges)

    def build_matrix(self, edges):
        matrix = [["00"] * self.n for _ in range(self.n)]
        for u, v in edges:
            matrix[u-1][v-1] = "+1"
            matrix[v - 1][u - 1] = "-1"
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

    def display(self):

        if self.mode == 'ms':
            for row in self.data:
                print(row)

        elif self.mode == 'ln':
            mapa_wyswietlania = {}
            for i, neighbors in self.data.items():
                poprawieni_sasiedzi = []
                for v in neighbors:
                    poprawieni_sasiedzi.append(v + 1)
                mapa_wyswietlania[i + 1] = poprawieni_sasiedzi
            for key in mapa_wyswietlania:
                print(f"{key}: {mapa_wyswietlania[key]}")

        elif self.mode == 'lk':
            for u,v in self.data:
                print([u + 1, v + 1])

    def get_neighbors(self, u):
        if self.mode == 'ms':
            #w macierzy sąsiedztwa sprawdzamy cały wiersz u dla v.
            return [v for v, val in enumerate(self.data[u]) if val == 1]

        elif self.mode == 'ln':
            # liście następników zwracamy listę pod indeksem u.
            return self.data[u]

        elif self.mode == 'lk':
            # liście krawędzi przechodzimy przez wszystkie pary (start, end).
            return [v for start, v in self.data if start == u]

    def tarjan_sort(self, start_node):
        #0 - biały, 1 - szary, 2 - czarny
        colors = [0] * self.n
        entry_times = [0] * self.n  #moment wejścia do wierzchołka
        exit_times = [0] * self.n  #moment wyjścia z wierzchołka
        self.timer = 0  #licznik kroków
        stack = []
        recursion_stack = []

        def dfs(u):
            #oznaczamy jako szary
            colors[u] = 1
            recursion_stack.append(u)
            self.timer += 1
            entry_times[u] = self.timer

            #przeszukujemy sąsiadów
            for v in self.get_neighbors(u):
                if colors[v] == 1: #nastepnik jest szary
                    cycle_idx = recursion_stack.index(v)
                    cycle_nodes = [node + 1 for node in recursion_stack[cycle_idx:]]
                    print(f"\nWykryto cykl, brak mozliwosci sortowania.")
                    print(f"Wierzchołki tworzące cykl: {cycle_nodes}")
                    sys.exit()

                if colors[v] == 0:
                    dfs(v)

            #oznaczamy jako czarny
            colors[u] = 2
            self.timer += 1
            exit_times[u] = self.timer

            #dodajemy do wyniku po przetworzeniu sąsiadów
            stack.append(u + 1)
            recursion_stack.pop()

        print(f"--- Tarjan-sort ({self.mode}) ---")
        start_perf = time.perf_counter()

        s = start_node - 1
        if colors[s] == 0:
            dfs(s)

        for i in range(self.n):
            if colors[i] == 0:
                dfs(i)

        end_perf = time.perf_counter()

        #wynik to odwrócona kolejność zdejmowania ze stosu
        result = stack[::-1]

        if self.n <= 12:
            print("\n[TRYB DEMO - Czasy odwiedzin]")
            print("Wierzchołek: [Wejście / Wyjście]")
            for i in range(self.n):
                print(f"  V{i + 1}: [{entry_times[i]} / {exit_times[i]}]")

        print(f"\nCzas wykonania algorytmu: {end_perf - start_perf:.6f} s")
        return result


def load_from_file(filename):
    with open(filename, 'r') as file:
        first_line = file.readline().split()

        n = int(first_line[0])

        edges = []
        for line in file:
            parts = line.split()
            if len(parts) == 2:
                u, v = map(int, parts)
                edges.append((u, v))

        return n, edges


def generate_random_dag(n, s):
    """
    Generuje losowy graf acykliczny (DAG).
    n - liczba wierzchołków
    s - nasycenie w ułamku (np. 0.5 dla 50%)
    """
    #maksymalna liczba krawędzi w grafie
    max_edges = int(n * (n - 1) / 2)

    #ile krawędzi wygenerować dla danego nasycenia
    target_m = int(s * max_edges)

    #tworzymy liste mozliwych krawedzi
    all_possible_edges = []
    for u in range(1, n + 1):
        for v in range(u + 1, n + 1):
            all_possible_edges.append((u, v))

    #losujemy losowe krawędzie
    if target_m > len(all_possible_edges):
        target_m = len(all_possible_edges)

    edges = random.sample(all_possible_edges, target_m)

    return n, edges


print("\n===============================")
print("=== MENU GŁÓWNE - ALGORYTMY GRAFOWE ===")
tryb = input("1. Tryb demo(d)(dla n<=12) czy eksperyment(e): ")
reprezentacja = input("2. Wybierz typ reprezentacji maszynowej - ms, ln, lk: ")
zrodlo = input("3. Wybierz zrodlo - plik(p), losowy(l): ")
print("\n===============================")

if tryb == 'd':
    if zrodlo == 'p':
        n, edges = load_from_file("graf.txt")
    elif zrodlo == 'l':
        n = int(input("4. Podaj liczbę wierzchołków (n): "))
        s = float(input("5. Podaj nasycenie (s): ")) / 100
        n, edges = generate_random_dag(n, s)

    mode = reprezentacja
    graf = tarjan(n, edges, mode)

    if n<=12:
        graf.display()

    start_v = int(input("Wybierz wierzcholek startowy: "))
    wynik = graf.tarjan_sort(start_v)
    if wynik:
        print(f"Porzadek topologiczny: {wynik}")