import time


class wezelAVL:
    __slots__ = ['key', 'left', 'right']  # Optymalizacja zużycia pamięci

    def __init__(self, klucz):
        self.key = klucz
        self.left = None
        self.right = None


class AVL:
    def __init__(self):
        self.root = None

    def buduj_z_bisekcji(self, tablica):
        """Optymalne budowanie z posortowanej tablicy (bez kopiowania list)."""

        def bisekcja(start, end):
            if start > end:
                return None

            mid = (start + end) // 2
            wezel = wezelAVL(tablica[mid])

            wezel.left = bisekcja(start, mid - 1)
            wezel.right = bisekcja(mid + 1, end)

            return wezel

        self.root = bisekcja(0, len(tablica) - 1)

    def find_max(self):
        """Znajdowanie maksimum to proste zejście maksymalnie w prawo."""
        if self.root is None:
            return None
        curr = self.root
        while curr.right is not None:
            curr = curr.right
        return curr.key


# ==========================================
# FUNKCJE DO TESTÓW EKSPERYMENTALNYCH
# ==========================================

def zapisz_wynik(operacja, eksperyment, typCiagu, n, czas_ms):
    """Zapisuje wyniki do odpowiedniego pliku z dopiskiem rodzaju operacji."""
    if eksperyment == 1:
        nazwa_pliku = f"wyniki/punkt1_eksperyment1_avl_{operacja}.txt"
    elif eksperyment == 2:
        nazwa_pliku = f"wyniki/punkt1_eksperyment2_avl_{operacja}.txt"
    else:
        return

    with open(nazwa_pliku, "a", encoding="utf-8") as f:
        f.write(f"Operacja: {operacja}; Typ: {typCiagu}; n: {n}; Czas: {czas_ms:.4f} ms;\n")


def wykonaj_pomiary(typCiagu, n, ciag, eksperyment):
    """
    Wykonuje 2 pomiary wymagane w instrukcji dla AVL (Tworzenie i Max).
    """
    drzewo = AVL()

    # 1. Pomiar czasu tworzenia drzewa AVL
    start = time.perf_counter()

    # Bisekcja działa tylko na posortowanych danych!
    # Używamy wbudowanego algorytmu Timsort O(n log n).
    ciag.sort()
    drzewo.buduj_z_bisekcji(ciag)

    stop = time.perf_counter()
    czas_tworzenia_ms = (stop - start) * 1000
    zapisz_wynik("tworzenie", eksperyment, typCiagu, n, czas_tworzenia_ms)

    # 2. Pomiar czasu wyszukiwania maksimum
    start = time.perf_counter()

    drzewo.find_max()

    stop = time.perf_counter()
    czas_max_ms = (stop - start) * 1000
    zapisz_wynik("max", eksperyment, typCiagu, n, czas_max_ms)