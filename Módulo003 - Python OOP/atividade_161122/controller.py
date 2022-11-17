from conta import Conta

contas = Conta()

def create(conta):
    contas = open('contas.txt', 'a')
    contas.write(str(conta)+'\n')
    contas.close()

def read(conta):
    lista_contas = []
    contas = open('contas.txt', 'r')
    for conta in contas:
        conta_obj = conta.strip()
        conta = conta.split(' ;')
        
    conta.titular[0]
    conta.numero[1]
    conta.saldo[2]
 
    conta.close()
    

