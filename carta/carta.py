class Carta( object ):
    def __init__(self, valor, traje):
        self.valor = valor
        self.traje = traje

    def __repr__(self):
        return f"{self.valor} de {self.traje}"

