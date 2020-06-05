#To jest gra "Postaw na milion". Brakuje niestety timera odliczającego minutę dla każdej rundy.
import random
import time
import os

def poziom_gry_cztery_zapadki(k1, k2, k3, k4, pieniadze, numer_poziomu):
    def poprawna_zapadka(kategoria): #określanie prawidłowej zapadki dla danego pytania
        n = random.randint(0,2)
        print("Odpowiedzi to:")
        for odpowiedz in kategoria[n][1]:
            time.sleep(1)
            print(odpowiedz)
        time.sleep(1)
        print("A oto pytanie")
        print(kategoria[n][0])

        literka = "".join(kategoria[n][2])
        return "zapadka_" + literka

    def kladzenie_banknotow(zapadka, identyfikator, ilosc_pieniedzy): #pierwsze rozkładanie
        liczba_A = -1
        while liczba_A < 0 or liczba_A > pieniadze:
            print("Ile plików banknotów chcesz położyć na zapadkę", identyfikator,"?")
            liczba_A = int(input())
            if not liczba_A < 0 and not liczba_A > pieniadze:
                slownik[zapadka] = liczba_A
                ilosc_pieniedzy -= liczba_A
                print("Pozostało ci jeszcze tyle plików:", ilosc_pieniedzy)
                return ilosc_pieniedzy
            else:
                print("Liczba nieprawidłowa")

    def przekladanie_pieniedzy(zapadka, identyfikator, ilosc_pieniedzy): #początkowe przekładanie, tuż po pierwszym rozłożeniu
        while True:
            print("Ile pieniędzy chcesz zabrać z zapadki", identyfikator, "?")
            ilosc = int(input())
            if not ilosc < 0 and ilosc <= int(slownik[zapadka]):
                roznica = int(slownik[zapadka]) - ilosc
                slownik[zapadka] = roznica
                ilosc_pieniedzy += ilosc
                print("Teraz na zapadce", identyfikator, "znajduje się", roznica, "banknotów")
                return ilosc_pieniedzy
                break
            else:
                print("Liczba nieprawidłowa!")

    def umieszczanie_banknotow(zapadka, identyfikator, ilosc_pieniedzy): #sluzy do kladzenia banknktow w "drugiej turze" rozkladania.
        while True:
            print("Ile plików banknotów chcesz położyć na zapadkę", identyfikator, "?")
            liczba = int(input())
            if not liczba < 0 and not liczba > nowa_liczba_pieniedzy:
                slownik[zapadka] = int(slownik[zapadka]) + liczba
                ilosc_pieniedzy -= liczba
                print("Pozostało ci jeszcze tyle plików:", ilosc_pieniedzy)
                print("Teraz zapadki wyglądają tak", slownik)
                return ilosc_pieniedzy
                break
            else:
                print("Liczba nieprawidłowa")

    def zabieranie_banknotow(zapadka, identyfikator, ilosc_pieniedzy): #sluzy do zabierania banknotów w drugiej turze
        while True:
            print("Ile pieniędzy chcesz zabrać z zapadki", identyfikator, "?")
            ilosc = int(input())
            if not ilosc < 0 and ilosc <= int(slownik[zapadka]):
                roznica = int(slownik[zapadka]) - ilosc
                slownik[zapadka] = roznica
                ilosc_pieniedzy += ilosc
                print("Masz teraz w rękach taką liczbę banknotów:", ilosc_pieniedzy)
                print("Teraz na zapadce", identyfikator, "znajduje się", roznica, "banknotów")
                return ilosc_pieniedzy
                break
            else:
                print("Liczba nieprawidłowa!")

    def obwarowanie_przed_idiotami(pytanie, opcja1, opcja2, opcja3, opcja4):
          odpowiedz = ""
          while odpowiedz != opcja1 and odpowiedz != opcja2 and odpowiedz != opcja3 and odpowiedz != opcja4:
              print(pytanie)
              odpowiedz = input()
              if odpowiedz != opcja1 and odpowiedz != opcja2 and odpowiedz != opcja3 and odpowiedz != opcja4:
                  print("Nieprawdiłowa wartość!")
              elif odpowiedz == opcja1 or odpowiedz == opcja2 or odpowiedz == opcja3 or odpowiedz == opcja4:
                  return odpowiedz

    print("Poziom", numer_poziomu)
    kategorie_poziomu = [k1,k2,k3,k4]

    wylosowana_kategoria1 = ""
    wylosowana_kategoria2 = ""
    while wylosowana_kategoria1 == wylosowana_kategoria2:
        wylosowana_kategoria1 = random.choice(kategorie_poziomu)
        wylosowana_kategoria2 = random.choice(kategorie_poziomu)


    print("Kategorie do wyboru to:")
    print("1)", wylosowana_kategoria1[3])
    print("2)", wylosowana_kategoria2[3])
    print("Wpisz numer wybranej kategorii")
    wybrany_numer = int(input())
    if wybrany_numer == 1:
        prawidlowa_zapadka = poprawna_zapadka(wylosowana_kategoria1)
    elif wybrany_numer == 2:
        prawidlowa_zapadka = poprawna_zapadka(wylosowana_kategoria2)


    print("Masz", pieniadze, "plików banknotów. Teraz będziesz rozkładał pliki banknotów na zapadkach. Jedna z zapadek musi pozostać pusta.")
    slownik = {"zapadka_A":"banknoty", "zapadka_B":"banknoty", "zapadka_C":"banknoty", "zapadka_D":"banknoty"}
    pliki_na_poczatku = pieniadze

    while True:
        pieniadze = kladzenie_banknotow("zapadka_A","A", pieniadze)
        pieniadze = kladzenie_banknotow("zapadka_B","B", pieniadze)
        pieniadze = kladzenie_banknotow("zapadka_C","C", pieniadze)
        print("Dla zapadki D pozostało tyle plików:", pieniadze)
        liczba_D = pieniadze
        if not liczba_D < 0 and not liczba_D > pieniadze:
            slownik["zapadka_D"] = liczba_D
        else:
            print("Liczba nieprawidłowa")
        if not 0 in slownik.values():
            print("Nie pozostawiłeś pustej zapadki! Popraw to.")
            pieniadze = pliki_na_poczatku
        else:
            break
    odpowiedz_zmiana = obwarowanie_przed_idiotami("""Tak wyglądają zapadki:""" + str(slownik) + """.Czy chcesz je zmienić? (Wpisz \"T\" jeśli \"Tak\" lub \"N\" jeśli \"Nie\")""", "T", "N", "N", "T")
    nowa_liczba_pieniedzy = 0
    if odpowiedz_zmiana == "N":
        if 0 in slownik.values():
            if slownik[str(prawidlowa_zapadka)] == 0:
                print("Przegrałeś!")
                time.sleep(7)
                os.system("cls")
                return 0
            else:
                pieniadze = slownik[str(prawidlowa_zapadka)]
                print("Brawo! Na prawidłowej zapadce znajdowały się banknoty! Liczba zachowanych przez Ciebie plików to:", pieniadze)
                time.sleep(7)
                os.system("cls")
                return pieniadze
    if odpowiedz_zmiana == "T":
        odpowiedz = obwarowanie_przed_idiotami("Z której zapadki chcesz zabrać pieniądze?", "A", "B", "C", "D")
        if odpowiedz == "A":
            nowa_liczba_pieniedzy = przekladanie_pieniedzy("zapadka_A", "A", nowa_liczba_pieniedzy)
        elif odpowiedz == "B":
            nowa_liczba_pieniedzy = przekladanie_pieniedzy("zapadka_B", "B", nowa_liczba_pieniedzy)
        elif odpowiedz == "C":
            nowa_liczba_pieniedzy = przekladanie_pieniedzy("zapadka_C", "C", nowa_liczba_pieniedzy)
        elif odpowiedz == "D":
            nowa_liczba_pieniedzy = przekladanie_pieniedzy("zapadka_D", "D", nowa_liczba_pieniedzy)
    if odpowiedz_zmiana == "T":
        while True:
            odpowiedz = obwarowanie_przed_idiotami("""Czy teraz chcesz położyć pieniądze na inną zapadkę (wciśnij \"P\"), czy znów zabrać pienądze z zapadki? (wciśnij \"Z\".
            Jeżeli chcesz zakończyć rozkładanie pieniędzy wciśnij \"Q\"""", "Q", "P", "Z", "Z")
            if odpowiedz == "P":
                odpowiedz = obwarowanie_przed_idiotami("Na którą zapadkę chcesz położyc pieniądze?", "A", "B", "C", "D")
                if odpowiedz == "A":
                    nowa_liczba_pieniedzy = umieszczanie_banknotow("zapadka_A", "A", nowa_liczba_pieniedzy)
                elif odpowiedz == "B":
                    nowa_liczba_pieniedzy = umieszczanie_banknotow("zapadka_B", "B", nowa_liczba_pieniedzy)
                elif odpowiedz == "C":
                    nowa_liczba_pieniedzy = umieszczanie_banknotow("zapadka_C", "C", nowa_liczba_pieniedzy)
                elif odpowiedz == "D":
                    nowa_liczba_pieniedzy = umieszczanie_banknotow("zapadka_D", "D", nowa_liczba_pieniedzy)
            elif odpowiedz == "Z":
                odpowiedz = obwarowanie_przed_idiotami("Z której zapadki chcesz zabrać pieniądze?", "A", "B", "C", "D")
                if odpowiedz == "A":
                    nowa_liczba_pieniedzy = zabieranie_banknotow("zapadka_A", "A", nowa_liczba_pieniedzy)
                elif odpowiedz == "B":
                    nowa_liczba_pieniedzy = zabieranie_banknotow("zapadka_B", "B", nowa_liczba_pieniedzy)
                elif odpowiedz == "C":
                    nowa_liczba_pieniedzy = zabieranie_banknotow("zapadka_C", "C", nowa_liczba_pieniedzy)
                elif odpowiedz == "D":
                    nowa_liczba_pieniedzy = zabieranie_banknotow("zapadka_D", "D", nowa_liczba_pieniedzy)
            elif odpowiedz == "Q":
                if nowa_liczba_pieniedzy > 0:
                    print("Nie umieściłeś na zapadkach wszystkich banknotów!")
                if not 0 in slownik.values():
                    print("Nie pozostawiłeś pustej zapadki! Popraw to.")
                    print("Teraz zapadki wyglądają tak:", slownik, "a ty masz w rękach", nowa_liczba_pieniedzy, "banknotów")

                else:
                        if slownik[str(prawidlowa_zapadka)] == 0:
                            print("Przegrałeś!")
                            time.sleep(7)
                            os.system("cls")
                            return 0
                        else:
                            pieniadze = slownik[str(prawidlowa_zapadka)]
                            print("Brawo! Na prawdiłowej zapadce znajdowały się banknoty. Liczba zachowanych przez Ciebie plików to:", pieniadze, ". Przechodzisz do kolejnego poziomu!")
                            time.sleep(7)
                            os.system("cls")
                            return pieniadze
                        break

