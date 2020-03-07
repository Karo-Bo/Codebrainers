# zadanie: wizytówka, wyrównanie do lewej (*wyśrodkowana krótsza nazwa)
nazwisko = "Karolina Bochenek"
tytul = "Tester"
dl_nazwisko = len(nazwisko)
dl_tytul = len(tytul)
roznica = abs(dl_nazwisko - dl_tytul)
left_padding = roznica // 2
right_padding = roznica - left_padding

print("+-" + "-" * dl_nazwisko + "-+")
print("| " + nazwisko + " |")
print("| " + " " * left_padding + tytul + " " * right_padding + " |")
print("+-" + "-" * dl_nazwisko + "-+")

# moja wersja I :
# card = ("+" + "-" * (len(nazwisko)+2) + "+\n" + "| " + nazwisko + " |\n"
#         "| " + (len(nazwisko)-len(tytul)) // 2 * " " + tytul +
#         ((len(nazwisko)-len(tytul)) // 2 + 1) * " " + " |\n"
#         "+" + "-" * (len(nazwisko)+2) + "+")
# print(card)