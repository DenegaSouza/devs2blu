# Crie um documento com namespace main e 
# realize a importação da classe Conta e realize a importação, também do nosso CRUD e suas funções.

from conta import Conta
from controller import create, read, update, delete

# Crie uma funcao menu 
def menu():
    # Dentro do menu crie um objeto de conta
    conta = Conta()
    # Através da variável referência do nosso objeto chame cada atributo interno da nossa classe  e atribua valores aos mesmos
    conta.titular = 'teste'
    conta.numero = 123456
    conta.saldo = 5000

    # Chame a função create e salve os dados inseridos no nosso objeto no arquivo txt
    #create(conta)
    # Crie uma variável lista_contas e atribua a função read
    #lista_contas = read()
    # Crie um print para imprimir lista_contas 
    #print(lista_contas)
    # Crie um for com uma  c, variável  está, percorrendo a nossa variável que recebeu a função read lista_contas. 
    # Dentro desse for crie um print imprimindo a variável c
    #for c in lista_contas:
        #print(c)
    update(123456)

menu()