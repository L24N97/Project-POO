
class Carta(object):
    def __init__(self, valor, traje): 
        self.valor = valor 
        self.traje = traje

    def __repr__(self): # Metodo OOP; retorna el objeto Carta.
        return f"{self.valor} de {self.traje}"

class MazoCarta:

    def __init__(self):
        trajes = ['Diamantes', 'Corazones', 'Espadas', 'Treboles']
        valores = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                7': 7, '8': 8, '9': 9, '10': 10, 'J': 11,
                'Q': 12, 'K': 13, 'As': 14}

        
