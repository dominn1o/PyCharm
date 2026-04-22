import time


class HMIN:
    def __init__(self):
        self.data = []

    def build_heap(self, tablica):
        """
        Optymalne budowanie kopca algorytmem Floyda w czasie O(n).
        Znacznie szybsze niż wielokrotne wywoływanie insert().
        """
        # ZMIANA: list(tablica) zamiast tablica[:] - wymusza czystą listę Pythona,
        # co rozwiązuje problemy z tablicami z biblioteki NumPy.
        self.data = list(tablica)
        n = len(self.data)

        # Zaczynamy od ostatniego węzła posiadającego dzieci (n // 2 - 1)
        # i przesiewamy w dół aż do korzenia (0).
        for i in range(n // 2 - 1, -1, -1):
            self._sift_down(i, n)

    def _sift_down(self, i, n):
        """Iteracyjne przesiewanie w dół (szybsze i bezpieczniejsze niż rekurencja)."""
        data = self.data
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i

            if left < n and data[left] < data[smallest]:
                smallest = left
            if right < n and data[right] < data[smallest]:
                smallest = right

            if smallest != i:
                # Zamiana
                data[i], data[smallest] = data[smallest], data[i]
                i = smallest  # Przechodzimy niżej
            else:
                break

    def find_max(self):
        """
        W kopcu minimalnym, maksimum ZAWSZE znajduje się w liściach.
        Liście zaczynają się od indeksu n // 2.
        Używamy wbudowanej funkcji max() z Pythona, bo działa w C i jest błyskawiczna.
        """
        # ZMIANA: Używamy len() == 0 zamiast "not self.data".
        # Działa w 100% bezpiecznie niezależnie od typu danych.
        if len(self.data) == 0:
            return None

        n = len(self.data)

        # Jeśli kopiec ma tylko 1 element
        if n == 1:
            return self.data[0]

        return max(self.data[n // 2:])


# ==========================================
# FUNKCJE DO TESTÓW EKSPERYMENTALNYCH
# ==========================================

def zapisz_wynik(operacja, eksperyment, typCiagu, n, czas_ms):
    """Zapisuje wyniki do odpowiedniego pliku z dopiskiem rodzaju operacji."""
    if eksperyment == 1:
        nazwa_pliku = f"wyniki/punkt1_eksperyment1_hmin_{operacja}.txt"
    elif eksperyment == 2:
        nazwa_pliku = f"wyniki/punkt1_eksperyment2_hmin_{operacja}.txt"
    else:
        return

    with open(nazwa_pliku, "a", encoding="utf-8") as f:
        f.write(f"Operacja: {operacja}; Typ: {typCiagu}; n: {n}; Czas: {czas_ms:.4f} ms;\n")


def wykonaj_pomiary(typCiagu, n, ciag, eksperyment):
    """
    Wykonuje 2 pomiary wymagane w instrukcji dla HMIN (Tworzenie i Max).
    """
    kopiec = HMIN()

    # 1. Pomiar czasu tworzenia Kopca Minimalnego
    start = time.perf_counter()

    kopiec.build_heap(ciag)

    stop = time.perf_counter()
    czas_tworzenia_ms = (stop - start) * 1000
    zapisz_wynik("tworzenie", eksperyment, typCiagu, n, czas_tworzenia_ms)

    # 2. Pomiar czasu wyszukiwania maksimum
    start = time.perf_counter()

    kopiec.find_max()

    stop = time.perf_counter()
    czas_max_ms = (stop - start) * 1000
    zapisz_wynik("max", eksperyment, typCiagu, n, czas_max_ms)