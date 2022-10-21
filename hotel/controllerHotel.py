
import os

def saudacao():
    pass

def menu():
    poli = '='*10
    print(f"\n{poli} MENU DO HOTEL {poli}\n1. Fazer Check-In\n2. Relatório de Hóspedes\n3. Busca de Hóspedes\n4. Fazer Check-Out\n5. Finalizar atendimento")

def cadastrar():
    print("A opção selecionada foi: 1. Fazer Check-In")
    hospedeDict = {}
    hospedeDict['cpf'] = str(input("Digite o CPF do hóspede: "))
    hospedeDict['nome'] = str(input("Digite o nome do hóspede: "))    
    hospedeDict['sobrenome'] = str(input("Digite o sobrenome do hóspede: "))
    hospedeDict['idade'] = int(input("Digite a idade do hóspede: "))
    os.system('cls')
    print(f"{hospedeDict['nome']} foi cadastrado com sucesso com as seguintes informações:\n{hospedeDict}")
    return salvar(hospedeDict)


def salvar(hospedeDict):
    with open("hospedes.txt","a") as arquivo:
        arquivo.writelines(str(f"{hospedeDict}\n"))
        arquivo.close()

def listar():
    with open('hospedes.txt','r') as arquivo:
        print(arquivo.readlines())

        arquivo.close()


def checkout():
    hospedeDict.clear()
