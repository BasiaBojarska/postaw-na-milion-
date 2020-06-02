import random
import time

def poziom_gry_cztery_zapadki(k1, k2, k3, k4, pieniadze):
    def poprawna_zapadka(kategoria): #określanie prawidłowej zapadki dla danego pytania
        n = random.randint(0,2)
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
                return 0
            else:
                pieniadze = slownik[str(prawidlowa_zapadka)]
                print("Brawo! Na prawidłowej zapadce znajdowały się banknoty! Liczba zachowanych przez Ciebie plików to:", pieniadze)
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
                            return 0
                        else:
                            pieniadze = slownik[str(prawidlowa_zapadka)]
                            print("Brawo! Na prawdiłowej zapadce znajdowały się banknoty. Liczba zachowanych przez Ciebie plików to:", pieniadze, ". Przechodzisz do kolejnego poziomu!")
                            return pieniadze
                        break
def poziom_gry_trzy_zapadki(k1, k2, k3, k4, pieniadze):
    def poprawna_zapadka(kategoria): #określanie prawidłowej zapadki dla danego pytania
        n = random.randint(0,2)
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
    odpowiedz_zmiana = obwarowanie_przed_idiotami("Tak wyglądają zapadki:",slownik,".Czy chcesz je zmienić? (Wpisz \"T\" jeśli \"Tak\" lub \"N\" jeśli \"Nie\")", "T", "N", "N", "T")
    nowa_liczba_pieniedzy = 0
    if odpowiedz_zmiana == "N":
        if 0 in slownik.values():
            if slownik[str(prawidlowa_zapadka)] == 0:
                print("Przegrałeś!")
                return 0
            else:
                pieniadze = slownik[str(prawidlowa_zapadka)]
                print("Brawo! Na prawidłowej zapadce znajdowały się banknoty! Liczba zachowanych przez Ciebie plików to:", pieniadze)
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
                        else:
                            pieniadze = slownik[str(prawidlowa_zapadka)]
                            print("Brawo! Na prawdiłowej zapadce znajdowały się banknoty. Liczba zachowanych przez Ciebie plików to:", pieniadze, ". Przechodzisz do kolejnego poziomu!")
                            return pieniadze
                        break
def poziom_gry_dwie_zapadki(k1, k2, k3, k4, pieniadze):
    def poprawna_zapadka(kategoria): #określanie prawidłowej zapadki dla danego pytania
        n = random.randint(0,2)
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
    odpowiedz_zmiana = obwarowanie_przed_idiotami("Tak wyglądają zapadki:",slownik,".Czy chcesz je zmienić? (Wpisz \"T\" jeśli \"Tak\" lub \"N\" jeśli \"Nie\")", "T", "N", "N", "T")
    nowa_liczba_pieniedzy = 0
    if odpowiedz_zmiana == "N":
        if 0 in slownik.values():
            if slownik[str(prawidlowa_zapadka)] == 0:
                print("Przegrałeś!")
                return 0
            else:
                pieniadze = slownik[str(prawidlowa_zapadka)]
                print("Brawo! Na prawidłowej zapadce znajdowały się banknoty! Liczba zachowanych przez Ciebie plików to:", pieniadze)
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
                            return 0
                        else:
                            pieniadze = slownik[str(prawidlowa_zapadka)]
                            print("Brawo! Na prawdiłowej zapadce znajdowały się banknoty. Liczba zachowanych przez Ciebie plików to:", pieniadze, ". Przechodzisz do kolejnego poziomu!")
                            return pieniadze
                        break
