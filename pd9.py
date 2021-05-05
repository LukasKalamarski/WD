import numpy as np
import pandas as pd
import xlrd
import openpyxl

# # z1
xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)
# print(df)

# z2
# print(df[df['Liczba'] < 1000])
# print(df[df['Imie'] == 'ŁUKASZ'])
# print(df.groupby(['Rok']).agg({'Liczba':['sum']}))
# print(df[(df['Rok'] >= 2005) & (df['Rok'] <= 2010)].groupby(['Rok']).agg({'Liczba':['sum']}))
# print(df[(df['Rok'] == 2000) & (df['Plec'] == 'M')].agg({'Liczba': ['sum']}))
# print(df.groupby(['Rok']).agg({'Liczba': ['max']}))
# print(df.groupby(['Rok', 'Plec']).agg({'Liczba': ['max']}))

# z3
df2 = pd.read_csv('zamowienia.csv', header=0, sep=';', decimal='.')
# print(df2.groupby(['Sprzedawca']).agg({'Sprzedawca': ['unique']}))
# print(df2['Sprzedawca'].unique())
# print(df2.sort_values(by=['Utarg'], ascending=False).head(10))
# print(df2['Sprzedawca'].value_counts())
# print(df2['Kraj'].value_counts())
# dft1 = df2[(df2['Kraj'] == 'Polska') & (df2['Data zamowienia'] >= '2005-01-01') & (df2['Data zamowienia'] <= '2005-12-31')].groupby(['Sprzedawca']).agg({'Utarg': ['sum']})
# dft = df2[(df2['Data zamowienia'] >= '2004-01-01') & (df2['Data zamowienia'] <= '2004-12-31')]
# dft2 = dft['Utarg'].mean()
# dft1.to_csv('zamówienia_2005.csv')
# dft2.to_csv('zamówienia_2004.csv')
