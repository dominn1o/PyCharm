def algorytm_zachlanny(b, elementy):
    # Sortowanie po współczynniku opłacalności
    sort_elementy = sorted(elementy, key=lambda x: x[2] / x[1] if x[1] > 0 else 0, reverse=True)

    calkowita_uzytecznosc = 0
    calkowity_rozmiar = 0
    ok_elementy = []

    for id_elem, rozmiar, uzytecznosc in sort_elementy:
        if calkowity_rozmiar + rozmiar <= b:
            calkowity_rozmiar += rozmiar
            calkowita_uzytecznosc += uzytecznosc
            ok_elementy.append(id_elem)

    return calkowita_uzytecznosc, calkowity_rozmiar, ok_elementy