def poziom_gry_trzy_zapadki(k1, k2, k3, k4, pieniadze, numer_poziomu):
    def poprawna_zapadka(kategoria): #określanie prawidłowej zapadki dla danego pytania
        n = random.randint(0,2)
        print("Odpowiedzi to:")
        for odpowiedz in kategoria[n][1]:
            time.sleep(1)
            print(odpowiedz)
        time.sleep(1)
        print("A oto pytanie")
        print(kategoria[n][0])

        literka = "".join(kategoria[n][2])
        return "zapadka_" + literka

    def kladzenie_banknotow(zapadka, identyfikator, ilosc_pieniedzy): #pierwsze rozkładanie
        liczba_A = -1
        while liczba_A < 0 or liczba_A > pieniadze:
            print("Ile plików banknotów chcesz położyć na zapadkę", identyfikator,"?")
            liczba_A = int(input())
            if not liczba_A < 0 and not liczba_A > pieniadze:
                slownik[zapadka] = liczba_A
                ilosc_pieniedzy -= liczba_A
                print("Pozostało ci jeszcze tyle plików:", ilosc_pieniedzy)
                return ilosc_pieniedzy
            else:
                print("Liczba nieprawidłowa")

    def przekladanie_pieniedzy(zapadka, identyfikator, ilosc_pieniedzy): #początkowe przekładanie, tuż po pierwszym rozłożeniu
        while True:
            print("Ile pieniędzy chcesz zabrać z zapadki", identyfikator, "?")
            ilosc = int(input())
            if not ilosc < 0 and ilosc <= int(slownik[zapadka]):
                roznica = int(slownik[zapadka]) - ilosc
                slownik[zapadka] = roznica
                ilosc_pieniedzy += ilosc
                print("Teraz na zapadce", identyfikator, "znajduje się", roznica, "banknotów")
                return ilosc_pieniedzy
                break
            else:
                print("Liczba nieprawidłowa!")

    def umieszczanie_banknotow(zapadka, identyfikator, ilosc_pieniedzy): #sluzy do kladzenia banknktow w "drugiej turze" rozkladania.
        while True:
            print("Ile plików banknotów chcesz położyć na zapadkę", identyfikator, "?")
            liczba = int(input())
            if not liczba < 0 and not liczba > nowa_liczba_pieniedzy:
                slownik[zapadka] = int(slownik[zapadka]) + liczba
                ilosc_pieniedzy -= liczba
                print("Pozostało ci jeszcze tyle plików:", ilosc_pieniedzy)
                print("Teraz zapadki wyglądają tak", slownik)
                return ilosc_pieniedzy
                break
            else:
                print("Liczba nieprawidłowa")

    def zabieranie_banknotow(zapadka, identyfikator, ilosc_pieniedzy): #sluzy do zabierania banknotów w drugiej turze
        while True:
            print("Ile pieniędzy chcesz zabrać z zapadki", identyfikator, "?")
            ilosc = int(input())
            if not ilosc < 0 and ilosc <= int(slownik[zapadka]):
                roznica = int(slownik[zapadka]) - ilosc
                slownik[zapadka] = roznica
                ilosc_pieniedzy += ilosc
                print("Masz teraz w rękach taką liczbę banknotów:", ilosc_pieniedzy)
                print("Teraz na zapadce", identyfikator, "znajduje się", roznica, "banknotów")
                return ilosc_pieniedzy
                break
            else:
                print("Liczba nieprawidłowa!")
    def obwarowanie_przed_idiotami(pytanie, opcja1, opcja2, opcja3, opcja4):
          odpowiedz = ""
          while odpowiedz != opcja1 and odpowiedz != opcja2 and odpowiedz != opcja3 and odpowiedz != opcja4:
              print(pytanie)
              odpowiedz = input()
              if odpowiedz != opcja1 and odpowiedz != opcja2 and odpowiedz != opcja3 and odpowiedz != opcja4:
                  print("Nieprawdiłowa wartość!")
              elif odpowiedz == opcja1 or odpowiedz == opcja2 or odpowiedz == opcja3 or odpowiedz == opcja4:
                  return odpowiedz

    print("Poziom", numer_poziomu)
    kategorie_poziomu = [k1,k2,k3,k4]

    wylosowana_kategoria1 = ""
    wylosowana_kategoria2 = ""
    while wylosowana_kategoria1 == wylosowana_kategoria2:
        wylosowana_kategoria1 = random.choice(kategorie_poziomu)
        wylosowana_kategoria2 = random.choice(kategorie_poziomu)


    print("Kategorie do wyboru to:")
    print("1)", wylosowana_kategoria1[3])
    print("2)", wylosowana_kategoria2[3])
    print("Wpisz numer wybranej kategorii")
    wybrany_numer = int(input())
    if wybrany_numer == 1:
        prawidlowa_zapadka = poprawna_zapadka(wylosowana_kategoria1)
    elif wybrany_numer == 2:
        prawidlowa_zapadka = poprawna_zapadka(wylosowana_kategoria2)


    print("Masz", pieniadze, "plików banknotów. Teraz będziesz rozkładał pliki banknotów na zapadkach. Jedna z zapadek musi pozostać pusta.")
    slownik = {"zapadka_A":"banknoty", "zapadka_B":"banknoty", "zapadka_C":"banknoty"}
    pliki_na_poczatku = pieniadze

    while True:
        pieniadze = kladzenie_banknotow("zapadka_A","A", pieniadze)
        pieniadze = kladzenie_banknotow("zapadka_B","B", pieniadze)
        print("Dla zapadki C pozostało tyle plików:", pieniadze)
        liczba_C = pieniadze
        if not liczba_C < 0 and not liczba_C > pieniadze:
            slownik["zapadka_C"] = liczba_C
        else:
            print("Liczba nieprawidłowa")
        if not 0 in slownik.values():
            print("Nie pozostawiłeś pustej zapadki! Popraw to.")
            pieniadze = pliki_na_poczatku
        else:
            break
    odpowiedz_zmiana = obwarowanie_przed_idiotami("""Tak wyglądają zapadki:""" + str(slownik) + """.Czy chcesz je zmienić? (Wpisz \"T\" jeśli \"Tak\" lub \"N\" jeśli \"Nie\")""", "T", "N", "N", "T")
    nowa_liczba_pieniedzy = 0
    if odpowiedz_zmiana == "N":
        if 0 in slownik.values():
            if slownik[str(prawidlowa_zapadka)] == 0:
                print("Przegrałeś!")
                time.sleep(7)
                os.system("cls")
                return 0
            else:
                pieniadze = slownik[str(prawidlowa_zapadka)]
                print("Brawo! Na prawidłowej zapadce znajdowały się banknoty! Liczba zachowanych przez Ciebie plików to:", pieniadze)
                time.sleep(7)
                os.system("cls")
                return pieniadze
    if odpowiedz_zmiana == "T":
        odpowiedz = obwarowanie_przed_idiotami("Z której zapadki chcesz zabrać pieniądze?", "A", "B", "C", "C")
        if odpowiedz == "A":
            nowa_liczba_pieniedzy = przekladanie_pieniedzy("zapadka_A", "A", nowa_liczba_pieniedzy)
        elif odpowiedz == "B":
            nowa_liczba_pieniedzy = przekladanie_pieniedzy("zapadka_B", "B", nowa_liczba_pieniedzy)
        elif odpowiedz == "C":
            nowa_liczba_pieniedzy = przekladanie_pieniedzy("zapadka_C", "C", nowa_liczba_pieniedzy)
    if odpowiedz_zmiana == "T":
        while True:
            odpowiedz = obwarowanie_przed_idiotami("""Czy teraz chcesz położyć pieniądze na inną zapadkę (wciśnij \"P\"), czy znów zabrać pienądze z zapadki? (wciśnij \"Z\".
            Jeżeli chcesz zakończyć rozkładanie pieniędzy wciśnij \"Q\"""", "Q", "P", "Z")
            if odpowiedz == "P":
                odpowiedz = obwarowanie_przed_idiotami("Na którą zapadkę chcesz położyć pieniądze?", "A", "A", "B", "C")
                if odpowiedz == "A":
                    nowa_liczba_pieniedzy = umieszczanie_banknotow("zapadka_A", "A", nowa_liczba_pieniedzy)
                elif odpowiedz == "B":
                    nowa_liczba_pieniedzy = umieszczanie_banknotow("zapadka_B", "B", nowa_liczba_pieniedzy)
                elif odpowiedz == "C":
                    nowa_liczba_pieniedzy = umieszczanie_banknotow("zapadka_C", "C", nowa_liczba_pieniedzy)

            elif odpowiedz == "Z":
                print("Z której zapadki chcesz zabrać pieniądze?")
                odpowiedz = input()
                if odpowiedz == "A":
                    nowa_liczba_pieniedzy = zabieranie_banknotow("zapadka_A", "A", nowa_liczba_pieniedzy)
                elif odpowiedz == "B":
                    nowa_liczba_pieniedzy = zabieranie_banknotow("zapadka_B", "B", nowa_liczba_pieniedzy)
                elif odpowiedz == "C":
                    nowa_liczba_pieniedzy = zabieranie_banknotow("zapadka_C", "C", nowa_liczba_pieniedzy)

            elif odpowiedz == "Q":
                if nowa_liczba_pieniedzy > 0:
                    print("Nie umieściłeś na zapadkach wszystkich banknotów!")
                if not 0 in slownik.values():
                    print("Nie pozostawiłeś pustej zapadki! Popraw to.")
                    print("Teraz zapadki wyglądają tak:", slownik, "a ty masz w rękach", nowa_liczba_pieniedzy, "banknotów")

                else:
                        if slownik[str(prawidlowa_zapadka)] == 0:
                            print("Przegrałeś!")
                            return 0
                            time.sleep(7)
                            os.system("cls")
                        else:
                            pieniadze = slownik[str(prawidlowa_zapadka)]
                            print("Brawo! Na prawdiłowej zapadce znajdowały się banknoty. Liczba zachowanych przez Ciebie plików to:", pieniadze, ". Przechodzisz do kolejnego poziomu!")
                            time.sleep(7)
                            os.system("cls")
                            return pieniadze

                        break

