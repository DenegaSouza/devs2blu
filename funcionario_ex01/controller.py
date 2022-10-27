import os

def cadastrarFunc():
    print("CADASTRO DE FUNCIONÁRIO")
    cadastroFunc = {}
    cadastroFunc['nome'] = str(input("Digite o nome do funcionário: ")) 
    cadastroFunc['ano_nasc'] = str(input("Digite o ano de nascimento: "))
    cadastroFunc['cart_trab'] = int(input("Digite o número da carteira de Trabalho ou 0 se não possuir "))
    if cadastroFunc['cart_trab'] != 0:
        cadastroFunc['ano_inicio'] = int(input("Digite o ano de contratação: ")) 
        cadastroFunc['salario'] = float(input("Digite o salário: "))
    os.system('cls')         
    print("Cadastrado com sucesso. Segue dados:")
    print("Nome:", cadastroFunc['nome'])
    print("Ano de Nascimento:", cadastroFunc['ano_nasc'])
    print("Carteira de Trabalho: sem carteira de trabalho.")
    if cadastroFunc['cart_trab'] != 0:
        print("Ano de Contratação:", cadastroFunc['ano_inicio'])
        print("Salário:", cadastroFunc['salario'])