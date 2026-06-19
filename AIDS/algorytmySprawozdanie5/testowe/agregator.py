import os
import statistics


def wyciagnij_dane_czas(linia):
    elementy = [e.strip() for e in linia.split(';') if e.strip()]
    alg = elementy[0].split(': ')[1]
    n = int(elementy[1].split(': ')[1])
    b = int(elementy[2].split(': ')[1])
    czas = float(elementy[3].split(': ')[1])
    return czas, (alg, n, b)


def agreguj_pliki():
    os.makedirs("wyniki_plecak_finalne", exist_ok=True)
    folder_wejsciowy = "wyniki_plecak"

    for plik in os.listdir(folder_wejsciowy):
        if not plik.endswith(".txt") or "exp3" in plik:
            continue

        sciezka = os.path.join(folder_wejsciowy, plik)
        sciezka_wyjscia = os.path.join("wyniki_plecak_finalne", plik.replace(".txt", "_srednie.txt"))

        with open(sciezka, 'r', encoding="utf-8") as f, \
                open(sciezka_wyjscia, 'w', encoding="utf-8") as out:

            out.write("Algorytm;N;B;Srednia_ms;Odchylenie_ms\n")

            bufor_czasow = []
            ostatnie_info = None

            for linia in f:
                if not linia.strip():
                    continue

                czas, info = wyciagnij_dane_czas(linia)
                bufor_czasow.append(czas)
                ostatnie_info = info

                # Zapisujemy średnią po zebraniu paczki 10 powtórzeń
                if len(bufor_czasow) == 10:
                    srednia = statistics.mean(bufor_czasow)
                    odchylenie = statistics.stdev(bufor_czasow) if len(bufor_czasow) > 1 else 0

                    alg, n, b = ostatnie_info
                    out.write(f"{alg};{n};{b};{srednia:.4f};{odchylenie:.4f}\n")

                    bufor_czasow = []


if __name__ == "__main__":
    print("Rozpoczynam agregację danych pomiarowych...")
    agreguj_pliki()
    print("Agregacja zakończona! Zagregowane pliki txt znajdują się w 'wyniki_plecak_finalne'.")