import random
import time


kategorie_p1=["Zwierzęta","Mitologia grecka","Święta","Przysłowia"]
kategorie_p2=["Królowie Polscy","Muzyka filmowa","Ogrodnictwo","Sporty ekstremalne"]
kategorie_p3=["Miasta wojewódzkie","Znane strony internetowe","Zabytki","Jedzenie"]
kategorie_p4=["Komputery","Muzyka klasyczna","Religie i wierzenia","Literatura"]
kategorie_p5=["Imiona Żeńskie","Komiksy","Geografia","Alkohol"]
kategorie_p6=["Wyspy","Nawiązania religijne w kinematografii","Seriale","Psychologia"]
kategorie_p7=["Kuchnie świata","Polska fantastyka ","Góry","Waluta"]
kategorie_p8=["Uczeni wszechczasów","Gry wideo","Kosmos","PRL"]

zwierzeta=[["Zwierzęta",["Które z tych zwierząt jest tradycyjnie nazywane najlepszym przyjacielem człowieka?",["Kot",0],["Chomik",0],["Pies",1],["Papuga",0]],["Które z tych zwierząt nie występuje naturalnie w Afryce?",["Lew",0],["Panda wielka",1],["Zebra",0],["Żyrafa",0]],["Jaki ptak znajduje się na polskim godle?",["Kondor wielki",0],["Orzeł bielik",1],["Jastrząb zwyczajny",0],["Biała gołębica",0]]]]
mitologiagrecka=[["Mitologia grecka",["Który z podanych herosów w mitologii greckiej uchodził za syna Zeusa?",["Achilles",0],["Jazon",0],["Perseusz",1],["Hippotoon",0]],["Która z podanych bogiń, była opiekunką ogniska domowego?",["Atena",0],["Artemida",0],["Demeter",0],["Hestia",1]],["Kim były Erynie?",["boginiami losu",0],["boginiami zemsty",1],["bóstwami morskimi",0],["boginiami młodości",0]]]]
swieta=[["Święta",["W Polsce obchodzimy święto flagi:",["2 maja",1],["3 maja",0],["2 czerwca",0],["3 czerwca",0]],["Tradycyjną potrawą spożywaną z okazji Dnia Dziękczynienia jest:",["pieczony indyk",1],["kurczak z rożna",0],["bażant z pieca",0],["kaczka po wietnamsku",0]],["Polowanie na jajka to zwyczaj zwiazany z:",["Wielkanocą",1],["Bożym Narodzeniem",0],["Halloween",0],["Chanuką",0]]]]
przyslowia=[["Przysłowia",["Dokończ zdanie: a co po czyjej wielkości, jak nie ma w głowie…",["radości",0],["mądrości",1],["ufności",0],["miłości",0]],["Dokończ zdanie: czym skorupka za młodu nasiąknie, tym na starość…",["się stanie",0],["trąci",1],["będzie",0],["się okaże",0]],["Najpopularniejszym polskim przysłowiem w roku 2018 zostało: ",["Łaska pańska na pstrym koniu jeździ",0],["Grosz do grosza, a będzie kokosza",0],["Dzieci i ryby głosu nie mają",0],["Bez pracy nie ma kołaczy",1]]]]
krolowiepolski=[["Królowie Polski",["Kto był pierwszym koronowanym królem Polski?",["Bolesław Chrobry",1],["Mieszko I",0],["Bolesław Śmiały",0],["Mieszko II",0]],["Który król Polski był mężem Królowej Jadwigi Andegaweńskiej?",["Mieszko I",0],["Bolesław Śmiały",0],["Bolesław Krzywousty",0],["Władysław Jagiełło",1]],["Za rządów którego króla wydano przywilej koszycki?",["Ludwika Węgierskiego",1],["Władysława Jagiełły",0],["Stanisława Augusta Poniatowskiego",0],["Bolesława Krzywoustego",0]]]]
muzykafilmowa=[["Muzyka filmowa",["Kto jest autorem muzyki do filmu Christophera Nolana pod tytułem “Interstellar”?",["Thomas Newman",0],["Hans Zimmer",1],["John Williams",0],["James Horner",0]],["Za muzykę do którego filmu Ennio Morricone otrzymał Oscara w 2016 roku?",["“Pewnego Razu na Dzikim Zachodzie”",0],["“Nienawistna Ósemka”",1],[" “Za garść dolarów”",0],["“Dawno Temu w Ameryce”",0]],["W którym roku Howard Shore otrzymał Oscara za muzykę do “Władcy Pierścieni - Drużyny Pierścienia”?",["2003",0],["2001",0],["2002",1],["2004",0]]]]
ogrodnictwo=[["Ogrodnictwo",["Nowalijki to warzywa, które ukazują się najczęściej:",["późnym latem",0],["wczesną wiosną",0],["wczesną jesienią",1],["na przełomie wiosny i lata",0]],["Gargamele, malinowe, bawole serca to popularne gatunki:",["papryki",0],["ogórków",0],["pomidorów",1],["cebuli",0]],["“Zimni ogrodnicy” to okres, w którym występują majowe przymrozki. Nazwa tego zjawiska jest związana ze wspomnieniem świętych:",["św. Pawła, św. Piotra, św. Alojzego, św. Anny",0],["św. Pankracego, św. Serwacego, św. Bonifacego, św. Zofii",1],["św. Walentego, św. Józefa, św. Danuty, św. Łukasza",0],["św. Agnieszki, św. Anastazego, św. Ildefonsa, św. Tymoteusza",0]]]]
sportyekstremalne=[["Sporty ekstremalne",["Tak zwany solo climbing to rodzaj sporu ekstremalnego, który polega na wspinaczce bez:",["partnerów",0],["partnerów oraz lin zabezpieczających",0],["lin zabezpieczających",0],["partnerów i jakiegokolwiek sprzętu ochronnego",1]],["W którym wieku Janina Mey jako pierwsza Polka wykonała skok ze spadochronem?",["XX w.",0],["XIX w.",1],["XVIII w.",0],["XVI w.",0]],["Który z wymienionych sportów nie jest uznawany za sport ekstremalny?",["rower górski",0],["wyścigi łodzi motorowych",0],["spacery na linie",0],["kajakarstwo",1]]]]
miastawojewodzkie=[["Miasta wojewódzkie",["Olsztyn jest miastem wojewódzkim którego województwa?",["Warmińsko-mazurskiego",1],["Kujawsko-pomorskiego",0],["Zachodniopomorskiego",0],["Podkarpackiego",0]],[" Które miasto wojewódzkie liczy najwięcej ludności?",["Kraków",0],["Warszawa",1],["Poznań",0],["Bydgoszcz",0]],["W którym mieście  wojewódzkim możemy oglądać Spodek?",["W Katowicach",1],["W Krakowie",0],["W Bydgoszczy",0],["W Poznaniu",0]]]]
znanestronyinternetowe=[["Znane strony internetowe",["Biała, niekompletna kula ułożona z puzzli, to logo jakiej strony internetowej?",["Twittera",0],["Google",0],["Wikipedii",1],["Yahoo!",0]],["Wymień, w poprawnej kolejności, kolory znajdujące się na logo strony Google.com?",["Żółty, niebieski, czerwony, niebieski, zielony, żółty",0],["Niebieski, czerwony, żółty, niebieski, zielony, czerwony",1],["Czerwony, zielony, niebieski, czerwony, żółty, niebieski",0],["Zielony, żółty, czerwony, niebieski, czerwony, niebieski",0]],["W którym roku powstał portal społecznościowy Facebook?",["2005",0],["2006",0],["2004",1],["2003",0]]]]
zabytki=[["Zabytki",["Budowę katedry Notre Dame datuje się na",["XII-XIV wiek",0],["XV-XVIII wiek",0],["IX-XI wiek",0],["XVIII-XX wiek",0]],["Tadż Mahal to:",["kościół",0],["zamek",0],["pałac",0],["mauzoleum",1]],["Stonehenge znajduje się w",["Wielkiej Brytanii",1],["Stanach Zjednoczonych",0],["Chile",0],["Brazylii",0]]]]
jedzenie=[["Jedzenie",["Silnie trująca ryba, będącą tradycyjnym japońskim przysmakiem to:",["Fugu",1],["Koi",0],["Tara",0],["Tsuna",0]],["Pizza hawajska pochodzi:",["z Norwegii",0],["z Francji",0],["z Kanady",1],["z Wielkiej Brytanii",0]],["Co uznawane jest za najsłodszy owoc na świecie?",["mango",0],["granaty",0],["figi",1],["banan",0]]]]
komputery=[["Komputery",["Która z wymienionych nazw nie jest nazwą języka programowania?",["Python",0],["Prolog",0],["Braor",1],["Nim",0]],["Który słynny uczony jest nazywany ojcem nowoczesnego systemu binarnego?",["Gottfried Leibniz",1],["Isaac Newton",0],["Noam Chomsky",0],["Marvin Minsky",0]],["Kto jest uznawany za twórcę pierwszego programu komputerowego?",["Marvin Minsky",0],["Ada Lovelace",1],["Ludwig Wittgenstein",0],["Gottfried Leibniz",0]]]]
muzykaklasyczna=[["Muzyka klasyczna",["W jakim mieście pochowany jest Fryderyk Chopin?",["W Paryżu",1],["W Warszawie",0],["W Wilnie",0],["W Krakowie",0]],["Które z podanych dzieł skomponował Jan Sebastian Bach?",["Aria na strunie G",1],["Clair de Lune",0],["Lacrimosa",0],["Dies irae",0]],["Kto jest autorem “Jeziora Łabędziego”?",["Pyotr Ilyich Tchaikovsky",0],["Wolfgang Amadeus Mozart",0],["Karl Ditters von Dittensdorf",0],["Franciszek Liszt",0]]]]
religieiwierzenia=[["Religie i wierzenia",["Wedy to święte księgi:",["buddyzmu",0],["hinduizmu",1],["islamu",0],["judaizmu",0]],["Za początek islamu uznaje się:",["VII wiek n.e",1],["VII wiek p.n.e",0],["V wiek n.e",0],["V wiek p.n.e",0]]]]
literatura=[["Literatura",["Autorem powieści pt. “Lolita” uchodzącej za jedno z najbardziej kontrowersyjnych dzieł w historii jest: ",["Michaił Bułhakow",0],["Andriej Płatonow",0],["Vladimir Nabokov",1],["Dmitrij Bykow",0]],["“Lalka” Bolesława Prusa to powieść:",["romantyczna",0],["pozytywistyczna",1],["oświeceniowa",0],["z okresu XX-lecia międzywojennego",0]],["Jaki tytuł nosi najważniejsze dzieło Andrzeja Frycza Modrzewskiego?",["Kazania sejmowe",0],["Wojna chocimska",0],["O poprawie Rzeczypospolitej",1],["Rymy albo wiersze polskie",0]]]]
imionazenskie=[["Imiona Żeńskie",["Które z tych imion jest jednocześnie nazwą języka programowania wykorzystywanym w kontroli lotów?",["Ada",1],["Martha",0],["Sasha",0]],["Które z tych imion wywodzi się z języka greckiego?",["Julia",0],["Barbara",1],["Rebeka",0]]]]
komiksy=[["Komiksy",["Który z podanych bohaterów jest komiksowym dzieckiem rysownika Boba Kane'a?",["Spider-Man",0],["Batman",1],["Superman",0]],["Superbohater DC Comics poruszający się z wielką prędkością to:",["Shazzam",0],["Flash",1],["Green Lantern",0]],["Który z podanych bohaterów komiksów Marvela jest nazywany “Pierwszym Avengersem”?",["Iron Man",0],["Thor",0],["Kapitan Ameryka",0]]]]
geografia=[["Geografia",["Honolulu jest stolicą:",["Jamajki",0],["Hawajów",1],["Honolulu",0]],["Tadżykistan leży w:",["Afryce",0],["Azji ",1],["Ameryce Południowej",0]],["Najdłuższą rzeką świata jest Nil. Drugie miejsce zajmuje:",["Amazonka",1],["Jangcy",0],["Missisipi",0]]]]
alkohol=[["Alkohol",["Dochód ze sprzedaży jednego z najdroższych piw na świecie- Nail Brewing's Antarctic Nail Ale- przekazywany jest fundacji zajmującej się ochroną:",["niedźwiedzi polarnych",0],["wielorybów",1],["fok",0]],["Kiedy została wymyślona jedna z najpopularniejszych gier alkoholowych tzw. beer pong?",["lata 50 XX wieku",1],["lata 90 XX wieku",0],[" ata 20 XX wieku",0]],["Jaki alkohol jest uważany za trunek handlarzy niewolników, oszustów i przemytników?",["whisky",0],["rum",1],["piwo",0]]]]
wyspy=[["Wyspy",["Które z tych wysp wchodzą w skład terytorium Australii?",["Wyspy Kokosowe",1],["Wyspy Cooka",0],["Wyspy Wielkanocne",0]],["Do terytorium którego z tych państw nie zalicza się wyspa Borneo?",["Indonezja",0],["Brunei",0],["Papua-Nowa Gwinea",1]],["Do terytorium jakiego państwa zalicza się Wyspa Wiktorii?",["Kanada",1],["Nowa Zelandia",0],["Wielka Brytania",0]]]]
religiawfilmach=[["Nawiązania religijne w kinematografii",["Po jakiej krainie spaceruje Jack, główny bohater filmu Larsa von Triera pod tytułem “Dom, który zbudował Jack?”?",["Po niebie",0],["Po Edenie",0],["Po piekle",1]],["Kim jest mężczyzna, partner tytułowej Matki, w filmie Darrena Aronofsky’ego pod tytułem “Mother!”?",["Poetą",0],["Bogiem",1],["Artystą",0]],["Który z siedmiu grzechów głównych reprezentuje John Doe, antagonista filmu pod tytułem “Se7en” w reżyserii Davida Finchera?",["Pychę",0],["Złość",0],["Zazdrość",1]]]]
seriale=[["Seriale",["W Polsce najchętniej oglądanym serialem Netflixa w 2019 roku był:",["“Dom z papieru”",0],["“Stranger Things”",0],["“Wiedźmin”",1]],["Cytat “Dzieci się zawsze źle komponują w mieszkaniu” pochodzi z",["“Czterdziestolatka”",1],["“Złotopolskich”",0],["“Świata według Kiepskich”",0]],["Który z tych seriali nakręcono najwcześniej?",["“Przyjaciele”",0],["“Słoneczny patrol”",1],["“Jak poznałem waszą matkę”",0]]]]
psychologia=[["Psychologia",["Prawo głoszące, że im więcej czasu mamy na wykonanie jakiejś pracy, tym więcej czasu nam ono zabiera, nazywany:",["Prawem Parkinsona",1],["Prawem Morisona",0],["Prawem Pareta",0]],["Tendencja do automatycznego, pozytywnego lub negatywnego, przypisywania cech na podstawie pierwszego wrażenia to:",["Efekt Rosenthala",0],["Efekt halo",1],["Efekt Pollyanny",0]],["Efekt cocktail party polega na:",["uwrażliwieniu na wszelkie bodźce odnoszące się bezpośrednio do nas",1],["uwrażliwieniu na bodźce odnoszące się do środowiska, w którym się znajdujemy",0],["dostosowywaniu naszego zachowania do zachowań powszechnych, społecznie akceptowalnych",0]]]]
kuchnieswiata=[["Kuchnie świata",["Włoska potrawa cotoletta alla milanese najbardziej przypomina...",["Pierogi z kapustą i z grzybami",0],["Placki ziemniaczane",0],["Kotlet schabowy",1]],["Gazpacho to zupa, która zazwyczaj ma kolor…",["Czerwony",1],["Zielony",0],["Żółty",0]],["Jedna z najpopularniejszych w Chinach zup jest robiona z jaskółczych…",["Łap",0],["Gniazd",1],["Języków"]]]]
polskafantastyka=[["Polska fantastyka",["Imię ukochanej Daimona Freya, bohatera “Siewcy Wiatru” autorstwa Mai Lidii Kossakowskiej?",["Hija",1],["Lilith",0],["Drop",0]],["Imię czarodziejki z serii książek o Wiedźminie, autorstwa Andrzeja Sapkowskiego, która należała do Rady Królewskiej Temerii?",["Keira Metz",1],["Yennefer z Vengerbergu",0],["Fringilla Vigo",0]],["Kim była obrończyni, którą otrzymał od klasztoru Amszilas inkwizytor Mordimer Madderdin, bohater serii książek Jacka Piekary?",["Inkwizytorką",1],["Zakonnicą",0],["Anielicą",1]]]]
gory=[["Góry",["Który łańcuch górski z podanych poniżej jest najmłodszy?",["Sudety",0],["Karpaty",1],["Góry Świętokrzyskie",0]],["Jaki jest najwyższy szczyt Azerbejdżanu?",["Bazardüzü",1],["Hazrat Sulton",0],["Czogori",0]],["Jaka jest średnia roczna temperatura na szczycie Śnieżki?",["5 st. C",0],[" 0,4 st. C",1],["-4 st. C",0]]]]
waluta=[["Waluty",["Waluta wenezuelska to:",["dolar",0],["somoni",0],["boliwar",1]],["Państwem, w którym walutą nie jest peso, jest/są:",["Filipiny",0],["Dominikana",0],["Bahamy",1]],["1 peso meksykańskie to w przeliczeniu:",["1,08 zł",0],["0,18 zł",1],["0,46 zł",0]]]]
uczeni=[["Uczeni wszechczasów",["Który z tych XVII-wiecznych uczonych urodził się wcześniej?",["Gottfried Leibniz",0],["Isaac Newton",1]],["W którym roku został ścięty Antoine Lavoisier, wybitny francuski chemik?",["W 1793",0],["W 1794",1]],["W którym z tych włoskich miast urodził się Galileusz?",["Piza",1],["Mediolan",0]]]]
grywideo=[["Gry wideo",["Miejsce akcji dodatku do Bioshocka Infinite Burial at Sea?",["Colombia",0],["Rapture",1]],["Nazwa starszego smoka w grze Monster Hunter: World, którego główny atak polega na zabieraniu życia graczowi?",["Kushala Daora",0],["Vaal Hazak",1]],["Imię postaci w grze Dota 2, demona, którego znamy pod przydomkiem Queen of Pain?",["Akasha",1],["Shendelzare",0]]]]
kosmos=[["Kosmos",["Ile księżyców ma Jowisz?",["79",1],["89",0]],["W którym roku odbył się pierwszy turystyczny lot w kosmos?",[" 2005",0],["2001",1]],["Kiedy najszybciej będziemy mogli obserwować kometę Halleya?",["w 2050 r",0],["w 2061 r.",1]]]]
prl=[["PRL",["Ile mierzyła Warszawska Radiostacja Centralna w Gąbinie, która do 1991 roku była najwyższym obiektem wzniesionym przez człowieka?",["ponad 646 metrów",1],["ponad 846 metrów",0]],["Pierwsze częściowo wolne wybory w historii Polski po II wojnie światowej odbyły się w roku:",["1991",0],["1989",1]],["Co, według propagandy PRL, Amerykanie zrzucali z samolotów nad Polską?",["stronkę ziemniaczaną",1],["odpady promieniotwórcze",0]]]]

