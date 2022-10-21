import datetime
import os
from time import sleep
from controllerHotel import *

if __name__ == "__main__":
    while True:
        menu()
        opcao = int(input("Por favor, digite o nr. da opção desejada: "))
        
        if opcao == 1:
            os.system('cls') 
            cadastrar()
                           
        elif opcao == 2:
            print("2. Relatório de Hóspedes")

        elif opcao == 3:
            os.system('cls')
            nome = input("Por favor, digite o nome do hóspede: ")
            print("A Lista de Nomes Inseridos\n", listar())

        elif opcao == 4:
            print("4. Fazer Check-Out")
            checkout = checkout(input("Digite o nome do hóspede para deletar: "))

        elif opcao == 5:
            os.system('cls')
            print("\nAtendimento encerrado.\n")
            break
        else:
            os.system('cls')
            print("Opção Inválida. Escolha entre 1 e 5!\n")