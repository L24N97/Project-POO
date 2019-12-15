import random

class Carta( object ):
    def __init__(self, valor, traje): 
        self.valor = valor 
        self.traje = traje
        # self.mostrar_carta = False

    # Mostrar estado de cartas
    def __repr__(self):
        return f"{self.valor} de {self.traje}"

class Mazo( object ):
    def __init__(self):
        self.valores = [x for x in range(2, 11)] + ['Jack', 'Queen', 'king', 'Ace']
        self.trajes = ['♣', '♠', '♡', '♢']
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

        # Primeras 3 Cartas en mesa
        self.cartas_en_mesa = [self.deck.dealer() for i in range(3)]

        # Jugador recibe 2 cartas
        self.mano_jugador = []
        for i in range(1,13):
            if i == 6 or i == 12:
                self.mano_jugador.append(self.deck.dealer())
            else:
                self.deck.dealer()

    def mostrar_cartas_mesa(self):                
        banner = '|' + 'CARTAS EN MESA'.center(30) + '|'
        print('-' * len(banner))
        print(banner)
        print('-' * len(banner))

        # Muestra las cartas en la mesa
        for card in self.cartas_en_mesa:
            print('|' + f'{card.valor} de {card.traje}'.center(30) + '|')
        print('-' * len(banner) + '\n')

    def jugador(self):
        banner = '|' + 'CARTAS JUGADOR 1'.center(30) + '|'
        print('-' * len(banner))
        print(banner)
        print('-' * len(banner))

        # Muestra las cartas del Jugador
        for card in self.mano_jugador:
            print('|' + f'{card.valor} de {card.traje}'.center(30) + '|')
        print('-' * len(banner))

    def analisis(self):
        
        self.mostrar_cartas_mesa()
        self.jugador()
        
        banner = '|' + 'ANALISIS'.center(30) + '|' 
        print('-' * len(banner))
        print(banner)
        print('-' * len(banner))

        # Evaluar
        carta_pool = self.cartas_en_mesa + self.mano_jugador

        # valores/pares
        valor_carta = [carta.valor for carta in carta_pool]

        # par
        for value in set(valor_carta):
            if valor_carta.count(value) == 4:
                mano = [carta for carta in carta_pool if carta.valor == value]
                print('|' + f'[4] Dos pares: [{value}]'.center(30) + '|')

            if valor_carta.count(value) == 3:
                mano = [carta for carta in carta_pool if carta.valor == value]
                print('|' + f'[3] Tres de un tipo: [{value}]'.center(30) + '|')

            if valor_carta.count(value) == 2:
                mano = [carta for carta in carta_pool if carta.valor == value]
                print('|' + f'[P] Un Par: [{value}]'.center(30) + '|')

        # base 
        carta_traje = [carta.traje for carta in carta_pool]
        for suit in set(carta_traje):
            if carta_traje.count(suit) >= 5:
                print(f'[F] flush: {suit}')

        # cierre
        print('-' * len(banner))

p = Juego()
p.analisis()


# m = Mazo()
# m.barajar()
# rand = m.dealer()
# cartas = [m.dealer() for i in range(3)]
# # print(cartas)


# jugador = []
# for i in range(1,13):
#     if i == 6 or i == 12:
#        jugador.append(m.dealer())
#     else:
#         rand

# # print(jugador)

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

# j = Juego()
# j.mostrar_cartas_mesa()
# j.jugador()

# bannner = '|' + 'ANALISIS'.center(30) + '|' 
# print('-' * len(bannner))
# print(bannner)
# print('-' * len(bannner))

# # Evaluar
# carta_pool = j.cartas_en_mesa + j.mano_jugador
# # print(carta_pool)

# # valores/pares
# valor_carta = [carta.valor for carta in carta_pool]
# print(f"Los valores son: {valor_carta}")

# # par
# for value in set(valor_carta):
#     if valor_carta.count(value) == 4:
#         mano = [carta for carta in carta_pool if carta.valor == value]
#         print('|' + f'[4] Four of a kind: [{value}]'.center(30) + '|')

#     if valor_carta.count(value) == 3:
#         mano = [carta for carta in carta_pool if carta.valor == value]
#         print('|' + f'[3] Three of a kind: [{value}]'.center(30) + '|')

#     if valor_carta.count(value) == 2:
#         mano = [carta for carta in carta_pool if carta.valor == value]
#         print('|' + f'[P] Par: [{value}]'.center(30) + '|')

# # base 
# carta_traje = [carta.traje for carta in carta_pool]
# for suit in set(carta_traje):
#     if carta_traje.count(suit) >= 5:
#         print(f'[F] flush: {suit}')

# # cierre
# print('-' * len(bannner))