def poziom_gry_dwie_zapadki(k1, k2, k3, k4, pieniadze, numer_poziomu):
    def poprawna_zapadka(kategoria): #określanie prawidłowej zapadki dla danego pytania
        n = random.randint(0,2)
        print("Odpowiedzi to:")
        for odpowiedz in kategoria[n][1]:
            time.sleep(1)
            print(odpowiedz)
        time.sleep(1)
        print("A oto pytanie")
        print(kategoria[n][0])

        literka = "".join(kategoria[n][2])
        return "zapadka_" + literka

    def kladzenie_banknotow(zapadka, identyfikator, ilosc_pieniedzy): #pierwsze rozkładanie
        liczba_A = -1
        while liczba_A < 0 or liczba_A > pieniadze:
            print("Ile plików banknotów chcesz położyć na zapadkę", identyfikator,"?")
            liczba_A = int(input())
            if not liczba_A < 0 and not liczba_A > pieniadze:
                slownik[zapadka] = liczba_A
                ilosc_pieniedzy -= liczba_A
                print("Pozostało ci jeszcze tyle plików:", ilosc_pieniedzy)
                return ilosc_pieniedzy
            else:
                print("Liczba nieprawidłowa")

    def przekladanie_pieniedzy(zapadka, identyfikator, ilosc_pieniedzy): #początkowe przekładanie, tuż po pierwszym rozłożeniu
        while True:
            print("Ile pieniędzy chcesz zabrać z zapadki", identyfikator, "?")
            ilosc = int(input())
            if not ilosc < 0 and ilosc <= int(slownik[zapadka]):
                roznica = int(slownik[zapadka]) - ilosc
                slownik[zapadka] = roznica
                ilosc_pieniedzy += ilosc
                print("Teraz na zapadce", identyfikator, "znajduje się", roznica, "banknotów")
                return ilosc_pieniedzy
                break
            else:
                print("Liczba nieprawidłowa!")

    def umieszczanie_banknotow(zapadka, identyfikator, ilosc_pieniedzy): #sluzy do kladzenia banknktow w "drugiej turze" rozkladania.
        while True:
            print("Ile plików banknotów chcesz położyć na zapadkę", identyfikator, "?")
            liczba = int(input())
            if not liczba < 0 and not liczba > nowa_liczba_pieniedzy:
                slownik[zapadka] = int(slownik[zapadka]) + liczba
                ilosc_pieniedzy -= liczba
                print("Pozostało ci jeszcze tyle plików:", ilosc_pieniedzy)
                print("Teraz zapadki wyglądają tak", slownik)
                return ilosc_pieniedzy
                break
            else:
                print("Liczba nieprawidłowa")

    def zabieranie_banknotow(zapadka, identyfikator, ilosc_pieniedzy): #sluzy do zabierania banknotów w drugiej turze
        while True:
            print("Ile pieniędzy chcesz zabrać z zapadki", identyfikator, "?")
            ilosc = int(input())
            if not ilosc < 0 and ilosc <= int(slownik[zapadka]):
                roznica = int(slownik[zapadka]) - ilosc
                slownik[zapadka] = roznica
                ilosc_pieniedzy += ilosc
                print("Masz teraz w rękach taką liczbę banknotów:", ilosc_pieniedzy)
                print("Teraz na zapadce", identyfikator, "znajduje się", roznica, "banknotów")
                return ilosc_pieniedzy
                break
            else:
                print("Liczba nieprawidłowa!")

    def obwarowanie_przed_idiotami(pytanie, opcja1, opcja2, opcja3, opcja4):
          odpowiedz = ""
          while odpowiedz != opcja1 and odpowiedz != opcja2 and odpowiedz != opcja3 and odpowiedz != opcja4:
              print(pytanie)
              odpowiedz = input()
              if odpowiedz != opcja1 and odpowiedz != opcja2 and odpowiedz != opcja3 and odpowiedz != opcja4:
                  print("Nieprawdiłowa wartość!")
              elif odpowiedz == opcja1 or odpowiedz == opcja2 or odpowiedz == opcja3 or odpowiedz == opcja4:
                  return odpowiedz

    print("Poziom", numer_poziomu)
    kategorie_poziomu = [k1,k2,k3,k4]

    wylosowana_kategoria1 = ""
    wylosowana_kategoria2 = ""
    while wylosowana_kategoria1 == wylosowana_kategoria2:
        wylosowana_kategoria1 = random.choice(kategorie_poziomu)
        wylosowana_kategoria2 = random.choice(kategorie_poziomu)


    print("Kategorie do wyboru to:")
    print("1)", wylosowana_kategoria1[3])
    print("2)", wylosowana_kategoria2[3])
    print("Wpisz numer wybranej kategorii")
    wybrany_numer = int(input())
    if wybrany_numer == 1:
        prawidlowa_zapadka = poprawna_zapadka(wylosowana_kategoria1)
    elif wybrany_numer == 2:
        prawidlowa_zapadka = poprawna_zapadka(wylosowana_kategoria2)


    print("Masz", pieniadze, "plików banknotów. Teraz będziesz rozkładał pliki banknotów na zapadkach. Jedna z zapadek musi pozostać pusta.")
    slownik = {"zapadka_A":"banknoty", "zapadka_B":"banknoty"}
    pliki_na_poczatku = pieniadze

    while True:
        pieniadze = kladzenie_banknotow("zapadka_A","A", pieniadze)
        print("Dla zapadki B pozostało tyle plików:", pieniadze)
        liczba_B = pieniadze
        if not liczba_B < 0 and not liczba_B > pieniadze:
            slownik["zapadka_B"] = liczba_B
        else:
            print("Liczba nieprawidłowa")
        if not 0 in slownik.values():
            print("Nie pozostawiłeś pustej zapadki! Popraw to.")
            pieniadze = pliki_na_poczatku

        else:
            break
    odpowiedz_zmiana = obwarowanie_przed_idiotami("""Tak wyglądają zapadki:""" + str(slownik) + """.Czy chcesz je zmienić? (Wpisz \"T\" jeśli \"Tak\" lub \"N\" jeśli \"Nie\")""", "T", "N", "N", "T")
    nowa_liczba_pieniedzy = 0
    if odpowiedz_zmiana == "N":
        if 0 in slownik.values():
            if slownik[str(prawidlowa_zapadka)] == 0:
                print("Przegrałeś!")
                time.sleep(7)
                os.system("cls")
                return 0
            else:
                pieniadze = slownik[str(prawidlowa_zapadka)]
                print("Brawo! Na prawidłowej zapadce znajdowały się banknoty! Liczba zachowanych przez Ciebie plików to:", pieniadze)
                time.sleep(7)
                os.system("cls")
                return pieniadze
    if odpowiedz_zmiana == "T":
        odpowiedz = obwarowanie_przed_idiotami("Z której zapadki chcesz zabrac pieniądze?", "A", "A", "B", "B")
        if odpowiedz == "A":
            nowa_liczba_pieniedzy = przekladanie_pieniedzy("zapadka_A", "A", nowa_liczba_pieniedzy)
        elif odpowiedz == "B":
            nowa_liczba_pieniedzy = przekladanie_pieniedzy("zapadka_B", "B", nowa_liczba_pieniedzy)
    if odpowiedz_zmiana == "T":
        while True:
            odpowiedz = obwarowanie_przed_idiotami("""Czy teraz chcesz położyć pieniądze na inną zapadkę (wciśnij \"P\"), czy znów zabrać pienądze z zapadki? (wciśnij \"Z\".
            Jeżeli chcesz zakończyć rozkładanie pieniędzy wciśnij \"Q\"""", "Q", "P", "Z", "Z")

            if odpowiedz == "P":
                odpowiedz = obwarowanie_przed_idiotami("Na którą zapadkę chcesz położyć pieniądze?", "A", "A", "B", "B")
                if odpowiedz == "A":
                    nowa_liczba_pieniedzy = umieszczanie_banknotow("zapadka_A", "A", nowa_liczba_pieniedzy)
                elif odpowiedz == "B":
                    nowa_liczba_pieniedzy = umieszczanie_banknotow("zapadka_B", "B", nowa_liczba_pieniedzy)
            elif odpowiedz == "Z":
                odpowiedz = obwarowanie_przed_idiotami("Z której zapadki chcesz zabrac pieniądze?", "A", "A", "B", "B")
                if odpowiedz == "A":
                    nowa_liczba_pieniedzy = zabieranie_banknotow("zapadka_A", "A", nowa_liczba_pieniedzy)
                elif odpowiedz == "B":
                    nowa_liczba_pieniedzy = zabieranie_banknotow("zapadka_B", "B", nowa_liczba_pieniedzy)

            elif odpowiedz == "Q":
                if nowa_liczba_pieniedzy > 0:
                    print("Nie umieściłeś na zapadkach wszystkich banknotów!")
                if not 0 in slownik.values():
                    print("Nie pozostawiłeś pustej zapadki! Popraw to.")
                    print("Teraz zapadki wyglądają tak:", slownik, "a ty masz w rękach", nowa_liczba_pieniedzy, "banknotów")

                else:
                        if slownik[str(prawidlowa_zapadka)] == 0:
                            print("Przegrałeś!")
                            time.sleep(7)
                            os.system("cls")
                            return 0
                        else:
                            pieniadze = slownik[str(prawidlowa_zapadka)]
                            print("Brawo! Na prawdiłowej zapadce znajdowały się banknoty. Liczba zachowanych przez Ciebie plików to:", pieniadze, ". Przechodzisz do kolejnego poziomu!")
                            time.sleep(7)
                            os.system("cls")
                            return pieniadze
                        break
