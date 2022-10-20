""""
crie novo documento mainSalario 
Crie variáveis com tipos predefinidos que suportem a inserção de dados com casas decimais 
representando os 4 últimos salários de uma pessoa. 
crie uma função de impressão de dados para definir o cabeçalho de uma calculadora, 
utilizando o conceito de polimorfismo e imprima a palavra, Calculadora no centro da sua aplicação console. 
utilizando o conceito de máscara de substituição imprima descritivamente cada salário e a soma entre os mesmos imprimindo o resultado final. 
Ex " primeira variável : {} " os dados devem ser apresentados um em cada linha na sua aplicação console, 
deve ser utilizado os caracteres especiais de quebra de linha e na impressão deve apresentar apenas duas casas após a vírgula 
imprima no final utilizando a variável de soma para imprimir o resultado final do seu exercício. 
no documento controller crie uma função para calcular a soma do salario"""

from controller import somaSal

poli = '='*5, "Calculadora", '='*5
sal1 = float(input("Digite o 1º salário: "))
sal2 = float(input("Digite o 2º salário: "))
sal3 = float(input("Digite o 3º salário: "))
sal4 = float(input("Digite o 4º salário: "))
somaSalario = float(somaSal(sal1, sal2, sal3, sal4))

print(poli,"\n1º salário: R${:.2f}\n2º salário: R${:.2f}\n3º salário: R${:.2f}\n4º salário: R${:.2f}\nA soma dos salários é de: R${:.2f}" .format(sal1, sal2, sal3, sal4, somaSalario))