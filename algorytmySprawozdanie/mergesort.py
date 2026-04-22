import time

def mergesort(typCiagu, n, ciag, eksperyment):
    A = ciag[:]
    porownania = 0
    liczba_scalen = 0

    def merge(l1, l2):
        nonlocal porownania, liczba_scalen
        liczba_scalen += 1
        rlist = []
        i = j = 0
        while i < len(l1) and j < len(l2):
            porownania += 1
            #warunek > dla sortowania malejącego
            if l1[i] > l2[j]:
                rlist.append(l1[i])
                i += 1
            else:
                rlist.append(l2[j])
                j += 1
        rlist.extend(l1[i:])
        rlist.extend(l2[j:])
        return rlist

    def merge_sort_recursive(lista):
        if len(lista) <= 1:
            return lista
        p = len(lista) // 2
        l1 = merge_sort_recursive(lista[:p])
        l2 = merge_sort_recursive(lista[p:])
        return merge(l1, l2)

    start = time.perf_counter()

    posortowana_lista = merge_sort_recursive(A)

    end = time.perf_counter()
    czas_ms = (end - start) * 1000

    """
    print(f"---")
    print(f"Czas sortowania: {czas_ms:.3f} ms")
    print(f"Liczba scaleń podzbiorów: {liczba_scalen}")
    print(f"Liczba porównań: {porownania}")
    print("Posortowany ciąg: ", posortowana_lista)
    """

    if eksperyment == 1:
        with open("wyniki/punkt1_eksperyment1_mergesort.txt", "a", encoding="utf-8") as f:
            f.write(f"Typ: {typCiagu}; n: {n}; Czas: {czas_ms:.4f} ms;\n")
    elif eksperyment == 2:
        with open("wyniki/punkt1_eksperyment2_mergesort.txt", "a", encoding="utf-8") as f:
            f.write(f"Typ: {typCiagu}; n: {n}; Czas: {czas_ms:.4f} ms;\n")
    elif eksperyment == 0:
        pass

    return posortowana_lista

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

mergesort("a",n,A,0)
"""