zachowane_pieniadze = 1
if zachowane_pieniadze != 0:
    p1_zwierzeta = [[["Które z tych zwierząt jest tradycyjnie nazywane najlepszym przyjacielem człowieka?"],["A) Kot","B) Chomik","C) Pies","D) Papuga"],["C"]], [["Które z tych zwierząt nie występuje naturalnie w Afryce?"], ["A) Lew", "B) Panda Wielka", "C) Zebra", "D) Żyrafa"], ["B"]], [["Jaki ptak znajduje się na polskim godle?"], ["A) Kondor wielki", "B) Orzeł bielik", "C) Jastrząb zwyczajny", "D) Biała gołębica"], ["B"]], ["Zwierzęta"]]
    p1_przyslowia = [[["Dokończ zdanie: a co po czyjej wielkości, jak nie ma w głowie…"],["A) radości", "B) mądrości", "C) ufności", "D) miłości"],["B"]], [["Dokończ zdanie: czym skorupka za młodu nasiąknie, tym na starość…"], ["A) się stanie", "B) trąci", "C) będzie", "D) się okaże"], ["B"]], [["Najpopularniejszym polskim przysłowiem w roku 2018 zostało:"],
    ["A) łaska pańska na pstrym koniu jeździ ", "B) Grosz do grosza, a będzie kokosza","C) Dzieci i ryby głosu nie mają ","D) Bez pracy nie ma kołaczy"], ["D"]], ["Przysłowia"]]
    p1_swieta = [[["W Polsce obchodzimy święto flagi:"],["A) 2 maja", "B) 3 maja", "C) 2 czerwca", "D) 3 czerwca"], ["A"]], [["Tradycyjną potrawą spożywaną z okazji Dnia Dziękczynienia jest:"],["A) pieczony indyk", "B) kurczak z rożna", "C) bażant z pieca", "D) kaczka po wietnamsku"], ["A"]], [["Polowanie na jajka to zwyczaj zwiazany z: "], ["A) Wielkanocą", "B) Bożym Narodzeniem", "C) Halloween", "D) Chanuką"], ["A"]], ["Święta"]]
    p1_mitologia_grecka = [[["Który z podanych herosów w mitologii greckiej uchodził za syna Zeusa?"],["A) Achilles", "B) Jazon", "C) Perseusz", "D) Hippotoon"], ["C"]], [["Która z podanych bogiń była opiekunką ogniska domowego?"],["A) Atena", "B) Artemida", "C) Demeter", "D) Hestia"], ["D"]], [["Kim były Erynie?"], ["A) boginiami losu", "B) boginiami zemsty", "C) bóstwami morskimi", "D) boginiami młodości"], ["B"]], ["Mitologia grecka"]]
    zachowane_pieniadze = poziom_gry_cztery_zapadki(p1_zwierzeta, p1_przyslowia, p1_swieta, p1_mitologia_grecka, 40, "1")
