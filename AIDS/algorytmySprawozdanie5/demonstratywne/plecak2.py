import time
import random


def algorytm_dynamiczny(b, elementy):
    n = len(elementy)
    macierz_ad = [[0 for _ in range(b + 1)] for _ in range(n + 1)]
    sygnatury = []

    for i in range(1, n + 1):
        id, rozmiar, uzytecznosc = elementy[i - 1]
        for j in range(1, b + 1):
            if rozmiar <= j:
                macierz_ad[i][j] = max(macierz_ad[i - 1][j], macierz_ad[i - 1][j - rozmiar] + uzytecznosc)
                if macierz_ad[i - 1][j] == macierz_ad[i - 1][j - rozmiar] + uzytecznosc and macierz_ad[i][j] > 0:
                    sygnatury.append(f"{i}-{j}")
            else:
                macierz_ad[i][j] = macierz_ad[i - 1][j]

    max_uzytecznosc = macierz_ad[n][b]
    obecna_pojemnosc = b
    ok_elementy = []
    calkowity_rozmiar = 0

    for i in range(n, 0, -1):
        if max_uzytecznosc <= 0:
            break
        if max_uzytecznosc == macierz_ad[i - 1][obecna_pojemnosc]:
            continue
        else:
            id, rozmiar, uzytecznosc = elementy[i - 1]
            ok_elementy.append(id)
            max_uzytecznosc -= uzytecznosc
            obecna_pojemnosc -= rozmiar
            calkowity_rozmiar += rozmiar

    ok_elementy.reverse()

    return macierz_ad[n][b], calkowity_rozmiar, ok_elementy, sygnatury, macierz_ad


def algorytm_zachlanny(b, elementy):
    sort_elementy = sorted(elementy, key=lambda x: x[2] / x[1] if x[1] > 0 else 0, reverse=True)

    calkowita_uzytecznosc = 0
    calkowity_rozmiar = 0
    ok_elementy = []
    log = []

    for id, rozmiar, uzytecznosc in sort_elementy:
        if calkowity_rozmiar + rozmiar <= b:
            calkowity_rozmiar += rozmiar
            calkowita_uzytecznosc += uzytecznosc
            ok_elementy.append(id)
            log.append(f"Dodano {id}")
        else:
            log.append(f"Odrzucono {id}")

    return calkowita_uzytecznosc, calkowity_rozmiar, ok_elementy, log


def wczytaj_z_pliku():
    filename = input("Podaj nazwę pliku: ").strip()
    items = []

    with open(filename, 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file if line.strip()]

        first_line = lines[0].split()
        n = int(first_line[0])
        capacity = int(first_line[1])

        item_id = 1
        for line in lines[1:]:
            rozmiar, uzytecznosc = map(int, line.split())
            items.append((item_id, rozmiar, uzytecznosc))
            item_id += 1

    return capacity, items


def generuj_losowe(n):
    capacity = random.randint(10, 50)
    items = []

    for item_id in range(1, n + 1):
        rozmiar = random.randint(1, 10)
        uzytecznosc = random.randint(1, 20)
        items.append((item_id, rozmiar, uzytecznosc))

    return capacity, items


if __name__ == "__main__":
    wybor = input("Wybierz rodzaj danych (1 - plik, 2 - losowe): ").strip()

    if wybor == '1':
        pojemnosc_ladunkowa, wyposazenie = wczytaj_z_pliku()
    elif wybor == '2':
        n_losowe = int(input("Podaj liczbę elementów do wygenerowania: "))
        pojemnosc_ladunkowa, wyposazenie = generuj_losowe(n_losowe)
        print("Wygenerowano dane.")
    else:
        print("Nieznana opcja.")
        exit()

    print(f"\nDostępna pojemność: {pojemnosc_ladunkowa}")
    print(f"Wczytano {len(wyposazenie)} elementów.")

    print("\nWyposażenie:")
    for id_elem, rozmiar, uzytecznosc in wyposazenie:
        print(f"ID: {id_elem:2} Rozmiar: {rozmiar:2} Użyteczność: {uzytecznosc:2}")

    while True:
        demo = input("Czy tryb demo? (y/n) ").strip().lower()
        if demo == "y":
            tryb_demo = True
            break
        elif demo == "n":
            tryb_demo = False
            break
        else:
            print("Nie ma takiej opcji. Wpisz y lub n.")

    start_time = time.time()
    ad_utility, ad_size, ad_items, sygn, macierz = algorytm_dynamiczny(pojemnosc_ladunkowa, wyposazenie)
    ad_time = time.time() - start_time

    print("\n--- ALGORYTM PROGRAMOWANIA DYNAMICZNEGO (AD) ---")
    print(f"Czas obliczeń:        {ad_time:.6f} sekund")
    print(f"Łączna użyteczność:   {ad_utility}")
    print(f"Sumaryczny rozmiar:   {ad_size}")
    print(f"Wybrane elementy ID:  {ad_items}")

    if tryb_demo:
        print("Tabela programowania dynamicznego:")
        for wiersz in macierz:
            print(wiersz)
        print(f"Sygnatury podproblemów mających więcej niż jedno rozwiązanie: {sygn}")

    start_time = time.time()
    az_utility, az_size, az_items, az_log = algorytm_zachlanny(pojemnosc_ladunkowa, wyposazenie)
    az_time = time.time() - start_time

    print("\n--- ALGORYTM ZACHŁANNY (AZ) ---")
    print(f"Czas obliczeń:        {az_time:.6f} sekund")
    print(f"Łączna użyteczność:   {az_utility}")
    print(f"Sumaryczny rozmiar:   {az_size}")
    print(f"Wybrane elementy ID:  {az_items}")

    if tryb_demo:
        print("Kolejne decyzje podejmowane przez algorytm zachłanny:")
        for log in az_log:
            print(log)

    print("")
    opt = input("Sprawdzić, czy rozwiązanie AZ jest optymalne? (y)").strip().lower()
    if opt == "y":
        if az_utility == ad_utility:
            print("Rozwiązanie algorytmu zachłannego (AZ) JEST optymalne.")
        else:
            print("Rozwiązanie algorytmu zachłannego (AZ) NIE JEST optymalne.")