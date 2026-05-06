import statistics

def wyciagnij_dane(linia):

    # Rozdzielamy linię po średniku i usuwamy puste spacje z każdego elementu
    elementy = [e.strip() for e in linia.split(';') if e.strip()]

    # Pobieramy konkretne wartości po dwukropku
    operacja = elementy[0].split(': ')[1]
    typ = elementy[1].split(': ')[1]
    n = elementy[2].split(': ')[1]
    nasycenie = elementy[3].split(': ')[1]

    # Wyciągamy samą liczbę z czasu (usuwamy " ms")
    czas_str = elementy[4].split(': ')[1].replace(' ms', '')
    czas = float(czas_str)

    return czas, (operacja, typ, n, nasycenie)


def calculateAverage(plik_wejsciowy, plik_wyjsciowy):

    with open(plik_wejsciowy, 'r', encoding="utf-8") as f, \
            open(plik_wyjsciowy, 'w', encoding="utf-8") as out:

        # Zaktualizowany nagłówek dla plików CSV/TXT z uwzględnieniem nasycenia
        out.write("Operacja;Typ;N;Nasycenie;Srednia_ms;Odchylenie_ms\n")

        bufor_czasow = []
        ostatnie_info = None

        for linia in f:
            if not linia.strip():
                continue

            czas, info = wyciagnij_dane(linia)
            if czas is not None:
                bufor_czasow.append(czas)
                ostatnie_info = info

            # Co 10 pomiarów liczymy statystyki (bo w eksperymencie daliśmy pętlę na 10)
            if len(bufor_czasow) == 10:
                srednia = statistics.mean(bufor_czasow)
                odchylenie = statistics.stdev(bufor_czasow)

                # Rozpakowujemy krotkę z informacjami
                op, typ, n, nas = ostatnie_info

                # Zapis do pliku
                out.write(f"{op};{typ};{n};{nas};{srednia:.4f};{odchylenie:.4f}\n")

                # Resetujemy bufor dla kolejnej porcji danych
                bufor_czasow = []

    print(f"Sukces! Wyniki uśrednione zapisano w: {plik_wyjsciowy}")


# --- PRZYKŁAD UŻYCIA DLA TWOJEJ STRUKTURY PLIKÓW ---
if __name__ == "__main__":
    # Możesz to wstawić w pętlę, jeśli chcesz przetworzyć wszystkie wygenerowane pliki naraz
    # np. dla eksperymentu 1, tarjan, macierz sąsiedztwa (ms):

    plik_in = 'wyniki/eksperyment1_tarjan_ms.txt'
    plik_out = 'wyniki/srednie_eksperyment1_tarjan_ms.txt'

    calculateAverage(plik_in, plik_out)