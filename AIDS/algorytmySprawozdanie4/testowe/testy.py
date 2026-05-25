import euler
import hamilton
import grafy
import obliczanieSrednich as avg
import os


def log_wynik(plik, operacja, typ, n, s, czas, back=None):
    with open(plik, "a", encoding="utf-8") as f:
        line = f"Operacja: {operacja}; Typ: {typ}; n: {n}; Nasycenie: {s:.2f}; Czas: {czas * 1000:.4f} ms;"
        if back is not None:
            line += f" Backtracki: {back};"
        f.write(line + "\n")


def uruchom_pojedynczy_algorytm(n_vals, nasycenia, alg, is_exp2=False):
    typy = [False, True]  # False = nieskierowany, True = skierowany

    for n in n_vals:
        for s in nasycenia:
            for is_directed in typy:
                typ_str = "skierowany" if is_directed else "nieskierowany"
                print(f"Test: Algorytmu {alg}, n={n}, s={s}, typ={typ_str}, Exp={2 if is_exp2 else 1}")

                for _ in range(10):  # 10 niezależnych powtórzeń
                    if alg in ['DEC', 'SEC']:
                        edges = grafy.generate_eulerian_graph(n, s,
                                                              is_directed) if is_exp2 else grafy.generate_random_graph(
                            n, s, is_directed)
                        matrix = grafy.build_macierz_grafu(n, edges) if is_directed else grafy.build_macierz_sasiedztwa(
                            n, edges)
                        instancja = euler.Euler(n, edges, is_directed, matrix)

                        if alg == 'DEC':
                            res, t = instancja.dec()
                            log_wynik("wyniki/exp1_DEC.txt", "DEC", typ_str, n, s, t)
                        elif alg == 'SEC':
                            res, t, b = instancja.sec()
                            plik = "wyniki/exp2_SEC.txt" if is_exp2 else "wyniki/exp1_SEC.txt"
                            log_wynik(plik, "SEC", typ_str, n, s, t, b)

                    elif alg in ['DHC', 'SHC']:
                        edges = grafy.generate_hamiltonian_graph(n, s,
                                                                 is_directed) if is_exp2 else grafy.generate_random_graph(
                            n, s, is_directed)
                        matrix = grafy.build_macierz_grafu(n, edges) if is_directed else grafy.build_macierz_sasiedztwa(
                            n, edges)
                        instancja = hamilton.Hamilton(n, edges, is_directed, matrix)

                        if alg == 'DHC':
                            res, t = instancja.dhc()
                            log_wynik("wyniki/exp1_DHC.txt", "DHC", typ_str, n, s, t)
                        elif alg == 'SHC':
                            res, t, b = instancja.shc()
                            plik = "wyniki/exp2_SHC.txt" if is_exp2 else "wyniki/exp1_SHC.txt"
                            log_wynik(plik, "SHC", typ_str, n, s, t, b)


def usun_katalogi():
    os.makedirs("wyniki", exist_ok=True)
    os.makedirs("wynikiFin", exist_ok=True)
    for folder in ["wyniki", "wynikiFin"]:
        for f in os.listdir(folder):
            file_path = os.path.join(folder, f)
            if os.path.isfile(file_path):
                os.remove(file_path)


if __name__ == "__main__":
    usun_katalogi()

    # --- BEZPIECZNE ZAKRESY WIELKOŚCI N DLA PYTHON ---
    # Zamiast 5000 (gdzie tworzenie macierzy trwa wieczność), używamy mniejszych skoków liniowych.
    n_vals_dec = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]
    n_vals_dhc = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]

    n_vals_sec = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    n_vals_shc = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    # Zakresy nasyceń
    nasycenia_exp1 = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    nasycenia_exp2 = [0.5, 0.6, 0.7, 0.8, 0.9]

    # --- EKSPERYMENT 1 (Losowe grafy) ---
    print("\n=== Start Eksperymentu 1 ===")
    uruchom_pojedynczy_algorytm(n_vals_dec, nasycenia_exp1, alg='DEC', is_exp2=False)
    uruchom_pojedynczy_algorytm(n_vals_dhc, nasycenia_exp1, alg='DHC', is_exp2=False)

    # Backtracking musi lecieć na mniejszych instancjach
    uruchom_pojedynczy_algorytm(n_vals_sec, nasycenia_exp1, alg='SEC', is_exp2=False)
    uruchom_pojedynczy_algorytm(n_vals_shc, nasycenia_exp1, alg='SHC', is_exp2=False)

    # --- EKSPERYMENT 2 (Grafy z cyklem) ---
    print("\n=== Start Eksperymentu 2 ===")
    uruchom_pojedynczy_algorytm(n_vals_sec, nasycenia_exp2, alg='SEC', is_exp2=True)
    uruchom_pojedynczy_algorytm(n_vals_shc, nasycenia_exp2, alg='SHC', is_exp2=True)

    # --- AGREGACJA ---
    print("\n=== Agregacja Wyników ===")
    for f in os.listdir("wyniki"):
        if f.endswith(".txt"):
            avg.calculateAverage(os.path.join("wyniki", f), os.path.join("wynikiFin", f.replace(".txt", "_fin.txt")))

    print("Gotowe. Wszystkie wyniki zagregowane w folderze wynikiFin.")