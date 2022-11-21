
from conta import Conta
from controller import create, read, update, delete

# Crie uma funcao menu 
def menu():
    # Dentro do menu crie um objeto de conta
    #conta = Conta()
    # Através da variável referência do nosso objeto chame cada atributo interno da nossa classe  e atribua valores aos mesmos
    #conta.titular = 'teste update'
    #conta.numero = 123456
    #conta.saldo = 10000
    #create(conta)    
    
    update_conta = Conta()
    update_conta.titular = 'teste'
    update_conta.saldo = int(500)
    
    update(update_conta)

    #delete(666)

menu()