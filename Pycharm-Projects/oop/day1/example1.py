konto1 = {
    'stan': 0,
    'imie': 'Artur',
    'nazwisko': 'Król',
    'numer': 123456789,
}
list

# Podejście proceduralno - strukturalne
# Pierwsze rozwiązanie

def wplac(kwota, stan):
    return stan + kwota


konto1['stan'] = wplac(1000, konto1['stan'])
print(konto1['stan'])


def wyplac(kwota, stan):
    return stan - kwota


konto1['stan'] = wyplac(50, konto1['stan'])
print(konto1['stan'])

# def zmien_nazwisko(nowe):
#     return(nowe)
#
# konto1['nazwisko'] = zmien_nazwisko('Blabla')

print(konto1)


# Drugie rozwiązanie

def wplac2(kwota, konto):
    konto['stan'] = konto['stan'] + kwota


wplac2(1000, konto1)
print(konto1)


def wyplac2(kwota, konto):
    konto['stan'] = konto['stan'] - kwota


wyplac2(500, konto1)
print(konto1)