zachowane_pieniadze = 1
if zachowane_pieniadze != 0:
    p1_zwierzeta = [[["Które z tych zwierząt jest tradycyjnie nazywane najlepszym przyjacielem człowieka?"],["A) Kot","B) Chomik","C) Pies","D) Papuga"],["C"]], [["Które z tych zwierząt nie występuje naturalnie w Afryce?"], ["A) Lew", "B) Panda Wielka", "C) Zebra", "D) Żyrafa"], ["B"]], [["Jaki ptak znajduje się na polskim godle?"], ["A) Kondor wielki", "B) Orzeł bielik", "C) Jastrząb zwyczajny", "D) Biała gołębica"], ["B"]], ["Zwierzęta"]]
    p1_przyslowia = [[["Dokończ zdanie: a co po czyjej wielkości, jak nie ma w głowie…"],["A) radości", "B) mądrości", "C) ufności", "D) miłości"],["B"]], [["Dokończ zdanie: czym skorupka za młodu nasiąknie, tym na starość…"], ["A) się stanie", "B) trąci", "C) będzie", "D) się okaże"], ["B"]], [["Najpopularniejszym polskim przysłowiem w roku 2018 zostało:"], ["A) łaska pańska na pstrym koniu jeździ ", "B) Grosz do grosza, a będzie kokosza","C) Dzieci i ryby głosu nie mają ","D) Bez pracy nie ma kołaczy"], ["D"]], ["Przysłowia"]]
    p1_swieta = [[["W Polsce obchodzimy święto flagi:"],["A) 2 maja", "B) 3 maja", "C) 2 czerwca", "D) 3 czerwca"], ["A"]], [["Tradycyjną potrawą spożywaną z okazji Dnia Dziękczynienia jest:"],["A) pieczony indyk", "B) kurczak z rożna", "C) bażant z pieca", "D) kaczka po wietnamsku"], ["A"]], [["Polowanie na jajka to zwyczaj zwiazany z: "], ["A) Wielkanocą", "B) Bożym Narodzeniem", "C) Halloween", "D) Chanuką"], ["A"]], ["Święta"]]
    p1_mitologia_grecka = [[["Który z podanych herosów w mitologii greckiej uchodził za syna Zeusa?"],["A) Achilles", "B) Jazon", "C) Perseusz", "D) Hippotoon"], ["C"]], [["Która z podanych bogiń była opiekunką ogniska domowego?"],["A) Atena", "B) Artemida", "C) Demeter", "D) Hestia"], ["D"]], [["Kim były Erynie?"], ["A) boginiami losu", "B) boginiami zemsty", "C) bóstwami morskimi", "D) boginiami młodości"], ["B"]], ["Mitologia grecka"]]
    zachowane_pieniadze = poziom_gry_cztery_zapadki(p1_zwierzeta, p1_przyslowia, p1_swieta, p1_mitologia_grecka, 40)
if zachowane_pieniadze != 0:
    p2_zwierzeta = [[["Które z tych zwierząt jest tradycyjnie nazywane najlepszym przyjacielem człowieka?"],["A) Kot","B) Chomik","C) Pies","D) Papuga"],["C"]], [["Które z tych zwierząt nie występuje naturalnie w Afryce?"], ["A) Lew", "B) Panda Wielka", "C) Zebra", "D) Żyrafa"], ["B"]], [["Jaki ptak znajduje się na polskim godle?"], ["A) Kondor wielki", "B) Orzeł bielik", "C) Jastrząb zwyczajny", "D) Biała gołębica"], ["B"]], ["Zwierzęta"]]
    p2_przyslowia = [[["Dokończ zdanie: a co po czyjej wielkości, jak nie ma w głowie…"],["A) radości", "B) mądrości", "C) ufności", "D) miłości"],["B"]], [["Dokończ zdanie: czym skorupka za młodu nasiąknie, tym na starość…"], ["A) się stanie", "B) trąci", "C) będzie", "D) się okaże"], ["B"]], [["Najpopularniejszym polskim przysłowiem w roku 2018 zostało:"], ["A) łaska pańska na pstrym koniu jeździ ", "B) Grosz do grosza, a będzie kokosza","C) Dzieci i ryby głosu nie mają ","D) Bez pracy nie ma kołaczy"], ["D"]], ["Przysłowia"]]
    p2_swieta = [[["W Polsce obchodzimy święto flagi:"],["A) 2 maja", "B) 3 maja", "C) 2 czerwca", "D) 3 czerwca"], ["A"]], [["Tradycyjną potrawą spożywaną z okazji Dnia Dziękczynienia jest:"],["A) pieczony indyk", "B) kurczak z rożna", "C) bażant z pieca", "D) kaczka po wietnamsku"], ["A"]], [["Polowanie na jajka to zwyczaj zwiazany z: "], ["A) Wielkanocą", "B) Bożym Narodzeniem", "C) Halloween", "D) Chanuką"], ["A"]], ["Święta"]]
    p2_mitologia_grecka = [[["Który z podanych herosów w mitologii greckiej uchodził za syna Zeusa?"],["A) Achilles", "B) Jazon", "C) Perseusz", "D) Hippotoon"], ["C"]], [["Która z podanych bogiń była opiekunką ogniska domowego?"],["A) Atena", "B) Artemida", "C) Demeter", "D) Hestia"], ["D"]], [["Kim były Erynie?"], ["A) boginiami losu", "B) boginiami zemsty", "C) bóstwami morskimi", "D) boginiami młodości"], ["B"]], ["Mitologia grecka"]]
    zachowane_pieniadze = poziom_gry_cztery_zapadki(p2_zwierzeta, p2_przyslowia, p2_swieta, p2_mitologia_grecka, zachowane_pieniadze)
