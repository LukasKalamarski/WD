import numpy as np
import pandas as pd
import xlrd
import openpyxl
import matplotlib.pyplot as plt

# z1
# t = [1/x for x in range(1, 21)]
# # temp = np.array(t)
# # plt.plot(temp)
# # plt.xlabel('x')
# # plt.ylabel('f(x)')
# # plt.axis([1, temp.size, 0, 1])
# # plt.show()

# z2
# t = [1/x for x in range(1, 21)]
# temp = np.array(t)
# plt.plot(temp, 'g^--', label="f(x)=1/x")
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.legend()
# plt.show()

# z3
# x = np.arange(0, 30, 0.1)
# s = np.sin(x)
# c = np.cos(x)
# plt.plot(x, s, 'c', label='f(x)=cos(x)')
# plt.plot(x, c, 'y', label='f(x)=sin(x)')
# plt.axis([0, 2*np.pi, -1, 1])
# plt.legend()
# plt.show()

# z4
# x = np.arange(0, 30, 0.1)
# s = np.sin(x)
# s2 = np.sin(x*(-1))-2
# plt.plot(x, s, '#2ECC71', label='f(x)=sin(x)')
# plt.plot(x, s2, '#F39C12', label='f(x)=sin(x)')
# plt.axis([0, 30, -3, 1])
# plt.legend(loc='center left')
# plt.show()

# z5
# df = pd.read_csv('iris.data', header=0, sep=',', decimal='.')
# x = df.SepalLenght.tolist()
# y = df.SepalWidth.tolist()
# ts = [abs(x[i] - y[i]*15) for i in range(len(x))]
# data = {'a': x,
#         'b': y,
#         'c': np.random.randint(0, 150, 150),
#         'd': ts}
# plt.scatter('a', 'b', c='c', s='d', data=data)
# plt.show()

# z6
# xlsx = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(xlsx, header=0)
# c = df[df['Plec'] == 'M'].agg({'Liczba': ['sum']})
# c = c['Liczba'].values[0]
# d = df[df['Plec'] == 'K'].agg({'Liczba': ['sum']})
# d = d['Liczba'].values[0]
# etykiety = ['Mężczyźni', 'Kobiety']
# wartosci = [c, d]
# plt.subplot(1, 3, 1)
# plt.bar(etykiety, wartosci, color=['#5DADE2', '#FF3FC1'])
#
# plt.subplot(1, 3, 2)
# plt.plot(df[df['Plec'] == 'M'].groupby(['Rok']).agg({'Liczba': ['sum']}), '#5DADE2')
# plt.plot(df[df['Plec'] == 'K'].groupby(['Rok']).agg({'Liczba': ['sum']}), '#FF3FC1')
#
# plt.subplot(1, 3, 3)
# temp = df.groupby(['Rok']).agg({'Liczba': ['sum']})
# w = temp.plot.bar(color=['r'])
# plt.show()

# z7
# df = pd.read_csv('zamowienia.csv', header=0, sep=';', decimal='.')
# temp = df.groupby(['Sprzedawca']).agg({'Sprzedawca': ['size']})
# w = temp.plot.pie(subplots=True, autopct='%.2f %%', explode=[0.2, 0.1, 0, 0, 0, 0, 0, 0, 0], shadow=True )
# plt.legend(loc='upper left')
# plt.show()
