import requests
import json
import os.path, time
from datetime import datetime
import colorama as color
import termcolor as colors
color.init()

def pobranie_pliku():
    try:
        url_nbp = "https://ewib.nbp.pl/plewibnra?dokNazwa=plewibnra.txt"
        r = requests.get(url_nbp, allow_redirects=True)
        open('plewibnra.txt', 'wb').write(r.content)
        print(colors.colored('  Uaktualniono listę rachunków bankowych', 'green'))
        data_2 = os.path.getmtime("plewibnra.txt")
        modificationTime_2 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(data_2))
        print("   Data pliku 'plewibnra.txt': ", modificationTime_2, "\n")
    except:
        print("Nie udało się uaktualnić listy. Spróbuj ręcznie.")

def ladowanie_pliku():
    data = open("plewibnra.txt", "r", encoding="852")

    lista = []
    for index in data:
        linia = index.replace("\t", "+").replace("  ", "").replace("\n", "")
        lista.append(linia)
    return lista

def slownik(lista_nowa):
    nowa_lista = []
    for i in lista_nowa:
        data = i.split("+")
        nowa_lista.append(data)
    return nowa_lista
        
def lista_bankow(nowa_lista):
    banki = {}
    for i in nowa_lista:
        numer = i[4]
        nazwa = i[1] + ", " + i[5] + ", " + i[9] + " " + i[7] + ", " + i[8] + ", skr. pocztowa: " + i[11] + ", tel." + i[14] + ", tel." + i[15] + ", fax." + i[16] + ", fax." + i[17] + ", strona internetowa : " + i[21]
        banki[numer] = nazwa
    return banki

try:
    lista_nowa = ladowanie_pliku()
    nowa_lista = slownik(lista_nowa)
    lista_bankow = lista_bankow(nowa_lista)
    data_1 = os.path.getmtime("plewibnra.txt")
    modificationTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(data_1))
except:
    print(colors.colored("* Błąd! Program nie zadziała *", 'red'))
    print(colors.colored("* Czyżby brak pliku 'plewibnra.txt'? *", 'red'))
    print(colors.colored("* Aktualny plik do pobrania na stronie 'https://ewib.nbp.pl/' *", 'yellow'))
    print(colors.colored("* W zakładce 'Dane do pobrania' -> 'Dane z ewidencji' *", 'yellow'))
    print(colors.colored("* Umieść plik 'plewibnra.txt' w tym samym miejscu co program :) *", 'yellow'))
    input()
    exit()
    
print("   \nBaza rachunków z dnia: ", modificationTime, "\n")




########################## STAŁE/ZMIENNE/LISTY ##################################

