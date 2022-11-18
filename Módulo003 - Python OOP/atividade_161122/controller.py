from conta import Conta

# Crie a  função create recebendo um atributo conta
def create(conta):
    # Crie uma variável contas escrevendo no arquivo txt
    contas = open('contas.txt', 'a')
    # Chame essa variável, chamando a função interna do python que escreve .write()
    # Coloque o atributo da função dentro de parênteses convertido para string, 
    # faça com que cada dado inserido seja escrito na próxima linha utilizando quebra de linha.
    contas.write(str(conta)+'\n')
    # Escreva a função interna contas.close() para fechar o arquivo
    contas.close()

#Crie a função read  dentro do bloco da função.
def read():
    # crie uma variável lista_contas recebendo uma lista vazia.
    lista_contas = []
    # Crie uma segunda variável contas abrindo nosso arquivo txt
    contas = open('contas.txt', 'r')

    # Crie um 'for' com uma variável conta percorrendo a variável contas do arquivo txt 
    for conta in contas:
        # faça novamente a variável do f'or conta' e atribua a função interna do python Que retira os espaços .strip
        conta_objeto = conta.split(';')
        # Crie uma variável conta_objeto recebendo a variável conta e 
        # utilize a função interna do python que identifica um índice na lista .strip()
        conta = conta.strip()
        print(f'print do read: {conta_objeto}')
        # Crie um objeto de conta e chame cada atributo da nossa classe titular número e saldo.
        conta = Conta()
        # insira para cada atributo um índice da lista
        conta.titular = conta_objeto[0]
        conta.numero = conta_objeto[1]
        conta.saldo = conta_objeto[2]
        # Chame a variável criada inicialmente lista_contas e recebendo a função interna do python .append(
        lista_contas.append(conta)
    # Chame a variável contas do arquivo txt e receba a função interna do python para fechar o arquivo txt .close()
    contas.close()
    return lista_contas
