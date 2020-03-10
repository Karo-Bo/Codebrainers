# while

index = 0

while index < 10:
    print(f"Hello World x{index}")
    index += 1 # == index = index + 1

# for
#kolekcja = ["Piotr", "Jakub", "Artur", "Piotr"]  element listy, wcześniej
# element stringa
kolekcja = {
    "Linux": "Jakub",
    "Web": "Piotr",
    "Python": "Piotr",
    "OOP": "Artur",
}
for klucz, wartosc in kolekcja.items():
    print(klucz, wartosc) # tupla

# for klucz in kolekcja.items():
#     print(klucz) /////// kluczem będzie cała tupla

# Zadanie
# lista liczb od 2 do 20 włącznie,
# używając pętli for wyświetl te liczby, ich kwadraty i pierwiastki

lista = list(range(2, 21)) # lewostronnie obejmuje, prawostronnie nie

for element in lista:
    print(element, element ** 2, element ** 0.5)

lista = ["Jakub", "Piotr", "Piotr", "Artur"]
for klucz, element in enumerate(lista): # zwraca miejsce elementu w liście 
                                        # i sam element
    print(klucz, element)

index = 0

while index < 10:
    print(f"Hello World x{index}")
    index += 1

# for "a la C++"

# range(0, 10, 2) -> krok o 2

for i in range(0, 10):
    if i % 2 == 0:
        continue # przejście do nowej iteracji, ignoruje dalszą część pętli
    print(f"Hello World x{i}") # wyświetli tylko nieparzyste elementy
    # break - w ogóle wychodzi z pętli, np:
    # if i >= 5:
    #   break

lista = ["Jakub", "Piotr"]
for imie in lista:
    print(imie)
else:
    print("Koniec listy") # else działa jeśli for zakończył się naturalnie
                            # bez break'a



    