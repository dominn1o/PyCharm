import generatoryCiagow as gen
import heapsort as h
import mergesort as m
import quicksortrecur as qr
import quicksortiter as qi
import shellsort as s
import obliczanieSrednich as avg

def eksperyment1(n):
    zakres_qs = range(5000, 30001, 5000)
    zakres_standard = range(5000, 50001, 5000)

    match n:
        case 1: # heap
            for j in range(1, 6):
                for i in zakres_standard:
                    for k in range(10):
                        if j == 1: ciag = gen.randomList(i); h.heapsort("random", i, ciag, 1)
                        elif j == 2: ciag = gen.growingList(i); h.heapsort("growing", i, ciag, 1)
                        elif j == 3: ciag = gen.descendingList(i); h.heapsort("descending", i, ciag, 1)
                        elif j == 4: ciag = gen.aShapedList(i); h.heapsort("a-shaped", i, ciag, 1)
                        elif j == 5: ciag = gen.vShapedList(i); h.heapsort("v-shaped", i, ciag, 1)
            avg.calculateAverage("wyniki/punkt1_eksperyment1_heapsort.txt", "/wynikiFin/punkt1_eksperyment1_heapsort_fin.txt")

        case 2: # merge
            for j in range(1, 6):
                for i in zakres_standard:
                    for k in range(10):
                        if j == 1: ciag = gen.randomList(i); m.mergesort("random", i, ciag, 1)
                        elif j == 2: ciag = gen.growingList(i); m.mergesort("growing", i, ciag, 1)
                        elif j == 3: ciag = gen.descendingList(i); m.mergesort("descending", i, ciag, 1)
                        elif j == 4: ciag = gen.aShapedList(i); m.mergesort("a-shaped", i, ciag, 1)
                        elif j == 5: ciag = gen.vShapedList(i); m.mergesort("v-shaped", i, ciag, 1)
            avg.calculateAverage("wyniki/punkt1_eksperyment1_mergesort.txt", "/wynikiFin/punkt1_eksperyment1_mergesort_fin.txt")

        case 3: # quickrecursive
            for j in range(1, 6):
                for i in zakres_qs:
                    for k in range(10):
                        if j == 1: ciag = gen.randomList(i); qr.quicksort("random", i, ciag, 1)
                        elif j == 2: ciag = gen.growingList(i); qr.quicksort("growing", i, ciag, 1)
                        elif j == 3: ciag = gen.descendingList(i); qr.quicksort("descending", i, ciag, 1)
                        elif j == 4: ciag = gen.aShapedList(i); qr.quicksort("a-shaped", i, ciag, 1)
                        elif j == 5: ciag = gen.vShapedList(i); qr.quicksort("v-shaped", i, ciag, 1)
            avg.calculateAverage("wyniki/punkt1_eksperyment1_quickrecursive.txt", "/wynikiFin/punkt1_eksperyment1_quickrecursive_fin.txt")

        case 4: # quickiterative
            for j in range(1, 6):
                for i in zakres_qs:
                    for k in range(10):
                        if j == 1: ciag = gen.randomList(i); qi.quicksortiter("random", i, ciag, 1)
                        elif j == 2: ciag = gen.growingList(i); qi.quicksortiter("growing", i, ciag, 1)
                        elif j == 3: ciag = gen.descendingList(i); qi.quicksortiter("descending", i, ciag, 1)
                        elif j == 4: ciag = gen.aShapedList(i); qi.quicksortiter("a-shaped", i, ciag, 1)
                        elif j == 5: ciag = gen.vShapedList(i); qi.quicksortiter("v-shaped", i, ciag, 1)
            avg.calculateAverage("wyniki/punkt1_eksperyment1_quickiterative.txt", "/wynikiFin/punkt1_eksperyment1_quickiterative_fin.txt")

        case 5: # shell
            for j in range(1, 6):
                for i in zakres_standard:
                    for k in range(10):
                        if j == 1: ciag = gen.randomList(i); s.shellsort("random", i, ciag, 1)
                        elif j == 2: ciag = gen.growingList(i); s.shellsort("growing", i, ciag, 1)
                        elif j == 3: ciag = gen.descendingList(i); s.shellsort("descending", i, ciag, 1)
                        elif j == 4: ciag = gen.aShapedList(i); s.shellsort("a-shaped", i, ciag, 1)
                        elif j == 5: ciag = gen.vShapedList(i); s.shellsort("v-shaped", i, ciag, 1)
            avg.calculateAverage("wyniki/punkt1_eksperyment1_shellsort.txt", "/wynikiFin/punkt1_eksperyment1_shellsort_fin.txt")

