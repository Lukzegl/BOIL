from console.console import wczytaj_dane_v1, wczytaj_dane_v2, wypisz
from core.cpm import oblicz_cpm
from core.gantt import rysuj_gantty

#grafy1
from core.graphs import rysuj_cpm

def main():
    print("Wybierz opcje wpisywania danych:")
    print("1) Z czynnosciami poprzedzajacymi")
    print("2) Z nastepstwem zdarzen")

    while True:
        try:
            opcja = int(input("Wybieram opcje nr: "))
            if opcja in (1, 2):
                break
        except ValueError:
            pass
        print("Niepoprawny wybor!")

    print("\n======================================")

    dane = wczytaj_dane_v1() if opcja == 1 else wczytaj_dane_v2()
    dane = oblicz_cpm(dane)

    print("======================================")
    wypisz(dane)

    rysuj_gantty(dane)
    print(dane)

    rysuj_cpm(dane)
    print("\nKoniec!")

if __name__ == "__main__":
    main()