if zachowane_pieniadze != 0:
    p2_krolowie = [[["Kto był pierwszym koronowanym królem Polski?"],["A) Bolesław Chrobry","B) Mieszko I","C) Bolesław Śmiały","D) Mieszko II"],["A"]], [["Który król Polski był mężem Królowej Jadwigi Andegaweńskiej?"], ["A) Bolesław Chrobry", "B) Mieszko I", "C) Bolesław Krzywousty", "D) Władysław Jagiełło"], ["D"]], [["Za rządów którego króla wydano przywilej koszycki?"], ["A) Ludwika Węgierskiego", "B) Stanisława Augusta Poniatowskiego", "C) Bolesława Śmiałego", "D) Władysława Jagiełły"], ["A"]], ["Królowie Polski"]]
    p2_sporty = [[["Który z wymienionych sportów nie jest uznawany za sport ekstremalny? "],["A) Rower górski","B) Wyścigi łodzi motorowych","C) Spacer po linie","D) Kajakarstwo"],["D"]], [["Początek bungee jumpingu miał miejsce:"], ["A) W Wielkiej Brytanii", "B) W Rosji", "C) W Norwegii", "D) W Polsce"], ["A"]], [["W którym wieku Janina Mey jako pierwsza Polka wykonała skok ze spadochronem? "], ["A) XX", "B) XIX", "C) XVIII", "D) XVI"], ["B"]], ["Sporty ekstremalne"]]
    p2_ogrodnictwo = [[["Nowalijki to warzywa, które ukazują się najczęściej: "],["A) Późnym latem","B) Wczesną wiosną","C) Wczesną jesienią","D) Na przełomie wiosny i lata"],["C"]], [["Gargamele, malinowe, bawole serca to popularne gatunki:"], ["A) Papryki", "B) Ogórków", "C) Pomidorów", "D) Cebuli"], ["C"]], [["“Zimni ogrodnicy” to okres, w którym występują majowe przymrozki. Nazwa tego zjawiska jest związana ze wspomnieniem świętych:"],
    ["A) św. Pawła, św. Piotra, św. Alojzego, św. Anny ", "B) św. Pankracego, św. Serwacego, św. Bonifacego, św. Zofii", "C) św. Walentego, św. Józefa, św. Danuty, św. Łukasza", "D) św. Agnieszki, św. Anastazego, św. Ildefonsa, św. Tymoteusza "], ["B"]], ["Ogrodnictwo"]]
    p2_muzfilm = [[["Kto jest autorem muzyki do filmu Christophera Nolana pod tytułem “Interstellar”?"],["A) Thomas Newman","B) Hans Zimmer","C) John Williams","D) James Horner"],["B"]], [["Za muzykę do którego filmu Ennio Morricone otrzymał Oscara w 2016 roku?"], ["A) Pewnego razu na Dzikim Zachodzie", "B) Nienawistna Ósemka", "C) Za garść dolarów", "D) Dawno temu w Ameryce "], ["B"]], [["W którym roku Howard Shore otrzymał Oscara za muzykę do “Władcy Pierścieni - Drużyny Pierścienia”?"],
    ["A) 2003", "B) 2001", "C) 2002", "D) 2004"], ["C"]], ["Muzyka filmowa"]]
    zachowane_pieniadze = poziom_gry_cztery_zapadki(p2_krolowie, p2_sporty, p2_ogrodnictwo, p2_muzfilm, zachowane_pieniadze, "2")
