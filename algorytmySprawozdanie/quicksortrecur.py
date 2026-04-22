import time
import sys
sys.setrecursionlimit(100000)

def quicksort(typCiagu, n, ciag, eksperyment):
    A = ciag[:]
    porownania = 0
    zamiany_elementow = 0

    def placement(lista, low, high):
        nonlocal porownania, zamiany_elementow
        pivot = lista[low]
        # print(f"Aktualny Pivot: {pivot} dla {lista}")

        i = low
        for j in range(low + 1, high + 1):
            porownania += 1
            # >= dla sortowania malejącego
            if lista[j] >= pivot:
                i += 1
                if i != j:
                    lista[i], lista[j] = lista[j], lista[i]
                    zamiany_elementow += 1

        #wstawienie pivota w odpowiednie miejsce
        if low != i:
            lista[low], lista[i] = lista[i], lista[low]
            zamiany_elementow += 1
        return i

    def quick_sort_recursive(lista, low, high):
        if low < high:
            ltemp = placement(lista, low, high)
            quick_sort_recursive(lista, low, ltemp - 1)
            quick_sort_recursive(lista, ltemp + 1, high)

    start = time.perf_counter()

    if n > 1:
        quick_sort_recursive(A, 0, n - 1)

    end = time.perf_counter()
    czas_ms = (end - start) * 1000

    """
    print(f"---")
    print(f"Czas sortowania: {(end - start) * 1e3:.3f} ms")
    print(f"Liczba porównań: {porownania}")
    print(f"Liczba zamian: {zamiany_elementow}")
    print("Posortowany ciąg: ", A)
    """

    if eksperyment == 1:
        # Spójny format zapisu (taki sam jak w poprzednich algorytmach)
        with open("wyniki/punkt1_eksperyment1_quickrecursive.txt", "a", encoding="utf-8") as f:
            f.write(f"Typ: {typCiagu}; n: {n}; Czas: {czas_ms:.4f} ms;\n")
    elif eksperyment == 2:
        with open("wyniki/punkt1_eksperyment2_quickrecursive.txt", "a", encoding="utf-8") as f:
            f.write(f"Typ: {typCiagu}; n: {n}; Czas: {czas_ms:.4f} ms;\n")
    elif eksperyment == 0:
        pass

    return A


"""
#pobieranie danych
n = int(input("Ile elementów w ciągu (<= 12): "))
while n > 12 or n < 0:
    n = int(input("wartość od 0 do 12: "))

A = []
if n > 0:
    print("Wypisz po kolei nieposortowane elementy: ")
    for i in range(n):
        A.append(int(input(f"Element {i + 1}: ")))

print("Ciąg: ",A)

quicksort("a",n,A,0)
"""