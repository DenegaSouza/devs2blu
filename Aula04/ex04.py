"""
04-EXERCÍCIO: 
Crie variáveis com tipos predefinidos que suportem a inserção de dados com casas decimais representando os 4 últimos salários de uma (pessoa). 
crie uma variável para realizar a soma entre estes salários. 
crie uma função de impressão de dados para definir o cabeçalho de uma calculadora, 
utilizando o conceito de polimorfismo imprima a palavra Calculadora no centro da sua aplicação console, 
Logo em seguida use apenas uma vez a função de impressão, descreva cada campo com uma máscara de substituição, 
Ex " primeira variável : {} " os dados devem ser apresentados um em cada linha na sua aplicação console, 
deve ser utilizado os caracteres especiais de quebra de linha 
e na impressão deve apresentar apenas duas casas após a vírgula 
imprima no final utilizando a variável de soma para imprimir o resultado final do seu exercício.
"""

salMaio = float(input("Insira o salário de Maio: "))
salJunho = float(input("Insira o salário de Junho: "))
salJulho = float(input("Insira o salário de Julho: "))
salAgosto = float(input("Insira o salário de Agosto: "))

somaSal = salMaio + salJunho + salJulho + salAgosto

print("="*5, "CALCULADORA", "="*5)
print("Salário de Maio: {:.2f}\nSalário de Junho: {:.2f}\nSalário de Julho: {:.2f}\nSalário de Agosto: {:.2f}\nTotal de salários dos últimos 4 meses é de {:.2f}".format(salMaio, salJunho, salJulho, salAgosto, somaSal))