import statistics

input_file = 'wyniki.txt'
output_file = 'wyniki_srednia.txt'


def wyciagnij_dane(linia):
    # Przykładowa linia: Typ: a; n: 10; Czas: 0.0123 ms; Porównania: 40; Zamiany: 20
    try:
        czesci_czasu = linia.split("Czas: ")
        czas_str = czesci_czasu[1].split(" ms")[0].strip()

        info_str = czesci_czasu[0].replace("Typ: ", "").replace("n: ", "").replace(" ", "")

        return float(czas_str), info_str.strip(";")
    except (IndexError, ValueError):
        return None, None


def calculateAverage(plik_wejsciowy, plik_wyjsciowy):

    with open(plik_wejsciowy, 'r', encoding="utf-8") as f, open(plik_wyjsciowy, 'w', encoding="utf-8") as out:
        out.write("Typ;N;Srednia_ms;Odchylenie_ms\n")

        bufor_czasow = []
        ostatnie_info = ""

        for linia in f:
            if not linia.strip(): continue

            czas, info = wyciagnij_dane(linia)
            if czas is not None:
                bufor_czasow.append(czas)
                ostatnie_info = info

            # Co 10 pomiarów dla tego samego N i Typu
            if len(bufor_czasow) == 10:
                srednia = statistics.mean(bufor_czasow)
                # stdev wymaga min. 2 elementów, co mamy (10)
                odchylenie = statistics.stdev(bufor_czasow)

                out.write(f"{ostatnie_info};{srednia:.4f};{odchylenie:.4f}\n")
                bufor_czasow = []

    print(f"Sukces! Wyniki zapisano w: {plik_wyjsciowy}")