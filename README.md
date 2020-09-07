# BALD

## Info
* Program BALD pobiera numery NIP z dokumentu tekstowego 'nip.txt' i wyszukuje dane w bazie
Ministerstwa Finansów - Krajowej Administracji Skarbowej za pomocą interfejsu programistycznego
API Wykazu podatników VAT.
* Dla podanych nr NIP, wyszukuje rachunki bankowe.
* Możesz wyszukać dane dla 30 nr NIP jednocześnie.
* Wynik wyszukania exportowany jest jako:
  - dokument tekstowy 'wynikVAT.txt' (Nazwa firmy + rachunki bankowe)
  - dokument tekstowy 'wynikVATadresy.txt' (rachunki bankowe, nazwy i dane teleadresowe banków)
* Podczas wykonywania programu w podglądzie dostępne są również:
  - Nazwa firmy, REGON, KRS, Status VAT, Adres siedziby i zamieszkania,
    data i unikalny identyfikator – klucz elektroniczny, który jest potwierdzeniem
    wykonania zapytania.
* Ponadto w bazie programu, znajduje się ponad 3100 numerów identyfikacyjnych placówek banków polskich
  służących do identyfikacji banków i adresów dla wyszukanych rachunków bankowych.
* Baza rachunków aktualizowana jest średnio co 10 dni na stronie 'https://ewib.nbp.pl'
  w zakładce 'Dane do pobrania' ->> 'Dane z ewidencji'
* Program daje możliwość pobrania pliku i aktualizacji ale gdyby coś nie działało..
  Wystarczy pobrać plik 'plewibnra.txt' i umieścić w tym samym folderze co program
  reszta wykona się automatycznie :)
* Wymagane jest podłączenie do internetu.

## Biblioteki
Program zbudowany przy wykorzystaniu języka Python 3.8.5 
wykorzystuje poniższe biblioteki:
* requests
* os.path
* json
* join
* time
* datetime
* colorama
* termcolor

## Jak zacząć?
Na początku pobierz repozytorium
* W foldrze powinny znajdować się 3 pliki: 
   - [1] bald.py - program *(jeśli jest skompilowany będziesz miał - bald.exe)
   - [2] nip.txt - dokument tekstowy w którym wpisujesz numery NIP
   - [3] plewibnra.txt - dokument tekstowy zawierający numery rachunków i adresy placówek bankowych
* Jeśli nie masz pliku 'nip.txt' utwórz go klikając:
   - Prawy przycisk myszy > Nowy > Dokument tekstowy > Nazwij 'nip'
* Jeśli nie masz pliku 'plewibnra.txt', pobierz go ze strony: https://ewib.nbp.pl/faces/pages/daneDoPobrania.xhtml
* Otwórz plik 'nip.txt' i wpisz numery NIP szukanych firm w n/w formacie: (bez myślników)
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
* Zapisz plik 'nip.txt' lub użyj skrótu 'CTR+S'
* Uruchom program i postępuj zgodnie ze wskazówkami na ekranie

Licencja
----

MIT

**Darmowy**

## Od autora
To mój pierwszy poważniejszy projekt i niestety nie przywiązywałem wagi do czytelności kodu.
Ten program nie jest wolny od wad i błędy po stronie TEJ aplikacji mogą wystąpić.
Twój komputer nie wybuchnie :) ale nie gwarantuje, że zawsze będzie działał. 
