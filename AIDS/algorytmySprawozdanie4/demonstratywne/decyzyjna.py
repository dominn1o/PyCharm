import random
import itertools

class Graf():
        def __init__(self, liczbaWierzcholkow, liczbaKrawedzi, edges, problem, skierowany):
            self.liczbaWierzcholkow = liczbaWierzcholkow
            self.liczbaKrawedzi = liczbaKrawedzi
            self.edges = edges
            self.skierowany = skierowany

            if problem == 'e':
                self.reprezentacja = self.build_macierz_sasiedztwa(edges)
            elif problem == 'h':
                self.reprezentacja = self.build_macierz_incydencji(edges)

        def display(self):
            print(f"V: {self.liczbaWierzcholkow}, E: {self.liczbaKrawedzi}")
            for row in self.reprezentacja:
                print(row)

        def build_macierz_sasiedztwa(self, edges):
            matrix = [[0] * self.liczbaWierzcholkow for _ in range(self.liczbaWierzcholkow)]
            for u, v in edges:
                matrix[u - 1][v - 1] = 1
                if not self.skierowany:
                    matrix[v - 1][u - 1] = 1
            return matrix

        def build_macierz_incydencji(self, edges):
            # Macierz V x E (wierzchołki x krawędzie)
            matrix = [[0] * self.liczbaKrawedzi for _ in range(self.liczbaWierzcholkow)]
            for e, (u, v) in enumerate(edges):
                if self.skierowany:
                    matrix[u - 1][e] = -1  # wychodząca
                    matrix[v - 1][e] = 1  # wchodząca
                else:
                    matrix[u - 1][e] = 1
                    matrix[v - 1][e] = 1
            return matrix

        def dec_euler_nieskierowany(self):
            # 1. Sprawdzenie parzystości stopni wierzchołków
            for i in range(self.liczbaWierzcholkow):
                stopien = sum(self.reprezentacja[i])
                if stopien % 2 != 0:
                    print("\nDEC-EULER: NIE (Wierzchołek", i + 1, "ma nieparzysty stopień)")
                    return False

            # 2. Sprawdzenie spójności za pomocą BFS (ignorujemy izolowane wierzchołki)
            start_node = -1
            for i in range(self.liczbaWierzcholkow):
                if sum(self.reprezentacja[i]) > 0:
                    start_node = i
                    break

            # Jeśli są jakieś krawędzie (start_node != -1), sprawdzamy czy dojdziemy wszędzie
            if start_node != -1:
                visited = [False] * self.liczbaWierzcholkow
                queue = [start_node]
                visited[start_node] = True

                while queue:
                    u = queue.pop(0)
                    for v in range(self.liczbaWierzcholkow):
                        if self.reprezentacja[u][v] == 1 and not visited[v]:
                            visited[v] = True
                            queue.append(v)

                # Jeśli jest jakiś wierzchołek, który ma krawędzie, a nie został odwiedzony -> graf niespójny
                for i in range(self.liczbaWierzcholkow):
                    if sum(self.reprezentacja[i]) > 0 and not visited[i]:
                        print("\nDEC-EULER: NIE (Graf jest niespójny)")
                        return False

            print("\nDEC-EULER: TAK (Graf spełnia warunek konieczny i wystarczający)")
            return True

        def dec_euler_skierowany(self):
            # 1. Sprawdzenie czy in-degree == out-degree dla wszystkich wierzchołków
            for i in range(self.liczbaWierzcholkow):
                out_degree = sum(self.reprezentacja[i])  # suma wiersza
                in_degree = sum(self.reprezentacja[j][i] for j in range(self.liczbaWierzcholkow))  # suma kolumny

                if out_degree != in_degree:
                    print(f"\nDEC-EULER: NIE (Wierzchołek {i + 1} ma różny stopień wchodzący i wychodzący)")
                    return False

            # 2. Spójność (w digrafie spełniającym in==out wystarczy 1 zwykły BFS po krawędziach wychodzących)
            start_node = -1
            for i in range(self.liczbaWierzcholkow):
                if sum(self.reprezentacja[i]) > 0:
                    start_node = i
                    break

            if start_node != -1:
                visited = [False] * self.liczbaWierzcholkow
                queue = [start_node]
                visited[start_node] = True

                while queue:
                    u = queue.pop(0)
                    for v in range(self.liczbaWierzcholkow):
                        if self.reprezentacja[u][v] == 1 and not visited[v]:
                            visited[v] = True
                            queue.append(v)

                for i in range(self.liczbaWierzcholkow):
                    if sum(self.reprezentacja[i]) > 0 and not visited[i]:
                        print("\nDEC-EULER: NIE (Digraf nie jest silnie spójny)")
                        return False

            print("\nDEC-EULER: TAK (Digraf spełnia warunek konieczny i wystarczający)")
            return True

        def dhc_hamilton_nieskierowany_ore(self):
            n = self.liczbaWierzcholkow
            if n < 3:
                print("\nDHC-HAMILTON: NIE (Twierdzenie Orego wymaga co najmniej 3 wierzchołków)")
                return False

            # Sprawdzamy każdą parę wierzchołków u i v
            for u in range(n):
                for v in range(u + 1, n):
                    # 1. Czy u i v są połączone? (szukamy wspólnej krawędzi w macierzy incydencji)
                    sa_polaczone = False
                    for e in range(self.liczbaKrawedzi):
                        if self.reprezentacja[u][e] == 1 and self.reprezentacja[v][e] == 1:
                            sa_polaczone = True
                            break

                    # 2. Jeśli NIE są połączone, sprawdzamy warunek Orego
                    if not sa_polaczone:
                        deg_u = sum(self.reprezentacja[u])
                        deg_v = sum(self.reprezentacja[v])

                        if deg_u + deg_v < n:
                            print(f"\nDHC-HAMILTON: BRAK ROZSTRZYGNIĘCIA")
                            print(f"Twierdzenie Orego nie zostało spełnione dla wierzchołków {u + 1} i {v + 1}.")
                            print(f"Ich stopnie: {deg_u} + {deg_v} = {deg_u + deg_v} (wymagane >= {n})")
                            print("Graf nadal może być hamiltonowski, ale to twierdzenie tego nie gwarantuje.")
                            return False

            print("\nDHC-HAMILTON: TAK (Graf spełnia warunek wystarczający z Tw. Orego)")
            return True

        def dhc_hamilton_skierowany_woodall(self):
            n = self.liczbaWierzcholkow
            if n < 3:
                print("\nDHC-HAMILTON: NIE (Twierdzenie Woodalla wymaga co najmniej 3 wierzchołków)")
                return False

            # Sprawdzamy każdą uporządkowaną parę (u, v) - w grafie skierowanym kierunek ma znaczenie!
            for u in range(n):
                for v in range(n):
                    if u == v:
                        continue

                    # 1. Czy istnieje łuk od u do v?
                    # (w macierzy incydencji u ma -1 (wychodzi), a v ma 1 (wchodzi) w tej samej kolumnie e)
                    luk_istnieje = False
                    for e in range(self.liczbaKrawedzi):
                        if self.reprezentacja[u][e] == -1 and self.reprezentacja[v][e] == 1:
                            luk_istnieje = True
                            break

                    # 2. Jeśli NIE ma łuku u -> v, sprawdzamy warunek Woodalla
                    if not luk_istnieje:
                        # out-degree u (liczba -1 w wierszu u)
                        out_u = self.reprezentacja[u].count(-1)
                        # in-degree v (liczba 1 w wierszu v)
                        in_v = self.reprezentacja[v].count(1)

                        if out_u + in_v < n:
                            print(f"\nDHC-HAMILTON: BRAK ROZSTRZYGNIĘCIA")
                            print(f"Tw. Woodalla nie spełnione dla braku łuku {u + 1} -> {v + 1}.")
                            print(f"Out-deg({u + 1}) + In-deg({v + 1}) = {out_u} + {in_v} = {out_u + in_v} (wymagane >= {n})")
                            print("Uwaga: Graf nadal może być hamiltonowski, ale to twierdzenie tego nie gwarantuje.")
                            return False

            print("\nDHC-HAMILTON: TAK (Digraf spełnia warunek wystarczający z Tw. Woodalla)")
            return True



