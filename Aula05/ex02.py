"""
exercício-02 
usando a biblioteca interna random use o conceito de importação de toda biblioteca. 
crie quatro variáveis recebendo valores, 
essas variáveis devem ser com tipos predefinidos tipo string, 
crie uma variável recebendo uma lista das 4 variáveis, 
logo em seguida utilize importação da biblioteca e atribua a função embaralhar(shuffle). 
essa importação irá realizar o embaralhamento dos valores recebidos atribua a lista a esta função. 
crie uma função de impressão utilizando polimorfismo e quebra de linhas para definir um cabeçalho para sua aplicação console. 
utilizando a interpolação exiba em seguida com a função de impressão a ordem definida dos nomes da variável lista.
"""

#importanto a biblioteca random
import random

#criando 4 variáveis recebendo valores tipo string.
c1 = str(input("Digite uma cor: "))
c2 = str(input("Digite uma cor:: "))
c3 = str(input("Digite uma cor:: "))
c4 = str(input("Digite uma cor:: "))

#variável que recebe uma lista com as 4 variáveis já criadas.
lista = [c1, c2, c3, c4]

#variável recebendo a função de embaralhar.
embaralhar = random.shuffle(lista)

# função impressão com polimorfismo e quebra de linhas (\n). Mostrando o resultado da função embaralhar.
print("="*5, "EMBARALHANDO","="*5, f"\n A lista embaralhada ficou: {lista}")