def eksperyment2(n):
    zakres_n = [500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 128000, 256000]

    match n:
        case 1:  # heap
            for j in range(1, 6):
                for i in zakres_n:
                    for k in range(10):
                        if j == 1: ciag = gen.randomList(i); h.heapsort("random", i, ciag, 2)
                        elif j == 2: ciag = gen.growingList(i); h.heapsort("growing", i, ciag, 2)
                        elif j == 3: ciag = gen.descendingList(i); h.heapsort("descending", i, ciag, 2)
                        elif j == 4: ciag = gen.aShapedList(i); h.heapsort("a-shaped", i, ciag, 2)
                        elif j == 5: ciag = gen.vShapedList(i); h.heapsort("v-shaped", i, ciag, 2)
            avg.calculateAverage("wyniki/punkt1_eksperyment2_heapsort.txt", "/wynikiFin/punkt1_eksperyment2_heapsort_fin.txt")

        case 2:  # merge
            for j in range(1, 6):
                for i in zakres_n:
                    for k in range(10):
                        if j == 1: ciag = gen.randomList(i); m.mergesort("random", i, ciag, 2)
                        elif j == 2: ciag = gen.growingList(i); m.mergesort("growing", i, ciag, 2)
                        elif j == 3: ciag = gen.descendingList(i); m.mergesort("descending", i, ciag, 2)
                        elif j == 4: ciag = gen.aShapedList(i); m.mergesort("a-shaped", i, ciag, 2)
                        elif j == 5: ciag = gen.vShapedList(i); m.mergesort("v-shaped", i, ciag, 2)
            avg.calculateAverage("wyniki/punkt1_eksperyment2_mergesort.txt", "/wynikiFin/punkt1_eksperyment2_mergesort_fin.txt")

        case 3:  # quickrecursive
            for j in range(1, 6):
                for i in zakres_n[0:7]:
                    for k in range(10):
                        if j == 1: ciag = gen.randomList(i); qr.quicksort("random", i, ciag, 2)
                        elif j == 2: ciag = gen.growingList(i); qr.quicksort("growing", i, ciag, 2)
                        elif j == 3: ciag = gen.descendingList(i); qr.quicksort("descending", i, ciag, 2)
                        elif j == 4: ciag = gen.aShapedList(i); qr.quicksort("a-shaped", i, ciag, 2)
                        elif j == 5: ciag = gen.vShapedList(i); qr.quicksort("v-shaped", i, ciag, 2)
            avg.calculateAverage("wyniki/punkt1_eksperyment2_quickrecursive.txt", "/wynikiFin/punkt1_eksperyment2_quickrecursive_fin.txt")

        case 4:  # quickiterative
            for j in range(1, 6):
                for i in zakres_n[0:7]:
                    for k in range(10):
                        if j == 1: ciag = gen.randomList(i); qi.quicksortiter("random", i, ciag, 2)
                        elif j == 2: ciag = gen.growingList(i); qi.quicksortiter("growing", i, ciag, 2)
                        elif j == 3: ciag = gen.descendingList(i); qi.quicksortiter("descending", i, ciag, 2)
                        elif j == 4: ciag = gen.aShapedList(i); qi.quicksortiter("a-shaped", i, ciag, 2)
                        elif j == 5: ciag = gen.vShapedList(i); qi.quicksortiter("v-shaped", i, ciag, 2)
            avg.calculateAverage("wyniki/punkt1_eksperyment2_quickiterative.txt", "/wynikiFin/punkt1_eksperyment2_quickiterative_fin.txt")

        case 5:  # shell
            for j in range(1, 6):
                for i in zakres_n:
                    for k in range(10):
                        if j == 1: ciag = gen.randomList(i); s.shellsort("random", i, ciag, 2)
                        elif j == 2: ciag = gen.growingList(i); s.shellsort("growing", i, ciag, 2)
                        elif j == 3: ciag = gen.descendingList(i); s.shellsort("descending", i, ciag, 2)
                        elif j == 4: ciag = gen.aShapedList(i); s.shellsort("a-shaped", i, ciag, 2)
                        elif j == 5: ciag = gen.vShapedList(i); s.shellsort("v-shaped", i, ciag, 2)
            avg.calculateAverage("wyniki/punkt1_eksperyment2_shellsort.txt", "/wynikiFin/punkt1_eksperyment2_shellsort_fin.txt")

def wyczysc_pliki():
    pliki = [
        "wyniki/punkt1_eksperyment1_heapsort.txt", "wyniki/punkt1_eksperyment1_mergesort.txt",
        "wyniki/punkt1_eksperyment1_quickrecursive.txt", "wyniki/punkt1_eksperyment1_quickiterative.txt",
        "wyniki/punkt1_eksperyment1_shellsort.txt",
        "wyniki/punkt1_eksperyment2_heapsort.txt", "wyniki/punkt1_eksperyment2_mergesort.txt",
        "wyniki/punkt1_eksperyment2_quickrecursive.txt", "wyniki/punkt1_eksperyment2_quickiterative.txt",
        "wyniki/punkt1_eksperyment2_shellsort.txt",
        "/wynikiFin/punkt1_eksperyment1_heapsort_fin.txt", "/wynikiFin/punkt1_eksperyment1_mergesort_fin.txt",
        "/wynikiFin/punkt1_eksperyment1_quickrecursive_fin.txt", "/wynikiFin/punkt1_eksperyment1_quickiterative_fin.txt",
        "/wynikiFin/punkt1_eksperyment1_shellsort_fin.txt",
        "/wynikiFin/punkt1_eksperyment2_heapsort_fin.txt", "/wynikiFin/punkt1_eksperyment2_mergesort_fin.txt",
        "/wynikiFin/punkt1_eksperyment2_quickrecursive_fin.txt", "/wynikiFin/punkt1_eksperyment2_quickiterative_fin.txt",
        "/wynikiFin/punkt1_eksperyment2_shellsort_fin.txt"
    ]
    for nazwa_pliku in pliki:
        with open(nazwa_pliku, "w", encoding="utf-8") as f:
            pass # otwarcie z  'w' czyści plik


wyczysc_pliki()
print("Pliki wyczyszczone")

for i in range(4, 6):
    eksperyment1(i)

for i in range(1, 6):
    eksperyment2(i)

print("all tests completed succesfully")