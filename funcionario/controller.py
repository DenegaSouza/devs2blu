import os

def cadastrarFunc():
    print("CADASTRO DE FUNCIONÁRIO")
    cadastroFunc = {}
    cadastroFunc['nome'] = str(input("Digite o nome do funcionário: ")) 
    cadastroFunc['ano_nasc'] = str(input("Digite o ano de nascimento: "))
    cadastroFunc['cart_trab'] = int(input("Digite o número da carteira de Trabalho: "))
    if cadastroFunc['cart_trab'] != 0:
        cadastroFunc['ano_inicio'] = int(input("Digite o ano de contratação: ")) 
        cadastroFunc['salario'] = int(input("Digite o salário: "))
            
    else:
        print(f"Cadastrado com sucesso. Segue dados: \n{cadastroFunc}") 
    return salvar(cadastroFunc)

def salvar(cadastroFunc):
    with open("cadastroFunc.txt","a") as arquivo:
        arquivo.writelines((str(cadastroFunc)) + "\n")
        arquivo.close()

def cadastrarPessoa():          
        
    print("CADASTRO DE PESSOAS")
    listaPessoa = []
    cadastroPessoa = {}
    cadastroPessoa['nome'] = str(input("Digite o nome da pessoa: ")) 
    cadastroPessoa['sexo'] = str(input("Digite o sexo: "))
    cadastroPessoa['idade'] = int(input("Digite a idade: "))
    print(cadastroPessoa)


def listarFunc():
    with open('cadastroFunc.txt','r') as arquivo:
        print(arquivo.read())
        arquivo.close()