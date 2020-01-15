import random

class Carta( object ):
    def __init__(self, valor, traje): 
        self.valor = valor 
        self.traje = traje
        self.showing = False

    def __repr__(self):
        if self.showing:
            return f"{self.valor} de {self.traje}"
        else:
            return "CARTA"

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
        self.cartas_en_mesa = [self.deck.dealer() for i in range(5)]

        # Turn 
        # self.cartas_en_mesa += [self.deck.dealer() for i in range(1)]

        # # River
        # self.cartas_en_mesa += [self.deck.dealer() for i in range(1)]

        # Jugadores reciben 2 cartas
        self.mano_jugador1 = []
        for i in range(1,13):
            if i == 6 or i == 12:
                self.mano_jugador1.append(self.deck.dealer())
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

    def jugador1(self):
        banner = '|' + 'CARTAS JUGADOR'.center(30) + '|'
        print('-' * len(banner))
        print(banner)
        print('-' * len(banner))

        # Muestra las cartas del Jugador
        for card in self.mano_jugador1:
            print('|' + f'{card.valor} de {card.traje}'.center(30) + '|')
        print('-' * len(banner))

    def analisis(self):
        
        self.mostrar_cartas_mesa()
        self.jugador1()
        
        banner = '|' + 'ANALISIS'.center(30) + '|' 
        print('-' * len(banner))
        print(banner)
        print('-' * len(banner))

        # Evaluar
        carta_pool = self.cartas_en_mesa + self.mano_jugador1

        # valores/pares
        valor_carta = [carta.valor for carta in carta_pool]

        print(valor_carta)
#################################################
        # carta_jugador = self.cartas_en_mesa + self.mano_jugador1

        # valor_carta1 = [carta.valor for carta in carta_jugador]
        # print(valor_carta1)

        # print(carta_jugador)
#########################################

        for value in set(valor_carta):
            # Tercia
            if valor_carta.count(value) == 3:
                mano = [carta for carta in carta_pool if carta.valor == value]
                print('|' + f'[3] Tres de un tipo: [{value}]'.center(30) + '|')
            # Par
            elif valor_carta.count(value) == 2:
                mano = [carta for carta in carta_pool if carta.valor == value]
                print('|' + f'[P] Un Par: [{value}]'.center(30) + '|')
            # Cuatro de un tipo
            elif valor_carta.count(value) == 4:
                mano = [carta for carta in carta_pool if carta.valor == value]
                print('|' + f"[4] Cuatro de un tipo: [{value}]".center(30) + '|')

        # Color
        carta_traje = [carta.traje for carta in carta_pool]
        for suit in set(carta_traje):
            if carta_traje.count(suit) >= 5:
                print(f'[F] Color: {suit}')

        # cierre
        print('-' * len(banner))

    
#################

def main():
    poker = Juego()
    poker.mostrar_cartas_mesa()
    poker.analisis()

if __name__ == "__main__":
    main()    
