# with open('blahblah.txt') as f:
#     read_file = f.read()
#     print(read_file)
#
# print(f.read()) # plik jest już zamknięty, więc wyskoczy błąd

class OurOpen:
    def __init__(self, file_path):
        self._file_path = file_path # przypisany jako atrybut obiektu
        # żeby metoda poniżej też się

    def __enter__(self):
        print('Enter')
        self.file = open(self._file_path)
        return self.file

    def __exit__(self, _, _1, _2):  # kolejne argumenty
        self.file.close()
        print('Exit')


with OurOpen('blahblah.txt') as f:
    print(f)
    print(f.read())
    print('I"m inside with')

# print(f.read())
# open('blahblah.txt', 'r')
