from conta import Conta

class PessoaJuridica(Conta):
    __segundo_titular = ''
    def __init__(self, titular, cnpj, saldo_inicial, segundo_titular):
        super().__init__(9876, 123-9, 'Pessoa Jurídica')
        self.__titular = titular
        self.__cnpj = cnpj
        self.__saldo_inicial = saldo_inicial
        self.__segundo_titular = segundo_titular
        print("Passando pelo construtor da classe PessoaJuridica")   
        
    
    @property
    def segundo_titular(self):
        return self.__segundo_titular
    
    @segundo_titular.setter
    def segundo_titular(self, segundo_titular):
        self.__segundo_titular = segundo_titular
        
    def __str__(self):
        return f'{super().__str__()}\nTitular: {self.__titular}\nCNPJ: {self.__cnpj}\nSaldo Inicial: {self.__saldo_inicial}\nSegundo titular: {self.__segundo_titular}'
        