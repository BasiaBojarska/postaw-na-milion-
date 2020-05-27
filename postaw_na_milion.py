import random
import time


def poprawna_zapadka(kategoria): #określanie prawidłowej zapadki dla danego pytania
    n = random.randint(0,2)
    for odpowiedz in kategoria[n][1]:
        time.sleep(1)
        print(odpowiedz)
    time.sleep(1
    )    
    print("A oto pytanie")
    print(kategoria[n][0])

    literka = "".join(kategoria[n][2])
    return "zapadka_" + literka

def kladzenie_banknotow(zapadka, identyfikator, ilosc_pieniedzy): #pierwsze rozkładanie
    liczba_A = -1
    while liczba_A < 0 or liczba_A > 40:
        print("Ile plików banknotów chcesz położyć na zapadkę", identyfikator,"?")
        liczba_A = int(input())
        if not liczba_A < 0 and not liczba_A > 40:
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
        if not liczba < 0 and not liczba > nowa_liczba_plikow:
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

baza_kategorii_p1 = []
p1_zwierzeta = [[["Które z tych zwierząt jest tradycyjnie nazywane najlepszym przyjacielem człowieka?"],["A) Kot","B) Chomik","C) Pies","D) Papuga"],["C"]], [["Które z tych zwierząt nie występuje naturalnie w Afryce?"], ["A) Lew", "B) Panda Wielka", "C) Zebra", "D) Żyrafa"], ["B"]], [["Jaki ptak znajduje się na polskim godle?"], ["A) Kondor wielki", "B) Orzeł bielik", "C) Jastrząb zwyczajny", "D) Biała gołębica"], ["B"]], ["Zwierzęta"]]
p1_przyslowia = [[[" Dokończ zdanie: a co po czyjej wielkości, jak nie ma w głowie…"],["A) radości", "B) mądrości", "C) ufności", "4) miłości"],["B"]], [["Dokończ zdanie: czym skorupka za młodu nasiąknie, tym na starość…"], ["A) się stanie”, „B) trąci”, „C) będzie”, „D) się okaże"], ["B"]], [["Najpopularniejszym polskim przysłowiem w roku 2018 zostało:"], ["A Łaska pańska na pstrym koniu jeździ ", "B) Grosz do grosza, a będzie kokosza","C) Dzieci i ryby głosu nie mają ","D) Bez pracy nie ma kołaczy"], ["D"]], ["Przysłowia"]]
p1_swieta = [[["W Polsce obchodzimy święto flagi:"],["A) 2 maja", "B) 3 maja", "C) 2 czerwca", "D) 3 czerwca"], ["A"]], [["Tradycyjną potrawą spożywaną z okazji Dnia Dziękczynienia jest:"],["A) pieczony indyk", "B) kurczak z rożna", "C) bażant z pieca", "D) kaczka po wietnamsku"], ["A"]], [["Polowanie na jajka to zwyczaj zwiazany z: "], ["A) Wielkanocą", "B) Bożym Narodzeniem", "C) Halloween", "D) Chanuką"], ["A"]], ["Święta"]]
p1_mitologia_grecka = [[["Który z podanych herosów w mitologii greckiej uchodził za syna Zeusa?"],["A) Achilles", "B) Jazon", "C) Perseusz", "D) Hippotoon"], ["C"]], [["Która z podanych bogiń była opiekunką ogniska domowego?"],["A) Atena", "B) Artemida", "C) Demeter", "D) Hestia"], ["D"]], [["Kim były Erynie?"], ["A) boginiami losu", "B) boginiami zemsty", "C) bóstwami morskimi", "D) boginiami młodości"], ["B"]], ["Mitologia grecka"]]

baza_kategorii_p1 = [p1_zwierzeta, p1_przyslowia, p1_swieta, p1_mitologia_grecka]

wylosowana_kategoria1 = ""
wylosowana_kategoria2 = ""
while wylosowana_kategoria1 == wylosowana_kategoria2:
    wylosowana_kategoria1 = random.choice(baza_kategorii_p1)
    wylosowana_kategoria2 = random.choice(baza_kategorii_p1)


print("Kategorie do wyboru to:")
print("1)", wylosowana_kategoria1[3])
print("2)", wylosowana_kategoria2[3])
print("Wpisz numer wybranej kategorii")
wybrany_numer = int(input())
if wybrany_numer == 1:
    prawidlowa_zapadka = poprawna_zapadka(wylosowana_kategoria1)
elif wybrany_numer == 2:
    prawidlowa_zapadka = poprawna_zapadka(wylosowana_kategoria2)


