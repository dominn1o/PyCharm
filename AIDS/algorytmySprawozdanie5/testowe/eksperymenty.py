import os
import time
import random
from agregator import agreguj_pliki

# Nowe, uporządkowane importy
from dynamiczny import algorytm_dynamiczny
from zachlanny import algorytm_zachlanny
from silowy import algorytm_silowy


def generuj_przedmioty(n):
    return [(i, random.randint(1, 20), random.randint(10, 100)) for i in range(1, n + 1)]


def log_czas(plik, alg, n, b, czas):
    with open(plik, "a", encoding="utf-8") as f:
        f.write(f"Algorytm: {alg}; n: {n}; b: {b}; Czas: {czas * 1000:.4f}\n")


def log_exp3(plik, n, b, opt, zach, error):
    with open(plik, "a", encoding="utf-8") as f:
        f.write(f"n: {n}; b: {b}; AD_optymalne: {opt}; AZ_suboptymalne: {zach}; Blad: {error:.4f}\n")


def przygotuj_katalogi():
    os.makedirs("wyniki_plecak", exist_ok=True)
    for f in os.listdir("wyniki_plecak"):
        os.remove(os.path.join("wyniki_plecak", f))


def eksperyment_1():
    print("\n=== Start Eksperymentu 1: Wpływ N na czas działania ===")
    n_wartosci = [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
    b_stale = 50

    for n in n_wartosci:
        print(f"Testowanie dla n={n}")
        for _ in range(10):
            przedmioty = generuj_przedmioty(n)

            start = time.perf_counter()
            algorytm_dynamiczny(b_stale, przedmioty)
            log_czas("wyniki_plecak/exp1_AD.txt", "AD", n, b_stale, time.perf_counter() - start)

            start = time.perf_counter()
            algorytm_zachlanny(b_stale, przedmioty)
            log_czas("wyniki_plecak/exp1_AZ.txt", "AZ", n, b_stale, time.perf_counter() - start)

            # Odchudzony algorytm siłowy
            start = time.perf_counter()
            algorytm_silowy(b_stale, przedmioty)
            log_czas("wyniki_plecak/exp1_AB.txt", "AB", n, b_stale, time.perf_counter() - start)


def eksperyment_2():
    print("\n=== Start Eksperymentu 2: Wpływ B na czas działania ===")
    n_stale = 20
    b_wartosci = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]

    for b in b_wartosci:
        print(f"Testowanie dla b={b}")
        for _ in range(10):
            przedmioty = generuj_przedmioty(n_stale)

            start = time.perf_counter()
            algorytm_dynamiczny(b, przedmioty)
            log_czas("wyniki_plecak/exp2_AD.txt", "AD", n_stale, b, time.perf_counter() - start)

            start = time.perf_counter()
            algorytm_zachlanny(b, przedmioty)
            log_czas("wyniki_plecak/exp2_AZ.txt", "AZ", n_stale, b, time.perf_counter() - start)

            start = time.perf_counter()
            algorytm_silowy(b, przedmioty)
            log_czas("wyniki_plecak/exp2_AB.txt", "AB", n_stale, b, time.perf_counter() - start)


def eksperyment_3():
    print("\n=== Start Eksperymentu 3: Jakość Algorytmu Zachłannego ===")
    liczba_instancji = 1000
    znalezione_optima = 0
    max_blad = 0
    suma_bledow = 0

    for i in range(liczba_instancji):
        n = random.randint(10, 50)
        b = random.randint(20, 100)
        przedmioty = generuj_przedmioty(n)

        # Rozpakowywanie ujednoliconych wyników (potrzebujemy tylko pierwszego elementu - użyteczności)
        ad_utility, _, _ = algorytm_dynamiczny(b, przedmioty)
        az_utility, _, _ = algorytm_zachlanny(b, przedmioty)

        if ad_utility == 0:
            continue

        blad = 100 * ((ad_utility - az_utility) / ad_utility)
        suma_bledow += blad

        if blad == 0:
            znalezione_optima += 1
        if blad > max_blad:
            max_blad = blad

        log_exp3("wyniki_plecak/exp3_jakosc.txt", n, b, ad_utility, az_utility, blad)

        if (i + 1) % 200 == 0:
            print(f"Przetworzono {i + 1}/1000 instancji...")

    procent_opt = (znalezione_optima / liczba_instancji) * 100
    srednia_jakosc = suma_bledow / liczba_instancji

    print("\n--- PODSUMOWANIE EKSPERYMENTU 3 ---")
    print(f"Liczba sprawdzonych instancji: {liczba_instancji}")
    print(f"Procent rozwiązań optymalnych AZ: {procent_opt:.2f}%")
    print(f"Średni błąd względny AZ od optimum: {srednia_jakosc:.2f}%")
    print(f"Największe zaobserwowane odchylenie od optimum: {max_blad:.2f}%")


if __name__ == "__main__":
    przygotuj_katalogi()
    eksperyment_1()
    eksperyment_2()
    eksperyment_3()
    print("\nWszystkie eksperymenty zakończone pomyślnie. Pliki zapisano w katalogu 'wyniki_plecak'.")

    print("Rozpoczynam agregację danych pomiarowych...")
    agreguj_pliki()
    print("Agregacja zakończona! Zagregowane pliki txt znajdują się w 'wyniki_plecak_finalne'.")