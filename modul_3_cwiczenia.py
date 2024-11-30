def zadanie_1_2():
    print("Zadanie 1,2")
    lista_wejscie = [1,2,3,4,5,6,7,8,9,10]
    method = len(lista_wejscie) // 2
    podzial1 = lista_wejscie[:method]
    podzial2 = lista_wejscie[method:]
    print(f"Zawartosc podzielonych list to {podzial1}, {podzial2}")

    lista1 = [podzial1]
    print(f"Zawartosc listy 1 to {lista1}")

    lista_polaczona = podzial1 + podzial2
    print(f"Połączone listy to: {lista_polaczona}")

    lista_polaczona.insert(0,0)

    print(f"Lista połączona po dodaniu 0 to: {lista_polaczona}")

    lista_kopia = lista_polaczona.copy()
    print(f"Kopia listy: {lista_kopia}")

    lista_kopia.sort(reverse=True)
    print(f"Kopia listy posortowana malejąco: {lista_kopia}")

def zadanie_3():
    print("Zadanie 3")
    tekst = input("Wprowadź tekst:")

    znaki_unikalne = list(set(tekst.lower()))
    znaki_unikalne.sort()

    print(f"Unikalne znaki alfabetyczne to: {''.join(znaki_unikalne)}")

def wyswietl_menu():
    print("\n--- Moduł 3 rozwiązania zadań. Wybierz zadanie: ---")
    print("1. Zadania 1,2")
    print("2. Zadanie 3")
    print("3. Zadanie 4")
    print("4. Zadanie 5")
    print("5. Zadanie 6")
    print("6. Zadanie 7")
    print("7. Zadanie 8")
    print("8. Zakończ program")

def pytanie_o_kontynuacje():
    print("\n--- OPCJE ---")
    print("1. Powrót do menu")
    print("2. Przejdź do kolejnego zadania")
    print("3. Zakończ program")
    opcja = input("Wybierz opcję: ").strip()
    return opcja

def main():
    zadania = [zadanie_1_2,zadanie_3]
    while True:
        wyswietl_menu()
        wybor = input("Wybierz numer zadania (1-6) lub 7, aby zakończyć: ").strip()
        if wybor == '8':
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