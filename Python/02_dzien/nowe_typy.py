# Stringi
# Listy

# Tuple | krotki (jedna krotka, one tuple)
# niemodyfikowalna, podobna do listy

T1 = ("Piotr", "Banaszkiewicz")
print(T1)

T2 = ("Piotr", )  # jeśli bez przecinka to traktowane jako string
T3 = (
    "Alfa",
    "Bravo",
    "Charlie",
    "Delta",
)
print(T3[2])
print(len(T3))

# Rozbijanie elementów
T4 = ("Karo", "Boch")
# imie = T4[0]
# nazwisko = T4[1]

imie, nazwisko = T4  # domyślna tupla utworzona przy rozbijaniu elementów
print(imie, nazwisko)

# Słownik (dict)
# (typ mapujący, typ haszujący)
D1 = {
    "klucz": "wartość", # klucz nie może być mutowalny (jak lista)
    123: "Student",
    (0, 0, 7): "Bond. James Bond",
}
print(D1)
print(D1["klucz"])
print(D1[123])
print(D1[(0, 0, 7)])

print(list(D1.keys())[1])
print(list(D1.values())[1])

D1.items() # lista tupli dwuelementowych "Klucz", "wartość"
print(list(D1.items()))

print(list(D1.keys()))
print(D1.keys()) # wyświetla opis dict_keys()

# Zbiór (set)
Z1 = {2, 3, 4, 5, 2, 3, 1, 2, 4, 5}
print(Z1) # tylko niepowtarzalne elementy