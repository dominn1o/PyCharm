import math
import time

class wezelBST:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def wstaw(korzen, key):
    #jeśli drzewo puste, nowy wezel staje się korzeniem
    if korzen is None:
        return wezelBST(key)

    obecny = korzen
    while True:
        #jesli klucz mniejszy od obecnego, idz do lewego poddrzewa
        if key < obecny.key:
            if obecny.left is None:
                obecny.left = wezelBST(key)  #wstaw jako lewe dziecko
                break
            else:
                obecny = obecny.left
        #jesli wiekszy wstaw jako prawe dziecko
        else:
            if obecny.right is None:
                obecny.right = wezelBST(key)
                break
            else:
                obecny = obecny.right

    return korzen


def wyswietlDrzewo(korzen, prefix="", jest_ostatni=True, nazwa_relacji="root"):
    if korzen is None:
        return

    #symbole gałęzi
    symbol = "└── " if jest_ostatni else "├── "

    #wyswietlenie aktualnego wezla, czy to L czy R dziecko
    relacja = f"[{nazwa_relacji}] " if nazwa_relacji != "root" else ""
    print(f"{prefix}{symbol}{relacja}{korzen.key}")

    nowy_prefix = prefix + ("    " if jest_ostatni else "│   ")

    #tworzymy listę dzieci
    dzieci = []
    if korzen.left:
        dzieci.append((korzen.left, "L"))
    if korzen.right:
        dzieci.append((korzen.right, "R"))

    #rekurencyjnie wstaw dzieci
    for i, (dziecko, typ) in enumerate(dzieci):
        czy_ostatnie_dziecko = (i == len(dzieci) - 1)
        wyswietlDrzewo(dziecko, nowy_prefix, czy_ostatnie_dziecko, typ)


def wysokosc(korzen):
    #jeśli wezel nie istnieje zwracamy -1 - wtedy korzen ma wysokosc 0
    if korzen is None:
        return -1

    lewaWys = wysokosc(korzen.left)
    prawaWys = wysokosc(korzen.right)

    if lewaWys > prawaWys:
        return lewaWys + 1
    else:
        return prawaWys + 1


def najwiekszyEl(korzen):
    start = time.perf_counter()

    if korzen is None:
        end = time.perf_counter()
        return None, [], 1, (end - start) * 1000

    sciezka = []
    porownania = 0
    obecny = korzen

    #logika algorytmu
    while obecny.right is not None:
        sciezka.append(obecny.key)
        porownania += 1
        obecny = obecny.right

    porownania += 1  #ostatnie porównanie, które daje None
    sciezka.append(obecny.key)

    end = time.perf_counter()
    czas_ms = (end - start) * 1000

    return obecny.key, sciezka, porownania, czas_ms


def najmniejszyEl(korzen):
    start = time.perf_counter()

    if korzen is None:
        end = time.perf_counter()
        return None, [], 1, (end - start) * 1000

    sciezka = []
    porownania = 0
    obecny = korzen

    while obecny.left is not None:
        sciezka.append(obecny.key)
        porownania += 1
        obecny = obecny.left

    porownania += 1
    sciezka.append(obecny.key)

    end = time.perf_counter()
    czas_ms = (end - start) * 1000

    return obecny.key, sciezka, porownania, czas_ms



