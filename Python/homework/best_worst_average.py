import csv

data = []

with open("przykladowy.csv", "r") as f:

    reader = csv.DictReader(f)
    for row in reader:

        data.append(
            {
                "year" : int(row["Year"]),
                "score" : int(row["Score"]),
                "title" : row["Title"],
            }
        )

# wypisać najgorszą ocenę filmu
# wypisać tytuły najgorzej ocenianych filmów

worst_title = []
worst_score = data[0]["score"]
for entry in data:
    if entry["score"] < worst_score:
        worst_score = entry["score"]
        worst_title = []

    if entry["score"] == worst_score:
        worst_title.append(entry["title"])

print(f"Najgorsza ocena filmu z RdN to: {worst_score}")
print(f"Najgorzej ocenione filmy z RdN to: " + ", ".join(worst_title))      
print()

# najlepsza ocena filmów z RdN
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
print("Najlepiej ocenione filmy z RdN to: " + ", ".join(best_title))  
print()    

# Znajdź średnią ocen filmów RdN

sum_score = 0

for entry in data:
    sum_score += entry["score"]

print(round(sum_score / len(data)))
