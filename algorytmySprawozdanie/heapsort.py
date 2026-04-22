import time

def heapsort(typCiagu, n, ciag,eksperyment):
    A = ciag
    porownania = 0
    zamiany_elementow = 0

    def heapify(A, n, i):
        nonlocal porownania, zamiany_elementow
        smallest = i
        lewy = 2 * i + 1
        prawy = 2 * i + 2

        #szukamy najmniejszego elementu wśród rodzica i dzieci
        if lewy < n:
            porownania += 1
            if A[lewy] < A[smallest]:
                smallest = lewy

        if prawy < n:
            porownania += 1
            if A[prawy] < A[smallest]:
                smallest = prawy

        if smallest != i:
            A[i], A[smallest] = A[smallest], A[i]
            zamiany_elementow += 1
            heapify(A, n, smallest)

    start = time.perf_counter()

    #budowanie kopca min-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(A, n, i)

    #wyjmowanie elementów - najmniejsze trafiają na koniec (tworzy ciag malejacy)
    for i in range(n - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        zamiany_elementow += 1
        heapify(A, i, 0)

    end = time.perf_counter()
    czas_ms = (end - start) * 1000

    """
    print(f"---")
    print(f"Czas sortowania: {(end - start) * 1e3:.3f} ms")
    print(f"Liczba porównań: {porownania}")
    print(f"Liczba zamian: {zamiany_elementow}")
    print("Posortowane: ",A)
    """

    if eksperyment == 1:
        with open("wyniki/punkt1_eksperyment1_heapsort.txt", "a", encoding="utf-8") as f:
            f.write(f"Typ: {typCiagu}; n: {n}; Czas: {czas_ms:.4f} ms;\n")
    elif eksperyment == 2:
        with open("wyniki/punkt1_eksperyment2_heapsort.txt", "a", encoding="utf-8") as f:
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

heapsort("a",n,A,0)
"""