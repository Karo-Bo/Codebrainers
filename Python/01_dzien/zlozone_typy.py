# Stringi 

# Lista

# Przykłady łamania linii

pantadeusz = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, " + \
             "sed do eiusmod tempor incididunt ut labore et dolore magna" + \
             " aliqua."
pantadeusz = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit, " +
              "sed do eiusmod tempor incididunt ut labore et dolore magna" +
              " aliqua.")
pantadeusz = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
              "sed do eiusmod tempor incididunt ut labore et dolore magna"
              " aliqua.")

uczestnicy = ["Karo", "Kami", "Asia", "Mich.M", "Sabi", "Grze", "Mich.K", 
             "Maks", "Dami", 123, 3546, True, False, None]
             
print(uczestnicy[0])
print(uczestnicy[9])
print(uczestnicy[-1])

print(len(uczestnicy))
print(len(pantadeusz))

# Zagnieżdżone listy

nested = [
    [
        "Piotr",
    ],
    [
        "Max", "Karolina",
    ],
    [
        "Asia", "Kamila",
    ],
    [
        "Sabina", "Michał", "Grzesiek",
    ],
    [
        "Michał", "Damian",
    ],
]

print(nested)
print(nested[-1])
print(nested[-2][1])
print(len(nested)) # Liczba ławek
print(len(nested[-2])) # Liczba osób w drugiej ławce od końca

nested.append("Rafał")
nested.append( ["Rafał"] )
nested[-1].append( "Rafał" )
print(nested)

# nazwisko = "Kowalski"
# lista = [nazwisko, "Jan"]
# print(lista)

# nazwisko = "grrrrgrg"
# print(lista) 
# cały czas pokazuje wpis zadany poprzednio, żeby zmienić co jest
# w liście, trzeba by na nowo ją określić po zmianie nazwiska

