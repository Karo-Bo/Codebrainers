# policz wystąpienia literek w tekście
# użyj dict

text = "Ala ma kota, kota ma ale, a to jest kanapa pana Kota"

counter = dict()

for s in text:
    if s in counter:
        counter[s] += 1
    else:
        counter[s] = 1

print(counter)
print(len(text))