if zachowane_pieniadze != 0:
    p3_miasta_wojewodzkie=[[["Olsztyn jest miastem wojewódzkim którego województwa?"],["A)Warmińsko-mazurskiego","B)Kujawsko-pomorskiego","C)Zachodniopomorskiego","D) Podkarpackiego"],["A"]], [["Które miasto wojewódzkie liczy najwięcej ludności?"], ["A) Kraków", "B) Warszawa", "C) Poznań", "D) Bydgoszcz"], ["B"]], [["W którym mieście  wojewódzkim możemy oglądać Spodek?"], ["A)W Katowicach", "B) W Krakowie", "C) W Bydgoszczy", "D) W Poznaniu"], ["A"]], ["Miasta wojewódzkie"]]
    p3_jedzenie=[[["silnie trująca ryba, będącą tradycyjnym japońskim przysmakiem to:"],["A) Fugu","B) Koi","C) Tara","D) Tsuna "],["A"]], [["Pizza hawajska pochodzi: "], ["A)  z Norwegii ", "B) z Francji", "C) z Kanady", "D) z Wielkiej Brytanii "], ["C"]], [["Co uznawane jest za najsłodszy owoc na świecie?"], ["A) mango", "B) granaty", "C) figi", "D) banan"], ["C"]], ["Jedzenie"]]
    p3_zabytki=[[["Budowę katedry Notre Dame datuje się na:"],["A) XII-XIV wiek","B) XV-XVIII wiek","C) IX-XI wiek ","D) XVIII-XX wiek "],["A"]], [[" Tadź Mahal to: "], ["A) kościół", "B) zamek", "C) pałac", "D)mauzoleum"], ["D"]], [["Stonehenhe znajduje się w:"], ["A)Wielkiej Brytanii", "B)Stanach Zjednoczonych", "C)Chile", "D) Brazylii"], ["A"]], ["Zabytki"]]
    p3_znane_strony_internetowe=[[["Biała, niekompletna kula ułożona z puzzli, to logo jakiej strony internetowej?"],["A) Twittera","B) Google","C) Wikipedii","D) Yahoo!"],["C"]], [["Wymień w poprawnej kolejności kolory znajdujące się na logo strony Google.com:"],
    ["A) Żółty, niebieski, czerwony, niebieski, zielony, żółty", "B) Niebieski, czerwony, żółty, niebieski, zielony, czerwony", "C) Czerwony, zielony, niebieski, czerwony, żółty, niebieski", "D) Zielony, żółty, czerwony, niebieski, czerwony niebieski"], ["B"]], [["W którym roku powstał portal społecznościowy Facebook?"], ["A) 2005", "B) 2006", "C) 2004", "D) 2003"], ["C"]], ["znane strony internetowe"]]
    zachowane_pieniadze = poziom_gry_cztery_zapadki(p3_miasta_wojewodzkie, p3_jedzenie, p3_zabytki, p3_znane_strony_internetowe, zachowane_pieniadze, "3")
