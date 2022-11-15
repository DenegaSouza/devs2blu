#Classe mãe (ou superclasse)

class Conta:
    def __init__(self, numero, tipo):
        self.numero = numero
        self.tipo = tipo
        print("Passando pelo construtor da classe Conta")
        
    def __str__(self):
        return f'Nr. de conta: {self.numero}\nTipo de conta: {self.tipo}'