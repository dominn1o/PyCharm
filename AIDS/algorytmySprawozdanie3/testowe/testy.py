import tarjan
import kahn
import obliczanieSrednich as avg

def eksperyment1(strukturaID):

    zakres = range(150, 1501, 150)
    match strukturaID:
        case 1: #tarjan
            for typReprezentacji in range(1, 4): # 1 - macierz sasiedztwa, 2 - lista nastepnikow, 3 - lista krawedzi
                for n in zakres: #liczba elementow ciagu
                    for i in range(10): #obowiazkowe powtorzenia
                        tarjan.wykonaj_pomiary(typReprezentacji, n, 1)

            #liczenie srednich
            typyReprezentacji = ["ms","ln", "lk"]
            for typ in typyReprezentacji:
                plik_we = f"wyniki/eksperyment1_tarjan_{typ}.txt"
                plik_wy = f"wynikiFin/eksperyment1_tarjan_{typ}_fin.txt"
                avg.calculateAverage(plik_we, plik_wy)
            print("tarjan experiment 1 done")

        case 2: #kahn
            for typReprezentacji in range(1, 4):  # 1 - macierz sasiedztwa, 2 - lista nastepnikow, 3 - lista krawedzi
                for n in zakres:  # liczba elementow ciagu
                    for i in range(10):  # obowiazkowe powtorzenia
                        kahn.wykonaj_pomiary(typReprezentacji, n, 1)

            # liczenie srednich
            typyReprezentacji = ["ms", "ln", "lk"]
            for typ in typyReprezentacji:
                plik_we = f"wyniki/eksperyment1_kahn_{typ}.txt"
                plik_wy = f"wynikiFin/eksperyment1_kahn_{typ}_fin.txt"
                avg.calculateAverage(plik_we, plik_wy)
            print("kahn experiment 1 done")


def eksperyment2(strukturaID):

    n = 1000
    match strukturaID:
        case 1: #tarjan
            for typReprezentacji in range(1, 4): # 1 - macierz sasiedztwa, 2 - lista nastepnikow, 3 - lista krawedzi
                for nasycenie in range(1, 10):
                    krokNasycenia = nasycenie/10
                    for i in range(10):
                        tarjan.wykonaj_pomiary(typReprezentacji ,n , 2, krokNasycenia)

            #liczenie srednich
            typyReprezentacji = ["ms","ln", "lk"]
            for typ in typyReprezentacji:
                plik_we = f"wyniki/eksperyment2_tarjan_{typ}.txt"
                plik_wy = f"wynikiFin/eksperyment2_tarjan_{typ}_fin.txt"
                avg.calculateAverage(plik_we, plik_wy)
            print("tarjan experiment 2 done")

        case 2:  #kahn
            for typReprezentacji in range(1, 4):  # 1 - macierz sasiedztwa, 2 - lista nastepnikow, 3 - lista krawedzi
                for nasycenie in range(1, 10):
                    krokNasycenia = nasycenie / 10
                    for i in range(10):
                        kahn.wykonaj_pomiary(typReprezentacji, n, 2, krokNasycenia)

            #liczenie srednich
            typyReprezentacji = ["ms","ln", "lk"]
            for typ in typyReprezentacji:
                plik_we = f"wyniki/eksperyment2_kahn_{typ}.txt"
                plik_wy = f"wynikiFin/eksperyment2_kahn_{typ}_fin.txt"
                avg.calculateAverage(plik_we, plik_wy)
            print("kahn experiment 2 done")



# --- DZIAŁANIE PROGRAMU ---

def wyczysc_pliki():

    struktury = ["tarjan", "kahn"]
    reprezentacje = ["ms", "ln", "lk"]
    eksperymenty = [1, 2]

    pliki_do_usuniecia = []

    # Automatyczne generowanie listy wszystkich możliwych plików dla nowych algorytmów
    for struktura in struktury:
        for rep in reprezentacje:
            for e in eksperymenty:
                pliki_do_usuniecia.append(f"wyniki/eksperyment{e}_{struktura}_{rep}.txt")
                pliki_do_usuniecia.append(f"wynikiFin/eksperyment{e}_{struktura}_{rep}_fin.txt")

    for nazwa_pliku in pliki_do_usuniecia:
        try:
            # Nadpisuje plik pustym ciągiem znaków (zeruje go)
            with open(nazwa_pliku, "w", encoding="utf-8") as f:
                pass
        except Exception:
            pass

# Czyszczenie
wyczysc_pliki()
print("Katalogi gotowe, stare pliki wyczyszczone.\nRozpoczynam testy...\n")

# Uruchomienie dla 2 algorytmów (1 - Tarjan, 2 - Kahn)
for alg_id in range(1, 3):
    eksperyment1(alg_id)

for alg_id in range(1, 3):
    eksperyment2(alg_id)

print("\nWszystkie testy zakończone pomyślnie!")