CYFR = 10
cyfra = 0
lista = []
slownik = {}
pozycja = 0
slownikN = {}
starter = 0
PIERWA = []
poczatek = []
moc = 0
wartownik2 = "pq"
poker = 0
answer = None
while answer != 2:
    print(colors.colored("             ______        ___       __       _______  ", 'cyan', attrs=['bold']))
    print(colors.colored("            |   _  \      /   \     |  |     |       \ ", 'cyan', attrs=['bold']))
    print(colors.colored("            |  |_)  |    /  ^  \    |  |     |  .--.  |", 'cyan'))
    print(colors.colored("            |   _  <    /  /_\  \   |  |     |  |  |  |", 'blue', attrs=['bold']))
    print(colors.colored("            |  |_)  |  /  _____  \  |  `----.|  '--'  |", 'blue'))
    print(colors.colored("            |______/  /__/     \__\ |_______||_______/ ", 'blue'))

    print(colors.colored('\n\n                            Menu startowe', 'blue', attrs=['bold']))
    print(colors.colored('                         ==================', 'blue', attrs=['dark']))
    print(" ")
    print("                          1. Instrukcja")
    print(colors.colored("                      --> 2. START", 'green'))
    print("                          3. O programie")
    print("                          4. O autorze")
    print(colors.colored("                          5. Aktualizuj rachunki bankowe", 'yellow'))
    print(colors.colored("             |", 'green'))
    print(colors.colored("             V", 'green'))
    answer = input(" Wybieram.. :")
    
    if answer == "2":
        break
    elif answer == "1":
        print(colors.colored("\n          Instrukcja", 'cyan'))
        print("""          1. W foldrze powinny znajdować się 3 pliki: 'bald.exe', 'nip.txt i 'plewibnra.txt'
          1a.Jeśli nie masz pliku 'nip.txt' utwórz go klikając:
             Prawy przycisk myszy > Nowy > Dokument tekstowy > Nazwij 'nip'
          1b.Jeśli nie masz pliku 'plewibnra.txt', pobierz go ze strony:
             https://ewib.nbp.pl/faces/pages/daneDoPobrania.xhtml
          2. Otwórz plik 'nip.txt' i wpisz numery NIP szukanych firm w n/w formacie: (bez myślników)
             XXXXXXXXXX
             XXXXXXXXXX
             XXXXXXXXXX
             XXXXXXXXXX  itd.
          2. Zapisz plik 'nip.txt' lub użyj skrótu 'CTR+S'
          3. Uruchom program i postępuj zgodnie ze wskazówkami""")
    elif answer == "4":
        print(colors.colored("\n          Łukasz Sawczuk", 'cyan'))
        print("""
          Autorski program, napisany w języku Python.
          W przypadku pytań lub błędów:""")
        print(colors.colored("          eimearofficial@gmail.com\n", 'cyan'))
        print("""          *Kod blędu można uzyskać otwierając program w interpreterze poleceń (konsoli)
          **2-krotnie kliknij ścieżkę w folderze z programem (C://Windows/....) i wpisz 'cmd'.
          W wierszu poleceń wpisz 'bald.exe'
          Po uruchomieniu programu, wyślij mi kod błędu e-mailem :)\n""")    
        
    elif answer == "3":
        print("\n")
        print(colors.colored("                                                        UWAGA!", "red"))
        print("""
        -----------------------------------------------------------------------------------------------------
        |                                 Korzystanie z API jest limitowane!                                 |
        |                          Program wykorzystuje metodę „search” - 10 zapytań                         |
        |                               o maksymalnie 30 podmiotów jednocześnie.                             |
        |                     W przypadku utraty dostępu, limit zostaje zdjęty o północy.                    |
        |               (szczegóły - https://www.gov.pl/web/kas/api-wykazu-podatnikow-vat)                   |
        -----------------------------------------------------------------------------------------------------""")
        print("""
        1.Program pobiera numery NIP z dokumentu tekstowego 'nip.txt' i wyszukuje dane w bazie
          Ministerstwa Finansów - Krajowej Administracji Skarbowej za pomocą interfejsu programistycznego
          API Wykazu podatników VAT.
        2.Dla podanych nr NIP, wyszukuje rachunki bankowe.
        2a. Możesz wyszukać dane dla 30 nr NIP jednocześnie.
        3.Wynik wyszukania exportowany jest jako:
          - dokument tekstowy 'wynikVAT.txt' (Nazwa firmy + rachunki bankowe)
          - dokument tekstowy 'wynikVATadresy.txt' (rachunki bankowe, nazwy i dane teleadresowe banków)
        4.Podczas wykonywania programu w podglądzie dostępne są również:
          - Nazwa firmy, REGON, KRS, Status VAT, Adres siedziby i zamieszkania,
          data i unikalny identyfikator – klucz elektroniczny, który jest potwierdzeniem
          wykonania zapytania.
        4.Ponadto w bazie programu, znajduje się ponad 3100 numerów identyfikacyjnych placówek banków polskich
          służących do identyfikacji banków i adresów dla wyszukanych rachunków bankowych.""")
        print(colors.colored("          Baza rachunków aktualizowana jest średnio co 10 dni na stronie 'https://ewib.nbp.pl'", "yellow"))
        print(colors.colored("          w zakładce 'Dane do pobrania' ->> 'Dane z ewidencji'", "yellow"))
        print(colors.colored("          Program daje możliwość pobrania pliku i aktualizacji ale gdyby coś nie działało..", "yellow"))
        print(colors.colored("          Wystarczy pobrać plik 'plewibnra.txt' i umieścić w tym samym folderze co program", "yellow"))
        print(colors.colored("          reszta wykona się automatycznie :)", "yellow"))
        print("        5.Wymagane jest podłączenie do internetu.")

    elif answer == "5":
        pobranie_pliku()
    else:
        print("Nie rozumiem.. wybierz od 1 do 3.")
    

################ OTWARCIE PLIKU ########################

