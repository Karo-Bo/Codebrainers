germs = ['bacteria', 'virus', 'fungus', 'odour']

virus_removed_germs = filter(lambda type: type != "virus", germs)

print()

# Lazy Evaluation
#
# if True:
#     exit()

print(virus_removed_germs)
print(list(virus_removed_germs))
# zrzutowanie tutaj jest bardziej optymalne (optymalizacja zużycia pamięci), przy bardzo długich listach
# bo dopiero przy rzutowaniu zapisujemy całą listę z wszystkimi elementami w pamięci
# filter tworzy tylko 'przepis'