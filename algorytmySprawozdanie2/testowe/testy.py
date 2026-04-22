import generatoryCiagow as gen
import obliczanieSrednich as avg
import BST as BST
import AVL as AVL
import HMIN as HMIN

def eksperyment1(struktura_id):
    zakres_skrocony = range(5000, 30001, 5000) # Skrócony zakres dla pesymistycznych wariantów BST
    zakres_standard = range(5000, 50001, 5000)

    match struktura_id:
        case 1: # BST
            for j in range(1, 4): # Tylko 3 typy: 1-losowe, 2-rosnące, 3-malejące
                # Dla BST ciągi posortowane (j=2, j=3) to przypadek pesymistyczny, używamy skróconego zakresu
                zakres = zakres_skrocony if j in [2, 3] else zakres_standard
                for i in zakres:
                    for k in range(10):
                        if j == 1: ciag = gen.randomList(i); BST.wykonaj_pomiary("random", i, ciag, 1)
                        elif j == 2: ciag = gen.growingList(i); BST.wykonaj_pomiary("growing", i, ciag, 1)
                        elif j == 3: ciag = gen.descendingList(i); BST.wykonaj_pomiary("descending", i, ciag, 1)
            # Wyliczanie średnich dla 3 osobnych plików
            operacje = ["tworzenie", "max", "rownowazenie"]
            for op in operacje:
                plik_we = f"wyniki/punkt1_eksperyment1_bst_{op}.txt"
                plik_wy = f"wynikiFin/punkt1_eksperyment1_bst_{op}_fin.txt"
                avg.calculateAverage(plik_we, plik_wy)
            print("BST experiment 1 done")

        case 2: # AVL
            for j in range(1, 4):
                for i in zakres_standard:
                    for k in range(10):
                        if j == 1: ciag = gen.randomList(i); AVL.wykonaj_pomiary("random", i, ciag, 1)
                        elif j == 2: ciag = gen.growingList(i); AVL.wykonaj_pomiary("growing", i, ciag, 1)
                        elif j == 3: ciag = gen.descendingList(i); AVL.wykonaj_pomiary("descending", i, ciag, 1)
            # PO ZAKOŃCZENIU TESTÓW AVL LICZYMY ŚREDNIE:
            operacje_avl = ["tworzenie", "max"]
            for op in operacje_avl:
                plik_we = f"wyniki/punkt1_eksperyment1_avl_{op}.txt"
                plik_wy = f"wynikiFin/punkt1_eksperyment1_avl_{op}_fin.txt"
                avg.calculateAverage(plik_we, plik_wy)
            print("AVL experiment 1 done")

        case 3: # HMIN (Kopiec)
            for j in range(1, 4):
                for i in zakres_standard:
                    for k in range(10):
                        if j == 1: ciag = gen.randomList(i); HMIN.wykonaj_pomiary("random", i, ciag, 1)
                        elif j == 2: ciag = gen.growingList(i); HMIN.wykonaj_pomiary("growing", i, ciag, 1)
                        elif j == 3: ciag = gen.descendingList(i); HMIN.wykonaj_pomiary("descending", i, ciag, 1)
            # PO ZAKOŃCZENIU TESTÓW HMIN LICZYMY ŚREDNIE:
            operacje_hmin = ["tworzenie", "max"]
            for op in operacje_hmin:
                plik_we = f"wyniki/punkt1_eksperyment1_hmin_{op}.txt"
                plik_wy = f"wynikiFin/punkt1_eksperyment1_hmin_{op}_fin.txt"
                avg.calculateAverage(plik_we, plik_wy)
            print("HMIN experiment 1 done")

