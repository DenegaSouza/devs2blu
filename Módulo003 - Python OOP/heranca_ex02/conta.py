
#criando superclasse Conta
class Conta:
    def __init__(self, numero, agencia, tipo):
        self.__numero = numero
        self.__agencia = agencia
        self.__tipo = tipo
        print("Passando pelo construtor da classe Conta")   
        
    def __str__(self):
        return f'Número: {self.__numero}\nAgência: {self.__agencia}\nTipo: {self.__tipo}'
    