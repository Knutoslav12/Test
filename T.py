# skracanie ułamków
def nwd(a, b):
    if b == 0:
        return a
    else:
        return nwd(b, a % b)


licznik = int(input("Podaj licznik: "))
mianownik = int(input("Podaj mianownik: "))

skr_licznik = licznik / nwd(licznik, mianownik)
skr_mianownik = mianownik / nwd(licznik, mianownik)

if skr_mianownik == 1.0:
    print(f'Otrzymana liczba w wyniku skracania to {skr_licznik}')
else:
    print(f'Skrócony ułamek to {skr_licznik}/{skr_mianownik}')


# zespół programistyczny

def nwd(a, b):
    if b == 0:
        return a
    else:
        return nwd(b, a % b)


a = int(input("Podaj liczbę dni a: "))
b = int(input("Podaj liczbę dni b: "))

spotkanie = (a * b) / nwd(a, b)
print(spotkanie)

# średnia wyrazów ciągu fibonacciego
n = int(input("Podaj n: "))


def fibonacci_r(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_r(n - 1) + fibonacci_r(n - 2)


def srednia(n):
    suma = 0
    for i in range(1, n + 1):
        suma += fibonacci_r(i)
    srednia = suma / n
    return srednia


print(srednia(n))
