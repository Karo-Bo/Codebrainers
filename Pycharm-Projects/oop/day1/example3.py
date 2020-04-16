class Pies:
    def szczekaj(self):
        pass

def moje_szczekaj(_):
    print('Hau Hau')

Pies.szczekaj = moje_szczekaj

obiekt_pies = Pies()
obiekt_pies.szczekaj()