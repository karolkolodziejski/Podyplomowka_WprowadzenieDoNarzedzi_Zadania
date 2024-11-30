import string

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

def zadanie_4_5():
    miesiace_pl = {
        1: "styczeń",
        2: "luty",
        3: "marzec",
        4: "kwiecień",
        5: "maj",
        6: "czerwiec",
        7: "lipiec",
        8: "sierpień",
        9: "wrzesień",
        10: "październik",
        11: "listopad",
        12: "grudzień"}

    miesiace_en = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December" }

    polaczone_miesiace= {"pl": miesiace_pl, "en": miesiace_en}

    print(polaczone_miesiace["pl"][3])
    print(polaczone_miesiace["en"] [3])

def zadanie_6():
    imie = "Marianna"
    slownik = dict.fromkeys(imie, 1)
    print(slownik)

def zadanie7():
    tekst = input("Wprowadź dowolny łańcuch znaków: ")

    zbior_znakow_lower = string.ascii_lowercase
    zbior_znakow_digits = string.digits

    liczba_znakow = len(tekst)
    liczba_pasujacych_lower = sum(1 for znak in tekst if znak in zbior_znakow_lower)
    liczba_pasujacych_digits = sum(1 for znak in tekst if znak in zbior_znakow_digits)

    procent_pasujacych_lower = (liczba_pasujacych_lower / liczba_znakow) * 100 if liczba_znakow > 0 else 0
    procent_pasujacych_digits = (liczba_pasujacych_digits / liczba_znakow) * 100 if liczba_znakow > 0 else 0

    print(f"Liczba znaków w łańcuchu: {liczba_znakow}")
    print(f"Liczba pasujących znaków do lowercase: {liczba_pasujacych_lower}")
    print(f"Procent znaków pasujących do lowercase: {procent_pasujacych_lower:.2f}%")
    print(f"Liczba pasujących znaków do digits: {liczba_pasujacych_digits}")
    print(f"Procent znaków pasujących do digits: {procent_pasujacych_digits:.2f}%")

def zadanie8():
    start = int(input("Podaj wartość start: "))
    stop = int(input("Podaj wartość stop: "))
    step = int(input("Podaj wartość step: "))

    for i in range(start, stop, step):
        print(i)

def wyswietl_menu():
    print("\n--- Moduł 3 rozwiązania zadań. Wybierz zadanie: ---")
    print("1. Zadania 1,2")
    print("2. Zadanie 3")
    print("3. Zadanie 4,5")
    print("4. Zadanie 6")
    print("5. Zadanie 7")
    print("6. Zadanie 8")
    print("7. Zakończ program")

def pytanie_o_kontynuacje():
    print("\n--- OPCJE ---")
    print("1. Powrót do menu")
    print("2. Przejdź do kolejnego zadania")
    print("3. Zakończ program")
    opcja = input("Wybierz opcję: ").strip()
    return opcja

def main():
    zadania = [zadanie_1_2,zadanie_3,zadanie_4_5,zadanie_6, zadanie7, zadanie8]
    while True:
        wyswietl_menu()
        wybor = input("Wybierz numer zadania (1-6) lub 7, aby zakończyć: ").strip()
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