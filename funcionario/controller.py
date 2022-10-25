import os

def cadastrarFunc():
    print("CADASTRO DE FUNCIONÁRIO")
    cadastro = {}
    cadastro['nome'] = str(input("Digite o nome do funcionário: ")) 
    cadastro['ano_nasc'] = str(input("Digite o ano de nascimento: "))
    cadastro['cart_trab'] = int(input("Digite o número da carteira de Trabalho: "))
    if cadastro['cart_trab'] != 0:
        cadastro['ano_inicio'] = int(input("Digite o ano de contratação: ")) 
        cadastro['salario'] = int(input("Digite o salário: "))
        print(f"Cadastrado com sucesso. Segue dados: \n{cadastro}")
        
    else:
        print(f"Cadastrado com sucesso. Segue dados: \n{cadastro}") 
        
        
def cadastrarPessoa():
    print("CADASTRO DE PESSOAS")
    cadastroPessoa = {}
    cadastroPessoa['nome'] = str(input("Digite o nome da pessoa: ")) 
    cadastroPessoa['sexo'] = str(input("Digite o sexo: "))
    cadastroPessoa['idade'] = int(input("Digite a idade: "))
    
    #transformar dict em lista
    dictPessoa = dict.items(cadastroPessoa)
    print(cadastroPessoa)
    print((len(dictPessoa)))