if zachowane_pieniadze != 0:
    p3_zwierzeta = [[["Które z tych zwierząt jest tradycyjnie nazywane najlepszym przyjacielem człowieka?"],["A) Kot","B) Chomik","C) Pies","D) Papuga"],["C"]], [["Które z tych zwierząt nie występuje naturalnie w Afryce?"], ["A) Lew", "B) Panda Wielka", "C) Zebra", "D) Żyrafa"], ["B"]], [["Jaki ptak znajduje się na polskim godle?"], ["A) Kondor wielki", "B) Orzeł bielik", "C) Jastrząb zwyczajny", "D) Biała gołębica"], ["B"]], ["Zwierzęta"]]
    p3_przyslowia = [[["Dokończ zdanie: a co po czyjej wielkości, jak nie ma w głowie…"],["A) radości", "B) mądrości", "C) ufności", "D) miłości"],["B"]], [["Dokończ zdanie: czym skorupka za młodu nasiąknie, tym na starość…"], ["A) się stanie", "B) trąci", "C) będzie", "D) się okaże"], ["B"]], [["Najpopularniejszym polskim przysłowiem w roku 2018 zostało:"], ["A) łaska pańska na pstrym koniu jeździ ", "B) Grosz do grosza, a będzie kokosza","C) Dzieci i ryby głosu nie mają ","D) Bez pracy nie ma kołaczy"], ["D"]], ["Przysłowia"]]
    p3_swieta = [[["W Polsce obchodzimy święto flagi:"],["A) 2 maja", "B) 3 maja", "C) 2 czerwca", "D) 3 czerwca"], ["A"]], [["Tradycyjną potrawą spożywaną z okazji Dnia Dziękczynienia jest:"],["A) pieczony indyk", "B) kurczak z rożna", "C) bażant z pieca", "D) kaczka po wietnamsku"], ["A"]], [["Polowanie na jajka to zwyczaj zwiazany z: "], ["A) Wielkanocą", "B) Bożym Narodzeniem", "C) Halloween", "D) Chanuką"], ["A"]], ["Święta"]]
    p3_mitologia_grecka = [[["Który z podanych herosów w mitologii greckiej uchodził za syna Zeusa?"],["A) Achilles", "B) Jazon", "C) Perseusz", "D) Hippotoon"], ["C"]], [["Która z podanych bogiń była opiekunką ogniska domowego?"],["A) Atena", "B) Artemida", "C) Demeter", "D) Hestia"], ["D"]], [["Kim były Erynie?"], ["A) boginiami losu", "B) boginiami zemsty", "C) bóstwami morskimi", "D) boginiami młodości"], ["B"]], ["Mitologia grecka"]]
    zachowane_pieniadze = poziom_gry_cztery_zapadki(p3_zwierzeta, p3_przyslowia, p3_swieta, p3_mitologia_grecka, zachowane_pieniadze)
