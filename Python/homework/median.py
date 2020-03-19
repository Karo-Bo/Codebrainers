# Znajdź medianę ocen filmów RdN

import csv

scores = []
median = 0

with open("przykladowy.csv", "r") as f:

    reader = csv.DictReader(f)
    for row in reader:

        scores.append(int(row["Score"]))

scores.sort()
n = len(scores)

if n % 2 != 0:
    median = scores[((n + 1) // 2) - 1]

else:
    median = scores[((n // 2 + (n // 2 + 1)) // 2) - 1]

print(median)
    