import csv
from functools import reduce


class CsvReaader:
    # __init__ wczytanie pliku csv poprzez podanie scieżki + stworzenie 2 pól _path, _sheet (2d list)
    # get_sheet zwórcenie sheeta

    def __init__(self, file_path):
        self._path = file_path  # pole
        with open(self._path) as file:
            temp = csv.reader(file)
            self._sheet = list(temp)[1:]  # pole

    def get_file(self):  # metoda
        return self._sheet


class SheetCalculator:
    #  __init__ pobranie CsvReadera i wczytanie sheeta do własnego pola
    # get_column
    # get_row
    # count_column
    # count_row
    # sum_column
    # mul_column
    # mean_column
    # apply_function_on_column

    def __init__(self, content):
        self._content = content

    def count_row(self):
        return len(self._content)

    def get_row(self, number):
        # self._index = number
        return self._content[number]

    def count_column(self):
        return len(self._content[0])

    def get_column(self, number):
        # chosen_column =
        return [row[number] for row in self._content]

    def sum_column(self, number):
        # dla kolumn, które mają wartości liczbowe
        return reduce(lambda first_row, second_row: int(first_row) + int(second_row), self.get_column(number))

    def mul_column(self, number):
        return reduce(lambda first_row, second_row: int(first_row) * int(second_row), self.get_column(number))

    def mean_column(self, number):
        return self.sum_column(number) / self.count_row()

    # high order functions
    def apply_function_on_column(self, number, function):
        return reduce(function, self.get_column(number))


# new_file = CsvReaader('data/data.csv')
# # print(new_file.get_file())
# content = new_file.get_file()
#
# new_sheet = SheetCalculator(content)
# print(new_sheet.count_row())
# print(new_sheet.get_row(0))
# print(new_sheet.count_column())
# print(new_sheet.get_column(1))
# print(new_sheet.sum_column(0))
# print(new_sheet.mul_column(0))
# print(new_sheet.mean_column(0))

sheet = SheetCalculator(CsvReaader('data/data.csv').get_file())
print(sheet.apply_function_on_column(1, lambda x, y: x + y))
print(sheet.apply_function_on_column(6, lambda x, y: int(x) + int(y)))