import random

class Carta( object ):
    def __init__(self, valor, traje): 
        self.valor = valor 
        self.traje = traje
        self.showing = False

class Mazo( object ):
    def __init__(self):
        self.valores = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
        '8': 8, '9': 9, '10': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14} 
        self.trajes = {'Corazones': '♡', 'Diamantes': '♢', 'Treboles': '♣', 'Espadas': '♠'} # Los 'Corazones y los Diamantes son ROJOS. Los Treboles y las Espadas son NEGRAS
        self.carta = [Carta(valor, traje) for traje in self.trajes for valor in self.valores]

    # Barajador de tarjetas
    def barajar(self, times=1):
        random.shuffle(self.carta)

    # Repartidor de cartas
    def dealer(self):
        return self.carta.pop(0)
    

class Juego( object ):
    def __init__(self):

        # Genera cartas aleatorias
        self.deck = Mazo()
        self.deck.barajar()

        # Flop
        self.cartas_en_mesa = [self.deck.dealer() for i in range(3)]

        # Jugador recibe 2 cartas
        self.mano_jugador1 = []
        for i in range(1,13):
            if i == 6 or i == 12:
                self.mano_jugador1.append(self.deck.dealer())
            else:
                self.deck.dealer()

        self.mano_jugador2 = []
        for i in range(1,13):
            if i == 5 or i == 10:
                self.mano_jugador2.append(self.deck.dealer())
            else:
                self.deck.dealer()


        """ 
        Valor inicial. Jugador con valor de monedas. FLOOP, PRE FLOOP y RIVER. 
        Agregar jugador. Clase jugador que crees instancias jugadores. 
        Mostrar cartas si igualan precios. 
        
        Apuestas. 
        Jugador.
        Carta alta. Si arreglo vacio encontrar mas alta.

        """

        # Turn 
        # self.cartas_en_mesa += [self.deck.dealer() for i in range(1)]

        # River
        # self.cartas_en_mesa += [self.deck.dealer() for i in range(1)]
    def mostrar_cartas_mesa(self):                
        banner = '|' + 'CARTAS EN MESA'.center(30) + '|'
        print('-' * len(banner))
        print(banner)
        print('-' * len(banner))

        # Muestra las cartas en la mesa
        for card in self.cartas_en_mesa:
            print('|' + f'{card.valor} de {card.traje}'.center(30) + '|')
        print('-' * len(banner) + '\n')

    def jugador1(self):
        banner = '|' + 'CARTAS JUGADOR1'.center(30) + '|'
        print('-' * len(banner))
        print(banner)
        print('-' * len(banner))

        # Muestra las cartas del Jugador
        for card in self.mano_jugador1:
            print('|' + f'{card.valor} de {card.traje}'.center(30) + '|')
        print('-' * len(banner))

    def jugador2(self):
            banner = '|' + 'CARTAS JUGADOR2'.center(30) + '|'
            print('-' * len(banner))
            print(banner)
            print('-' * len(banner))

            # Muestra las cartas del Jugador
            for card in self.mano_jugador2:
                print('|' + f'{card.valor} de {card.traje}'.center(30) + '|')
            print('-' * len(banner))
    
    def analisis(self):
        
        self.mostrar_cartas_mesa()
        self.jugador1()
        self.jugador2()
        
        banner = '|' + 'ANALISIS'.center(30) + '|' 
        print('-' * len(banner))
        print(banner)
        print('-' * len(banner))

        # Evaluar
        carta_pool = self.cartas_en_mesa + self.mano_jugador1

        # valores/pares
        valor_carta = [carta.valor for carta in carta_pool]

        # par
        for value in set(valor_carta):
            if valor_carta.count(value) == 4:
                mano = [carta for carta in carta_pool if carta.valor == value]
                print('|' + f'[4] Dos pares: [{value}]'.center(30) + '|')

            elif valor_carta.count(value) == 3:
                mano = [carta for carta in carta_pool if carta.valor == value]
                print('|' + f'[3] Tres de un tipo: [{value}]'.center(30) + '|')

            elif valor_carta.count(value) == 2:
                mano = [carta for carta in carta_pool if carta.valor == value]
                print('|' + f'[P] Un Par: [{value}]'.center(30) + '|')

            elif valor_carta.count(value) == 2:
                mano = [carta for carta in carta_pool if carta.valor == value]
                print('|' + f'[P] Dos Pares: [{value}]'.center(30) + '|')

        # base 
        carta_traje = [carta.traje for carta in carta_pool]
        for suit in set(carta_traje):
            if carta_traje.count(suit) >= 5:
                print(f'[F] flush: {suit}')

        # cierre
        print('-' * len(banner))

