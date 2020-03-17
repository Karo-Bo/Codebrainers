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

print(data[0])