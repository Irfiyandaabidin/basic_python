# -*- coding: utf-8 -*-
"""Pertemuan 3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1e9J88DLHS9TwANTtgRYvdIgCe1JYf40H
"""

## Praktik ke 1
bilangan = 100
PHI = 3.14
nama = 'anto'
flag = True
var = None

print('Jenis Variabel: ')
print('bilangan: ', type(bilangan))
print('PHI: ', type(PHI))
print('nama: ', type(nama))
print('flag: ', type(flag))
print('var: ', type(var))

## Praktik ke 2
## Operator assigment dan aritmatika
a = 5 + 9
b = 7 - 4
c = 20 / 3
d = 5 * 6
e = 8 // 3
f = 9 % 5
g = 4 ** 3
print('a: ', a)
print('b: ', b)
print('c: ', c)
print('d: ', d)
print('e: ', e)
print('f: ', f)
print('g: ', g)

## Praktik ke 3
## Operator perbandingan
a = 5 == 7
b = 2 != 6
c = 4 < 3
d = 5 > 2
e = 8 >= 8
f = 9 <= 11

print('a: ', a)
print('b: ', b)
print('c: ', c)
print('d: ', d)
print('e: ', e)
print('f: ', f)

## Praktik le 4
## Operator logika
a = True and True
b = True and False
c = True or False
d = False or False
e = not False
f = not (True and False)

print('a: ', a)
print('b: ', b)
print('c: ', c)
print('d: ', d)
print('e: ', e)
print('f: ', f)

## Praktik ke 5
## Operator bitwise
a = 4 & 5
b = 6 & 7
c = 8 | 5
d = 9 | 3
e = 5 >> 2
f = 8 << 2

print('a: ', a)
print('b: ', b)
print('c: ', c)
print('d: ', d)
print('e: ', e)
print('f: ', f)

## Praktik ke 6
## Konversi Tipe Data
jumlah_hari = int(input("Masukkan jumlah hari : "))
jumlah_tahun = int(jumlah_hari/365)
jumlah_minggu = int(jumlah_hari % 365 / 7)
sisa_jumlah_hari = int(jumlah_hari % 365 % 7)
print(f"Tahun = {jumlah_tahun}, Minggu = {jumlah_minggu}, Hari = {sisa_jumlah_hari}")