# with open('blahblah.txt') as f:
#     read_file = f.read()
#     print(read_file)
#
# print(f.read()) # plik jest już zamknięty, więc wyskoczy błąd

class OurWith:
    def __enter__(self):
        print('Enter')

    def __exit__(self, _, _1, _2): # kolejne argumenty
        print('Exit')

with OurWith():
    print('I"m inside with')