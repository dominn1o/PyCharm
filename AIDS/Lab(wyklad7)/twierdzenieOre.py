import sys
import random

#sprawdzanie czy w grafie istnieje cykl hamiltona
class Graf:
    def __init__(self, n, edges, mode):
        self.n = n
        self.mode = mode
        self.data = self.build_data(edges)

    def build_matrix(self, edges):
        matrix = [["00"] * self.n for i in range(self.n)]
        for u, v in edges:
            matrix[u - 1][v - 1] = "1"
            matrix[v - 1][u - 1] = "1"
        return matrix

    def build_data(self, edges):
            return self.build_matrix(edges)

    def display(self):
        for row in self.data:
            print(row)

    def check_prosty(self, edges):
        #sprawdzamy petle(krawedzie laczace wierzcholek z samym soba)
        for i in edges:
            if i[0] == i[1]:
                print("Graf nie spelnia wymagan, nie jest prosty.")
                print(f"Wierzcholek {i[0]} zawiera petlę.")
                return False

        seen_edges = set()

        for u, v in edges:
            # stardard krawedz - zawsze tak samo zapisana
            standardized_edge = (min(u, v), max(u, v))

            if standardized_edge in seen_edges:
                print("Graf nie spelnia wymagan, nie jest prosty.")
                print(f"Wierzchołki {u} oraz {v} zawierają krawędź wielokrotną.")
                return False

            seen_edges.add(standardized_edge)

        return True


    def check_wierzcholki(self, n):
        #sprawdzamy czy suma stopni 2 niepolaczonych wierzcholkow jest wieksza od liczby wierzcholkow
        if n <= 2:
            print("Graf nie spelnia wymagan, zbyt mala liczba wierzcholkow(n<=2).")
            return False

        return True

    def check_stopnie(self, n, edges):

        wierzcholki = {}

        for i, j in edges:
            wierzcholki[i] = set()
            wierzcholki[j] = set()

        for i, j in edges:
            wierzcholki[i].add(j)
            wierzcholki[j].add(i)

        lista_wierzcholkow = list(wierzcholki.keys())

        #deg(u) + deg(v) >= n dla niepolaczonych
        for i in range(len(lista_wierzcholkow)):
            for j in range(i + 1, len(lista_wierzcholkow)):
                u = lista_wierzcholkow[i]
                v = lista_wierzcholkow[j]

                # Sprawdzamy, czy wierzchołki nie sa połączone
                if v not in wierzcholki[u]:

                    #stopien wierzcholka to liczba jego sąsiadów
                    deg_u = len(wierzcholki[u])
                    deg_v = len(wierzcholki[v])

                    if deg_u + deg_v < n:
                        print(f"Graf nie spelnia wymagan, suma stopni 2 niepolaczonych wierzcholkow jest mniejszy od liczby wierzcholkow")
                        print(f"Wierzchołki {u} (stopień {deg_u}) i {v} (stopień {deg_v}) nie są połączone.")
                        print(f"Suma stopni < {n}.")
                        return False

        print("Sukces: Graf spełnia wszystkie warunki Twierdzenia Orego")
        return True




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


def generate_random_graph(n, s):
    #maksymalna liczba krawędzi w grafie
    max_edges = int(n * (n - 1) / 2)

    #ile krawędzi wygenerować dla danego nasycenia
    target_m = int(s * max_edges)

    #lista mozliwych krawedzi gdzie u<v
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
print("=== MENU GŁÓWNE - ALGORYTM OREGO ===")
print("\n===============================")
zrodlo = 'p'
tryb = 'd'
reprezentacja = 'ms'

if tryb == 'd':
    if zrodlo == 'p':
        n, edges = load_from_file("graf3.txt")

    elif zrodlo == 'l':
        n = int(input("4. Podaj liczbę wierzchołków (n): "))
        s = float(input("5. Podaj nasycenie (s): ")) / 100
        n, edges = generate_random_graph(n, s)

    mode = reprezentacja
    graf = Graf(n, edges, mode)

    if n<=12:
        graf.display()

    if not graf.check_prosty(edges):
        sys.exit(0)

    if not graf.check_wierzcholki(n):
        sys.exit(0)

    if not graf.check_stopnie(n, edges):
        sys.exit(0)