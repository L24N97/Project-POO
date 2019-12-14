import random

class Carta( object ):
    def __init__(self, valor, traje): 
        self.valor = valor 
        self.traje = traje
        self.mostrar_carta = False

    def __repr__(self):
        # Mostrar estado de cartas
        if self.mostrar_carta:
            return f"{self.valor} de {self.traje}"
        else:
            return "CARTA"

class Mazo( object ):
    def __init__(self):
        self.valores = [x for x in range(2, 11)] + ['J', 'Q', 'k', 'Ace']
        self.trajes = ['♣', '♠', '♡', '♢']
        self.carta = [Carta(valor, traje) for traje in self.trajes for valor in self.valores]

    # Barajador de tarjetas
    def barajar(self, times=1):
        random.shuffle(self.carta)
        print("Tarjetas Barajadas!")

    # Metodo DEAL 
    def dealer(self):
        return self.carta.pop(0)

m = Mazo()
rand = m.dealer()
rand.mostrar_carta = True
print(rand)
m.barajar()
rand = m.dealer()
rand.mostrar_carta = True
print(rand)
