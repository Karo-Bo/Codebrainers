import csv

data = []
# mamy listę, do której będziemy kolejno dodawać
# na koniec słowniki - każdy słownik to trzy pary 
# klucz : wartość, odpowiadające jednej linijce
# z pliku csv.

# otwarcie pliku
with open("przykladowy.csv", "r") as f:
    # DictReader pozwoli odczytywać dane z pliku CSV
    # i będzie je zwracał jako słowniki
    reader = csv.DictReader(f)

    # iterujemy po readerze
    for row in reader:
        # dokonujemy konwersji danych i dokładamy je na
        # koniec naszej listy

        data.append(
            {
                "year" : int(row["Year"]),
                "score" : int(row["Score"]),
                "title" : row["Title"],
            }
        )

# wypisać najgorszą ocenę filmu
# wypisać tytuły najgorzej ocenianych filmóww
worst_title = []
worst_score = data[0]["score"]
for entry in data:
    if entry["score"] < worst_score:
        worst_score = entry["score"]
        worst_title = []

    if entry["score"] == worst_score:
        worst_title.append(entry["title"])

# a.join robi nowego stringa, 
# w którym wstawia a pomiędzy elementy listy podanej jako argument 

print(f"Najgorsza ocena filmu z RdN to: {worst_score}")
print(f"Najgorzej ocenione filmy z RdN to: " + ", ".join(worst_title))      
print()

# tytuły najlepszych filmów z RdN

best_title = []
best_score = data[0]["score"]
for entry in data:
    if entry["score"] > best_score:
        best_score = entry["score"]
        best_title = []

    if entry["score"] == best_score:
        best_title.append(entry["title"])

print(f"Najlepsza ocena filmu z RdN to: {best_score}")
print(f"Najlepiej ocenione filmy z RdN to: " + ", ".join(best_title))      

# Znajdź średnią ocen filmów RdN

sum_score = 0

for entry in data:
    sum_score += entry["score"]

print(round(sum_score / len(data)))





