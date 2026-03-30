from core.models import Czynnosc

def wczytaj_dane_v1():
    dane = {}

    n = int(input("Podaj liczbe czynnosci: "))
    print()

    for i in range(n):
        print(f"Czynnosc {i+1}")

        nazwa = input("Nazwa: ")
        T = int(input("Czas: "))
        lpop = int(input("Liczba poprzednikow: "))

        poprzednicy = []

        print("Poprzednicy:")
        for _ in range(lpop):
            poprzednicy.append(input())

        dane[nazwa] = Czynnosc(nazwa, T, poprzednicy)
        print()

    return dane


def wczytaj_dane_v2():
    dane = {}

    n = int(input("Podaj liczbe czynnosci: "))
    print()

    start = []
    end = []
    nazwy = []

    for i in range(n):
        print(f"Czynnosc {i+1}")

        nazwa = input("Nazwa: ")
        T = int(input("Czas: "))

        print("Nastepstwo zdarzen:")
        s = int(input("od: "))
        e = int(input("do: "))

        start.append(s)
        end.append(e)
        nazwy.append(nazwa)

        dane[nazwa] = Czynnosc(nazwa, T)

    for i in range(n):
        if start[i] != 1:
            for j in range(n):
                if end[j] == start[i]:
                    dane[nazwy[i]].poprzednicy.append(nazwy[j])

    return dane


def wypisz(dane):
    for c in dane.values():
        print(c.nazwa)
        print(c.ES, c.T, c.EF)
        print(c.LS, c.R, c.LF)