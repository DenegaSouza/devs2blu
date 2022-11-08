'''
EXERCICIO-02 
crie um documento instanciando uma classe chamada conta, 
crie a função construtor, com a variável referência que acessa os atributos da classe no espaço alocado de memória,  
defina os atributos diretamente na função construtor número, titular, saldo, limite, 
crie um segundo documento main com variável conta 1, conta 2, conta 3 , 
insira valores diferentes para cada objeto, imprima no terminal o espaço  alocado de memória do objeto principal , 
e de cada variável de referência para o objeto!

'''
from ex01 import Conta

conta1 = Conta(1, "everton", 1000, 5000)
conta2 = Conta(2, "melissa", 5000, 50000)
conta3 = Conta(3, "haiko", 100, 500)

print(conta1)
print(conta2)
print(conta3)

conta1 = Conta()

print(conta1.numero)