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

    # Barajador de tarjetas
    def barajar(self, times=1):
        random.shuffle(self.mazo_carta)
        print("Tarjetas Barajadas!")

    # Metodo DEAL 
    def dealer(self):
        return self.mazo_carta.pop(0)

class Poker:
    def __init__(self):
        
        # Genera y baraja el mazo
        self.deck = Mazo()
        self.deck.barajar()

        # Primeras 3 cartas en la mesa
        self.cartas_mesa = [self.deck.dealer() for _ in range(3)]

        # Jugador recibe 2 cartas en la mano
        self.jugador_mano = []
        for _ in range(1,13):
            if _ == 6 or _ == 12:
                self.jugador_mano.append(self.deck.dealer())
            else:
                self.deck.dealer()

        # Solo agrega 
        self.cartas_mesa += [self.deck.dealer() for _ in range(2)]

    def mostrar_cartas_mesa(self):
        self.banner = '|' + 'Cartas Comunitarias'.center(30) + '|'
        print('-' * len(self.banner))
        print(self.banner)
        print('-' * len(self.banner))

        for card in self.cartas_mesa:
            print('|' + f'{card.valor} de {card.traje}'.center(30) + '|')
        print('-' * len(self.banner) + '\n')

    def por_mano(self):

        banner_mano = '|' + 'Cartas en mano'.center(30) + '|'
        print('-' *len(banner_mano))
        print(banner_mano)
        print('-' * len(banner_mano))

        for card in self.jugador_mano:
            print('|' + f'{card.valor} de {self.traje}'.center(30) + '|')
        print('-' * len(banner_mano) + '\n')

    def analisis_mano(self):

        self.mostrar_cartas_mesa()
        self.por_mano()

        banner = '|' + 'Analisis'.center(30) + '|'
        print('-' * len(banner))
        print(banner)
        print('-' * len(banner))


        pool = self.cartas_mesa + self.jugador_mano

        valor_carta = [carta.valor for carta in pool]


        for valor in set(valor_carta):
            if valor_carta.count(valor) == 4:
                mano = [carta for carta in pool if carta.valor == valor]
                print('|' + f'[4K] Four of a kind: [{valor}]'.center(30) + '|')

            if valor_carta.count(valor) == 3:
                mano = [carta for carta in pool if carta.valor == valor]
                print('|' + f'[3K] Three of a kind: [{valor}]'.center(30) + '|')

            if valor_carta.count(valor) == 2:
                mano = [carta for carta in pool if carta.valor == valor]
                print('|' + f'[P] Par: [{valor}]'.center(30) + '|')


    
        # Base trajes
        cartas_trajes = [carta.traje for carta in pool]
        for traje in set(cartas_trajes):
            if cartas_trajes.count(traje) >= 5:
                print(f'[F] flush: {traje}')

    
    # Closing
    # print('-' * len(banner))


p = Poker()
p.analisis_mano()



        

