'''
7. Crie um documento main, faça um cabeçalho com print, logo em seguida a variável recebendo o Objeto da classe ,  
atribua descritivamente input solicitando os valores digitados para cada atributo específico do nosso construtor. 
utilize os métodos extrato, depositar e sacar Para manipular nosso objeto.
8. Crie uma segunda variável recebendo o Objeto da classe, faça um cabeçalho com print, 
e atribua descritivamente input solicitando os valores digitados para cada atributo  específico do nosso construtor, 
utilize os métodos extrato, transferir manipule de forma visual as impressões do extrato para visualizar a nossa transferência.
'''

from conta import Conta

print("="*10, "MENU INICIAL", "="*10)

conta = Conta('Everton', 456789, 5000, 10000)
print("="*10, "Extrato da Conta", "="*10)
conta.extrato()

# depositar valor numa conta.
print(conta.depositar(float(input("Digite o valor do deposito:> "))))

print("="*10, "Extrato Deposito", "="*10)
# chama a função que imprimi extrato da conta.
conta.extrato()

print("*"*10,"\n")

print(conta.sacar(float(input("Digite o valor do Saque:> "))))
print("="*10, "Extrato Saque", "="*10)
conta.extrato()

print("="*10, "Inicio Menu", "="*10)
conta2 = Conta('Denega', 123456, 1000, 5000)

print("="*10, "Extrato Inicial da conta", "="*10)
conta2.extrato()

conta2.transferir(float(input("Valor para transferencia: ")), conta2, conta)
print("="*10, "Extrato Transferencia:", "="*10)
conta2.extrato()

conta.extrato()