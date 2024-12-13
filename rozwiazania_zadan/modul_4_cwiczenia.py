def zadanie_3():
    print("Zadanie 3")
    a = float(input("Podaj liczbę a: "))
    b = float(input("Podaj liczbę b: "))
    c = float(input("Podaj liczbę c: "))

    if (0 < a <= 10) and (a > b or b > c):
        print("Warunki zostały spełnione.")
    else:
        print("Warunki nie zostały spełnione.")

def zadanie_4():
    print("Zadanie 4")
    for liczba in range(0, 51, 5):
            print(liczba)

def zadanie_5():
    print("Zadanie 5")
    while (dane := input("Podaj liczby (lub 'quit'): ")) != "quit":
        for liczba in dane.split():
            print(f"Kwadrat {liczba} wynosi {float(liczba) ** 2}" if liczba.replace('.', '',1).isdigit() else f"'{liczba}' to nie liczba.")
    print("Zakończono.")

def zadanie_6():
    print("Zadanie 6")
    liczby = [float(d) for d in iter(lambda: input("Podaj liczbę ('stop' kończy): "), "stop") if
              d.replace('.', '', 1).isdigit()]
    print("Lista podanych liczb:", liczby)

def zadanie_9(n=35):
    print("Zadanie 9")

    max_rzad = len(str(n**2)) + 1

    print("    ", end="")
    for i in range(1, n+1):
        print(f"{i:>{max_rzad}}", end="")
    print("\n" + "    " + "-" * 40)

    for i in range(1, n+1):
        print(f"{i:2} |", end="")
        for j in range(1, n+1):
            print(f"{i * j:>{max_rzad}}", end="")
        print()

def zadanie_10():
    print("Zadanie 10")
    while True:
        try:
            height = int(input("Podaj wysokość diamentu (nieparzysta): "))
            if height in range(1, height + 1, 2):
                break
            print("Podaj liczbę nieparzystą!")
        except ValueError:
            print("Nieprawidłowy format. Podaj liczbę całkowitą.")

    for i in list(range(1, height + 1, 2)) + list(range(height - 2, 0, -2)):
        print(" " * (height // 2 - i // 2) + "o" * i)

def wyswietl_menu():
    print("\n--- Moduł 4 rozwiązania zadań. Wybierz zadanie: ---")
    print("3. Zadanie 3")
    print("4. Zadanie 4")
    print("5. Zadanie 5")
    print("6. Zadanie 6")
    print("9. Zadanie 9")
    print("10. Zadanie 10")
    print("20. Powrót do menu głównego")