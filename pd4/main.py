# cw1
# plik = open("plik.txt", "w+")
# import random
# lista = []
# for x in range(10):
#     plik.write(str(2*(random.randint(0, 31))) + "\n")
# plik.close()

# cw2
# with open("plik.txt", "r") as plik:
#     for x in plik:
#         print(x)

# cw3
# with open("plik2.txt", "w") as plik2:
#     for x in range(4):
#         plik2.write(input() + "\n")
# with open("plik2.txt", "r") as plik2:
#     for x in plik2:
#         print(x)

# z4
# class NaZakupy:
#     def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
#         self.nazwa_produktu = nazwa_produktu
#         self.ilosc = ilosc
#         self.jednostka_miary = jednostka_miary
#         self.cena_jed = cena_jed
#
#     def wyświetl_produkt(self):
#         print(self.nazwa_produktu + ", " + str(self.ilosc) + ", " + self.jednostka_miary + ", " + str(self.cena_jed))
#
#     def ile_produktu(self):
#         print(str(self.ilosc) + " " + self.jednostka_miary)
#
#     def ile_kosztuje(self):
#         return self.ilosc * self.cena_jed
#
# produkt = NaZakupy("chleb", 2, "bohenek", 2.5)
# produkt.wyświetl_produkt()
# produkt.ile_produktu()
# print(produkt.ile_kosztuje())

# cw5
# class Ciagi:
#     lista = []
#     def __init__(self, wartosc, roznica, ilosc):
#         self.wartosc = wartosc
#         self.roznica = roznica
#         self.ilosc = ilosc
#     def wyswietl_dane(self):
#         print(self.lista)
#     def pobierz_elementy(self):
#         for x in range(5):
#             self.lista.append(int(input()))
#     def pobierz_parametry(self):
#         for x in range(self.wartosc, self.ilosc, self.roznica):
#             self.lista.append(x)
#     def policz_sume(self):
#         return sum(self.lista)
#     def policz_elementy(self):
#         if self.roznica != 0:
#             self.wynik = 0
#             for x in self.lista:
#                 self.wynik = self.wynik + 1
#             return self.wynik
#         else:
#             return 0
#
# c = Ciagi(1, 2, 10)
# c.pobierz_parametry()
# c.wyswietl_dane()
# print(c.policz_sume())

# z6
# class Robaczek:
#     def __init__(self, x, y, krok):
#         self.x = x
#         self.y = y
#         self.krok = krok
#     def idz_w_gore(self, ile):
#         self.y = self.y + (self.krok * ile)
#     def idz_w_dol(self, ile):
#         self.y = self.y + ((-1)*(self.krok * ile))
#     def idz_w_lewo(self, ile):
#         self.x = self.x + ((-1)*(self.krok * ile))
#     def idz_w_prawo(self, ile):
#         self.x = self.x + (self.krok * ile)
#     def pokaz_gdzie_jestes(self):
#         print("x: " + str(self.x) + " y: " + str(self.y))
#
# r = Robaczek(0, 0, 2)
# r.idz_w_gore(2)
# r.idz_w_prawo(3)
# r.pokaz_gdzie_jestes()