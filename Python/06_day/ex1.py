# KeyError
slownik = dict()

try:
    print(slownik[1])

except KeyError:
    print("Błąd klucza")

# valueError
try:
    int(input("Podaj liczbę: "))
    
except ValueError:
    print("Błąd wartości")

# AttributeError
try:
    "Piotr".nieistniejacy_atrybuy
except AttributeError:
    print("Ten atrybut nie istnieje")

