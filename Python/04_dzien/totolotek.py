import random

liczba_kulek = 6
wylosowane_liczby = []

# while liczba_kulek > 0:
while len(wylosowane_liczby) < liczba_kulek:
    wylosowana = random.randint(1, 49)

    if wylosowana not in wylosowane_liczby:
        wylosowane_liczby.append(wylosowana)
    # else:
    #     continue

    # liczba_kulek -= 1 // nie działa bez else, dlaczego

print(wylosowane_liczby)
