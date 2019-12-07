import random

class Carta(object):
    def __init__(self, nombre, valor, traje): 
        self.nombre = nombre
        self.valor = valor 
        self.traje = traje
        self.m_carta = False # Muestra las cartas 

    def __repr__(self): # Metodo OOP; retorna el objeto Carta.
        if self.m_carta:
            return f"{self.nombre} de {self.traje}"
        else:
            return 'CARTA'

class MazoCarta:
    def __init__(self):
        self.cartas = [] # Lista vacia, para anexar. 
        trajes = ['Diamantes', 'Corazones', 'Espadas', 'Treboles']
        valores = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                    '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11,
                    'Q': 12, 'K': 13, 'As': 14}

        for nombre in valores:
            for traje in trajes:
                self.cartas.append(Carta(nombre, valores[nombre], traje))

    def __repr__(self):
        return "El mazo de cartas contiene: {0} Cartas.".format(len(self.cartas))

    def barajar(self, times=1):
        random.shuffle(self.cartas)
        print("Cartas Barajadas!")

    def dealer(self):
        return self.cartas.pop(0)


# deck = MazoCarta()
# rand = deck.dealer()
# rand.m_carta = True 
# print(rand)
# deck.barajar()
# ranD = deck.dealer()
# ranD.m_carta = True
# print(ranD)
