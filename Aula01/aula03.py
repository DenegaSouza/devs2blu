#Criando variáveis com valores informados no terminal
nome = str(input("Informe o nome: "))
idade = int(input("Digite sua idade: "))
salario = float(input("Informe seu salário: "))

print(f"O meu nome é {nome}, tenho {idade} anos e com um salário de R${salario}")

#Opção de formatação com salario em 2 casas decimais
print("O meu nome é {}, tenho {} anos e com um salário de R${:.2f}".format(nome, idade, salario))

