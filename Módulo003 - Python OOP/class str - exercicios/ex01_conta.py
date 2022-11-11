'''
EXERCICIO-01 
crie um documento instanciando uma classe chamada Conta 
com atributos número, titular, saldo, limite crie um método str com a variável referência 
que acessa o objeto no espaço alocado de memória, acessando diretamente o objeto de conta. 
insira os atributos na função através da variável referência padrão, 
e use f string para adicionar ao return

'''

class Conta:
    numero = 0
    titular = ''
    saldo = 0
    limite = 0
    
    def __str__(self):
        return f'A conta de nr {self.numero} pertence ao titular {self.titular}, possui saldo {self.saldo} e limite {self.limite}'
    
conta1 = Conta()
conta1.numero = 123
conta1.titular = "everton"
conta1.saldo = 1000
conta1.limite = 2000

print(conta1)