"""
Com base nas aulas passadas vamos criar uma calculadora utilizando o conceito de estrutura de decisão. 
crie duas variáveis recebendo dados numéricos com casas decimais, a descrição deve ser relacionada com primeira nota e segunda nota! 
crie uma variável para realizar este cálculo, não esqueça de utilizar o conceito de ordem de procedência aritmética. 
crie uma função de impressão utilizando polimorfismo e quebra de linhas para definir um cabeçalho para sua aplicação console. 
utilizando máscara de substituição imprima de forma descritiva a primeira nota, 
utilize quebra de linha, imprima a segunda nota, 
utilize a quebra de linha e imprima o resultado. 
usando estrutura de decisão crie uma condição onde o resultado for maior que sete imprima na sua aplicação console que este aluno está acima da média. 
usando estrutura de decisão crie uma condição onde o resultado for igual a sete imprima na sua aplicação console que este aluno está na média. 
usando estrutura de decisão crie uma condição onde o resultado for entre cinco e sete imprima na sua aplicação console que este aluno pode solicitar recuperação. 
usando estrutura de decisão crie uma condição onde o resultado for entre quatro e cinco imprima na sua aplicação console que este aluno deve procurar o professor. 
Usando estrutura de decisão crie uma condição de saída e imprima na sua aplicação console que este aluno infelizmente não atingiu o esperado!
"""

#criando variáveis n1 e n2 recebendo dados numéricos com casas decimais (float)
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

#cálculo da média das variáveis n1 e n2.
media = (n1 + n2) / 2

#função impressão com polimorfismo, quebra de linha e resultado do cálculo de média + notas através de máscara de substituição.
print("="*10,"CÁLCULO DE MÉDIA DO ALUNO", "="*10,"\nA primeira nota foi: {}.\nA segunda nota foi: {}.\nA média do aluno é {}".format(n1, n2, media))

#estrutura de decisão
if media >7:
    print("O aluno está acima da média.")
elif media == 7:
    print("O aluno está na média!")
elif media >5 and media <7:
    print("O aluno pode solicitar recuperação.")
elif media >=4 and media == 5:
    print("O aluno deve procurar o professor.")
else:
    print("O aluno não atingiu o esperado.")