if zachowane_pieniadze != 0:
    p4_zwierzeta = [[["Które z tych zwierząt jest tradycyjnie nazywane najlepszym przyjacielem człowieka?"],["A) Kot","B) Chomik","C) Pies","D) Papuga"],["C"]], [["Które z tych zwierząt nie występuje naturalnie w Afryce?"], ["A) Lew", "B) Panda Wielka", "C) Zebra", "D) Żyrafa"], ["B"]], [["Jaki ptak znajduje się na polskim godle?"], ["A) Kondor wielki", "B) Orzeł bielik", "C) Jastrząb zwyczajny", "D) Biała gołębica"], ["B"]], ["Zwierzęta"]]
    p4_przyslowia = [[["Dokończ zdanie: a co po czyjej wielkości, jak nie ma w głowie…"],["A) radości", "B) mądrości", "C) ufności", "D) miłości"],["B"]], [["Dokończ zdanie: czym skorupka za młodu nasiąknie, tym na starość…"], ["A) się stanie", "B) trąci", "C) będzie", "D) się okaże"], ["B"]], [["Najpopularniejszym polskim przysłowiem w roku 2018 zostało:"], ["A) łaska pańska na pstrym koniu jeździ ", "B) Grosz do grosza, a będzie kokosza","C) Dzieci i ryby głosu nie mają ","D) Bez pracy nie ma kołaczy"], ["D"]], ["Przysłowia"]]
    p4_swieta = [[["W Polsce obchodzimy święto flagi:"],["A) 2 maja", "B) 3 maja", "C) 2 czerwca", "D) 3 czerwca"], ["A"]], [["Tradycyjną potrawą spożywaną z okazji Dnia Dziękczynienia jest:"],["A) pieczony indyk", "B) kurczak z rożna", "C) bażant z pieca", "D) kaczka po wietnamsku"], ["A"]], [["Polowanie na jajka to zwyczaj zwiazany z: "], ["A) Wielkanocą", "B) Bożym Narodzeniem", "C) Halloween", "D) Chanuką"], ["A"]], ["Święta"]]
    p4_mitologia_grecka = [[["Który z podanych herosów w mitologii greckiej uchodził za syna Zeusa?"],["A) Achilles", "B) Jazon", "C) Perseusz", "D) Hippotoon"], ["C"]], [["Która z podanych bogiń była opiekunką ogniska domowego?"],["A) Atena", "B) Artemida", "C) Demeter", "D) Hestia"], ["D"]], [["Kim były Erynie?"], ["A) boginiami losu", "B) boginiami zemsty", "C) bóstwami morskimi", "D) boginiami młodości"], ["B"]], ["Mitologia grecka"]]
    zachowane_pieniadze = poziom_gry_cztery_zapadki(p4_zwierzeta, p4_przyslowia, p4_swieta, p4_mitologia_grecka, zachowane_pieniadze)
if zachowane_pieniadze != 0:
    p5_zwierzeta = [[["Które z tych zwierząt jest tradycyjnie nazywane najlepszym przyjacielem człowieka?"],["A) Kot","B) Chomik","C) Pies"],["C"]], [["Które z tych zwierząt nie występuje naturalnie w Afryce?"], ["A) Lew", "B) Panda Wielka", "C) Zebra"], ["B"]], [["Jaki ptak znajduje się na polskim godle?"], ["A) Kondor wielki", "B) Orzeł bielik", "C) Jastrząb zwyczajny"], ["B"]], ["Zwierzęta"]]
    p5_przyslowia = [[["Dokończ zdanie: a co po czyjej wielkości, jak nie ma w głowie…"],["A) radości", "B) mądrości", "C) ufności"],["B"]], [["Dokończ zdanie: czym skorupka za młodu nasiąknie, tym na starość…"], ["A) się stanie", "B) trąci", "C) będzie"], ["B"]], [["Najpopularniejszym polskim przysłowiem w roku 2018 zostało:"], ["A) łaska pańska na pstrym koniu jeździ ", "B) Grosz do grosza, a będzie kokosza","C) Bez pracy nie ma kołaczy"], ["C"]], ["Przysłowia"]]
    p5_swieta = [[["W Polsce obchodzimy święto flagi:"],["A) 2 maja", "B) 3 maja", "C) 2 czerwca"], ["A"]], [["Tradycyjną potrawą spożywaną z okazji Dnia Dziękczynienia jest:"],["A) pieczony indyk", "B) kurczak z rożna", "C) bażant z pieca"], ["A"]], [["Polowanie na jajka to zwyczaj zwiazany z: "], ["A) Wielkanocą", "B) Bożym Narodzeniem", "C) Halloween"], ["A"]], ["Święta"]]
    p5_mitologia_grecka = [[["Który z podanych herosów w mitologii greckiej uchodził za syna Zeusa?"],["A) Achilles", "B) Jazon", "C) Perseusz"], ["C"]], [["Która z podanych bogiń była opiekunką ogniska domowego?"],["A) Atena", "B) Artemida", "C) Hestia"], ["C"]], [["Kim były Erynie?"], ["A) boginiami losu", "B) boginiami zemsty", "C) bóstwami morskimi"], ["B"]], ["Mitologia grecka"]]
    zachowane_pieniadze = poziom_gry_trzy_zapadki(p5_zwierzeta, p5_przyslowia, p5_swieta, p5_mitologia_grecka, zachowane_pieniadze)