def load_from_file(filename):
    with open(filename, 'r') as file:
        first_line = file.readline().split()

        n = int(first_line[0])
        m = int(first_line[1])

        edges = []
        for line in file:
            parts = line.split()
            if len(parts) == 2:
                u, v = map(int, parts)
                edges.append((u, v))

        return n, m, edges



def generuj_losowy_graf(liczbaWierzcholkow, nasycenie, skierowany):
    wierzcholki = range(1, liczbaWierzcholkow + 1)

    if skierowany:
        max_krawedzi = liczbaWierzcholkow * (liczbaWierzcholkow - 1)
        # Używamy permutacji, bo kierunek ma znaczenie: (1, 2) to inny łuk niż (2, 1)
        wszystkie_krawedzie = list(itertools.permutations(wierzcholki, 2))
    else:
        max_krawedzi = liczbaWierzcholkow * (liczbaWierzcholkow - 1) // 2
        # Używamy kombinacji, bo kierunek nie ma znaczenia: (1, 2) i (2, 1) to ta sama krawędź
        wszystkie_krawedzie = list(itertools.combinations(wierzcholki, 2))

    m = int(max_krawedzi * nasycenie)

    wybrane_krawedzie = random.sample(wszystkie_krawedzie, m)

    return len(wybrane_krawedzie), wybrane_krawedzie

print("\n===============================")
print("=== MENU GŁÓWNE - ALGORYTMY Z POWRACANIEM (WERSJA DECYZYJNA) ===")
problem = input("1. Euler(e) czy Hamilton(h): ")
rodzajGrafu = input("2. Graf skierowany(s) czy nieskierowany(n): ")
zrodlo = input("3. Wybierz zrodlo - plik(p), losowy(l): ")
print("\n===============================")

skierowany = False
if rodzajGrafu == 's':
    skierowany = True

if zrodlo == 'p':
    n, m, edges = load_from_file("plik.txt")
elif zrodlo == 'l':
    n = int(input("4. Podaj liczbę wierzchołków (n): "))
    s = float(input("5. Podaj nasycenie (s): ")) / 100
    if skierowany:
        m, edges = generuj_losowy_graf(n, s, True)
    else:
        m, edges = generuj_losowy_graf(n, s, False)

graf = Graf(n,m, edges, problem, skierowany)
graf.display()

if problem == 'e':
    if rodzajGrafu == 's':
        graf.dec_euler_skierowany()
    elif rodzajGrafu == 'n':
        graf.dec_euler_nieskierowany()
elif problem == 'h':
    if rodzajGrafu == 's':
        graf.dhc_hamilton_skierowany_woodall()
    elif rodzajGrafu == 'n':
        graf.dhc_hamilton_nieskierowany_ore()