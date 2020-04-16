# def asd(self):
#     pass
import numbers


class Konto:
    def __init__(self, stan_poczatkowy, imie, nazwisko):  # stan_poczatkowy - argument konstruktora
        # self - słowo kluczowe, zawsze w metodach występuje na pierwszym miejscu
        # odwołanie do samego siebie (?)
        # print('jestem konstruktorem')
        self.stan = stan_poczatkowy  # Pole konstruktora w klasie, Class Field
        self.imie = imie
        self.nazwisko = nazwisko

    def __str__(self):
        return f"""Właściciel {self.imie} {self.nazwisko}
stan: {self.stan}"""

    def wplac(self, kwota):
        self.stan += kwota

    def wyplac(self, kwota):
        self.stan -= kwota
        return kwota

    def przelew(self, kwota, konto_docelowe):
        if not isinstance(kwota, int):
            raise Exception('Kwota jest niepoprawna')
        self.stan -= kwota
        konto_docelowe.stan += kwota

    def przelew2(self, kwota, konto_docelowe):
        self.wyplac(kwota)
        konto_docelowe.wplac(kwota)


Konto_Sabina = Konto(1000, 'Sabina', 'Kowalska')
Konto_Kamila = Konto(0, 'Kamila', 'Nowak')
print(Konto_Sabina)
print(Konto_Kamila)
Konto_Sabina.przelew(500, Konto_Kamila)
try:
    Konto_Sabina.przelew('100', Konto_Kamila)
except Exception:
    print('Podana kwota "100" jest niepoprawna')
print(Konto_Sabina)
print(Konto_Kamila)
# print(type(Konto_Sabina))
# print(Konto_Sabina.stan)
# print(Konto_Sabina.imie)
# print(Konto_Sabina.nazwisko)
#

# print(Konto_Kamila.stan)
#
# # print(Konto_Sabina)
# # print(Konto_Kamila) # pokazuje miejsce w pamięci, gdzie został utworzony dany obiekt
#
# Konto_Sabina.wplac(1000)
# print(Konto_Sabina.stan, Konto_Sabina.imie)
#
# Konto_Sabina.wyplac(500)
# print(Konto_Sabina.stan, Konto_Sabina.imie)
# portfel = Konto_Sabina.wyplac(250)
# print(portfel)
