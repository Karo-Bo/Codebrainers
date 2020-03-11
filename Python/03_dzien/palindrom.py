# Palindrom
# kajak
# civic
# Elf układał kufle
# A to kanapa pana kota
# Czy dane wyrażenie jest palindromem

yourPhrase = input("Wpisz wyrażenie: ")

yourPhraseLower = yourPhrase.lower()
noSpace = yourPhraseLower.replace(" ", "")
word = noSpace.replace("\t", "")
# slowo = slowo.replace("\n", "") 
# slowo = slowo.replace("\r", "")
# Czy da się pozbyć wszystkich białych znaków na raz?

for i in range(len(word) // 2):
    if word[i] == word[-i - 1]:
        palindrome = True
    else:
        palindrome = False
    
if palindrome == True:
    print("To jest palindrom")
else:
    print("To nie jest palindrom")
