import random
import time


class Plecak():
    def __init__(self, n, b, przedmioty):
        self.n = n
        self.b = b
        # przedmioty to lista krotek: (id, rozmiar, uzytecznosc)
        self.przedmioty = przedmioty

    def display(self):
        print(f"Liczba przedmiotów (n): {self.n}, Pojemność ładunkowa (b): {self.b}")
        print("Dostępne wyposażenie [ID: Rozmiar, Użyteczność]:")
        for p in self.przedmioty:
            print(f"  [{p[0]}]: Rozmiar: {p[1]}, Użyteczność: {p[2]}")

    def algorytm_silowy(self, tryb_demonstracyjny=False):
        najlepsza_uzytecznosc = -1
        najlepsze_rozwiazania = []

        sprawdzone_konfiguracje = 2 ** self.n
        rozwiazania_dopuszczalne = 0

        # Iterujemy po wszystkich możliwych kombinacjach kodowanych binarnie (od 0 do 2^n - 1)
        for i in range(sprawdzone_konfiguracje):
            obecny_rozmiar = 0
            obecna_uzytecznosc = 0
            wybrane_id = []

            # Sprawdzamy poszczególne bity liczby 'i'
            for j in range(self.n):
                # Jeśli j-ty bit jest ustawiony na 1, bierzemy j-ty przedmiot
                if (i >> j) & 1:
                    przedmiot = self.przedmioty[j]
                    wybrane_id.append(przedmiot[0])
                    obecny_rozmiar += przedmiot[1]
                    obecna_uzytecznosc += przedmiot[2]

            # Sprawdzamy czy konfiguracja nie przekracza pojemności (rozwiązanie dopuszczalne)
            if obecny_rozmiar <= self.b:
                rozwiazania_dopuszczalne += 1

                # Aktualizacja najlepszego rozwiązania
                if obecna_uzytecznosc > najlepsza_uzytecznosc:
                    najlepsza_uzytecznosc = obecna_uzytecznosc
                    najlepsze_rozwiazania = [(obecny_rozmiar, wybrane_id)]
                elif obecna_uzytecznosc == najlepsza_uzytecznosc:
                    # Zapisujemy, jeśli jest to kolejne rozwiązanie o takiej samej, optymalnej wartości
                    najlepsze_rozwiazania.append((obecny_rozmiar, wybrane_id))

        # Przygotowanie wyników
        liczba_rozwiazan_optymalnych = len(najlepsze_rozwiazania)

        # Zwracamy pierwsze z brzegu optymalne rozwiązanie do ostatecznego wyświetlenia
        if liczba_rozwiazan_optymalnych > 0:
            najlepszy_rozmiar, ostateczne_id = najlepsze_rozwiazania[0]
        else:
            najlepszy_rozmiar, ostateczne_id = (0, [])

        wyniki = {
            'uzytecznosc': najlepsza_uzytecznosc,
            'rozmiar': najlepszy_rozmiar,
            'id_elementow': ostateczne_id,
            'sprawdzone_konfig': sprawdzone_konfiguracje,
            'dopuszczalne': rozwiazania_dopuszczalne,
            'optymalne': liczba_rozwiazan_optymalnych
        }

        # Tryb demonstracyjny zgodny z pkt 4 zadań dla małych instancji
        if tryb_demonstracyjny:
            print("\n--- TRYB DEMONSTRACYJNY (Algorytm Siłowy AB) ---")
            print(f"Liczba sprawdzonych wszystkich konfiguracji: {wyniki['sprawdzone_konfig']}")
            print(f"Liczba rozwiązań dopuszczalnych (rozmiar <= {self.b}): {wyniki['dopuszczalne']}")
            print(f"Liczba znalezionych rozwiązań optymalnych: {wyniki['optymalne']}")
            print("------------------------------------------------")

        return wyniki


def load_from_file(filename):
    # Funkcja odporna na błędy (zgodnie z wymaganiem z obrazka)
    with open(filename, 'r') as file:
        # Wczytanie n i b z pierwszej linii
        first_line = file.readline().split()
        if len(first_line) < 2:
            raise ValueError("Brak wystarczających danych w pierwszej linii (wymagane: n b).")

        n = int(first_line[0])
        b = int(first_line[1])

        przedmioty = []
        for i in range(1, n + 1):
            line = file.readline().split()
            if len(line) >= 2:
                rozmiar = int(line[0])
                uzytecznosc = int(line[1])
                przedmioty.append((i, rozmiar, uzytecznosc))
            else:
                raise ValueError(f"Błąd w danych elementu {i}. Oczekiwano: rozmiar użyteczność.")

        return n, b, przedmioty


def generuj_losowe_dane(n, b):
    przedmioty = []
    for i in range(1, n + 1):
        # Losujemy rozmiar i użyteczność tak, by miały rozsądny zakres
        maks_rozmiar = max(2, b // (n // 3 + 1))
        rozmiar = random.randint(1, maks_rozmiar)
        uzytecznosc = random.randint(10, 100)
        przedmioty.append((i, rozmiar, uzytecznosc))
    return n, b, przedmioty


# ==========================================
# SKRYPT GŁÓWNY (Menu)
# ==========================================
print("\n===============================")
print("=== MENU GŁÓWNE - PROBLEM PLECAKOWY (AB) ===")
zrodlo = input("1. Wybierz źródło danych - plik(p) czy losowe(l): ")
tryb_demo_input = input("2. Czy uruchomić tryb demonstracyjny (t/n)? (zalecane dla n <= 15): ")
print("===============================\n")

tryb_demo = tryb_demo_input.lower() == 't'
n, b, przedmioty = None, None, None

# Pobieranie danych wejściowych
if zrodlo == 'p':
    nazwa_pliku = "plik.txt"
    n, b, przedmioty = load_from_file(nazwa_pliku)
elif zrodlo == 'l':
    try:
        n = int(input("Podaj liczbę dostępnych elementów wyposażenia (n): "))
        b = int(input("Podaj dostępną pojemność ładunkową (b): "))
        n, b, przedmioty = generuj_losowe_dane(n, b)
    except ValueError:
        print("Błąd: Należy podać liczby całkowite.")

# Uruchomienie algorytmu, jeśli dane wczytano poprawnie
if n is not None and przedmioty is not None:
    plecak = Plecak(n, b, przedmioty)
    plecak.display()

    # Ostrzeżenie przed zbyt dużym N dla algorytmu silowego
    if n > 22:
        print("\nOSTRZEŻENIE: Dla n > 22 algorytm siłowy może wykonywać się bardzo długo (złożoność wykładnicza).")

    # Właściwe mierzenie czasu i wykonanie
    start_time = time.perf_counter()
    wyniki = plecak.algorytm_silowy(tryb_demo)
    end_time = time.perf_counter()
    czas_wykonania = end_time - start_time

    # Wypisywanie zadeklarowanych w zadaniu rezultatów
    print("\n=== WYNIKI ALGORYTMU SIŁOWEGO (AB) ===")
    print(f"Wartość uzyskanego rozwiązania (łączna użyteczność): {wyniki['uzytecznosc']}")
    print(f"Sumaryczny rozmiar wybranego zestawu: {wyniki['rozmiar']} (Limit: {b})")
    print(f"Identyfikatory wybranych elementów wchodzących w skład: {wyniki['id_elementow']}")
    print(f"Czas obliczeń: {czas_wykonania:.6f} s")
    print("=======================================\n")
else:
    print("Program przerwany z powodu braku lub błędów danych.")