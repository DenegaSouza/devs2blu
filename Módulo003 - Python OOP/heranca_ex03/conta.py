
class Conta:
    def __init__(self, numero, agencia, tipo):
        self.__numero = numero
        self.__agencia = agencia
        self.__tipo = tipo
        print("Passando pelo construtor da classe Conta")        
  
    @property
    def numero(self):
        return self.__numero
    @numero.setter
    def numero (self, numero):
        self.__numero = numero
        
    @property
    def agencia(self):
        return self.__agencia
    @agencia.setter
    def agencia (self, agencia):
        self.__agencia = agencia
        
    @property
    def tipo(self):
        return self.__tipo
    @tipo.setter
    def tipo (self, tipo):
        self.__tipo = tipo
        
    @property
    def segundo_titular(self):
        return self.__segundo_titular
    @segundo_titular.setter
    def segundo_titular(self, segundo_titular):
        self.__segundo_titular = segundo_titular

    def __str__(self):
        return f'Número: {self.numero}\nAgência: {self.agencia}\nTipo: {self.tipo}'