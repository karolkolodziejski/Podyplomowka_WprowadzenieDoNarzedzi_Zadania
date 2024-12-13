def zadanie_1():
    print("Zadanie 1")
    data = input("Podaj linię danych: ")
    source_separator = input("Podaj separator źródłowy: ")
    target_separator = input("Podaj separator docelowy: ")
    split_data = data.split(source_separator)
    result = target_separator.join(split_data)
    print("Wynik:", result)

def zadanie_2():
    print("Zadanie 2")
    input_string = input("Podaj łańcuch znaków: ")
    method = len(input_string) // 2
    first_part, second_part = input_string[:method], input_string[method:]
    print("Pierwsza część:", first_part)
    print("Druga część:", second_part)

def zadanie_3():
    print("Zadanie 3")
    text = input("Podaj ciąg znaków:")
    print("Metoda title():", text.title())
    print("Metoda capitalize():", text.capitalize())
    print("Metoda zfill():", text.zfill(25))
    print("Metoda upper():", text.upper())
    print("Metoda count('a'):", text.count('a'))
    print("Metoda center():", text.center(30, '-'))

def zadanie_4():
    print("Zadanie 4")
    wejscie = input("Podaj dowolny łańcuch znaków: ")
    print(f"Łańcuch '{wejscie}' isalpha: {wejscie.isalpha()}")
    print(f"Łańcuch '{wejscie}' isascii: {wejscie.isascii()}")
    print(f"Łańcuch '{wejscie}' isprintable: {wejscie.isprintable()}")
    print(f"Łańcuch '{wejscie}' istitle: {wejscie.istitle()}")
    print(f"Łańcuch '{wejscie}' isupper: {wejscie.isupper()}")
    print(f"Łańcuch '{wejscie}' isdecimal: {wejscie.isdecimal()}")

def zadanie_5():
    print("Zadanie 5")
    wartosc= input("Podaj liczbę:")

    try:
        liczba=float(wartosc)
    except ValueError:
        print("Nie podałeś liczby!")
        return

    print(f"{liczba:>10}")
    print(f"{liczba:<10}")
    pi = 3.14159
    print(f"{pi:.2f}")
    print(f"{liczba:+}")
    print(f"{-liczba:+}")
    print(f"{liczba:*^10}")

def zadanie_6():
    print("Zadanie 6")
    unicode_codes = [
        "\u2713",
        "\u2600",
        "\u2601",
        "\u2668",
        "\u265A",
        "\u2654",
        "\u271D",
        "\u262E",
        "\u2639",
        "\u262A"
    ]
    for symbol in unicode_codes:
        print(f"{symbol} - {ord(symbol):08X}")

def wyswietl_menu():
    print("\n--- Moduł 2 rozwiązania zadań. Wybierz zadanie: ---")
    print("1. Zadanie 1")
    print("2. Zadanie 2")
    print("3. Zadanie 3")
    print("4. Zadanie 4")
    print("5. Zadanie 5")
    print("6. Zadanie 6")
    print("20. Powrót do menu głównego")