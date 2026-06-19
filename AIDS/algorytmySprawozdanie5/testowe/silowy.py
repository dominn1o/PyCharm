def algorytm_silowy(b, elementy):
    n = len(elementy)
    najlepsza_uzytecznosc = -1
    najlepszy_rozmiar = 0
    ostateczne_id = []

    sprawdzone_konfiguracje = 2 ** n

    # Iteracja po wszystkich kombinacjach (0 do 2^n - 1)
    for i in range(sprawdzone_konfiguracje):
        obecny_rozmiar = 0
        obecna_uzytecznosc = 0
        wybrane_id = []

        for j in range(n):
            if (i >> j) & 1:  # Jeśli j-ty bit jest zapalony
                id_elem, rozmiar, uzytecznosc = elementy[j]
                wybrane_id.append(id_elem)
                obecny_rozmiar += rozmiar
                obecna_uzytecznosc += uzytecznosc

        # Zapisz, jeśli mieści się w plecaku i jest lepsze
        if obecny_rozmiar <= b:
            if obecna_uzytecznosc > najlepsza_uzytecznosc:
                najlepsza_uzytecznosc = obecna_uzytecznosc
                najlepszy_rozmiar = obecny_rozmiar
                ostateczne_id = wybrane_id

    return najlepsza_uzytecznosc, najlepszy_rozmiar, ostateczne_id