""" 
Manos
1. Escalera Real: A,K,Q,J,10 del mismo palo
2. Escalera de Color: Cinco cartas en secuencia, todas del mismo palo. 
3. Cuatro de un tipo: Las cuatro cartas del mismo rango
4. Casa Llena (Poker): Tres de un tipo con un par.
5. Rubor: Cinco cartas del mismo palo, pero NO en secuencia.
6. Derecho: Cinco cartas en una secuencia, pero no del mismo palo.
7. Tres de un tipo: Tres cartas del mismo rango.
8. Dos pares: Dos pares diferentes.
9. Par: Dos cartas del mismo rango.
10. Carta alta: Cuando no se ha realizado ninguna de las manos anteriores, se juega la carta mas alta. 
"""

def main():
    # Agregar en un ciclo para las condiciones de apuestas.
    # print('ACCIONES\n"fold": Retirarse\n"call": Llamar (Igualar)\n"raise": Subir apuesta')
    # crupier = input("Ingresa tu accion: ")

    # while True:
    poker = Juego()
        # print('ACCIONES\n"fold": Retirarse\n"call": Llamar (Igualar)\n"raise": Subir apuesta')
        # crupier = input("Ingresa tu accion: ")
        # if crupier.lower() == "fold":
        #     print('FUERA ESTOY')
        #     break
        # if crupier.lower() == "call":
        #     poker.mostrar_cartas_mesa()
        # if crupier == "raise":
        #     poker.jugador()
        # # if crupier == "ana":
    poker.analisis()
        

if __name__ == "__main__":
    main()


# m = Mazo()
# m.barajar()
# rand = m.dealer()
# cartas = [m.dealer() for i in range(3)]
# # print(cartas)

# j = Juego()
# j.mostrar_cartas_mesa()
# j.jugador()


# jugador = []
# for i in range(1,13):
#     if i == 6 or i == 12:
#        jugador.append(m.dealer())
#     else:
#         rand

# # print(jugador)

# cartas += [m.dealer() for i in range(2)]

# banner = '|' + 'CARTAS EN MESA'.center(30) + '|'
# print('-' * len(banner))
# print(banner)
# print('-' * len(banner))

# for card in cartas:
#     print('|' + f'{card.valor} de {card.traje}'.center(30) + '|')
# print('-' * len(banner) + '\n')


# baner = '|' + 'CARTAS EN MANO'.center(30) + '|'
# print('-' * len(baner))
# print(baner)
# print('-' * len(baner))

# for card in jugador:
#     print('|' + f'{card.valor} de {card.traje}'.center(30) + '|')
# print('-' * len(baner))


# #############

# # baner = '|' + 'CARTAS OPONENTE'.center(30) + '|'
# # print('-' * len(baner))
# # print(baner)
# # print('-' * len(baner))

# # for card in jugador:
# #     print('|' + f'{card.valor} de {card.traje}'.center(30) + '|')
# # print('-' * len(baner))


# bannner = '|' + 'ANALISIS'.center(30) + '|' 
# print('-' * len(bannner))
# print(bannner)
# print('-' * len(bannner))

# # Evaluar
# carta_pool = j.cartas_en_mesa + j.mano_jugador
# # print(carta_pool)

# # valores/pares
# valor_carta = [carta.valor for carta in carta_pool]
# # print(f"Los valores son: {valor_carta}")

# value = [carta.valor for carta in carta_pool]
# # print(f'El value es: {set(value)}')


# # print(value)
# # par


# for value in set(valor_carta):
#     pair = valor_carta.count(value) == 2

#     if valor_carta.count(value) == 2 and valor_carta.count(value) == 3:
#         mano = [carta for carta in carta_pool if carta.valor == value]
#         print('|' + f'[P] full-House: [{value}]'.center(30) + '|')

#     # if valor_carta.count(value) == 2 and valor_carta.count(value) == 2:
#     #     mano = [carta for carta in carta_pool if carta.valor == value]
#     #     print('|' + f'[P] Two-Pair: [{value}]'.center(30) + '|')

#     if valor_carta.count(value) == 4:
#         mano = [carta for carta in carta_pool if carta.valor == value]
#         print('|' + f'[4] Four of a kind: [{value}]'.center(30) + '|')

#     if valor_carta.count(value) == 3:
#         mano = [carta for carta in carta_pool if carta.valor == value]
#         print('|' + f'[3] Three of a kind: [{value}]'.center(30) + '|')

#     if pair:
#         mano = [carta for carta in carta_pool if carta.valor == value]
#         print('|' + f'[P] One-Pair: [{value}]'.center(30) + '|')
            



# # base 
# carta_traje = [carta.traje for carta in carta_pool]
# for suit in set(carta_traje):
#     if carta_traje.count(suit) >= 5:
#         print(f'[F] flush: {suit}')
#     elif carta_traje.count == 1:
#         print(f'Mayor: {suit}')

# # cierre
# print('-' * len(bannner))