print("Masz 40 plików banknotów. Teraz będziesz rozkładał pliki banknotów na zapadkach. Jedna z zapadek musi pozostać pusta.")
slownik = {"zapadka_A":"banknoty", "zapadka_B":"banknoty", "zapadka_C":"banknoty", "zapadka_D":"banknoty"}
liczba_plików = 40
while True:
    liczba_plików = kladzenie_banknotow("zapadka_A","A", liczba_plików)
    liczba_plików = kladzenie_banknotow("zapadka_B","B", liczba_plików)
    liczba_plików = kladzenie_banknotow("zapadka_C","C", liczba_plików)
    print("Dla zapadki D pozostało tyle plików:", liczba_plików)
    liczba_D = liczba_plików
    if not liczba_D < 0 and not liczba_D > 40:
        slownik["zapadka_D"] = liczba_D
    else:
        print("Liczba nieprawidłowa")
    if not 0 in slownik.values():
        print("Nie pozostawiłeś pustej zapadki! Popraw to.")
        liczba_plików = 40
    else:
        break
print("Tak wyglądają zapadki:",slownik,".Czy chcesz je zmienić? (Wpisz \"T\" jeśli \"Tak\" lub \"N\" jeśli \"Nie\")")
odpowiedz_zmiana = input()
nowa_liczba_plikow = 0
if odpowiedz_zmiana == "N":
    if 0 in slownik.values():
        if slownik[str(prawidlowa_zapadka)] == 0:
            print("Przegrałeś!")
        else:
            liczba_plików = slownik[str(prawidlowa_zapadka)]
            print("Brawo! Na prawidłowej zapadce znajdowały się banknoty! Liczba zachowanych przez Ciebie plików to:", liczba_plików)
if odpowiedz_zmiana == "T":
    print("Z której zapadki chcesz zabrać pieniądze?")
    odpowiedz = input()
    if odpowiedz == "A":
        nowa_liczba_plikow = przekladanie_pieniedzy("zapadka_A", "A", nowa_liczba_plikow)
    elif odpowiedz == "B":
        nowa_liczba_plikow = przekladanie_pieniedzy("zapadka_B", "B", nowa_liczba_plikow)
    elif odpowiedz == "C":
        nowa_liczba_plikow = przekladanie_pieniedzy("zapadka_C", "C", nowa_liczba_plikow)
    elif odpowiedz == "D":
        nowa_liczba_plikow = przekladanie_pieniedzy("zapadka_D", "D", nowa_liczba_plikow)
if odpowiedz_zmiana == "T":
    while True:
        print("""Czy teraz chcesz położyć pieniądze na inną zapadkę (wciśnij \"P\"), czy znów zabrać pienądze z zapadki? (wciśnij \"Z\".
        Jeżeli chcesz zakończyć rozkładanie pieniędzy wciśnij \"Q\"""")
        odpowiedz = input()
        if odpowiedz == "P":
            print("Na którą zapadkę chcesz położyć pieniądze?")
            odpowiedz = input()
            if odpowiedz == "A":
                nowa_liczba_plikow = umieszczanie_banknotow("zapadka_A", "A", nowa_liczba_plikow)
            elif odpowiedz == "B":
                nowa_liczba_plikow = umieszczanie_banknotow("zapadka_B", "B", nowa_liczba_plikow)
            elif odpowiedz == "C":
                nowa_liczba_plikow = umieszczanie_banknotow("zapadka_C", "C", nowa_liczba_plikow)
            elif odpowiedz == "D":
                nowa_liczba_plikow = umieszczanie_banknotow("zapadka_D", "D", nowa_liczba_plikow)
        elif odpowiedz == "Z":
            print("Z której zapadki chcesz zabrać pieniądze?")
            odpowiedz = input()
            if odpowiedz == "A":
                nowa_liczba_plikow = zabieranie_banknotow("zapadka_A", "A", nowa_liczba_plikow)
            elif odpowiedz == "B":
                nowa_liczba_plikow = zabieranie_banknotow("zapadka_B", "B", nowa_liczba_plikow)
            elif odpowiedz == "C":
                nowa_liczba_plikow = zabieranie_banknotow("zapadka_C", "C", nowa_liczba_plikow)
            elif odpowiedz == "D":
                nowa_liczba_plikow = zabieranie_banknotow("zapadka_D", "D", nowa_liczba_plikow)
        elif odpowiedz == "Q":
            if nowa_liczba_plikow > 0:
                print("Nie umieściłeś na zapadkach wszystkich banknotów!")
            if not 0 in slownik.values():
                print("Nie pozostawiłeś pustej zapadki! Popraw to.")
                print("Teraz zapadki wyglądają tak:", slownik, "a ty masz w rękach", nowa_liczba_plikow, "banknotów")

            else:
                    if slownik[str(prawidlowa_zapadka)] == 0:
                        print("Przegrałeś!")
                    else:
                        liczba_plików = slownik[str(prawidlowa_zapadka)]
                        print("Brawo! Na prawdiłowej zapadce znajdowały się banknoty. Liczba zachowanych przez Ciebie plików to:", liczba_plików)
                    break
