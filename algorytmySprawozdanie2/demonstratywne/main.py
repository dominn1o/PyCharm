from algorytmySprawozdanie import mergesort as mergesort
import time
import AVL
import BST
import HMIN

# Główne zmienne przechowujące stan programu
program_dziala = True
wybrana_struktura = 0  # 1-BST, 2-AVL, 3-HMIN
dane = []
korzen = None

while program_dziala:
    print("\n===============================")
    print("=== MENU GŁÓWNE - WYBÓR STRUKTURY ===")
    print("1. Drzewo BST")
    print("2. Drzewo AVL (bisekcja)")
    print("3. Kopiec minimalny (HMIN)")
    print("0. Wyjście z programu")
    print("===============================")

    wybor = input("Wybierz opcję: ")

    if wybor == "0":
        print("Zamykanie programu...")
        program_dziala = False
        break

    elif wybor in ["1", "2", "3"]:
        wybrana_struktura = int(wybor)
        # WPROWADZANIE DANYCH
        print("\n--- wpisywanie danych ---")
        # Pobieranie liczby n z kontrolą zakresu
        n = int(input("Ile elementów w ciągu (<= 12): "))
        while n > 12 or n < 0:
            n = int(input("Wartość od 0 do 12: "))
        dane = []  # Twoja lista A
        if n > 0:
            print("Wypisz po kolei nieposortowane elementy: ")
            i = 0
            while i < n:
                element = int(input(f"Element {i + 1}: "))
                # Sprawdzenie unikalności (opcjonalne, ale ważne w tym zadaniu)
                if element in dane:
                    print("Błąd: Ta liczba już została podana! Podaj inną.")
                else:
                    dane.append(element)
                    i += 1

    # --- KONSTRUKCJA STRUKTURY ---
    if wybrana_struktura == 1:
        korzen = None  # Resetujemy stare drzewo
        for liczba in dane:
            korzen = BST.wstaw(korzen, liczba)
    elif wybrana_struktura == 2:
        korzen = None  # Resetujemy stare drzewo
        elementy = mergesort.mergesort("a", n, dane,0)
        elementy = elementy[::-1]
        korzen = AVL.wstaw(elementy)
    # --- ETAP: MENU OPERACJI DLA STRUKTURY ---
    w_menu_struktury = True
    while w_menu_struktury:
        nazwa = ""
        if wybrana_struktura == 1:
            nazwa = "BST"
        elif wybrana_struktura == 2:
            nazwa = "AVL"
        elif wybrana_struktura == 3:
            nazwa = "HMIN"

        print(f"\n--- WYBRANA STRUKTURA: {nazwa} ---")
        print(f"Dane wejściowe: {dane}")
        print("-------------------------------")
        print(f"WIZUALIZACJA DRZEWA {nazwa}")
        BST.wyswietlDrzewo(korzen)
        print(f"Statystyki: Wysokość: {BST.wysokosc(korzen)}, Liczba węzłów: {len(dane)}")
        print("-------------------------------")

        print("1. Wypisz najmniejszy i największy element")
        print("2. Wyszukaj element (klucz i droga)")
        print("3. Wypisz elementy malejąco")
        print("4. Usuń element")
        if wybrana_struktura == 1:
            print("5. Równoważenie drzewa BST (Algorytm DSW)")
        print("0. Powrót do menu głównego")

        operacja = input("\nWybierz operację: \n")

        if operacja == "0":
            w_menu_struktury = False

        elif operacja == "1":
            # Wypisz najmniejszy i największy
            if wybrana_struktura == 1:
                # Najmniejszy
                minimum, sciezka_min, por_min, czas_min = BST.najmniejszyEl(korzen)
                if minimum is not None:
                    print(f"\n[MIN] Element: {minimum}")
                    print(f"Ścieżka: {sciezka_min}")
                    print(f"Porównania: {por_min}, Czas: {czas_min:.4f} ms")

                print("-" * 20)

                # Największy
                maximum, sciezka_max, por_max, czas_max = BST.najwiekszyEl(korzen)
                if maximum is not None:
                    print(f"[MAX] Element: {maximum}")
                    print(f"Ścieżka: {sciezka_max}")
                    print(f"Porównania: {por_max}, Czas: {czas_max:.4f} ms")

            elif wybrana_struktura == 2:
                # Najmniejszy
                minimum, sciezka_min, por_min, czas_min = AVL.najmniejszyEl(korzen)
                if minimum is not None:
                    print(f"\n[MIN] Element: {minimum}")
                    print(f"Ścieżka: {sciezka_min}")
                    print(f"Porównania: {por_min}, Czas: {czas_min:.4f} ms")

                print("-" * 20)

                # Największy
                maximum, sciezka_max, por_max, czas_max = AVL.najwiekszyEl(korzen)
                if maximum is not None:
                    print(f"[MAX] Element: {maximum}")
                    print(f"Ścieżka: {sciezka_max}")
                    print(f"Porównania: {por_max}, Czas: {czas_max:.4f} ms")

            elif wybrana_struktura == 3:
                print("\n[HMIN] Min to korzeń (A[0]), Max wymaga przeszukania liści tablicy.")

            input("\nkliknij enter..")

        elif operacja == "2":
            # Wyszukaj element (klucz i droga)
            klucz = int(input("Podaj klucz do znalezienia: "))

            if wybrana_struktura == 1:
                BST.znajdzEl(korzen, klucz)

            elif wybrana_struktura == 2:
                AVL.znajdzEl(korzen, klucz)

            elif wybrana_struktura == 3:
                print(f"\n[HMIN] Szukam {klucz} w tablicy i podaję jego 'dzieci' w strukturze kopca.")

            input("\nkliknij enter..")

        elif operacja == "3":
            # Wypisz elementy malejąco

            if wybrana_struktura == 1:
                if korzen is None:
                    print("Drzewo jest puste")
                else:
                    print("\nElementy w kolejności malejącej: ", end="")

                    start = time.perf_counter()

                    elementyMalejaco, porownania = BST.wypiszMalejaco(korzen)

                    end = time.perf_counter()
                    czas_ms = (end - start) * 1000

                    print(elementyMalejaco)
                    print(f"\nPosortowano, czas działania operacji: {czas_ms:.4f} ms")
                    print(f"Liczba wykonanych porównań kluczy: {porownania}")

                    print()

            elif wybrana_struktura == 2:

                if korzen is None:
                    print("Drzewo jest puste")
                else:
                    print("\nElementy w kolejności malejącej: ")

                    start = time.perf_counter()

                    elementyMalejaco, porownania = AVL.wypiszMalejaco(korzen)

                    end = time.perf_counter()
                    czas_ms = (end - start) * 1000

                    print(elementyMalejaco)
                    print(f"\nPosortowano, czas działania operacji: {czas_ms:.4f} ms")
                    print(f"Liczba wykonanych porównań kluczy: {porownania}")


                    print()

            elif wybrana_struktura == 3:
                print("\nElementy w kolejnosci malejącej: ")

            input("\nkliknij enter..")

        elif operacja == "4":
            # Usuń element (z dodatkowym wyborem)
            klucz = int(input("Podaj klucz do usunięcia: "))
            print("Wybierz tryb usuwania:")
            print("a) Usuń tylko ten węzeł (i przepnij dzieci)")
            print("b) Usuń cały węzeł wraz z jego poddrzewem")
            tryb = input("Wybór (a/b): ")

            if wybrana_struktura == 1:
                print(f"\n Usuwanie {klucz} w trybie {tryb}.")

                start = time.perf_counter()

                korzen = BST.usunEL(korzen, klucz, tryb)

                end = time.perf_counter()
                czas_ms = (end - start) * 1000
                print(f"\nCzas działania operacji: {czas_ms:.4f} ms")

                BST.wyswietlDrzewo(korzen)
            elif wybrana_struktura == 2:

                print(f"\n Usuwanie {klucz} w trybie {tryb}.")

                start = time.perf_counter()

                korzen = AVL.usunEL(korzen, klucz, tryb)

                end = time.perf_counter()
                czas_ms = (end - start) * 1000
                print(f"\nCzas działania operacji: {czas_ms:.4f} ms")

                AVL.wyswietlDrzewo(korzen)

            elif wybrana_struktura == 3:
                print(f"\nUsuwanie {klucz} w trybie {tryb}")

            input("\nkliknij enter..")

        elif operacja == "5" and wybrana_struktura == 1:
            # Równoważenie BST
            print("\nRownoważenie drzewa algorytmem DSW")
            print("Pre-order przed DSW: ",end="")
            BST.wypiszPreOrder(korzen)

            start = time.perf_counter()

            porownaniaDSW, korzen = BST.rownowazenieDSW(korzen)

            end = time.perf_counter()
            czas_ms = (end - start) * 1000
            print(f"\nZrownowazono drzewo, czas działania operacji: {czas_ms:.4f} ms")
            print(f"\nLiczba wykonanych porównań kluczy/wskaźników: {porownaniaDSW}")

            print("\nPre-order po DSW: ",end="")
            BST.wypiszPreOrder(korzen)
            print("\n")
            BST.wyswietlDrzewo(korzen)

            input("\nkliknij enter..")

        else:
            print("Niepoprawna opcja lub operacja niedostępna dla tej struktury.")