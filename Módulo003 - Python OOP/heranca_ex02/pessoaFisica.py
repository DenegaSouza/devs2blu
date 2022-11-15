from conta import Conta


class PessoaFisica(Conta):
    __segundo_titular = ''
    def __init__(self, titular, cpf, saldo_inicial, segundo_titular):
        super().__init__(999, 123-45, 'Pessoa Física')
        self.__titular = titular
        self.__cpf = cpf
        self.__saldo_inicial = saldo_inicial
        self.__segundo_titular = segundo_titular
        print("Passando pelo construtor da classe PessoaFisica")
        
    @property
    def segundo_titular(self):
        return self.__segundo_titular
    
    @segundo_titular.setter
    def segundo_titular(self, segundo_titular):
        self.__segundo_titular = segundo_titular
        
    def __str__(self):
        return f'{super().__str__()}\nTitular: {self.__titular}\nCPF: {self.__cpf}\nSaldo inicial: {self.__saldo_inicial}\nSegundo titular: {self.__segundo_titular} '
        