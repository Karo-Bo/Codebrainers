# Palindrom
# kajak
# civic
# Elf układał kufle
# A to kanapa pana kota
# Czy dane wyrażenie jest palindromem

word = input("Wpisz wyrażenie: ")

word = word.lower()
word = word.replace(" ", "")
word = word.replace("\t", "")

# word = input("Wpisz wyrażenie: ").lower().replace(" ", "").replace("\t", "")

# slowo = slowo.replace("\n", "")
# slowo = slowo.replace("\r", "")
# Czy da się pozbyć wszystkich białych znaków na raz?

palindrome = True

for i in range(len(word) // 2):
    if word[i] != word[-i - 1]:
        palindrome = False
        break  # jeśli if spełniony, nie wykonuje już dalej pętli

if palindrome:
    print("To jest palindrom")
else:
    print("To nie jest palindrom")

# print(f"{=palindrome}")
# wyświetla nazwę zmiennej i jej wartość
# palindrome = True