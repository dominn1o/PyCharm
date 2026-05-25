import random


def build_macierz_sasiedztwa(n, edges):
    """Dla grafów nieskierowanych """
    matrix = [[0] * n for _ in range(n)]
    for u, v in edges:
        matrix[u - 1][v - 1] = 1
        matrix[v - 1][u - 1] = 1
    return matrix


def build_macierz_grafu(n, edges):
    """Zoptymalizowana budowa Macierzy Grafu dla grafów skierowanych """
    # Używamy set() dla dostępu w czasie O(1) zamiast O(N)
    L_N = [set() for _ in range(n + 1)]
    L_P = [set() for _ in range(n + 1)]

    for u, v in edges:
        L_N[u].add(v)
        L_P[v].add(u)

    matrix = [[0] * (n + 3) for _ in range(n)]

    for i in range(1, n + 1):
        set_N = L_N[i]
        set_P = L_P[i]

        # Sortujemy tylko raz na wiersz dla potrzeb 3 ostatnich kolumn
        sorted_N = sorted(list(set_N))
        sorted_P = sorted(list(set_P))

        L_B_i = [j for j in range(1, n + 1) if j not in set_N and j not in set_P]

        row = i - 1
        last_N = sorted_N[-1] if sorted_N else 0
        last_P = sorted_P[-1] if sorted_P else 0
        last_B = L_B_i[-1] if L_B_i else 0

        matrix[row][n] = sorted_N[0] if sorted_N else 0
        matrix[row][n + 1] = sorted_P[0] if sorted_P else 0
        matrix[row][n + 2] = L_B_i[0] if L_B_i else 0

        for j in range(1, n + 1):
            col = j - 1
            # Błyskawiczne sprawdzenie dzięki set()
            has_next = j in set_N
            has_prev = j in set_P

            if not has_next and not has_prev:
                matrix[row][col] = -last_B
            elif has_next and not has_prev:
                matrix[row][col] = last_N
            elif not has_next and has_prev:
                matrix[row][col] = last_P + n
            elif has_next and has_prev:
                matrix[row][col] = last_N + 2 * n
    return matrix


def max_edges(n, directed):
    return n * (n - 1) if directed else n * (n - 1) // 2


def generate_random_graph(n, s, directed=False):
    """Szybkie generowanie losowego grafu o zadanym nasyceniu."""
    m_target = int(max_edges(n, directed) * s)

    # Optymalizacja dla gęstych grafów: tworzymy listę i używamy sample
    if s >= 0.5 and n <= 2000:
        all_edges = []
        if directed:
            for u in range(1, n + 1):
                for v in range(1, n + 1):
                    if u != v: all_edges.append((u, v))
        else:
            for u in range(1, n + 1):
                for v in range(u + 1, n + 1):
                    all_edges.append((u, v))
        return random.sample(all_edges, m_target)
    else:
        edges = set()
        while len(edges) < m_target:
            u, v = random.randint(1, n), random.randint(1, n)
            if u != v:
                if not directed and u > v: u, v = v, u
                edges.add((u, v))
        return list(edges)


def generate_hamiltonian_graph(n, s, directed=False):
    """Generuje graf gwarantujący cykl Hamiltona."""
    vertices = list(range(1, n + 1))
    random.shuffle(vertices)
    edges = set()

    for i in range(n):
        u, v = vertices[i], vertices[(i + 1) % n]
        if not directed and u > v: u, v = v, u
        edges.add((u, v))

    m_target = max(len(edges), int(max_edges(n, directed) * s))

    # Zabezpieczenie przed nieskończoną pętlą (limit prób)
    fails = 0
    while len(edges) < m_target and fails < 1000:
        u, v = random.randint(1, n), random.randint(1, n)
        if u != v:
            if not directed and u > v: u, v = v, u
            if (u, v) not in edges:
                edges.add((u, v))
                fails = 0
            else:
                fails += 1
    return list(edges)


def generate_eulerian_graph(n, s, directed=False):
    """Generuje graf z małych cykli (Eulerowski)."""
    edges = set(generate_hamiltonian_graph(n, 0, directed))
    m_target = max(len(edges), int(max_edges(n, directed) * s))

    fails = 0
    while len(edges) < m_target and fails < 500:
        cycle_len = random.randint(3, max(3, n // 2))
        cycle_verts = random.sample(range(1, n + 1), cycle_len)

        new_edges = []
        for i in range(cycle_len):
            u, v = cycle_verts[i], cycle_verts[(i + 1) % cycle_len]
            if not directed and u > v: u, v = v, u
            new_edges.append((u, v))

        if all(e not in edges for e in new_edges):
            for e in new_edges:
                edges.add(e)
            fails = 0
        else:
            fails += 1

    return list(edges)