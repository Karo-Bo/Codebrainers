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

# ********************
# opcja 2: default dict

# import 
# from collections import defaultdict

# counter2 = defaultdict(int) #
# for s in text:
#     counter2[s] += 1

# print(counter2)

# *****************
# opcja 3:
# from collections import Counter

# counter3 = Counter(text)
# print(counter3)