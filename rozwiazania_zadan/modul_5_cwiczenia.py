import random
import math

def zadanie1():
    a = {1 / x for x in range(1, 11)}
    b = {2 ** x for x in range(11)}
    c = {x for x in b if x % 4 == 0}
    print("Zbiór A:", a)
    print("Zbiór B:", b)
    print("Zbiór C:", c)

def zadanie2():
    n = int(input("Podaj rozmiar macierzy (np. 4 dla macierzy 4x4): "))
    macierz = [[random.randint(1, 100) for _ in range(n)] for _ in range(n)]
    przekatna = [macierz[i][i] for i in range(n)]

    print("\nMacierz:")
    for row in macierz:
        print(row)

    print("\nPrzekątna macierzy:", przekatna)

def zadanie3():
    produkty = {
        "jabłka": "sztuki",
        "mleko": "litr",
        "chleb": "sztuki",
        "ziemniaki": "kg",
        "ser": "kg",
        "pomarańcze": "sztuki",
        "banany": "sztuki",
        "masło": "kg"
    }
    produkty_na_sztuki = [produkt for produkt, jednostka in produkty.items() if jednostka == "sztuki"]
    print("Produkty na sztuki:", produkty_na_sztuki)

def zadanie4():
    imie = str(input("Podaj swoje imie:"))
    print("Witaj", imie)

def zadanie5():
    try:
        value_input = input("Podaj wartość (domyślnie 4): ").strip()
        if value_input:
            value = int(value_input)
        else:
            value = 4
    except ValueError:
        print("Nieprawidłowa wartość. Użyto domyślnej wartości 4.")
        value = 4
    for _ in range(value):
        print(" ".join([str(value)] * value))

def zadanie6():
    try:
        liczby = input("Podaj liczby oddzielone przecinkiem:").split(",")
        if len(liczby) == 0:
            print("Brak liczb. Wynik: 1.0")
            return 1.0
        else:
            iloczyn = 1.0
        for i in liczby:
            iloczyn *= float(i)
        print("Iloczyn liczb wynosi:", iloczyn)
        return iloczyn
    except ValueError:
        print("Wprowadzono nieprawidłowe dane. Upewnij się, że podajesz liczby oddzielone przecinkami.")
        return None

def zadanie7():
    druzyny = {}
    n = int(input("Podaj liczbe drużyn:"))

    for _ in range(n):
        nazwa = input("Podaj nazwe drużyny:")
        punkty = int(input("Podaj punkty drużyny:"))
        druzyny[nazwa] = punkty

    suma_punktow = sum(druzyny.values())

    print(f"Suma wszystkich punktów: {suma_punktow}")

def wyswietl_menu():
    print("\n--- Moduł 5 rozwiązania zadań. Wybierz zadanie: ---")
    print("1. Zadanie 1")
    print("2. Zadanie 2")
    print("3. Zadanie 3")
    print("4. Zadanie 4")
    print("5. Zadanie 5")
    print("6. Zadanie 6")
    print("7. Zadanie 7")
    print("20. Powrót do menu głównego")