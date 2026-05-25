import random
import time
import sys

cycle = []
visited_vertexes = [] #bool for shc
backtracks = 0


############ WARUNKI ##############
def is_connected_euler(n, matrix, is_directed):
    start_node = -1

    for i in range(n):
        out_degree = sum(matrix[i])
        in_degree = sum(matrix[j][i] for j in range(n)) if is_directed else out_degree

        if out_degree > 0 or in_degree > 0:
            start_node = i
            break

    if start_node == -1:
        return True

    visited = [False] * n

    def dfs(v):
        visited[v] = True
        for u in range(n):
            edge_exists = matrix[v][u] > 0 or (is_directed and matrix[u][v] > 0)
            if edge_exists and not visited[u]:
                dfs(u)

    dfs(start_node)

    for i in range(n):
        out_degree = sum(matrix[i])
        in_degree = sum(matrix[j][i] for j in range(n)) if is_directed else out_degree

        if (out_degree > 0 or in_degree > 0) and not visited[i]:
            return False
    return True


def has_eulerian_cycle(n, matrix, is_directed):
    if not is_connected_euler(n, matrix, is_directed):
        return False

    if not is_directed:
        for i in range(n):
            degree = sum(matrix[i])
            if degree % 2 != 0:
                return False
    else:
        for i in range(n):
            out_degree = sum(matrix[i])
            in_degree = sum(matrix[j][i] for j in range(n))

            if in_degree != out_degree:
                return False

    return True


def is_simple(edges, is_directed):
    seen_edges = set()

    for u, v in edges:
        if u == v:
            return False

        if not is_directed:
            edge = tuple(sorted((u, v)))
        else:
            edge = (u, v)
        if edge in seen_edges:
            return False
        seen_edges.add(edge)
    return True

##############EULER##################
def sec(u, n, matrix):
    # search eulerian cycle
    # przechodzi przez każdą krawędź 1 raz i wraca do wierzchołka początkowego
    global cycle
    global backtracks

    if n == 0:
        return None

    for i in range(0, n):
        if matrix[u][i] == 1:
            matrix[u][i], matrix[i][u] = 0, 0
            sec(i, n, matrix)

    backtracks += 1
    cycle.append(u)


############## HAMILTON ###############
def shc(u, n, matrix):
    # search hamiltonian cycle
    # przechodzi przez każdy wierzchołek 1 raz i wraca do początkowego
    # roberts-flores
    global cycle
    global visited_vertexes
    global backtracks

    if n == 0:
        return False

    visited_vertexes[u] = True
    cycle.append(u)

    if len(cycle) == n: #koniec
        start_vertex = cycle[0]
        val = matrix[u][start_vertex]

        if (0 <= val <= n) or (2 * n + 1 <= val <= 3 * n):
            cycle.append(start_vertex)
            return True
    else:
        for i in range(n):
            val = matrix[u][i]

            if (0 <= val <= n) or (2 * n + 1 <= val <= 3 * n):
                if not visited_vertexes[i]:
                    if shc(i, n, matrix):
                        return True

    backtracks += 1
    visited_vertexes[u] = False
    cycle.pop()
    return False


def random_undirected_graph(n, simple=True):
    edges = []

    if simple:
        max_m = n *(n-1)//2
        m = random.randint(1, max_m) if max_m >= 1 else 0

        pairs = set()
        while len(pairs) < m:
            u = random.randint(1, n)
            v = random.randint(1, n)
            if u != v:
                pair = tuple(sorted((u, v)))
                if pair not in pairs:
                    pairs.add(pair)
                    edges.append((pair[0], pair[1]))
    else:
        m = random.randint(5, 15)
        for _ in range(m):
            u = random.randint(1, n)
            v = random.randint(1, n)
            u, v = sorted((u, v))
            edges.append((u, v))

    return n, edges


def random_directed_graph(n, simple=True):
    edges = []

    if simple:
        max_m = n * (n-1)
        m = random.randint(1, max_m) if max_m >= 1 else 0

        pairs = set()
        while len(pairs) < m:
            u = random.randint(1, n)
            v = random.randint(1, n)
            if u != v:
                pair = (u, v)
                if pair not in pairs:
                    pairs.add(pair)
                    edges.append((u, v))
    else:
        m = random.randint(5, 15)
        for _ in range(m):
            u = random.randint(1, n)
            v = random.randint(1, n)
            edges.append((u, v))

    return n, edges


def read_graph_from_user():
    filename = input("nazwa pliku: ").strip()
    edges = []
    with open(filename, 'r') as file:
        first_line = file.readline().strip().split()
        n = int(first_line[0])
        m = int(first_line[1])
        for _ in range(m):
            u, v = map(int, file.readline().strip().split())
            edges.append((u, v))
    return n, edges


#EULER
def adjacency_directed_matrix(n, edges):
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for u, v in edges:
        matrix[u - 1][v - 1] = 1
        matrix[v - 1][u - 1] = -1
    return matrix


