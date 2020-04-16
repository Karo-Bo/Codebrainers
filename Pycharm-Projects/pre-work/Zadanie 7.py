# Zadanie 7

figure = str(input('Podaj nazwę figury ze zbioru (Koło, Kwadrat, Prostokąt): '))
type = str(input('Podaj co chcesz obliczyć (Pole, Obwód)'))

if figure in ('Kwadrat', 'kwadrat'):
    x = int(input('Podaj bok kwadratu: '))
    if type in ('Pole', 'pole'):
        print(f'Pole kwadratu o podanym boku wynosi {x ** 2}')
    elif type in ('Obwód', 'obwód', 'obwod', 'Obwod'):
        print(f'Obwód kwadratu o zadanym boku wynosi {4 * x}')

elif figure in ('Koło', 'kolo', 'Kolo', 'koło'):
    r = int(input('Podaj promień koła: '))
    if type in ('Pole', 'pole'):
        print(f'Pole koła o podanym boku wynosi {2 * 3.14 * r}')
    elif type in ('Obwód', 'obwód', 'obwod', 'Obwod'):
        print(f'Obwód koła o zadanym promieniu wynosi: {2 * 3.14 * r}')

elif figure in ('Prostokąt', 'prostokąt', 'Prostokat', 'prostokat'):
    a = int(input('Podaj wartość pierwszego boku: '))
    b = int(input('Podaj wartość drugiego boku: '))
    if type in ('Pole', 'pole'):
        print(f'Pole prostokąta o podanych wymiarach wynosi: {a * b}')
    elif type in ('Obwód', 'obwód', 'obwod', 'Obwod'):
        print(f'Obwód prostokąta o podanych wymiarach wynosi: {2 * a + 2 * b}')
