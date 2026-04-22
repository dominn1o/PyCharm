import time

def quicksortiter(typCiagu, n, ciag, eksperyment):
    A = ciag[:]
    porownania = 0
    zamiany_elementow = 0

    def partition(arr, low, high):
        nonlocal porownania, zamiany_elementow
        pivot = arr[low]
        i = low

        for j in range(low + 1, high + 1):
            porownania += 1
            # element >= od pivota dla sortowania malejącego
            if arr[j] >= pivot:
                i += 1
                if i != j:
                    arr[i], arr[j] = arr[j], arr[i]
                    zamiany_elementow += 1
            #print(f"  Partycja (pivot {pivot}): {arr}")

        if low != i:
            arr[low], arr[i] = arr[i], arr[low]
            zamiany_elementow += 1
        return i

    def quicksort_iter_logic(arr, low, high):
        stos = []
        stos.append((low, high))

        while len(stos) > 0:
            l, h = stos.pop()
            p = partition(arr, l, h)

            if p - 1 > l:
                stos.append((l, p - 1))
            if p + 1 < h:
                stos.append((p + 1, h))

    start = time.perf_counter()

    if n > 1:
        quicksort_iter_logic(A, 0, n - 1)

    end = time.perf_counter()
    czas_ms = (end - start) * 1000

    """
    print(f"---")
    print(f"Czas sortowania: {(end - start) * 1e3:.3f} ms")
    print(f"Liczba porównań: {porownania}")
    print(f"Liczba zamian: {zamiany_elementow}")
    print("Posortowane (malejąco): ", A)
    """

    if eksperyment == 1:
        with open("wyniki/punkt1_eksperyment1_quickiterative.txt", "a", encoding="utf-8") as f:
            f.write(f"Typ: {typCiagu}; n: {n}; Czas: {czas_ms:.4f} ms;\n")
    elif eksperyment == 2:
        with open("wyniki/punkt1_eksperyment2_quickiterative.txt", "a", encoding="utf-8") as f:
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

quicksortiter("a",n,A,0)
"""