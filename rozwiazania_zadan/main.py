# main.py
import sys

def zaladuj_modul(modul_name):
    try:
        modul = __import__(modul_name)
        return modul
    except ImportError:
        print(f"Nie udało się załadować modułu {modul_name}")
        return None

def uruchom_zadanie(modul, zadanie_num):
    zadanie_func = getattr(modul, f"zadanie_{zadanie_num}", None)
    if zadanie_func:
        zadanie_func()
    else:
        print("Niepoprawny numer zadania!")

def wyswietl_menu_glowne():
    print("\n--- Menu główne ---")
    print("1. Moduł ćwiczeniowy 2")
    print("2. Moduł ćwiczeniowy 3")
    print("3. Moduł ćwiczeniowy 4")
    print("4. Moduł ćwiczeniowy 5")
    print("5. Zakończ")

def main():
    while True:
        wyswietl_menu_glowne()
        wybor_modulu = input("Wybierz numer modułu (1-5) lub 5, aby zakończyć: ").strip()

        if wybor_modulu == '5':
            print("Koniec programu.")
            break

        if wybor_modulu == '1':
            modul = zaladuj_modul('moduł_2_ćwiczenia')
        elif wybor_modulu == '2':
            modul = zaladuj_modul('modul_3_cwiczenia')
        elif wybor_modulu == '3':
            modul = zaladuj_modul('modul_4_cwiczenia')
        elif wybor_modulu == '4':
            modul = zaladuj_modul('modul_5_cwiczenia')
        else:
            print("Niepoprawny wybór. Spróbuj ponownie.")
            continue

        if modul:
            while True:
                modul.wyswietl_menu()
                wybor_zadania = input("Wybierz numer zadania (20 powraca do menu głównego): ").strip()
                if wybor_zadania in ['20']:
                    break
                uruchom_zadanie(modul, wybor_zadania)

if __name__ == "__main__":
    main()