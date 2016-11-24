f1 = open("plik1.txt","wb")

print f1.name

print f1.mode # tryb w jakim otworzono plik

print f1.closed #okresla czy plik zamkniety

#metody do obslugi pliku

f1.write("pierwszy plik")

f1.flush() # zapisuje dane z bufora do pliku przydatne w windows

f1.write("\nMowa linia")

f1.close() #zamykani pliku+

f1 = open("plik1.txt","r+b") #otwarcie do modyfikacji

print f1.read() #odczytuje z pliku napis

print f1.tell() #aktualna pozycja w pliku

f1.seek(0) #ustawia pozycje w pliku
f1.write("Nowy poczatek") #nadpisanie pliku
f1.seek(-14,1) #przesuniecie na wzgledna pozycje pliku
print f1.read(14) #wczytanie fragmentu zawartosci pliku w okresonej dlugosci
f1.writelines(["\n3 linia", "\n4 linia", "\n5 linia"]) #zapisanie do pliku sekwencji znakow

f1.seek(0)
print f1.readlines()
f1.truncate(30) # skraca plik na podanej pozycji
f1.seek(0)
print f1.read()

print f1.isatty() #zwraca true jezeli plik jest doloczony di urzadzenia terminalowego

import sys
ekran = sys.stdout
sys.stdout = open("wyjscie.txt","w")
print "jestem tutaj"
print "gdzie ty poszedles?"
sys.stdout = ekran
print open("wyjscie.txt","r").read()