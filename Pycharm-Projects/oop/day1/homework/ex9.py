class get_print_String():
    def __init__(self):
        self.string = ""

    def get_String(self):
        self.string = input("Podaj ciąg znaków: ")

    def print_String(self):
        print(self.string.upper())

str1 = get_print_String()
str1.get_String()
str1.print_String()