if zachowane_pieniadze != 0:
    p6_zwierzeta = [[["Które z tych zwierząt jest tradycyjnie nazywane najlepszym przyjacielem człowieka?"],["A) Kot","B) Chomik","C) Pies"],["C"]], [["Które z tych zwierząt nie występuje naturalnie w Afryce?"], ["A) Lew", "B) Panda Wielka", "C) Zebra"], ["B"]], [["Jaki ptak znajduje się na polskim godle?"], ["A) Kondor wielki", "B) Orzeł bielik", "C) Jastrząb zwyczajny"], ["B"]], ["Zwierzęta"]]
    p6_przyslowia = [[[" )okończ zdanie: a co po czyjej wielkości, jak nie ma w głowie…"],["A) radości", "B) mądrości", "C) ufności"],["B"]], [["Dokończ zdanie: czym skorupka za młodu nasiąknie, tym na starość…"], ["A) się stanie", "B) trąci", "C) będzie"], ["B"]], [["Najpopularniejszym polskim przysłowiem w roku 2018 zostało:"], ["A) łaska pańska na pstrym koniu jeździ ", "B) Grosz do grosza, a będzie kokosza","C) Bez pracy nie ma kołaczy"], ["C"]], ["Przysłowia"]]
    p6_swieta = [[["W Polsce obchodzimy święto flagi:"],["A) 2 maja", "B) 3 maja", "C) 2 czerwca"], ["A"]], [["Tradycyjną potrawą spożywaną z okazji Dnia Dziękczynienia jest:"],["A) pieczony indyk", "B) kurczak z rożna", "C) bażant z pieca"], ["A"]], [["Polowanie na jajka to zwyczaj zwiazany z: "], ["A) Wielkanocą", "B) Bożym Narodzeniem", "C) Halloween"], ["A"]], ["Święta"]]
    p6_mitologia_grecka = [[["Który z podanych herosów w mitologii greckiej uchodził za syna Zeusa?"],["A) Achilles", "B) Jazon", "C) Perseusz"], ["C"]], [["Która z podanych bogiń była opiekunką ogniska domowego?"],["A) Atena", "B) Artemida", "C) Hestia"], ["C"]], [["Kim były Erynie?"], ["A) boginiami losu", "B) boginiami zemsty", "C) bóstwami morskimi"], ["B"]], ["Mitologia grecka"]]
    zachowane_pieniadze = poziom_gry_trzy_zapadki(p6_zwierzeta, p6_przyslowia, p6_swieta, p6_mitologia_grecka, zachowane_pieniadze)
