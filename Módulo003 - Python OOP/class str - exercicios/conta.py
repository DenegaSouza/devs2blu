'''
1. Crie o método construtor recebendo atributos , este método deve conter variável de referência de acesso ao objeto, 
2. crie os seguintes atributos titular, número, saldo, limite
3. Crie um método encapsulando o extrato de uma conta, o extrato deve imprimir o número da conta, o nome do titular e o saldo inicial depositado.
4. Crie um método depositar, utilizando o atributo específico do método (valor), no encapsulamento acesse os atributos da classe e 
utilizando os operadores relacionais de incremento receba o  atributo do método em questão e retorne o mesmo.
5. Crie um método sacar utilizando o atributo específico do método (valor), no encapsulamento acesse os atributos da classe e 
utilizando operadores relacionais de decremento, retorne o atributo do método
6. Crie um método transferir, utilizando os atributos específicos do método valor origem e destino. 
no encapsulamento acesse os atributos do método e atribua as funções sacar  depositar recebendo o atributo valor.
7. Crie um documento main, faça um cabeçalho com print, logo em seguida a variável recebendo o Objeto da classe ,  
atribua descritivamente input solicitando os valores digitados para cada atributo específico do nosso construtor. 
utilize os métodos extrato, depositar e sacar Para manipular nosso objeto.

'''



class Conta:
    def __init__(self, titular, numero, saldo, limite):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo
        self.limite = limite
    
    # método 'extrato' imprime os dados da conta    
    def extrato(self):
        print(f'Titular: {self.titular} / Nr. da Conta: {self.numero} / Saldo: R${self.saldo} / Limite: R${self.limite}')
    
    # método para depositar um valor na conta. Incrementar o saldo.
    def depositar(self, valor):
        self.saldo += valor
        return valor
    
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            return "Saldo indisponível para saque."
    
    def transferir(self, valor, origem, destino):
        if self.saldo >= valor:
            self.origem -= valor
            self.destino += valor