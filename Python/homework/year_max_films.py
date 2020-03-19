# Znajdź rok, w którym RdN wydał najwięcej filmów

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

years = {}

for entry in data:
    if entry["year"] not in years.keys():

        years[entry["year"]] = 1

    else:
        years[entry["year"]] += 1

films_number = 0
max_years = []

for y in years:
    if years[y] > films_number:
        films_number = years[y]
        max_years = []

    if years[y] == films_number:
        max_years.append(str(y))

print("Najwięcej filmów RdN wydał w latach: " + ", ".join(max_years))
# print(films_number)
