"""
Com base nas aulas passadas vamos criar um sorteio de lista e utilizando o conceito de estrutura de decisão exibir qual foi a posição de ordem de inserção de dados que foi sorteada! 
usando o conceito de importação otimizada importe a função choice, 
logo em seguida crie quatro variáveis representadas por nomes n1, n2, n3, n4, 
essas variáveis devem ser do tipo string e devem solicitar dados. 
crie uma variável que receba como lista estas quatro variáveis. 
crie uma variável usando a importação otimizada e atribuindo a variável lista. 
crie uma função de impressão utilizando polimorfismo e quebra de linhas para definir um cabeçalho para sua aplicação console. 
utilizando o conceito de interpolação exiba qual foi o nome sorteado. 
utilizando o conceito de estrutura de decisão cria uma condição que exiba a ordem em que foi digitado o nome sorteado pela variável de sorteio da lista!
"""

#importando a função choice da biblioteca random.
from random import choice

#criando 4 variáveis tipo primitivo string com solicitação de dados
n1 = str(input("Digite a cor 1: "))
n2 = str(input("Digite a cor 2: "))
n3 = str(input("Digite a cor 3: "))
n4 = str(input("Digite a cor 4: "))

#criando variável lista para receber os inputs
lista = [n1, n2, n3, n4]

#criando variável sorteio para importar a função choice.
sorteio = choice(lista)

print("="*5, "SORTEANDO...","="*5, f"\nA cor sorteada foi: {sorteio}")

if sorteio == n1:
    print("Esta cor foi digitada na posição 1")
elif sorteio == n2:
    print("Esta cor foi digitada na posição 2")
elif sorteio == n3:
    print("Esta cor foi digitada na posição 3")
else:
    print("Esta cor foi digitada na posição 4")