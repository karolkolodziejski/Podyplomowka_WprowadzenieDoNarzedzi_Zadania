def zadanie3():
    print("Zadanie 3")
    a = float(input("Podaj liczbę a: "))
    b = float(input("Podaj liczbę b: "))
    c = float(input("Podaj liczbę c: "))

    if (0 < a <= 10) and (a > b or b > c):
        print("Warunki zostały spełnione.")
    else:
        print("Warunki nie zostały spełnione.")

def zadanie4():
    print("Zadanie 4")
    for liczba in range(0, 51, 5):
            print(liczba)

def zadanie5():
    print("Zadanie 5")
    while (dane := input("Podaj liczby (lub 'quit'): ")) != "quit":
        for liczba in dane.split():
            print(f"Kwadrat {liczba} wynosi {float(liczba) ** 2}" if liczba.replace('.', '',1).isdigit() else f"'{liczba}' to nie liczba.")
    print("Zakończono.")

def zadanie6():
    print("Zadanie 6")
    liczby = [float(d) for d in iter(lambda: input("Podaj liczbę ('stop' kończy): "), "stop") if
              d.replace('.', '', 1).isdigit()]
    print("Lista podanych liczb:", liczby)

def zadanie9(n=35):
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

def zadanie10():
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
    print("1. Zadanie 3")
    print("2. Zadanie 4")
    print("3. Zadanie 5")
    print("4. Zadanie 6")
    print("5. Zadanie 9")
    print("6. Zadanie 10")
    print("7. Zakończ program")

def pytanie_o_kontynuacje():
    print("\n--- OPCJE ---")
    print("1. Powrót do menu")
    print("2. Przejdź do kolejnego zadania")
    print("3. Zakończ program")
    opcja = input("Wybierz opcję: ").strip()
    return opcja

def main():
    zadania = [zadanie3,zadanie4,zadanie5,zadanie6, zadanie9, zadanie10]
    while True:
        wyswietl_menu()
        wybor = input("Wybierz numer zadania (1-4) lub 7, aby zakończyć: ").strip()
        if wybor == '7':
            print("Koniec programu.")
            break
        elif wybor in map(str, range(1, len(zadania) + 1)):
            index = int(wybor) - 1
            zadania[index]()
            while True:
                opcja = pytanie_o_kontynuacje()
                if opcja == '1':
                    break
                elif opcja == '2':
                    if index + 1 < len(zadania):
                        index += 1
                        zadania[index]()
                    else:
                        print("Nie ma kolejnego zadania. Powrót do menu.")
                        break
                elif opcja == '3':
                    print("Koniec programu.")
                    return
                else:
                    print("Niepoprawna opcja. Spróbuj ponownie.")
        else:
            print("Niepoprawny wybór. Spróbuj ponownie.")


if __name__ == "__main__":
    main()