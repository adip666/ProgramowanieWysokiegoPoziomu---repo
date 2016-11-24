# kolo fortuny
import linecache
import random

class Zawodnik:
    def add(self, index):
        self.index = index
        self.imie = str(raw_input())

    pass

print 'Ilosc uczestnikow'
liczbaLudziow = int(raw_input())
numerkiKolejnosci = range(1,liczbaLudziow+1)
count = len(open('Hasla.txt', 'rU').readlines())
wiersz = linecache.getline('Hasla.txt', random.randint(1,count))
haslo = wiersz[wiersz.find(" ")+1:]
print numerkiKolejnosci
#print numerkiKolejnosci.remove()
print "Kategoria: ", wiersz[0:wiersz.find(" ")]


