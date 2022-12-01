import math
"""1.funkcja dodająca"""
def dodawanie(x, y):
    return x + y
"""2.funkcja odejmująca"""
def odejmowanie(x, y):
    return x - y
"""3.funkcja mnożenia"""
def mnozenie(x, y):
    return x * y
"""4.funkcja dzielenia"""
def dzielenie(x, y):
    try:
        wynik = x / y
    except Exception as e:
        print("nie dziel przez zero")
        return 0
    else:
        try:
            wynik2 = y / x
        except Exception as e:
            print("nie dziel przez zero")
            return 0
    return wynik
"""5.funkcja potęgowania"""
def potegowanie(x, y):
    return math.pow(x, y)
"""6.funkcja pierwiastek kwadratowy"""
def pierwiastek_2_liczby(x):
    return math.sqrt(x)
"""7.funkcja logarytm naturalnego"""
def logarytmn_nturalny(x):
    return math.log(x)
"""8.funkcja logarytm dziesietnego"""
def logarytm_10(x):
    return math.log10(x)
"""9.funkcja sinusa liczby"""
def sinus(x):
    return math.sin(x)
"""10.funkcja tangensa liczby"""
def tangens(x):
    return math.tan(x)
"""11.funkcja histori obliczeń"""
obliczenia = []
def historia_dzialan(args):
    obliczenia.append(args)
def historia():
    if obliczenia == []:
        print("Nie było poprzednich obliczeń")
    else:
        for o in obliczenia:
            print(o)
"""rodzaje działań do wyboru"""
rodzaje_dzialan = (
    "Rodzaje działań: \n|||  1.Dodawanie  |||  2.Odejmowanie  \n|||  3.Mnożenie  |||  4.Dzielenie  \n|||  5.Potęgowanie "
    "|||  6.Pierwiastek kwadratowy liczby\n|||  7.Logarytm naturalny  |||  8.Logarytm dziesiętny  \n|||  9.Sinus liczby  |||  10.Tangens liczby")

"""właściwa część"""
while True:
    print(rodzaje_dzialan)
    wybor_dzialania = input("Dokonaj wyboru działania (1-10): ")
    if wybor_dzialania in ("1", "2", "3", "4", "5"):
        while True:
            try:
                liczba1 = float(input("Podaj pierwszą liczbę: "))
                break
            except ValueError:
                print("Nie podano liczby!")
        while True:
            try:
                liczba2 = float(input("Podaj drugą liczbę: "))
                break
            except ValueError:
                print("Nie podano liczby!")

        if wybor_dzialania == '1':
            wynik =
            print(liczba1, "+", liczba2, "=", dodawanie(liczba1, liczba2))

        elif wybor_dzialania == '2':
            wynik = odejmowanie(liczba1, liczba2)
            print(liczba1, "-", liczba2, "=", odejmowanie(liczba1, liczba2))

        elif wybor_dzialania == '3':
            wynik = mnozenie(liczba1, liczba2)
            print(liczba1, "*", liczba2, "=", mnozenie(liczba1, liczba2))

        elif wybor_dzialania == '4':
            wynik = dzielenie(liczba1, liczba2)
            print(liczba1, "/", liczba2, "=", )

        elif wybor_dzialania == '5':
            wynik = potegowanie(liczba1, liczba2)
            print(liczba1, "do potęgi", liczba2, "=", )

        nastepne_dzialanie = input("\nCzy chcesz wykonać następne działanie? (T/N): ").upper()
        if nastepne_dzialanie != "T":
            print("Nie wyrażono chęci kontynuowania")
            break

    elif wybor_dzialania in ("6", "7", "8", "9", "10"):
        while True:
            try:
                liczba3 = float(input("Podaj liczbę: "))
                break
            except ValueError:
                print("Nie podano liczby!")

        if wybor_dzialania == '6':
            print("Pierwiastek kwadratowy liczby", liczba3, "=", pierwiastek_2_liczby(liczba3))

        elif wybor_dzialania == '7':
            print("Logarytm naturalny liczby", liczba3, "=", logarytmn_nturalny(liczba3))

        elif wybor_dzialania == '8':
            print("Logarytm dziesiętny liczby", liczba3, "=", logarytm_10(liczba3))

        elif wybor_dzialania == '9':
            print("Sinus liczby", liczba3, "=", sinus(liczba3))

        elif wybor_dzialania == '10':
            print("Tangens liczby", liczba3, "=", tangens(liczba3))

        nastepne_dzialanie = input("\nCzy chcesz wykonać następne działanie? (T/N): ").upper()
        if nastepne_dzialanie != "T":
            print("Nie wyrażono chęci kontynuowania")
            break
    else:
        print("Zła liczba/nie ma takiego działania")