try:
    text = open('nip.txt', 'r', encoding='utf-8')
except FileNotFoundError:
    print(colors.colored('*************************', 'red'))
    print(colors.colored('*  Brak pliku "nip.txt" *', 'red'))
    print(colors.colored('*************************', 'red'))
    tajn = input("!!! Utwórz dokument tekstowy o nazwie 'nip.txt i ponownie uruchom program !!!")  
    while tajn != "blacha":
        tajn = input("!!! Utwórz dokument tekstowy o nazwie 'nip.txt' i ponownie uruchom program !!!")
    
czytacz = text.readlines()
for index in czytacz:
    numery = index.replace("\n", "")
    numery = numery.upper()
    lista.append(numery)
    

############### USTALENIE NR POZYCJI ###################
liczba = len(lista)
print("\n Liczba i nr NIP w dokumencie 'nip.txt'")


############## USTALENIE ZAWARTOŚCI DOK ################

if liczba == 0:
    print(colors.colored('\n*****************************', 'red'))
    print(colors.colored("* Plik 'nip.txt' jest pusty *", 'red'))
    print(colors.colored('*****************************', 'red'))
    print("""
        Uzupełnij dokument 'nip'txt' wpisując numery NIP firm w formie:
        XXXXXXXXXX
        XXXXXXXXXX
        XXXXXXXXXX
        XXXXXXXXXX itd.""")
    tajn = input("\n!!! Uzupełnij dane i ponownie uruchom program !!!")
    while tajn != "blacha":
        tajn = input("!!! Uzupełnij dane i ponownie uruchom program !!!")

############# WYPISANIE NR NIP ########################

kosz = 1
for i in lista:
    print(" Poz", kosz, "[", i, "]")
    kosz += 1


############################################################################################
###################### SPRAWDZENIE ILOŚCI CYFR W NIP #######################################
############################################################################################


while poker != liczba:
    kiszka = len(lista[poker])
    if kiszka != CYFR:
        while wartownik2 != "policja":
            print(colors.colored(" [ Nie zgadza się ilość cyfr w numerze NIP! ] ", "red"))
            print(" [ 1. Numer NIP składa się z 10 cyfr ] ")
            input(" [ 2. Jeśli przy którejś pozycji masz puste miejsce - usuń spacje w dokumencie 'nip.txt' ] ")
    poker += 1

input("\n Naciśnij 'Enter' by sprawdzić połączenie z API\n")

###########################################################################
########################## TEST URL API ###################################
###########################################################################
print(colors.colored(" [Sprawdzam połączenie z API] https://wl-api.mf.gov.pl", "yellow"))


urlVAT = 'https://wl-api.mf.gov.pl/'
try:
    responseVAT = requests.get(urlVAT)
except:
    print(colors.colored(" [Błąd!] Sprawdź połączenie z internetem..", "red"))
    input()
   
try:
    testURLVAT = str(responseVAT)
except NameError:
    print(colors.colored(" [Błąd!] Sprawdź połączenie z internetem..", "red"))
    input()

try:
    if testURLVAT == "<Response [200]>":
        print(colors.colored(" [Sukces!] API [mf.gov.pl] odpowiada poprawnie!", "green"))
    else:
        print(colors.colored(" [Błąd!] API [mf.gov.pl] nie odpowiada..", "red"))
        print(colors.colored(" Program nie zadziała..", "red"))
        odpyt = input(" Program nie zadziała..")
        while odpyt != "colors":
            odpyt = input(" Program nie zadziała..")
except ValueError:
    print(colors.colored(" [Błąd!] Brak połączenia z internetem..", "red"))

#############################################################################
##########################     DATA       ###################################
#############################################################################

data = input("\n Wprowadź datę wyszukiwania w formacie 'RRRR-MM-DD' :")
while not data:
    data = input(" Wprowadź datę wyszukiwania w formacie 'RRRR-MM-DD' :")
print("\n *Wprowadziłeś [", data, "]")

input("\n Program wykona się automatycznie, naciśnij Enter by kontynuować.\n")

#############################################################################
########################## PĘTLA PROGRAMU ###################################
#############################################################################

zawartoscVAT = {}
pokeflut = 0
nrRACH = 1

