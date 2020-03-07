wiek = int(input("Podaj mi twój wiek: "))
plec = input("Podaj płeć [K/M]: ")
plec = plec[0].upper()

# wiek_emerytalny = 65
# if plec == "K":
#     wiek_emerytalny = 60

if plec == "K":
    wiek_emerytalny = 60
else:
    wiek_emerytalny = 65

# Inny sposób zapisu:
# wiek_emerytalny = 60 if plec == "K" else 65

if 18 <= wiek < wiek_emerytalny:
    print("Musisz pracować")
    print("Taki mamy klimat")

elif wiek < 18:
    print("Ucz się młokosie")

elif wiek >= wiek_emerytalny:
    print("Gratulujemy emerytury. -ZUS")

else:
    print("Dziwna sytuacja :P")

# print("Po ifie")

# (Nie)jawna konwersja do typu logicznego
lista = []
if lista: # if not lista:
    pass
# pass jest pustą instrukcją -> przejdź dalej

# sprawdzam jawną konwersję na typ logiczny
print(bool(lista))

print(bool(0.0))
print(bool(-0.000001))

print(bool(0))
print(bool(-1))

bool(None)

# Operatory logiczne
# not
# and
# or