def znajdzEl(korzen, klucz):
    start = time.perf_counter()

    #1. szukanie węzła i poziomu
    obecny = korzen
    poziom = 0
    znaleziony_element = None
    porownania_szukanie = 0

    while obecny is not None:
        porownania_szukanie += 1
        if klucz == obecny.key:
            znaleziony_element = obecny
            break
        elif klucz < obecny.key:
            obecny = obecny.left
            poziom += 1
        else:
            obecny = obecny.right
            poziom += 1

    if znaleziony_element is None:
        print(f"\nBłąd: Klucz {klucz} nie istnieje w drzewie.")
        return

    print(f"\nKlucz: {klucz}")
    print(f"1. Poziom na którym znajduje się węzeł: {poziom}")


    def resztaElementowNaPoziomie(korzen, cel_poziom, obecny_poziom):
        if korzen is None:
            return

        #jesli dotarlismy na szukany poziom, wypisz klucz
        if obecny_poziom == cel_poziom:
            print(korzen.key, end=" ")
        else:
            resztaElementowNaPoziomie(korzen.left, cel_poziom, obecny_poziom + 1)
            resztaElementowNaPoziomie(korzen.right, cel_poziom, obecny_poziom + 1)

    print(f"2. Wszystkie elementy na poziomie {poziom}: ", end="")
    resztaElementowNaPoziomie(korzen, poziom, 0)


    def wysokoscPoddrzewa(korzen):
        if korzen is None:
            return -1  #pusty wezel ma wysokość -1

        lewa = wysokoscPoddrzewa(korzen.left)
        prawa = wysokoscPoddrzewa(korzen.right)

        if lewa > prawa:
            return lewa + 1
        else:
            return prawa + 1

    print(f"\n3. Wysokość poddrzewa o korzeniu {klucz}: {wysokoscPoddrzewa(znaleziony_element)}")


    def wypiszPreOrder(korzen):
        if korzen is None:
            return

        #najpierw klucz obecnego węzła (korzen)
        print(korzen.key, end=" ")

        #potem lewe dziecko
        wypiszPreOrder(korzen.left)

        #potem prawe dzidcko
        wypiszPreOrder(korzen.right)

    print(f"4. Poddrzewo w porządku pre-order: ", end="")
    wypiszPreOrder(znaleziony_element)

    end = time.perf_counter()
    czas_ms = (end - start) * 1000
    print(f"\nCzas działania operacji: {czas_ms:.4f} ms")
    print(f"Liczba wykonanych porównań kluczy: {porownania_szukanie}")

    print()


def wypiszMalejaco(korzen):
    if korzen is None:
        return [], 1

    porownania = 1
    wynikowe_elementy = []

    # idzie po drzewie in-order w odwrotnej kolejnosci

    # najpierw prawy
    prawe_elementy, p_prawo = wypiszMalejaco(korzen.right)
    wynikowe_elementy.extend(prawe_elementy)
    porownania += p_prawo

    #potem korzen
    wynikowe_elementy.append(korzen.key)

    #potem lewy
    lewe_elementy, p_lewo = wypiszMalejaco(korzen.left)
    wynikowe_elementy.extend(lewe_elementy)
    porownania += p_lewo

    return wynikowe_elementy, porownania


def usunEL(korzen, klucz, tryb):
    if korzen is None:
        print("Drzewo jest puste!")
        return None

    porownania_usun = 0

    #1. szukanie wezla ktorego usuwamy
    def znajdz(wezel, k):
        nonlocal porownania_usun
        if wezel is None:
            porownania_usun += 1
            return wezel

        porownania_usun += 1
        if wezel.key == k:
            return wezel

        porownania_usun += 1
        if k < wezel.key:
            return znajdz(wezel.left, k)
        return znajdz(wezel.right, k)

    target = znajdz(korzen, klucz)
    if target is None:
        print(f"Błąd: Klucz {klucz} nie istnieje.")
        return korzen

    # 2. logika usuwania
    #razem z calym poddrzewem
    if tryb == "b":
        def usun_poddrzewo(wezel, k):
            nonlocal porownania_usun
            if wezel is None:
                porownania_usun += 1
                return None

            porownania_usun += 1
            if k < wezel.key:
                wezel.left = usun_poddrzewo(wezel.left, k)
            else:
                porownania_usun += 1
                if k > wezel.key:
                    wezel.right = usun_poddrzewo(wezel.right, k)
                else:
                    return None
            return wezel

        wynik = usun_poddrzewo(korzen, klucz)
        print(f"Usunięto klucz {klucz} wraz z całym jego poddrzewem.")
        print(f"Liczba wykonanych porównań kluczy: {porownania_usun}")
        return wynik

    #sam element, przesuwanie dzieci
    elif tryb == "a":
        def znajdz_nastepce(wezel):
            nonlocal porownania_usun
            obecny = wezel.right
            while obecny.left is not None:
                porownania_usun += 1
                obecny = obecny.left
            porownania_usun += 1
            return obecny

        def usun_wezel(wezel, k):
            nonlocal porownania_usun
            if wezel is None:
                porownania_usun += 1
                return None

            porownania_usun += 1
            if k < wezel.key:
                wezel.left = usun_wezel(wezel.left, k)
            else:
                porownania_usun += 1
                if k > wezel.key:
                    wezel.right = usun_wezel(wezel.right, k)
                else:
                    #jedno dziecko, wstawiamy zamiast rodzica
                    if wezel.left is None:
                        return wezel.right
                    elif wezel.right is None:
                        return wezel.left

                    #nastepca jest najmniejszym elementem prawego poddrzewa
                    nastepca = znajdz_nastepce(wezel)
                    wezel.key = nastepca.key
                    wezel.right = usun_wezel(wezel.right, nastepca.key)
            return wezel

        wynik = usun_wezel(korzen, klucz)
        print(f"Usunięto tylko klucz {klucz}, dzieci zostały przepięte.")
        print(f"Liczba wykonanych porównań kluczy: {porownania_usun}")
        return wynik

