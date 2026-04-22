import time

def shellsort(typCiagu, n, ciag, eksperyment):
    A = ciag[:]
    porownania = 0
    zamiany_elementow = 0

    #generowanie przyrostów Knutha
    P = []
    h = 1
    while h < n:
        P.append(h)
        h = 3 * h + 1
    P = P[::-1]

    start = time.perf_counter()

    for p in P:
        for i in range(p, n):
            key = A[i]
            j = i

            #  warunek A[j - p] < key dla sortowania malejącego
            while j >= p:
                porownania += 1
                if A[j - p] < key:
                    A[j] = A[j - p]
                    zamiany_elementow += 1
                    j -= p
                else:
                    break
            A[j] = key
            zamiany_elementow += 1

    end = time.perf_counter()
    czas_ms = (end - start) * 1000

    """
    print(f"---")
    print(f"Czas sortowania: {(end - start) * 1e3:.3f} ms")
    print(f"Liczba porównań: {porownania}")
    print(f"Liczba zamian (przesunięć): {zamiany_elementow}")
    print("Posortowany ciąg: ", A)
    """

    if eksperyment == 1:
        with open("wyniki/punkt1_eksperyment1_shellsort.txt", "a", encoding="utf-8") as f:
            f.write(f"Typ: {typCiagu}; n: {n}; Czas: {czas_ms:.4f} ms;\n")
    elif eksperyment == 2:
        with open("wyniki/punkt1_eksperyment2_shellsort.txt", "a", encoding="utf-8") as f:
            f.write(f"Typ: {typCiagu}; n: {n}; Czas: {czas_ms:.4f} ms;\n")
    elif eksperyment == 0:
        pass

    return A


"""
#data input
n = int(input("Ile elementów w ciągu (<= 12): "))
while n > 12 or n < 0:
    n = int(input("Wpisz wartość w przedziale (0-12): "))

A = []
if n > 0:
    print("Wypisz po kolei nieposortowane elementy: ")
    for i in range(n):
        A.append(int(input(f"Element {i + 1}: ")))

print("Ciąg wejściowy: ", A)

shellsort("a", n, A,0)
"""