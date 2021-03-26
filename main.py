import numpy as np

print('Zadanie1')
a = np.arange(0, 45, 3)
print(a)

print('\nZadanie2')
lista = np.arange(0, 20, 1.4)
lista1 = np.int64(lista)
print(lista1)

print('\nZadanie3')


def parametr_n(n):
    x = np.arange(1, (n * n) + 1).reshape(n, n)
    return x


print(parametr_n(5))

print('\nZadanie4')


def potegi(x, y):
    result = np.logspace(1, y, num=y, base=x)
    return result


podstawa = int(input('Podaj podstawę potęgowania: '))
iloscpoteg = int(input('Podaj ilość kolejnych potęg do wygenerowania: '))
print(potegi(podstawa, iloscpoteg))

print('\nZadanie5')


def wektor(x):
    wektor = [x for x in range(x + 1)]
    wektor.reverse()
    result = np.diag(wektor)
    return result


dlugoscwektora = int(input('Podaj długość wektora: '))
print(wektor(dlugoscwektora))