def eksperyment2(struktura_id):
    zakres_n = [500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 128000, 256000]

    match struktura_id:
        case 1:  # BST
            for j in range(1, 4):
                # Skracamy zakres dla pesymistycznego BST, żeby nie przepełnić stosu / uniknąć nieskończonego czekania
                zakres = zakres_n[0:7] if j in [2, 3] else zakres_n
                for i in zakres:
                    for k in range(10):
                        if j == 1: ciag = gen.randomList(i); BST.wykonaj_pomiary("random", i, ciag, 2)
                        elif j == 2: ciag = gen.growingList(i); BST.wykonaj_pomiary("growing", i, ciag, 2)
                        elif j == 3: ciag = gen.descendingList(i); BST.wykonaj_pomiary("descending", i, ciag, 2)
            # Wyliczanie średnich dla 3 osobnych plików
            operacje = ["tworzenie", "max", "rownowazenie"]
            for op in operacje:
                plik_we = f"wyniki/punkt1_eksperyment2_bst_{op}.txt"
                plik_wy = f"wynikiFin/punkt1_eksperyment2_bst_{op}_fin.txt"
                avg.calculateAverage(plik_we, plik_wy)
            print("BST experiment 2 done")

        case 2:  # AVL
            for j in range(1, 4):
                for i in zakres_n:
                    for k in range(10):
                        if j == 1: ciag = gen.randomList(i); AVL.wykonaj_pomiary("random", i, ciag, 2)
                        elif j == 2: ciag = gen.growingList(i); AVL.wykonaj_pomiary("growing", i, ciag, 2)
                        elif j == 3: ciag = gen.descendingList(i); AVL.wykonaj_pomiary("descending", i, ciag, 2)
            # PO ZAKOŃCZENIU TESTÓW AVL LICZYMY ŚREDNIE:
            operacje_avl = ["tworzenie", "max"]
            for op in operacje_avl:
                plik_we = f"wyniki/punkt1_eksperyment2_avl_{op}.txt"
                plik_wy = f"wynikiFin/punkt1_eksperyment2_avl_{op}_fin.txt"
                avg.calculateAverage(plik_we, plik_wy)
            print("AVL experiment 1 done")

        case 3:  # HMIN
            for j in range(1, 4):
                for i in zakres_n:
                    for k in range(10):
                        if j == 1: ciag = gen.randomList(i); HMIN.wykonaj_pomiary("random", i, ciag, 2)
                        elif j == 2: ciag = gen.growingList(i); HMIN.wykonaj_pomiary("growing", i, ciag, 2)
                        elif j == 3: ciag = gen.descendingList(i); HMIN.wykonaj_pomiary("descending", i, ciag, 2)
            # PO ZAKOŃCZENIU TESTÓW HMIN LICZYMY ŚREDNIE:
            operacje_hmin = ["tworzenie", "max"]
            for op in operacje_hmin:
                plik_we = f"wyniki/punkt1_eksperyment2_hmin_{op}.txt"
                plik_wy = f"wynikiFin/punkt1_eksperyment2_hmin_{op}_fin.txt"
                avg.calculateAverage(plik_we, plik_wy)
            print("HMIN experiment 1 done")

"""
def wyczysc_pliki():

    struktury = [("bst", ["tworzenie", "max", "rownowazenie"]),
                 ("avl", ["tworzenie", "max"]),
                 ("hmin", ["tworzenie", "max"])]
    eksperymenty = [1, 2]

    pliki_do_usuniecia = []

    # Automatyczne generowanie listy wszystkich możliwych plików
    for struktura, operacje in struktury:
        for op in operacje:
            for e in eksperymenty:
                pliki_do_usuniecia.append(f"wyniki/punkt1_eksperyment{e}_{struktura}_{op}.txt")
                pliki_do_usuniecia.append(f"wynikiFin/punkt1_eksperyment{e}_{struktura}_{op}_fin.txt")

    for nazwa_pliku in pliki_do_usuniecia:
        try:
            with open(nazwa_pliku, "w", encoding="utf-8") as f:
                pass  # otwarcie z 'w' czyści plik
        except Exception:
            pass  # Ignorujemy błędy


wyczysc_pliki()
print("Pliki wyczyszczone i foldery przygotowane.")

# Uruchomienie dla 3 struktur (1 - BST, 2 - AVL, 3 - HMIN)
for i in range(1, 4):
    eksperyment1(i)

"""
eksperyment1(3)
for i in range(1, 4):
    eksperyment2(i)



print("All tests completed successfully.")