def adjacency_undirected_matrix(n, edges):
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for u, v in edges:
        matrix[u - 1][v - 1] = 1
        matrix[v - 1][u - 1] = 1
    return matrix

#HAMILTON
def graph_matrix(n, edges):
    L_N = {i: [] for i in range(1, n + 1)}  # następniki
    L_P = {i: [] for i in range(1, n + 1)}  # poprzedniki
    L_B = {i: [] for i in range(1, n + 1)}  # nieincydentne

    for u, v in edges:
        if v not in L_N[u]:
            L_N[u].append(v)
        if u not in L_P[v]:
            L_P[v].append(u)

    for i in range(1, n + 1):
        L_N[i].sort()
        L_P[i].sort()

        for j in range(1, n + 1):
            if j not in L_N[i] and j not in L_P[i]:
                L_B[i].append(j)
        L_B[i].sort()

    matrix = [[0] * (n + 4) for _ in range(n)]

    for i in range(1, n + 1):
        row = i - 1

        last_N = L_N[i][-1] if L_N[i] else 0
        last_P = L_P[i][-1] if L_P[i] else 0
        last_B = L_B[i][-1] if L_B[i] else 0

        # dodatkowe kolumny na końcu
        matrix[row][n] = L_N[i][0] if L_N[i] else 0  # pierwszy następnik
        matrix[row][n + 1] = L_P[i][0] if L_P[i] else 0  # pierwszy poprzednik
        matrix[row][n + 2] = L_B[i][0] if L_B[i] else 0  # ierwszy nieincydentny

        # główne kolumny
        for j in range(1, n + 1):
            col = j - 1

            has_next = j in L_N[i]
            has_previous = j in L_P[i]

            if not has_next and not has_previous:
                matrix[row][col] = -last_B

            elif has_next and not has_previous:
                matrix[row][col] = last_N

            elif not has_next and has_previous:
                matrix[row][col] = last_P + n

            elif has_next and has_previous:
                matrix[row][col] = last_N + 2 * n
    return matrix

def print_matrix(matrix):
    print("\nReprezentacja maszynowa grafu (Macierz):")
    for row in matrix:
        print("\t".join(f"{val:2}" for val in row))
    print()

if __name__ == "__main__":
    try:
        problem = input("Znaleźć cykl Eulera [E] czy cykl Hamiltona [H]?: ").strip().upper()
        graph_type = input("Czy graf ma być Skierowany [S] czy Nieskierowany [N]: ").strip().upper()
        generating = input("Wygenerować graf losowo (L) czy wczytać własny (W)? (L/W): ").strip().upper()

        if generating == 'W':
            n, edges = read_graph_from_user()
        else:
            n = int(input("Podaj liczbę wierzchołków dla losowego grafu: ").strip())
            if graph_type == 'S':
                n, edges = random_directed_graph(n, simple=True)
            else:
                n, edges = random_undirected_graph(n, simple=True)

        print(f"\nWygenerowano graf o {n} wierzchołkach.")
        print(f"Krawędzie ({len(edges)}): {edges}\n")

    except ValueError:
        print("Błąd: Podano nieprawidłowe dane wejściowe.")
        sys.exit(1)

    is_directed = (graph_type == 'S')
    if not is_simple(edges, is_directed):
        print("Błąd: Podany graf jest multigrafem (nie jest prosty). Podaj inny graf.")
        sys.exit(1)

    cycle.clear()
    visited_vertexes = [False] * n
    backtracks = 0

    if problem == 'E':
        if is_directed:
            matrix = adjacency_directed_matrix(n, edges)
        else:
            matrix = adjacency_undirected_matrix(n, edges)

        print_matrix(matrix)
        if has_eulerian_cycle(n, matrix, is_directed):
            start_time = time.time()
            sec(0, n, matrix)
            end_time = time.time()
            cycle.reverse()
            print(f"Znaleziono Cykl Eulera:\n{' -> '.join(str(v + 1) for v in cycle)}")
            print(f"Długość rozwiązania (liczba krawędzi): {len(cycle) - 1}")
            print(f"Liczba operacji cofania (backtracków): {backtracks}")
            print(f"Czas działania operacji: {end_time-start_time:.6f} s")
        else:
            print("Graf nie posiada cyklu Eulera.")

    elif problem == 'H':
        matrix = graph_matrix(n, edges)
        print_matrix(matrix)

        start_time = time.time()
        hamilton = shc(0, n, matrix)
        end_time = time.time()

        if hamilton:
            print(f"Znaleziono Cykl Hamiltona:\n{' -> '.join(str(v + 1) for v in cycle)}")
            print(f"Długość rozwiązania (liczba krawędzi): {len(cycle) - 1}")
            print(f"Liczba operacji cofania (backtracków): {backtracks}")
            print(f"Czas działania operacji: {end_time-start_time:.6f} s")

        else:
            print("Graf nie posiada cyklu Hamiltona.")
            print(f"Liczba operacji cofania (backtracków): {backtracks}")
            print(f"Czas działania operacji: {end_time - start_time:.6f} s")