if zachowane_pieniadze != 0:
    p7_zwierzeta = [[["Które z tych zwierząt jest tradycyjnie nazywane najlepszym przyjacielem człowieka?"],["A) Kot","B) Chomik","C) Pies"],["C"]], [["Które z tych zwierząt nie występuje naturalnie w Afryce?"], ["A) Lew", "B) Panda Wielka", "C) Zebra"], ["B"]], [["Jaki ptak znajduje się na polskim godle?"], ["A) Kondor wielki", "B) Orzeł bielik", "C) Jastrząb zwyczajny"], ["B"]], ["Zwierzęta"]]
    p7_przyslowia = [[["Dokończ zdanie: a co po czyjej wielkości, jak nie ma w głowie…"],["A) radości", "B) mądrości", "C) ufności"],["B"]], [["Dokończ zdanie: czym skorupka za młodu nasiąknie, tym na starość…"], ["A) się stanie", "B) trąci", "C) będzie"], ["B"]], [["Najpopularniejszym polskim przysłowiem w roku 2018 zostało:"], ["A) łaska pańska na pstrym koniu jeździ ", "B) Grosz do grosza, a będzie kokosza","C) Bez pracy nie ma kołaczy"], ["C"]], ["Przysłowia"]]
    p7_swieta = [[["W Polsce obchodzimy święto flagi:"],["A) 2 maja", "B) 3 maja", "C) 2 czerwca"], ["A"]], [["Tradycyjną potrawą spożywaną z okazji Dnia Dziękczynienia jest:"],["A) pieczony indyk", "B) kurczak z rożna", "C) bażant z pieca"], ["A"]], [["Polowanie na jajka to zwyczaj zwiazany z: "], ["A) Wielkanocą", "B) Bożym Narodzeniem", "C) Halloween"], ["A"]], ["Święta"]]
    p7_mitologia_grecka = [[["Który z podanych herosów w mitologii greckiej uchodził za syna Zeusa?"],["A) Achilles", "B) Jazon", "C) Perseusz"], ["C"]], [["Która z podanych bogiń była opiekunką ogniska domowego?"],["A) Atena", "B) Artemida", "C) Hestia"], ["C"]], [["Kim były Erynie?"], ["A) boginiami losu", "B) boginiami zemsty", "C) bóstwami morskimi"], ["B"]], ["Mitologia grecka"]]
    zachowane_pieniadze = poziom_gry_trzy_zapadki(p7_zwierzeta, p7_przyslowia, p7_swieta, p7_mitologia_grecka, zachowane_pieniadze)
if zachowane_pieniadze != 0:
    p8_zwierzeta = [[["Które z tych zwierząt jest tradycyjnie nazywane najlepszym przyjacielem człowieka?"],["A) Kot","B) Pies"],["B"]], [["Które z tych zwierząt nie występuje naturalnie w Afryce?"], ["A) Lew", "B) Panda Wielka"], ["B"]], [["Jaki ptak znajduje się na polskim godle?"], ["A) Kondor wielki", "B) Orzeł bielik"], ["B"]], ["Zwierzęta"]]
    p8_przyslowia = [[["Dokończ zdanie: a co po czyjej wielkości, jak nie ma w głowie…"],["A) radości", "B) mądrości", "4) miłości"],["B"]], [["Dokończ zdanie: czym skorupka za młodu nasiąknie, tym na starość…"], ["A) się stanie", "B) trąci"], ["B"]], [["Najpopularniejszym polskim przysłowiem w roku 2018 zostało:"], ["A) łaska pańska na pstrym koniu jeździ ","B) Bez pracy nie ma kołaczy"], ["B"]], ["Przysłowia"]]
    p8_swieta = [[["W Polsce obchodzimy święto flagi:"],["A) 2 maja", "B) 3 maja"], ["A"]], [["Tradycyjną potrawą spożywaną z okazji Dnia Dziękczynienia jest:"],["A) pieczony indyk", "B) kurczak z rożna"], ["A"]], [["Polowanie na jajka to zwyczaj zwiazany z: "], ["A) Wielkanocą", "B) Bożym Narodzeniem"], ["A"]], ["Święta"]]
    p8_mitologia_grecka = [[["Który z podanych herosów w mitologii greckiej uchodził za syna Zeusa?"],["A) Achilles", "B) Perseusz"], ["B"]], [["Która z podanych bogiń była opiekunką ogniska domowego?"],["A) Atena", "B) Hestia"], ["B"]], [["Kim były Erynie?"], ["A) boginiami losu", "B) boginiami zemsty"], ["B"]], ["Mitologia grecka"]]
    zachowane_pieniadze = poziom_gry_dwie_zapadki(p8_zwierzeta, p8_przyslowia, p8_swieta, p8_mitologia_grecka, zachowane_pieniadze)

print("Koniec gry! Dziękujemy za udział :)")
