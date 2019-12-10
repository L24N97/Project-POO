import random

class Carta( object ):
    def __init__(self, nombre, valor, traje, simbolo): 
        self.nombre = nombre
        self.valor = valor 
        self.traje = traje
        self.simbolo = simbolo
        self.m_carta = False # Muestra las cartas 

    def __repr__(self): 
        # Retorna (muestra) el objeto Carta.
        if self.m_carta:
            return self.simbolo
        else:
            return 'CARTA'

class Mazo( object ):
    def barajar(self, times=1):
        random.shuffle(self.cartas)
        print("Tarjetas Barajadas!")

    def dealer(self):
        return self.cartas.pop(0)

class MazoCarta(Mazo):
    def __init__(self):
        self.cartas = [] # Lista vacia, para anexar. 
        trajes = {'Diamantes': '♢', 'Corazones': '♡', 'Espadas': '♠', 'Treboles': '♣'}
        valores = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                    '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11,
                    'Q': 12, 'K': 13, 'As': 14}

        for nombre in valores:
            for traje in trajes:
                symbol = trajes[traje]
                if valores[nombre] < 11:
                    simbolo = str( valores[nombre] ) + symbol
                else:
                    simbolo = nombre[0] + symbol
                self.cartas.append( Carta(nombre, valores[nombre], traje, simbolo) )

    def __repr__(self):
        return "El mazo de tarjetas contiene: {0} Cartas.".format(len(self.cartas))

class Jugador( object ):
    def __init__(self):
        self.cartas = []

    def contarCartas(self):
        return len( self.cartas )

    def agregarCartas(self, carta):
        self.cartas.append(carta)

class Puntaje( object ):
    # Puntaje de juego
    def __init__(self, cartas):
        if not len(cartas) == 5:
            return 'ERROR: Recuento de tarjetas es incorrecto'
        self.cartas = cartas
    
    def manos(self):
        trajes = [carta.traje for carta in self.cartas]
        if len( set(trajes) ) == 1:
            return True
        else:
            return False

    def ordenManos(self):
        valores = [carta.valor for carta in self.cartas]
        valores.sort()

        if not len( set(valores) ) == 5: 
            return False

        if valores[4] == 14 and valores[0] == 2 and valores[1] == 3 and valores[2] == 4 and valores[3] == 5:
            return True
        else:
            if not valores[0] + 1 == valores[1]: 
                return False
            if not valores[1] + 1 == valores[2]: 
                return False
            if not valores[2] + 1 == valores[3]: 
                return False
            if not valores[3] + 1 == valores[4]: 
                return False

        return valores[4]

    def cartaAlta(self):
        valores = [carta.valor for carta in self.cartas]
        cartaAlta = None
        for carta in self.cartas:
            if cartaAlta is None:
                cartaAlta = carta
            elif cartaAlta.valor < carta.valor:
                cartaAlta = carta
        return cartaAlta
    
    def cuenta(self):
        contador = 0
        valores = [carta.valor for carta in self.cartas]
        for valor in valores:
            if valores.contador(valor) > contador:
                contador = valores.contador(valor)
        return contador


    def pares(self):
        pares = []
        valores = [carta.valor for carta in self.cartas]
        for valor in valores:
            if valores.count(valor) == 2 and valor not in pares:
                pares.append(valor)
        return pares

    def cuatroTipo(self):
        # "Four of a King"; en caso de empate en cuatro cartas, la quinta carta (pateador) mas alta gana. 
        valores = [carta.valor for carta in self.cartas]
        for valor in valores:
            if valores.count(valor) == 4:
                return True
    
    def casaLlena(self):
        # Full House
        dos = False
        tres = False

        valores = [carta.valor for carta in self.cartas]
        if valores.count(valores) == 2:
            dos = True
        elif valores.count(valores) == 3:
            tres = True
        
        if dos and tres:
            return True

        return False

    





# deck = MazoCarta()