if zachowane_pieniadze != 0:
    p4_muzyka_klasyczna=[[["W jakim mieście pochowany jest Fryderyk Chopin?"],["A) W Paryżu","B) W Warszawie","C) W Wilnie ","D) W Krakowie "],["A"]], [[" Które z podanych dzieł skomponował Jan Sebastian Bach?"], ["A) Aria na strunie G", "B) Clair de Lune", "C) Lacrimosa", "D) Dies irae"], ["A"]], [["Kto jest autorem “Jeziora Łabędziego”?"], ["A)Pyotr Ilyich Tchaikovsky", "B)Wolfgang Amadeus Mozart", "C) Karl Ditters von Dittensdorf", "D) Franciszek Liszt"], ["A"]], ["Muzyka klasyczna"]]
    p4_religie=[[["Wedy to święte księgi:"],["A) buddyzmu ","B)hinduizmu","C)islamu","D) judaizmu"],["B"]], [["Za początek islamu uznaje się:"], ["A) VII wiek n.e", "B)V wiek p.n.e", "C) VII wiek p.n.e", "D)V wiek n.e"], ["A"]], [["Na skutek wielkiej schizmy wschodniej: "], ["A)nastąpił podział Kościoła katolickiego ", "B)na tronie papieskim zasiadło trzech papieży jednocześnie ", "C)Wielka Brytania ustanowiła anglicyzm religię narodową ", "D) przeniesiono stolicę papieską z Paryża do Rzymu"], ["A"]], ["Religie i wierzenia"]]
    p4_literatura=[[["Autorem powieści pt. “Lolita” uchodzącej za jedno z najbardziej kontrowersyjnych dzieł w historii jest: "],["A)  Michaił Bułhakow","B) Andriej Płatonow ","C) Vladimir Nabokov ","D)  Dmitrij Bykow"],["C"]], [["“Lalka” Bolesława Prusa to powieść:"], ["A)romantyczna ", "B) pozytywistyczna", "C) oświeceniowa", "D)z okresu XX-lecia międzywojennego"], ["B"]], [["Jaki tytuł nosi najważniejsze dzieło Andrzeja Frycza Modrzewskiego? "],
    ["A)Kazania sejmowe ", "B) Wojna chocimska", "C) O poprawie Rzeczypospolitej", "D) Rytmy albo wiersze polskie "], ["C"]], ["Literatura"]]
    p4_komputery=[[["Która z wymienionych nazw nie jest nazwą języka programowania?"],["A) Python","B) Prolog","C) Braor","D) Nim"],["C"]], [["Który słynny uczony jest nazywany ojcem nowoczesnego systemu binarnego?"], ["A) Gottfried Leibniz", "B) Isaac Newton", "C) Noam Chomsky", "D) Marvin Minsky"], ["A"]], [["Kto jest uznawany za twórcę pierwszego programu komputerowego?"], ["A)Marvin Minsky", "B)Ada Lovelace", "C)Ludwig Wittgenstein", "D) Gottfried Leibniz"], ["B"]], ["Komputery"]]
    zachowane_pieniadze = poziom_gry_cztery_zapadki(p4_muzyka_klasyczna, p4_religie, p4_literatura, p4_komputery, zachowane_pieniadze, "4")
if zachowane_pieniadze != 0:
    p5_imiona = [[["Które z tych imion jest jednocześnie nazwą języka programowania wykorzystywanym w kontroli lotów?"],["A) Ada", "B) Martha", "C) Sasha"], ["A"]], [["Które z tych imion wywodzi się z języka greckiego?"],["A) Julia", "B) Barbara", "C) Rebeka"], ["B"]], [["Jak nazywa się postać biblijna, która ucięła głowę wodzowi Asyryjczyków?"], ["A) Judyta", "B) Batszeba", "C) Rebeka"], ["A"]], ["Imiona żeńskie"]]
    p5_alkohol = [[["Kiedy została wymyślona jedna z najpopularniejszych gier alkoholowych tzw. beer pong?"],["A) Lata 50 XX w.", "B) lata 90 XX w.", "C) lata 20 XX w."], ["A"]], [["Jaki alkohol jest uważany za trunek handlarzy niewolników, oszustów i przemytników?"],["A) Whisky", "B) Rum", "C) Piwo"], ["B"]], [["Alkohol destylowany z wina gronowego lub owocowego to:"], ["A) Whisky", "B) Brandy", "C) Rum"], ["B"]], ["Alkohol"]]
    p5_geografia = [[["Honolulu jest stolicą:"],["A) Jamajki", "B) Hawajów", "C) Honolulu"], ["B"]], [[" Tadżykistan leży w: "],["A) Afryce", "B) Azji", "C) Ameryce Południowej"], ["B"]], [["Najdłuższą rzeką świata jest Nil. Drugie miejsce zajmuje:"], ["A) Amazonka", "B) Jangcy", "C) Missisipi"], ["A"]], ["Geografia"]]
    p5_komiksy = [[["Który z podanych bohaterów jest komiksowym \"dzieckiem\" rysownika Boba Kane'a?"],["A) Spiderman", "B) Batman", "C) Superman"], ["B"]], [["Superbohater DC Comics poruszający się z wielką prędkością to:"],["A) Shazzam", "B) Flash", "C) Green Lantern"], ["B"]], [["Który z podanych bohaterów komiksów Marvela jest nazywany “Pierwszym Avengersem”?"], ["A) Iron Man", "B) Thor", "C) Kapitan Ameryka"], ["C"]], ["Komiksy"]]
    zachowane_pieniadze = poziom_gry_trzy_zapadki(p5_imiona, p5_alkohol, p5_geografia, p5_komiksy, zachowane_pieniadze, "5")
