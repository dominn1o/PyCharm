import statistics


def wyciagnij_dane(linia):
    elementy = [e.strip() for e in linia.split(';') if e.strip()]

    operacja = elementy[0].split(': ')[1]
    typ_grafu = elementy[1].split(': ')[1]
    n = elementy[2].split(': ')[1]
    nasycenie = elementy[3].split(': ')[1]
    czas = float(elementy[4].split(': ')[1].replace(' ms', ''))

    # Obsługa opcjonalnej liczby backtracków
    backtracki = 0
    if len(elementy) > 5 and 'Backtracki' in elementy[5]:
        backtracki = int(elementy[5].split(': ')[1])

    return czas, backtracki, (operacja, typ_grafu, n, nasycenie)


def calculateAverage(plik_wejsciowy, plik_wyjsciowy):
    with open(plik_wejsciowy, 'r', encoding="utf-8") as f, \
            open(plik_wyjsciowy, 'w', encoding="utf-8") as out:

        out.write("Operacja;TypGrafu;N;Nasycenie;Srednia_ms;Odchylenie_ms;Srednia_Backtrackow\n")

        bufor_czasow = []
        bufor_backtrackow = []
        ostatnie_info = None

        for linia in f:
            if not linia.strip() or "Błąd" in linia:
                continue

            czas, back, info = wyciagnij_dane(linia)
            bufor_czasow.append(czas)
            bufor_backtrackow.append(back)
            ostatnie_info = info

            if len(bufor_czasow) == 10:
                srednia = statistics.mean(bufor_czasow)
                odchylenie = statistics.stdev(bufor_czasow) if len(bufor_czasow) > 1 else 0
                srednia_back = statistics.mean(bufor_backtrackow)

                op, typ, n, nas = ostatnie_info
                out.write(f"{op};{typ};{n};{nas};{srednia:.4f};{odchylenie:.4f};{srednia_back:.2f}\n")

                bufor_czasow = []
                bufor_backtrackow = []
                