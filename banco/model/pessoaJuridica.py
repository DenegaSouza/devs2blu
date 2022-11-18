# Realize a importação da classe conta
from model.conta import Conta

# crie uma classe PessoaJuridica, faça a herança da classe conta 
# esta classe deve conter quatro atributos privados: segundo_titular, titular, cnpj e saldo_inicial inseridos diretamente na classe, 
# todos os atributos devem estar vazios, sem dados fixos
class PessoaJuridica(Conta):
    __segundo_titular = ''
    __titular = ''
    __cnpj = ''
    __saldo_inicial = ''
    
    # Crie anotações de @property e @setter para cada atributo privado da nossa classe.
    @property
    def segundo_titular(self):
        return self.__segundo_titular
    @segundo_titular.setter
    def segundo_titular(self, segundo_titular):
        self.__segundo_titular = segundo_titular

    @property
    def titular(self):
        return self.__titular
    @titular.setter
    def titular(self, titular):
        self.__titular = titular
    
    @property
    def cnpj(self):
        return self.__cnpj
    @cnpj.setter
    def cnpj(self, cnpj):
        self.__cnpj = cnpj
    
    @property
    def saldo_inicial(self):
        return self.__saldo_inicial
    @saldo_inicial.setter
    def saldo_inicial(self, saldo_inicial):
        self.__saldo_inicial = saldo_inicial  
    
    # Chame o método __str__ e retorne o método super().__str__() 
    # e acessando os atributos através das anotações de @property e @setter de titular, cnpj e saldo_inicial e segundo_titular,  
    # coloque ( ; ) na divisão entre  os atributos.
    def __str__(self):
        return f'{super().__str__()}; {self.segundo_titular}; {self.titular}; {self.cnpj}; {self.saldo_inicial}'