# Znajdź rok, w którym RdN wydał najwięcej filmów

import csv
from collections import Counter

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

# print(data)

# *************************************

years = Counter()

for entry in data:    
    years[entry["year"]] += 1

# *************************************

max_years = []
best_year = years.most_common()[0][1]

for year, number in years.most_common():
    if number == best_year:
        max_years.append(str(year))
    else:
        break

print("Najwięcej filmów RdN wydał w latach: " + ", ".join(max_years))

# *************************************

# years = {}

# for entry in data:
    # if entry["year"] in years:

    #     years[entry["year"]] += 1
        
    # else:
    #     years[entry["year"]] = 1

# ***********************************************

# films_number = 0
# max_years = []

# for y in years:
#     if years[y] > films_number:
#         films_number = years[y]
#         max_years = []

#     if years[y] == films_number:
#         max_years.append(str(y))

# print("Najwięcej filmów RdN wydał w latach: " + ", ".join(max_years))
# print(films_number)
