# cw1
# A = [1-x for x in range(1, 11)]
# print(A)
# B = [4**x for x in range(0, 8)]
# print(B)
# C = [4**x for x in range(0, 8) if 4**x % 2 == 0]
# print(C)

# cw2
# import random
# lista1 = []
# for x in range(10):
#     lista1.append(random.randint(1, 20))
#
# lista2 = [x for x in lista1 if x % 2 == 0]
# print(lista1)
# print(lista2)

# cw3
# sl = {"bułki" : "sztuki", "mąka" : "kg", "chleb" : "bohenek", "gruszki" : "sztuki"}
# l = [key for key, value  in sl.items() if value == "sztuki"]
# print(l)

# cw4
# def foo(a, b, c):
#     if a**2 + b**2 == c**2:
#         print("Jest prostokątny")
#     else:
#         print("Nie jest prostokątny")
# foo(5, 12, 13)

# cw5
# def trapez(a = 5, b = 3, h = 2):
#     return ((a+b)*h)/2
# print(trapez())

# cw6
# def foo(a = 1, b = 4, c = 10):
#     wynik = 1
#     lista = [x * b for x in range(a, c)]
#     for x in lista:
#         wynik = wynik * x
#     return wynik
# print(foo())

# cw7
# def foo(a = 1, b = 4, c = 10):
#     wynik = 1
#     lista = [x * b for x in range(a, c)]
#     for x in lista:
#         wynik = wynik * x
#     return wynik
# print(foo())

# cw8
# def foo(a):
#     suma = 0
#     ilosc = 0
#     for values in a.values():
#         suma = suma + values
#         ilosc+=1
#     print("Koszt produktów to " + str(suma) + ", a ilość produktów to " + str(ilosc))
# produkty = {"bułka" : 2, "chleb" : 3, "pepsi" : 7, "pierogi" : 12}
# foo(produkty)

# cw9
# from ciagi import *
# print(aryt.n_ty(1, 4, 2))
# print(geom.n_ty(1, 2, 3))
# print(aryt.suma_n(1, 3, 2))
# print(geom.suma_n(1, 2,3))