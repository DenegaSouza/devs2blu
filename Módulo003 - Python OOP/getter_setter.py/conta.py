class Conta:
    def __init__(self, numero, titular, saldo, limite):        
        self.__titular = titular
        self.__numero = numero
        self.__saldo = saldo
        self.__limite = limite
        
    def set_titular(self, titular):
        self.__titular = titular
    def get_titular(self):
        return self.__titular
    
    def set_numero(self, numero):
        self.__numero = numero
    def get_numero(self):
        return self.__numero
    
    def set_saldo(self, saldo):
        self.__saldo = saldo
    def get_saldo(self):
        return self.__saldo
    
    def set_limite(self, limite):
        self.__limite = limite
    def get_limite(self):
        return self.__limite
    
    def __str__(self):
        return f'Titular: {self.get_titular()}\nNúmero da conta: {self.get_numero()}\nSaldo: R${self.get_saldo()}\nLimite: R${self.get_limite()}'