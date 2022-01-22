## Informacj o bazie danych

Dane w bazie danych 12_swietokrzyskie.csv zawierają informacje o ocenie produktu poszczególnej marki w województwie Świętorzyskim. Kupujący podawali także swój wiek oraz płeć


Ścieżki do odpowiednich plików:

- Oryginalna baza danych - ../Original Data/12_swietokrzyskie.csv
- Metadane - ../Original Data/Metadata/metadane.md
- Plik wykonawczy konwersji danych (w języku Python Jupyter) prowadzący do formatu uporządkowanego według zadami tidydata oraz eksport do pliku wyniku - ../Command Files/konwersja.ipynb
- Baza danych poddana konwersji według zasad Tidy Data powstała w wyniku kodu wykonawczego - ../Analysis Data/tb_tidy.tb
DataAppendix

Do wykonana konwersji należy:
1. Zaimportować wymagane pakiety do uruchomienia skryptu konwersja.ipynb
2. Uruchomić skrypt z lokalizacji ../Command Files/konwersja.ipynb
3. Skrypt wykona operacie TidyData na wejściowej bazie danych, a następnie ją zapiszę 
4. W pliku ../Analysis Data/tb_tidy.tb będzie znajdować się gotowa do dalszych prac baza danych.