wszystkie_kategorie=[zwierzeta,mitologiagrecka,przyslowia,swieta,krolowiepolski,muzykafilmowa,ogrodnictwo,sportyekstremalne,jedzenie,miastawojewodzkie,zabytki,znanestronyinternetowe,religieiwierzenia,komputery,literatura,muzykaklasyczna,alkohol,geografia,imionazenskie,komiksy,psychologia,religiawfilmach,seriale,wyspy,kuchnieswiata,kuchnieswiata,polskafantastyka,waluta,waluta,grywideo,kosmos,prl,uczeni]

portfel = 1000000

class gra():

    def losowanie_kategorii(self,lista_kategorii):
        int_kategoria=random.randint(0,3)
        kategoria_return=[]
        kategoria_return.append(lista_kategorii[int_kategoria])
        kategoria_2=random.randint(0,3)
        while kategoria_2==int_kategoria:
            kategoria_2=random.randint(0,3)
        kategoria_return.append(lista_kategorii[kategoria_2])
        return kategoria_return

    def wybieranie_kategorii(self,mozliwe_kategorie):
        print(mozliwe_kategorie)
        print("Zeby wybrac pierwsza kategorie, nacisnij 1.\nZeby wybrac druga kategorie nacisnij 2.")
        wybrana_kategoria=int(input())
        wybrana_return=[]
        if wybrana_kategoria==1:
            wybrana_return=mozliwe_kategorie[0]
        elif wybrana_kategoria==2:
            wybrana_return=mozliwe_kategorie[1]
        else:
            print("Błędna komenda, uruchom program ponownie.")
        return wybrana_return

    def obstawianie(self,portfel,kategoria):
        for element in wszystkie_kategorie:
            if kategoria==element[0][0]:
                superzmienna = random.randint(1,3)
                pytanie=element[0][superzmienna][0]
                print(pytanie)
                index=1
                for value in element[0][superzmienna][1:]:
                    print(index,".",value[0])
                    index+=1
                break
        ilosc_obstawiona_1=0
        ilosc_obstawiona_2=0
        ilosc_obstawiona_3=0
        ilosc_obstawiona_4=0
        start = time.time()
        print("W przedstawionej kolejności podaj kwoty, które chcesz przypisać do kolejnych odpowiedzi. Ilość pieniędzy do obstawienia:",portfel)
        ilosc_obstawiona_1=int(input("Kwota na odpowiedź pierwszą:"))
        while ilosc_obstawiona_1 > portfel:
            print("wpisałeś kwotę wyzszą niż posiadasz, popraw to")
            ilosc_obstawiona_1 = int(input("Kwota na odpowiedź pierwszą:"))
        portfel-=ilosc_obstawiona_1
        if portfel>0 and (time.time()-start)<60:
            ilosc_obstawiona_2=int(input("Kwota na odpowiedź drugą:"))
            while ilosc_obstawiona_2 > portfel:
                print("wpisałeś kwotę wyzszą niż posiadasz, popraw to")
                ilosc_obstawiona_2 = int(input("Kwota na odpowiedź drugą:"))
            portfel -= ilosc_obstawiona_2

            if portfel>0 and (time.time()-start)<60:
                ilosc_obstawiona_3=int(input("Kwota na odpowiedź trzecią:"))
                while ilosc_obstawiona_3 > portfel:
                    print("wpisałeś kwotę wyzszą niż posiadasz, popraw to")
                    ilosc_obstawiona_3 = int(input("Kwota na odpowiedź trzecią:"))
                portfel -= ilosc_obstawiona_3

                if portfel > 0 and (time.time()-start)<60:
                    ilosc_obstawiona_4=int(input("Kwota na odpowiedź czwartą:"))
                    while ilosc_obstawiona_4 > portfel:
                        print("wpisałeś kwotę wyzszą niż posiadasz, popraw to")
                        ilosc_obstawiona_4 = int(input("Kwota na odpowiedź czwartą:"))
                    portfel -= ilosc_obstawiona_4
                else:
                    print("Obstawiłes już wszystkie posiadane pieniądze")
            else:
                print("Obstawiłes już wszystkie posiadane pieniądze")
        else:
            print("Obstawiłes już wszystkie posiadane pieniądze")
        portfel = (element[0][superzmienna][1][1]*ilosc_obstawiona_1) + (element[0][superzmienna][2][1] * ilosc_obstawiona_2) + (element[0][superzmienna][3][1] * ilosc_obstawiona_3) + (element[0][superzmienna][4][1] * ilosc_obstawiona_4)
        print("Brawo udało Ci się zachować:",portfel)
        return portfel