#funkcje pomocnicze do algorytmu zrownowazania DSW
def rotacjaPrawo(rodzicKorzenia, korzen, leweDziecko):
    #przepięcie dziecka do rodzica (jeśli rodzic istnieje)
    porownania = 0
    if rodzicKorzenia is not None:
        porownania += 1
        if rodzicKorzenia.right == korzen:
            rodzicKorzenia.right = leweDziecko
        else:
            rodzicKorzenia.left = leweDziecko

    #przekazanie prawego poddrzewa dziecka do lewej strony korzenia
    korzen.left = leweDziecko.right
    #ustawienie korzenia jako prawego dziecka nowego lidera leweDziecko
    leweDziecko.right = korzen
    return leweDziecko, porownania


def rotacjaLewo(rodzicKorzenia, korzen, praweDziecko):
    porownania = 0
    if rodzicKorzenia is not None:
        porownania += 1
        if rodzicKorzenia.right == korzen:
            rodzicKorzenia.right = praweDziecko
        else:
            rodzicKorzenia.left = praweDziecko

    korzen.right = praweDziecko.left
    praweDziecko.left = korzen
    return praweDziecko, porownania


def rownowazenieDSW(korzen):
    if korzen is None:
        return None

    suma_porownan_dsw = 0

    #tymczasowy korzen zeby latwiej operować na prawdziwym korzeniu
    temp = wezelBST(0)
    temp.right = korzen

    #1: tworzenie kregoslupa(vine)
    rodzicKorzenia = temp
    korzen = rodzicKorzenia.right
    n = 0
    #rotacje w prawo, az bedzie linkedlist rosnaca w dol
    while korzen is not None:
        suma_porownan_dsw += 1
        if korzen.left is not None:
            korzen, p = rotacjaPrawo(rodzicKorzenia, korzen, korzen.left)
            suma_porownan_dsw += p
        else:
            n += 1
            rodzicKorzenia = korzen
            korzen = korzen.right

    #2: zwijanie - rotacje w lewo
    #n - ilosc elementow
    #wysokosc drzewa dla ktorej kazdy poziom bedzie wypelniony
    h = int(math.log2(n + 1))
    #ile wezlow zmiesci sie w tym drzewie o wysokosci h
    m = 2 ** h - 1

    #pierwsza seria rotacji
    def wykonajRotacje(ile, start_node):
        nonlocal suma_porownan_dsw
        rodzicKorzenia2 = start_node
        for i in range(ile):
            korzen2 = rodzicKorzenia2.right
            dziecko2 = korzen2.right

            #wykonujemy rotację korzenia z jego prawym dzieckiem
            korzen2, p = rotacjaLewo(rodzicKorzenia2, korzen2, dziecko2)
            suma_porownan_dsw += p

            #przesuwamy rodzica na nowo powstały węzeł
            #aby w kolejnej iteracji rotować następną parę niżej na kręgosłupie
            rodzicKorzenia2 = korzen2

    #n-m to ilosc elementow w ostatnim poziomie zrownowazonego drzewa
    wykonajRotacje(n - m, temp)

    while m > 1:
        m //= 2
        wykonajRotacje(m, temp)

    return suma_porownan_dsw, temp.right

def wypiszPreOrder(korzen):
    if korzen is None:
        return

    print(korzen.key, end=" ")
    wypiszPreOrder(korzen.left)
    wypiszPreOrder(korzen.right)