if zachowane_pieniadze != 0:
    p6_wyspy = [[["Które z tych wysp wchodzą w skład terytorium Australii?"],["A) Wyspy Kokosowe", "B) Wyspy Cooka", "C) Wyspy Wielkanocne"], ["A"]], [["Do terytorium którego z tych państw nie zalicza się wyspa Borneo?"],["A) Indonezja", "B) Brunei", "C) Papua-Nowa Gwinea"], ["C"]], [["Do terytorium jakiego państwa zalicza się Wyspa Wiktorii?"], ["A) Kanada", "B) Nowa Zelandia", "C) Wielka Brytania"], ["A"]], ["Wyspy"]]
    p6_psychologia = [[["Prawo głoszące, że im więcej czasu mamy na wykonanie jakiejś pracy, tym więcej czasu nam ono zabiera, nazywany: "],["A) prawem Parkinsona", "B) prawem Morisona", "C) Prawem Pareta"], ["A"]], [["Tendencja do automatycznego, pozytywnego lub negatywnego, przypisywania cech na podstawie pierwszego wrażenia to:"],["A) efekt Rosenthala", "B) efekt halo", "C) efekt Pollyanny"], ["B"]], [["Efekt coctail party polega na: "], ["A) uwrażliwieniu na wszelkie bodźce odnoszące się bezpośrednio do nas", "B) uwrażliwieniu na bodźce odnoszące się do środowiska, w którym się znajdujemy ", "C) dostosowywaniu naszego zachowania do zachowań powszechnych, społecznie akceptowalnych"], ["A"]], ["Psychologia"]]
    p6_seriale = [[["W Polsce najchętniej oglądanym serialem Netflixa w 2019 roku był:"],["A) Dom z papieru", "B) Stranger Things", "C) Wiedźmin"], ["C"]], [["Cytat “Dzieci się zawsze źle komponują w mieszkaniu” pochodzi z:"],["A) Czterdziestolatka", "B) Świata według Kiepskich", "C) Złotopolskich"], ["A"]], [["Który z tych seriali nakręcono najwcześniej?"], ["A) Przyjaciele", "B) Słoneczny patrol", "C) Jak poznałem waszą matkę"], ["B"]], ["Seriale"]]
    p6_nawiazania = [[["Po jakiej krainie spaceruje Jack, główny bohater filmu Larsa von Triera pod tytułem “Dom, który zbudował Jack?”?"],["A) po Niebie", "B) po Edenie", "C) po Piekle"], ["C"]], [["Kim jest mężczyzna, partner tytułowej Matki, w filmie Darrena Aronofsky’ego pod tytułem “Mother!”?"],["A) Poetą", "B) Bogiem", "C) Artystą"], ["B"]], [["Który z siedmiu grzechów głównych reprezentuje antagonista filmu pod tytułem “Se7en” w reżyserii Davida Finchera?"], ["A) pychę", "B) złość", "C) zazdrość"], ["C"]], ["Nawiązania religijne we współczesnej kinematografii"]]
    zachowane_pieniadze = poziom_gry_trzy_zapadki(p6_wyspy, p6_psychologia, p6_seriale, p6_nawiazania, zachowane_pieniadze, "6")
if zachowane_pieniadze != 0:
    p7_kuchnie_swiata = [[["Włoska potrawa cotoletta alla milanese najbardziej przypomina..."],["A) pierogi z kapustą i grzybami", "B) placki ziemniaczane", "C) kotlet schabowy"], ["C"]], [["Gazpacho to zupa, która zazwyczaj ma kolor…"],["A) Czerwony", "B) Zielony", "C) Żółty"], ["A"]], [["Jedna z najpopularniejszych w Chinach zup jest robiona z jaskółczych…"], ["A) Łap", "B) Gniazd", "C) Języków"], ["B"]], ["Kuchnie świata"]]
    p7_waluty = [[["Waluta wenezuelska to:"],["A) dolar", "B) somoni", "C) boliwar"], ["C"]], [["Państwem, w którym walutą nie jest peso, jest/są:"],["A) Filipiny", "B) Dominikana", "C) Bahamy"], ["C"]], [["Waluta obowiązująca w Hongkongu to:"], ["A) dolar", "B) juan", "C) funt"], ["A"]], ["Waluty"]]
    p7_gory = [[["Który łańcuch górski z podanych poniżej jest najmłodszy?"],["A) Sudety", "B) Karpaty", "C) Góry Świętokrzyskie"], ["B"]], [["Jaki jest najwyższy szczyt Azerbejdżanu?"],["A) Bazardüzü", "B) Hazrat Sulton", "C) Czogori"], ["A"]], [["Jaka jest średnia roczna temperatura na szczycie Śnieżki? (w stopniach Celsjusza)"], ["A) 5", "B) 0,4", "C) -4"], ["B"]], ["Góry"]]
    p7_polska_fantastyka = [[["Imię ukochanej Daimona Freya, bohatera “Siewcy Wiatru” autorstwa Mai Lidii Kossakowskiej?"],["A) Hija", "B) Lilith", "C) Drop"], ["A"]], [["Imię czarodziejki z serii książek o Wiedźminie, autorstwa Andrzeja Sapkowskiego, która należała do Rady Królewskiej Temerii?"],["A) Keira Metz", "B) Yennefer z Vengerbergu", "C) Fringilla Vigo"], ["A"]], [["Kim była obrończyni, którą otrzymał od klasztoru Amszilas inkwizytor Mordimer Madderdin, bohater serii książek Jacka Piekary?"], ["A) inkwizytorką", "B) zakonnicą", "C) anielicą"], ["C"]], ["Polska fantastyka"]]
    zachowane_pieniadze = poziom_gry_trzy_zapadki(p7_kuchnie_swiata, p7_waluty, p7_gory, p7_polska_fantastyka, zachowane_pieniadze, "7")
if zachowane_pieniadze != 0:
    p8_uczeni_wszechczasow = [[["Który z tych XVII-wiecznych uczonych urodził się wcześniej?"],["A) Gottfried Leibniz","B) Izaak Newton"],["B"]], [["W którym roku został ścięty Antoine Lavoisier, wybitny francuski chemik?"], ["A) 1793", "B) 1794"], ["B"]], [["W którym z tych włoskich miast urodził się Galileusz?"], ["A) Piza", "B) Mediolan"], ["A"]], ["Uczeni wszechczasów"]]
    p8_prl = [[["Ile mierzyła Warszawska Radiostacja Centralna w Gąbinie, która do 1991 roku była najwyższym obiektem wzniesionym przez człowieka?"],["A) około 646 metrów", "B) około 846 metrów"],["A"]], [["Pierwsze częściowo wolne wybory w historii Polski po II wojnie światowej  odbyły się w roku:"], ["A) 1991", "B) 1989"], ["B"]], [["Co, według propagandy PRL, Amerykanie zrzucali z samolotów nad Polską?"], ["A) stonkę ziemniaczaną","B) odpady promieniotwórcze"], ["A"]], ["PRL"]]
    p8_kosmos = [[["Ile księżyców ma Jowisz?"],["A) 79", "B) 89"],["A"]], [["W którym roku odbył się pierwszy turystyczny lot w kosmos?"], ["A) 2005", "B) 2001"], ["B"]], [["Kiedy najszybciej będziemy mogli obserwować kometę Halleya?"], ["A) 2050","B) 2061"], ["B"]], ["Kosmos"]]
    p8_gry_wideo = [[["Miejsce akcji dodatku do Bioshocka Infinite Burial at Sea?"],["A) Colombia", "B) Rapture"],["B"]], [["Nazwa starszego smoka w grze Monster Hunter: World, którego główny atak polega na zabieraniu życia graczowi?"], ["A) Kushala Daora", "B) Vaal Hazak"], ["B"]], [["Imię postaci w grze Dota 2, demona, którego znamy pod przydomkiem Queen of Pain?"], ["A) Akasha","B) Shendelzare"], ["A"]], ["Gry wideo"]]
    zachowane_pieniadze = poziom_gry_dwie_zapadki(p8_uczeni_wszechczasow, p8_prl, p8_kosmos, p8_gry_wideo, zachowane_pieniadze, "8")

print("Koniec gry! Dziękujemy za udział :)")
