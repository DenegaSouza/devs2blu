
import os, pprint

def cadastrar():
    print("A opção selecionada foi: 1. Fazer Check-In")
    hospedeDict = {}
    hospedeDict['cpf'] = str(input("Digite o CPF do hóspede: "))
    hospedeDict['nome'] = str(input("Digite o nome do hóspede: "))    
    hospedeDict['sobrenome'] = str(input("Digite o sobrenome do hóspede: "))
    os.system('cls')
    print(f"{hospedeDict['nome']} foi cadastrado com sucesso com as seguintes informações:\n{hospedeDict}")
    return salvar(hospedeDict)

def salvar(hospedeDict):
    with open("hospedes.txt","a") as arquivo:
        arquivo.writelines((str(hospedeDict)) + "\n")
        arquivo.close()

def listar():
    with open('hospedes.txt','r') as arquivo:
        print(arquivo.read())
        arquivo.close()

def localizar(cliente):
    indice=0
    flag=0
    arquivo = open('hospedes.txt','r')
    
    for linha in arquivo:
        indice += 1
        if cliente == eval(linha)['nome']:
            flag = 1
    if flag == 0:
        print("Não encontrado.")
    
    else:
        print(f"{cliente} encontrado!")
    
    arquivo.close()

def checkout(hospedeCheckout):
    os.system('cls')
    with open('hospedes.txt') as arquivo:
        lines = arquivo.readlines()
    
    if(hospedeCheckout <= len(lines)):
        del lines[hospedeCheckout - 1]

        with open('hospedes.txt', "w") as arquivo:
            for line in lines:
                arquivo.write(line)
            print("Check-out efetuado com sucesso!")
    else:
        print(f"\nNão existe um hóspede com este índice {hospedeCheckout} <\n")
        
def teste(hospedeCheckout):
    os.system('cls')
    with open('hospedes.txt') as arquivo:
        lines = arquivo.readlines()
        
    if hospedeCheckout == eval(lines)['cpf']:
        del lines[hospedeCheckout - 1]

        with open('hospedes.txt', "w") as arquivo:
            for line in lines:
                arquivo.write(line)
            print("Check-out efetuado com sucesso!")
    else:
        print(f"\nNão existe hóspede com o índice {hospedeCheckout}\n")