from controller import salvar, listar

def menu():
    print("*"*20, "Menu", "*"*20)

    cond = "sim"
    while cond == "sim":
        nome = salvar(input("Digite seu nome: "))
        cond = str(input("Deseja continuar \nSim \nNÃ£o \n :> "))

menu()

print("A Lista de Nomes Inseridos\n", listar())