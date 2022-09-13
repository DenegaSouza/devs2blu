"""
exercício-01 
usando a biblioteca interna random use o conceito de importação otimizada de (Escolha (Choice)) de lista , 
crie quatro variáveis recebendo valores, 
essas variáveis devem ser com tipos predefinidos tipo string, 
crie uma variável recebendo uma lista das 4 variáveis, 
logo em seguida crie outra variável recebendo a importação , 
essa importação irá realizar o sorteio de um valor recebido. 
crie uma função de impressão utilizando polimorfismo e quebra de linhas para definir um cabeçalho para sua aplicação console. 
utilizando a interpolação exiba em seguida com a função de impressão o nome sorteado pela biblioteca random.
"""

#importando a função choice da biblioteca random.
from random import choice 

#criando 4 variáveis recebendo valores tipo primitivo string.
n1 = str(input("Digite o 1o item: "))
n2 = str(input("Digite o 2o item: "))
n3 = str(input("Digite o 3o item: "))
n4 = str(input("Digite o 4o item: "))

#variável que recebe uma lista com as 4 variáveis já criadas.
lista = [n1, n2, n3, n4]

#variável recebendo a importação.
sorteio = choice(lista)

#função impressão com polimorfismo e quebra de linhas. Usada interpolação {sorteio}.
print("="*5, "RESULTADO DO SORTEIO", "="*5,f"\n O item sorteado foi {sorteio}.")