# Realize a importação da classe
from model.pessoaJuridica import PessoaJuridica

# Crie a função create_psf recebendo um atributo interno create_psf (conta)
def create_pj(conta):
    
    contas = open('pessoajuridica.txt', 'a')
    # Crie uma variável contas escrevendo no arquivo pessoafisica.txt
    # Chame essa variável, chamando a função interna do python que escreve .write()
    # Coloque o atributo da função create_psf (conta) dentro de parênteses convertido para string.write(str(conta)) , 
    # faça com que cada dado inserido seja escrito na próxima linha utilizando quebra de linha, '\n'
    contas.write(str(conta)+'\n')
    # Escreva a função  interna contas.close() para fechar o arquivo
    contas.close()
    
# Crie a função read_psf  dentro do bloco da função 
def read_pj():
    # crie uma variável lista_contas recebendo uma lista vazia.
    lista_contas = []
    # Crie uma segunda variável contas abrindo nosso arquivo txt
    contas = open('pessoajuridica.txt', 'r')
    # Crie um for com uma variável conta percorrendo a variável contas do arquivo pessoajuridica.txt
    for conta in contas:
        # faça novamente a variável do for conta e atribua a função interna do python Que retira os espaços .strip()
        conta = conta.strip()
        # Crie uma variável conta_objeto recebendo a variável conta e 
        # utilize a função interna do python que identifica um índice na lista .split()
        conta_objeto = conta.split(';')
        print(conta_objeto)
        
        # Crie um objeto de conta 
        conta = PessoaJuridica()
        # e chame cada atributo da nossa classe, inclusive os dados da classe base (Conta) agencia, numero_agencia, titular, cnpj e saldo_inicial
        # E insira para cada atributo um índice da lista conforme a sequência de criação
        conta.agencia = conta_objeto[0]
        conta.numero_agencia = conta_objeto[1]
        conta.titular = conta_objeto[2]
        conta.cnpj = conta_objeto[3]
        conta.saldo_incial = conta_objeto[4]
        # Chame a variável criada inicialmente, lista_contas e recebendo a função interna do python .append()
        lista_contas.append(conta)
        
    # Chame a variável contas do arquivo txt e receba a função interna do python para fechar o arquivo txt
    contas.close()
    return lista_contas
    
# Atribua à variável de referência do objeto
