import random

class Carta:
    def __init__(self, nombre, valor, traje): 
        self.nombre = nombre
        self.valor = valor 
        self.traje = traje
        self.m_carta = False # Muestra las cartas 

    def __repr__(self): 
        # Retorna (muestra) el objeto Carta.
        if self.m_carta:
            return f"{self.nombre} de {self.traje}"
        else:
            return 'CARTA'

class Mazo:
    def barajar(self, times=1):
        random.shuffle(self.cartas)
        print("Tarjetas Barajadas!")

    def dealer(self):
        return self.cartas.pop(0)

class MazoCarta(Mazo):
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
        return "El mazo de tarjetas contiene: {0} Cartas.".format(len(self.cartas))

class Jugador:
    def __init__(self):
        self.cartas = []

    def contarCartas(self):
        return len( self.cartas )

class Puntaje:
    # Puntaje de juego
    def __init__(self, cartas):
        if not len(cartas) == 5:
            return 'ERROR: Recuento de tarjetas es incorrecto'
        self.cartas = cartas





# deck = MazoCarta()
# rand = deck.dealer()
# rand.m_carta = True 
# print(rand)
# deck.barajar()
# ranD = deck.dealer()
# ranD.m_carta = True
# print(ranD)
