
def saudacao():
    pass

def menu():
    poli = '='*10
    print(f"\n{poli} MENU DO HOTEL {poli}\n1. Fazer Check-In\n2. Relatório de Hóspedes\n3. Busca de Hóspedes\n4. Fazer Check-Out\n5. Finalizar atendimento")

def cadastrar():
    print("A opção selecionada foi: 1. Fazer Check-In")
    nome = input("Digite o nome do hóspede: ")
    sobrenome = input("Digite o sobrenome do hóspede: ")
    idade = int(input("Digite a idade do hóspede: "))
    print(f"{nome} foi cadastrado com sucesso!")
    cliente = salvar({nome, sobrenome, idade})
    print(cliente)

def salvar(cliente):
    with open("hospedes.txt","a") as arquivo:
        arquivo.write(f"{cliente}\n")