import os

def cadastrarPessoa():            
    print("CADASTRO DE PESSOAS")
    cadastroPessoa = {}
    cadastroPessoa['nome'] = str(input("Digite o nome da pessoa: ")) 
    cadastroPessoa['sexo'] = str(input("Digite o sexo: "))
    cadastroPessoa['idade'] = int(input("Digite a idade: "))
    return salvar(cadastroPessoa)


def salvar(cadastroPessoa):
    with open("cadastroPessoa.txt","a") as arquivo:
        arquivo.writelines((str(cadastroPessoa)) + "\n")
        arquivo.close()


def qtdCadastrados():
    with open('cadastroPessoa.txt','r') as arquivo:
        for contador, linha in enumerate(arquivo):
            pass
    print("Qtd de cadastrados: ",contador +1)
    arquivo.close()
    
def mediaIdade():
    arquivo = open('cadastroPessoa.txt','r')
    content = arquivo.readlines()
    a = 0
    for line in content:
         for i in line:
             if i.isdigit() == True:
                a += int(i)
                
    print("Soma: ", a)
