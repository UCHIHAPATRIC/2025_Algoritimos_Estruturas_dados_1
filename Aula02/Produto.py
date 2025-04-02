class Produto:
    def __init__(self, nome, cpf = None, preco = 10.0, qtd = 0 ):
        self.id = None
        self.nome = nome
        self.preco = preco
        self.qtd = qtd


    def __str__(self):
        txt = "Produto: " + self.nome
        txt += "\nPreço: " + str( self.preco )
        return txt