while pokeflut != liczba:
    try:
        urlVATX = ("https://wl-api.mf.gov.pl/api/search/nip/" + lista[pokeflut] + "?date=" + data)
        responseVATX = requests.get(urlVATX)
        testURLVATX = str(responseVATX)
    except TimeoutError:
        print("""Próba połączenia nie powiodła się, ponieważ połączona strona nie odpowiedziała poprawnie po ustalonym okresie czasu
lub utworzone połączenie nie powiodło się, ponieważ połączony host nie odpowiedział..""")
    if testURLVATX == "<Response [200]>":
        allVAT = responseVATX.json()
        result1 = allVAT['result']
        subject = result1['subject']
        request_date = result1['requestDateTime']
        request_id = result1['requestId']
        try:
            name = subject['name']
            konta = subject['accountNumbers']
            regon = subject['regon']
            krs = subject['krs']
            working_adress = subject['workingAddress']
            residence_adress = subject['residenceAddress']
            status = subject['statusVat']
            print(colors.colored("############################################################", "yellow"))
            print(colors.colored("############################################################", "yellow"))
            print("\nDla numeru NIP [", lista[pokeflut], "]")
            print("Firma [", name, "]")
            print("REGON [", regon, "]")
            print("KRS [", krs, "]")
            print("Status VAT [", status, "]")
            print("Adres siedziby [", residence_adress, "]")
            print("Adres prowadzonej działalności [", working_adress, "]")
            print("Data zapytania [", request_date, "]")
            print("Identyfikator zapytania [", request_id, "]")
            zawartoscVAT[name] = konta
            print("\nOdszukano numery rachunków:")
            for i in konta:
                print("[", nrRACH, "]", i)
                nrRACH += 1
            print(colors.colored("\n############################################################", "yellow"))
            print(colors.colored("############################################################", "yellow"))
            pokeflut += 1
            nrRACH = 1
        except (TypeError, NameError):
            print(colors.colored("UWAGA", "red"))
            print("Dla numeru NIP", lista[pokeflut], "nic nie odszukano")
            input("Wciśnij 'enter' by kontynuować wyszukiwanie.\n")
            pokeflut += 1
            nrRACH += 1
            continue
            
    else:
        print(colors.colored("UWAGA", "red"))
        print("Dla numeru NIP", lista[pokeflut], "nic nie odszukano")
        input("Wciśnij 'enter' by kontynuować wyszukiwanie.\n")
        pokeflut += 1
        nrRACH += 1

#############################################################################
##########################   EXPORT TXT   ###################################
#############################################################################


print(colors.colored("Tworzę plik tekstowy 'wynikVAT.txt'", "green"))
listek = []
kopek = []
ostateczna = []

listek = zawartoscVAT
for i in listek:
    ostateczna.append(i)
    kopek = zawartoscVAT[i]
    for d in kopek:
        ostateczna.append(d) 

stopa = []
for index in ostateczna:
    stopa.append(index)

lenik = len(stopa)
text_file2 = open("wynikVAT.txt", "w", encoding="utf-8")
for index in stopa:
    text_file2.write(index + '\n')
    
text_file2.close()   

print(colors.colored("Tworzę plik tekstowy 'wynikVATadresy.txt'", "yellow"))

pobranie_danych = []
nazwy_rach = []
startX1 = 1

text_file3 = open("wynikVAT.txt", "r", encoding="utf-8")
lista_rachunki = text_file3.readlines()
liczba_rachunkow = len(lista_rachunki)

wynikVATadresy = open("wynikVATadresy.txt", "w", encoding="utf-8")
for i in lista_rachunki:
    rach_bez = i.replace("\n", "")
    pobranie_danych.append(rach_bez[2:10])
try:
    while startX1 != liczba_rachunkow:
        if pobranie_danych[startX1] in lista_bankow:
            definicja = lista_bankow[pobranie_danych[startX1]]
            nazwy_rach.append(definicja)
            wynikVATadresy.write(lista_rachunki[startX1] + definicja + "\n\n")
            startX1 += 1
        else:
            startX1 += 1
except IndexError:
    print(colors.colored("\nDla podanych NIP nie znaleziono danych..", "red"))
    print(colors.colored("Utworzone pliki wynikowe pozostaną puste..", "red"))
    input("Wciśnij 'enter' by zakończyć.")

wynikVATadresy.close()

input("\aKoniec programu..")

