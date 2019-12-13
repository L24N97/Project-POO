import random

class Carta( object ):
    def __init__(self, valor, traje): 
        self.valor = valor 
        self.traje = traje

class Mazo( object ):

    def __init__(self):
        self.valores = [x for x in range(2, 11)] + ['J', 'Q', 'k', 'Ace']
        self.trajes = ['♣', '♠', '♡', '♢']
        self.mazo_carta = [Carta(valor, traje) for traje in self.trajes for valor in self.valores]

    def barajar(self, times=1):
        random.shuffle(self.cartas)
        print("Tarjetas Barajadas!")

    def dealer(self):
        return self.cartas.pop(0)

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
        count = 0
        valores = [carta.valor for carta in self.cartas]
        for valor in valores:
            if valores.count(valor) > count:
                count = valores.count(valor)
        return count


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

def gamePoker():
    # Funcion que invoca el juego

    player = Jugador()

    # Monto inicial 
    puntos = 200

    # costo por mano
    costo_mano = 10

    fin = False
    while not fin:
        print( 'Tienes {0} puntos'.format(puntos) )
        print()

        puntos -= 10

        # Ciclo mano
        deck = MazoCarta()
        deck.barajar()

        # Entrega de cartas
        for i in range(5):
            player.agregarCartas( deck.dealer() )

        # Mostrar cartas
        for carta in player.cartas:
            carta.m_carta = True
        print(player.cartas)

        entradaValida = False
        while not entradaValida:
            print( '¿Qué cartas quieres descartar? (es decir: 1, 2, 3)' )
            print( 'solo presiona enter para mantener todo, escribe "salir" para salir' )
            entradaStr = input()

            if entradaStr == 'salir':
                fin = True
                break

            try:
                listaEntrada = [int(inp.strip()) for inp in entradaStr.split(',') if inp]

                for inp in listaEntrada:
                    if inp > 6:
                        continue
                    if inp < 1:
                        continue

                for inp in listaEntrada:
                    player.cartas[inp-1] = deck.dealer()
                    player.cartas[inp-1].m_carta = True

                entradaValida = True
            except:
                print( 'Error de entrada: use comas para separar las tarjetas que desea mantener' )

        print(player.cartas)
        # Score
        score = Puntaje(player.cartas)
        straight = score.ordenManos()
        flush = score.manos()
        highestCount = score.cuenta()
        pares = score.pares()

        # Royal flush
        if straight and flush and straight == 14:
            print('Royal Flush!!!')
            print('+2000')
            puntos += 2000

        # Straight flush
        elif straight and flush:
            print("Straight Flush!")
            print("+250")
            puntos += 250

        # 4 of a kind
        elif score.cuatroTipo():
            print("Four of a kind!")
            print("+125")
            puntos += 125

        # Full House
        elif score.casaLlena():
            print("Full House!")
            print("+40")
            puntos += 40

        # Flush
        elif flush:
            print("Flush!")
            print("+25")
            puntos += 25

        # Straight
        elif straight:
            print("Straight!")
            print("+20")
            puntos += 20

        # 3 of a kind
        elif highestCount == 3:
            print("Three of a Kind!")
            print("+15")
            puntos += 15

        # 2 pair
        elif len(pares) == 2:
            print("Two Pairs!")
            print("+10")
            puntos += 10

        # Jacks or better
        elif pares and pares[0] > 10:
            print ("Jacks or Better!")
            print("+5")
            puntos += 5

        player.cards=[]

        print()
        print()
        print()

gamePoker()
        


""" 
Cartas 
Mazo de cartas
Jugador


"""