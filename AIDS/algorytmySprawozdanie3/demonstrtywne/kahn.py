import time
import random
import copy

#macierz sąsiedztwa
def kahn_ms(matrix, n):
    start_time = time.time()
    matrixcopy = copy.deepcopy(matrix)

    in_deg = {} #st wejsciowe
    for i in range(1, n + 1):
        in_deg[i] = 0

    for j in range(1, n + 1):
        for i in range(1, n + 1):
            if matrixcopy[j][i] == -1:
                in_deg[j] += 1

    zero_deg = [i for i in range(1, n + 1) if in_deg[i] == 0]
    result = []

    while zero_deg:
        print(f"Stopnie wejściowe: {in_deg}")
        u = zero_deg.pop(0)
        result.append(u)

        for v in range(1, n + 1):
            if matrixcopy[u][v] == 1: #znajdujemy wierzcholki do ktorych prowadzi u
                matrixcopy[u][v] = 0
                matrixcopy[v][u] = 0
                in_deg[v] -= 1

                if in_deg[v] == 0:
                    zero_deg.append(v)

    print(f"Stopnie wejściowe: {in_deg}")
    end_time = time.time()

    #wykrywanie cykli
    if len(result) != n:
        print(f"Wykryto cykl. Brak możliwości sortowania.")

        cycle_nodes = [v for v in range(1, n + 1) if in_deg[v] > 0]
        print(f"Wierzchołki tworzące cykl: {cycle_nodes}")
        return None, end_time - start_time

    return result, end_time - start_time

#lista nastepnikow
def kahn_ln(adj_list, n):
    start_time = time.time()
    adjcopy = copy.deepcopy(adj_list)

    in_deg = {}
    for i in range(1, n + 1):
        in_deg[i] = 0

    for i in range(1, n + 1):
        for v in adjcopy[i]: # dla wierzchołków przy i
            in_deg[v] += 1

    zero_deg = [i for i in range(1, n + 1) if in_deg[i] == 0]
    result = []

    while zero_deg:
        print(f"Stopnie wejściowe: {in_deg}")
        u = zero_deg.pop(0)
        result.append(u)

        while adjcopy[u]: #usuwamy krawędzie
            v = adjcopy[u].pop(0)
            in_deg[v] -= 1
            if in_deg[v] == 0:
                zero_deg.append(v)

    print(f"Stopnie wejściowe: {in_deg}")
    end_time = time.time()

    if len(result) != n:
        print(f"Wykryto cykl. Brak możliwości sortowania.")
        cycle_nodes = [v for v in range(1, n + 1) if in_deg[v] > 0]
        print(f"Wierzchołki tworzące cykl: {cycle_nodes}")
        return None, end_time - start_time

    return result, end_time - start_time

#lista krawedzi
def kahn_lk(edge_list, n):
    start_time = time.time()
    edgescopy = copy.deepcopy(edge_list)

    in_deg = {}
    for i in range(1, n + 1):
        in_deg[i] = 0

    for u, v in edgescopy:
        in_deg[v] += 1

    zero_deg = [i for i in range(1, n + 1) if in_deg[i] == 0]
    result = []

    while zero_deg:
        print(f"Stopnie wejściowe: {in_deg}")
        u = zero_deg.pop(0)
        result.append(u)

        edges_to_remove = [i for i in edgescopy if i[0] == u] #nowa lista kr z u

        for i in edges_to_remove:
            edgescopy.remove(i) #usuniecie z listy krawedzi
            v = i[1]
            in_deg[v] -= 1
            if in_deg[v] == 0:
                zero_deg.append(v)

    print(f"Stopnie wejściowe: {in_deg}")
    end_time = time.time()

    if len(result) != n:
        print(f"Wykryto cykl. Brak możliwości sortowania.")
        cycle_nodes = [v for v in range(1, n + 1) if in_deg[v] > 0]
        print(f"Wierzchołki tworzące cykl: {cycle_nodes}")
        return None, end_time - start_time

    return result, end_time - start_time


def generate_random_graph(n_nodes, edge_probability=0.3, is_dag=True):
    temp_edges = []

    for i in range(1, n_nodes + 1):
        for j in range(1, n_nodes + 1):
            if i == j:
                continue

            if is_dag:
                #z cyklami
                if i < j:
                    if random.random() < edge_probability:
                        temp_edges.append((i, j))
            else:
                #bez cykli
                if random.random() < edge_probability:
                    temp_edges.append((i, j))

    mapping = list(range(1, n_nodes + 1))
    random.shuffle(mapping)

    random_edges = []
    for u, v in temp_edges:
        new_u = mapping[u - 1]
        new_v = mapping[v - 1]
        random_edges.append((new_u, new_v))

    return n_nodes, random_edges

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

def build_structures(n_nodes, edges):
    matrix = {i: {j: 0 for j in range(1, n_nodes + 1)} for i in range(1, n_nodes + 1)}
    adj_list = {i: [] for i in range(1, n_nodes + 1)}
    edge_list = list(edges)

    for u, v in edges:
        matrix[u][v] = 1
        matrix[v][u] = -1
        adj_list[u].append(v)

    return matrix, adj_list, edge_list


if __name__ == "__main__":
    sposob = input("Wygenerować graf losowo (L) czy wczytać własny (W)? (L/W): ").strip().upper()

    if sposob == 'W':
        n, edges = read_graph_from_user()
    else:
        n_nodes = int(input("Podaj ilość wierzchołków: "))
        odp_cykl = input("Czy graf ma zawierać cykle? (T/N): ").strip().upper()
        is_dag = False if odp_cykl == 'T' else True
        n, edges = generate_random_graph(n_nodes, edge_probability=0.4, is_dag=is_dag)

    print("\nWybierz reprezentację grafu:")
    print("1 - Macierz sąsiedztwa")
    print("2 - Lista następników")
    print("3 - Lista krawędzi")
    wybor_rep = input("Twój wybór (1/2/3): ").strip()

    matrix, adj_list, edge_list = build_structures(n, edges)

    print(f"\nGraf (n={n}, liczba krawędzi={len(edges)})")

    if wybor_rep == '1':
        print(f"Macierz sąsiedztwa: {matrix}\n")
        result, exec_time = kahn_ms(matrix, n)
    elif wybor_rep == '2':
        print(f"Lista następników: {adj_list}\n")
        result, exec_time = kahn_ln(adj_list, n)
    elif wybor_rep == '3':
        print(f"Lista krawędzi: {edge_list}\n")
        result, exec_time = kahn_lk(edge_list, n)
    else:
        print("Nieprawidłowy wybór.")
        exit()

    if result:
        print(f"Wynik końcowy: {result}")
    print(f"Czas wykonania: {exec_time:.6f} s")