def killer(portfel):
    if portfel <= 0:
        print("przegrałeś")
        input()
        quit()


gracz=input()

print("Witaj,",gracz,"w programie Postaw na Milion!")
print("Twoim zadaniem będzie odpowiadanie na pytania na różnym poziomie trudności, obstawiając na odpowiedzi tytułowy milion złotych. Odpowiadaj poprawnie, by wygrać jak najwiecęj! ")
print("By wyświetlić zasady gry, naciśnij 1.")
print("By rozpocząć rozgrywkę wciśnij 2")
wybor_menu=int(input())
if wybor_menu==1:
    print("Na starcie gry do dyspozycji masz milion złotych.\nGra składa się z 8 poziomów, na każdym z nich będziesz musiał/musiała odpowiedzieć na jedno pytanie.\nOdpowiadasz obstawiając pieniądze, które dostaniesz na początku, na dane odpowiedzi.\nJeśli jesteś jakiejś pewny, możesz postawić na nią całą kwotę.\nJeśli nie, możesz rozłożyć ją na dodatkowe odpowiedzi.\nWszystko zależy od Ciebie. :) ")
elif wybor_menu==2:
    print("A zatem przejdźmy do rozgrywki.")

    kappa = gra()
    kategoria1 = kappa.losowanie_kategorii(kategorie_p1)
    kategoriawybrana1 = kappa.wybieranie_kategorii(kategoria1)
    portfel = kappa.obstawianie(portfel,kategoriawybrana1)
    killer(portfel)

    kappa2 = gra()
    kategoria2 = kappa2.losowanie_kategorii(kategorie_p2)
    kategoriawybrana2 = kappa2.wybieranie_kategorii(kategoria2)
    portfel = kappa2.obstawianie(portfel,kategoriawybrana2)
    killer(portfel)

    kappa3 = gra()
    kategoria3 = kappa3.losowanie_kategorii(kategorie_p3)
    kategoriawybrana3 = kappa3.wybieranie_kategorii(kategoria3)
    portfel = kappa3.obstawianie(portfel,kategoriawybrana3)
    killer(portfel)

    kappa4 = gra()
    kategoria4 = kappa4.losowanie_kategorii(kategorie_p4)
    kategoriawybrana4 = kappa4.wybieranie_kategorii(kategoria4)
    portfel = kappa4.obstawianie(portfel,kategoriawybrana4)
    killer(portfel)

    kappa5 = gra()
    kategoria5 = kappa5.losowanie_kategorii(kategorie_p5)
    kategoriawybrana5 = kappa5.wybieranie_kategorii(kategoria5)
    portfel = kappa5.obstawianie(portfel,kategoriawybrana5)
    killer(portfel)

    kappa6 = gra()
    kategoria6 = kappa6.losowanie_kategorii(kategorie_p6)
    kategoriawybrana6 = kappa6.wybieranie_kategorii(kategoria6)
    portfel = kappa6.obstawianie(portfel,kategoriawybrana6)
    killer(portfel)

    kappa7 = gra()
    kategoria7 = kappa7.losowanie_kategorii(kategorie_p7)
    kategoriawybrana7 = kappa7.wybieranie_kategorii(kategoria7)
    portfel = kappa7.obstawianie(portfel,kategoriawybrana7)
    killer(portfel)

    kappa8 = gra()
    kategoria8 = kappa8.losowanie_kategorii(kategorie_p8)
    kategoriawybrana8 = kappa8.wybieranie_kategorii(kategoria8)
    portfel = kappa8.obstawianie(portfel,kategoriawybrana8)

    print("Wygrałeś, udało Ci się zachować:",portfel,"punktów")
    input()
    quit()

else:
    print("Nieprawidłowa komenda. Uruchom program ponownie.")
