import time
import math


class Node:
    __slots__ = ['key', 'left', 'right']  # Optymalizacja zużycia pamięci i szybkości

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        """Iteracyjne wstawianie - bezpieczne dla dużych, posortowanych danych (brak błędu rekurencji)."""
        if self.root is None:
            self.root = Node(key)
            return

        curr = self.root
        while True:
            if key < curr.key:
                if curr.left is None:
                    curr.left = Node(key)
                    break
                curr = curr.left
            elif key > curr.key:
                if curr.right is None:
                    curr.right = Node(key)
                    break
                curr = curr.right
            else:
                break  # Zbiór: ignorujemy duplikaty

    def find_max(self):
        """Znajdowanie maksimum to po prostu zejście maksymalnie w prawo."""
        if self.root is None:
            return None
        curr = self.root
        while curr.right is not None:
            curr = curr.right
        return curr.key

    def balance_dsw(self):
        """Równoważenie drzewa algorytmem DSW (Day-Stout-Warren)."""
        if self.root is None:
            return

        # Faza 1: Tworzenie "kręgosłupa" (vine)
        pseudo_root = Node(0)
        pseudo_root.right = self.root
        tail = pseudo_root
        rest = tail.right
        node_count = 0

        while rest is not None:
            if rest.left is None:
                tail = rest
                rest = rest.right
                node_count += 1
            else:
                temp = rest.left
                rest.left = temp.right
                temp.right = rest
                rest = temp
                tail.right = temp

        # Faza 2: Transformacja kręgosłupa w idealnie zrównoważone drzewo
        leaves = node_count + 1 - 2 ** int(math.log2(node_count + 1))
        self._compress(pseudo_root, leaves)

        node_count -= leaves
        while node_count > 1:
            node_count //= 2
            self._compress(pseudo_root, node_count)

        self.root = pseudo_root.right

    def _compress(self, pseudo_root, count):
        """Funkcja pomocnicza dla DSW (wykonuje lewe rotacje)."""
        scanner = pseudo_root
        for _ in range(count):
            child = scanner.right
            scanner.right = child.right
            scanner = scanner.right
            child.right = scanner.left
            scanner.left = child


# ==========================================
# FUNKCJE DO TESTÓW EKSPERYMENTALNYCH
# ==========================================

def zapisz_wynik(operacja, eksperyment, typCiagu, n, czas_ms):
    """Zapisuje wyniki do odpowiedniego pliku z dopiskiem rodzaju operacji."""
    if eksperyment == 1:
        nazwa_pliku = f"wyniki/punkt1_eksperyment1_bst_{operacja}.txt"
    elif eksperyment == 2:
        nazwa_pliku = f"wyniki/punkt1_eksperyment2_bst_{operacja}.txt"

    with open(nazwa_pliku, "a", encoding="utf-8") as f:
        # Zapis zgodny z Twoim wzorem, wzbogacony o nazwę operacji
        f.write(f"Operacja: {operacja}; Typ: {typCiagu}; n: {n}; Czas: {czas_ms:.4f} ms;\n")


def wykonaj_pomiary(typCiagu, n, ciag, eksperyment):
    """
    Funkcja główna wołana z zewnętrznego skryptu testującego.
    Wykonuje 3 pomiary wymagane w instrukcji  i od razu zapisuje je do plików.
    """
    drzewo = BST()

    # 1. Pomiar czasu tworzenia drzewa
    start = time.perf_counter()
    for element in ciag:
        drzewo.insert(element)
    stop = time.perf_counter()
    czas_tworzenia_ms = (stop - start) * 1000
    zapisz_wynik("tworzenie", eksperyment, typCiagu, n, czas_tworzenia_ms)

    # 2. Pomiar czasu wyszukiwania maksimum
    start = time.perf_counter()
    drzewo.find_max()
    stop = time.perf_counter()
    czas_max_ms = (stop - start) * 1000
    zapisz_wynik("max", eksperyment, typCiagu, n, czas_max_ms)

    # 3. Pomiar czasu równoważenia drzewa (DSW)
    start = time.perf_counter()
    drzewo.balance_dsw()
    stop = time.perf_counter()
    czas_balans_ms = (stop - start) * 1000
    zapisz_wynik("rownowazenie", eksperyment, typCiagu, n, czas_balans_ms)