def algorytm_dynamiczny(b, elementy):
    n = len(elementy)
    macierz_ad = [[0 for _ in range(b + 1)] for _ in range(n + 1)]

    # Wypełnianie tablicy
    for i in range(1, n + 1):
        id_elem, rozmiar, uzytecznosc = elementy[i - 1]
        for j in range(1, b + 1):
            if rozmiar <= j:
                macierz_ad[i][j] = max(macierz_ad[i - 1][j], macierz_ad[i - 1][j - rozmiar] + uzytecznosc)
            else:
                macierz_ad[i][j] = macierz_ad[i - 1][j]

    max_uzytecznosc = macierz_ad[n][b]
    obecna_pojemnosc = b
    ok_elementy = []
    calkowity_rozmiar = 0

    # Odtwarzanie wybranych elementów
    temp_uzytecznosc = max_uzytecznosc
    for i in range(n, 0, -1):
        if temp_uzytecznosc <= 0:
            break
        if temp_uzytecznosc == macierz_ad[i - 1][obecna_pojemnosc]:
            continue
        else:
            id_elem, rozmiar, uzytecznosc = elementy[i - 1]
            ok_elementy.append(id_elem)
            temp_uzytecznosc -= uzytecznosc
            obecna_pojemnosc -= rozmiar
            calkowity_rozmiar += rozmiar

    ok_elementy.reverse()
    return max_uzytecznosc, calkowity_rozmiar, ok_elementy