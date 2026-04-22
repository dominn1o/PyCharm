import math
import time


class Hmin:
    def __init__(self):
        self.data = []

    @staticmethod
    def parent(i):
        return (i - 1) // 2

    @staticmethod
    def left(i):
        return 2 * i + 1

    @staticmethod
    def right(i):
        return 2 * i + 2

    def heapify(self, i):
        #sift down
        l = self.left(i)
        r = self.right(i)
        imin = i

        if l < len(self.data) and self.data[l] < self.data[imin]:
            imin = l

        if r < len(self.data) and self.data[r] < self.data[imin]:
            imin = r

        if imin != i:
            self.data[i], self.data[imin] = self.data[imin], self.data[i]
            self.heapify(imin)

    def insert(self, val):
        #sift up
        self.data.append(val)
        i = len(self.data) - 1
        while i > 0 and self.data[self.parent(i)] > self.data[i]:
            self.data[i], self.data[self.parent(i)] = self.data[self.parent(i)], self.data[i]
            i = self.parent(i)

    def min(self):
        #wartośc ścieżka porównania
        return self.data[0], [self.data[0]], 0

    def max(self):
        start_index = len(self.data) // 2 #połowa tablicy, maksimum jest liściem
        max_val = self.data[start_index]
        max_idx = start_index

        comparisons = 0

        for i in range(start_index + 1, len(self.data)):
            comparisons += 1
            if self.data[i] > max_val:
                max_val = self.data[i]
                max_idx = i

        path = [] #ścieżka do maksimum
        curr = max_idx
        while curr >= 0:
            path.append(self.data[curr])
            if curr == 0:
                break

            curr = self.parent(curr)

        return max_val, path[::-1], comparisons

    def search(self, x):
        start_time = time.perf_counter()
        try:
            idx = self.data.index(x)
        except ValueError:
            return None

        level = int(math.log2(idx + 1))

        level_start = 2 ** level - 1
        level_end = min(2 ** (level + 1) - 1, len(self.data))
        elements_on_level = self.data[level_start:level_end]

        def height(i):
            if i >= len(self.data):
                return -1

            return 1 + max(height(self.left(i)), height(self.right(i)))

        def pre_order(i, result):
            if i < len(self.data):
                result.append(self.data[i])
                pre_order(self.left(i), result)
                pre_order(self.right(i), result)

            return result
        end_time = time.perf_counter()

        return {
            "czas wykonania operacji": f"{(end_time - start_time):.8f} sekund",
            "poziom": level,
            "elementy na tym samym poziomie": elements_on_level,
            "wysokość poddrzewa": height(idx),
            "pre order poddrzewa": pre_order(idx, [])
        }

    def decreasing(self):
        temp_data = self.data[:]
        sorted = []

        #heapsort
        while len(self.data) > 0:
            sorted.append(self.data[0])
            self.data[0] = self.data[-1]
            self.data.pop()

            if len(self.data) > 0:
                self.heapify(0)

        self.data = temp_data

        return sorted[::-1]

    def delete(self, x, subtree=False):
        try:
            idx = self.data.index(x)
        except ValueError:
            return

        if subtree:
            #indeksy potomków x
            def indices(i, ids):
                if i < len(self.data):
                    ids.append(i)
                    indices(self.left(i), ids)
                    indices(self.right(i), ids)

            removed = []
            indices(idx, removed)
            #od końca by nie zmieniać adresów
            for i in sorted(removed, reverse=True):
                self.data.pop(i)

            #od rodzica do korzenia
            for i in range(len(self.data)//2, -1, -1):
                self.heapify(i)
        else:
            self.data[idx] = self.data[-1]
            self.data.pop()

            if idx < len(self.data):
                parent_idx = self.parent(idx)
                #up: jeżeli nie jest korzeniem i jest mniejszy niż rodzice
                if idx > 0 and self.data[idx] < self.data[parent_idx]:
                    curr = idx
                    while curr > 0 and self.data[self.parent(curr)] > self.data[curr]:
                        self.data[curr], self.data[self.parent(curr)] = self.data[self.parent(curr)], self.data[curr]
                        curr = self.parent(curr)

                #down
                else:
                    self.heapify(idx)
        return True

    def wyswietlDrzewo(self, index=0, prefix="", jest_ostatni=True, nazwa_relacji="root"):
        if index >= len(self.data):
            return

        #symbole gałęzi
        symbol = "└── " if jest_ostatni else "├── "

        #wyswietlenie aktualnego wezla, czy to L czy R dziecko
        relacja = f"[{nazwa_relacji}] " if nazwa_relacji != "root" else ""
        print(f"{prefix}{symbol}{relacja}{self.data[index]}")

        nowy_prefix = prefix + ("    " if jest_ostatni else "│   ")

        #tworzymy listę dzieci
        dzieci = []
        l = self.left(index)
        r = self.right(index)

        if l < len(self.data):
            dzieci.append((l, "L"))
        if r < len(self.data):
            dzieci.append((r, "R"))

        #rekurencyjnie wstaw dzieci
        for i, (dziecko_idx, typ) in enumerate(dzieci):
            czy_ostatnie_dziecko = (i == len(dzieci) - 1)
            self.wyswietlDrzewo(dziecko_idx, nowy_prefix, czy_ostatnie_dziecko, typ)
    pass

heap = Hmin()

def different_elements(list):
    return len(set(list)) == len(list)

while True:
    print("\n" + "=" * 50)
    print("MENU KOPCA MINIMALNEGO (HMIN)")
    print("1. Utworzenie struktury z ciągu")
    print("2. Wyszukanie minimum i maksimum")
    print("3. Wyszukanie elementu. Podanie poziomu, elementów na poziomie, wysokości poddrzewa, poddrzewa w pre-order")
    print("4. Wypisanie wszystkich elementów w porządku malejącym")
    print("5. Usunięcie elementu (pojedyńczo lub z poddrzewem)")
    print("6. Wyświetl strukturę drzewa")
    print("7. Zakończ program")
    print("=" * 50)

    choice = input("\nWybierz opcję (1-7): ").strip()

    if choice == '1':

        n = int(input("\nIle elementów w ciągu (<= 12): "))
        while n > 12 or n < 0:
            n = int(input("Wpisz wartość w przedziale (<=12): "))

        elements = []
        if n > 0:
            print("Wypisz po kolei elementy: ")
            for i in range(n):
                elements.append(int(input(f"Element {i + 1}: ")))

        if not different_elements(elements):
            print("Elementy się powtarzają. Spróbuj ponownie")
            continue

        heap.data = []

        start_time = time.perf_counter()
        for e in elements:
            heap.insert(e)
        end_time = time.perf_counter()

        num_nodes = len(heap.data)
        if num_nodes > 0:
            height = int(math.log2(num_nodes))
        else:
            height = 0

        print(f"\nUTWORZONO STRUKTURĘ:")
        heap.wyswietlDrzewo()
        print(f"Czas wykonania operacji: {(end_time - start_time):.8f} sekund")
        print(f"Liczba węzłów: {num_nodes}")
        print(f"Wysokość struktury: {height}")

    elif choice == '2':
        if not heap.data:
            print("Kopiec jest pusty")
            continue

        start_time = time.perf_counter()
        min_val, min_path, min_comp = heap.min()
        max_val, max_path, max_comp = heap.max()
        end_time = time.perf_counter()

        print(f"\nMINIMUM I MAKSIMUM")
        print(f"Czas wykonania operacji: {(end_time - start_time):.8f} sekund")
        print(f"MINIMUM: {min_val}")
        print(f"Ścieżka do minimum: {min_path}")
        print(f"Liczba porównań kluczy: {min_comp}")
        print(f"MAKSIMUM: {max_val}")
        print(f"Ścieżka do maksimum: {max_path}")
        print(f"Liczba porównań kluczy: {max_comp}")

    elif choice == '3':
        if not heap.data:
            print("Kopiec jest pusty")
            continue

        try:
            x = int(input("Podaj klucz do wyszukania: "))

        except ValueError:
            print("Podano nieprawidłową wartość.")
            continue

        result = heap.search(x)

        print(f"\nWYSZKUKIWANY ELEMENT")

        if result:
            for key, value in result.items():
                print(f"- {key}: {value}")
        else:
            print("Brak podanego elementu w strukturze.")

    elif choice == '4':
        if not heap.data:
            print("Kopiec jest pusty")
            continue

        start_time = time.perf_counter()
        decreasing_list = heap.decreasing()
        end_time = time.perf_counter()

        print(f"\nELEMENTY W PORZĄDKU MALEJĄCYM")
        print(f"Czas wykonania operacji: {(end_time - start_time):.8f} sekund")
        print(f"Ciąg: {decreasing_list}")

    elif choice == '5':
        if not heap.data:
            print("Kopiec jest pusty")
            continue

        try:
            x = int(input("Podaj klucz do usunięcia: "))
        except ValueError:
            print("Podano nieprawidłową wartość.")
            continue

        sub_input = input("Usunąć wraz z całym poddrzewem? (t/n): ").strip().lower()
        remove_subtree = (sub_input == 't')

        start_time = time.perf_counter()
        success = heap.delete(x, subtree=remove_subtree)
        end_time = time.perf_counter()

        print(f"\nUSUWANIE ELEMENTU")
        print(f"Czas wykonania operacji: {(end_time - start_time):.8f} sekund")
        if success:
            print("Operacja zakończona sukcesem.")
        else:
            print("Nie znaleziono takiego elementu.")

    elif choice == '6':
        if not heap.data:
            print("Kopiec jest pusty")
            continue

        print("\nSTRUKTURA DRZEWA: ")
        heap.wyswietlDrzewo()

    elif choice == '7':
        print("\nZamykanie programu...")
        break

    else:
        print("Nieznana opcja. Wybierz numer od 1 do 7")
