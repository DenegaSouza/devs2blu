import datetime
import os
from time import sleep
from controllerHotel import *

if __name__ == "__main__":    
    
    def menu():
        
        while True:
            poli = '='*10
            print(f"\n{poli} MENU DO HOTEL {poli}\n1. Fazer Check-In\n2. Relatório de Hóspedes\n3. Busca de Hóspedes\n4. Fazer Check-Out\n5. Finalizar atendimento")
        
            opcao = int(input("Por favor, digite o nr. da opção desejada: "))
            
            match opcao:
                case 1:
                    os.system('cls') 
                    cadastrar()
                            
                case 2:
                    print("2. Relatório de Hóspedes")
                    listar()

                case 3:
                    os.system('cls')
                    cliente = input("Por favor, digite o nome do hóspede: ")
                    localizar(cliente)

                case 4:
                    os.system('cls')
                    if os.path.getsize('hospedes.txt') == 0:
                        print(f"\nNão há hóspedes cadastrados\n")
                    else:
                        arquivo = open('hospedes.txt', 'r')

                        for numero, linha in enumerate(arquivo):
                            relatorio = linha.replace("{'cpf':","cpf:").replace("'","").replace("nome:","nome:").replace("sobrenome:","sobrenome:").replace("}","")
                            print(f"{numero + 1} -", relatorio)

                        print("Checkout de Hóspede ")
                        hospedeCheckout = int(input("Informe o índice para Checkout: "))
                        checkout(hospedeCheckout)

                case 5:
                    os.system('cls')
                    print("\nAtendimento encerrado.\n")
                
                case 9:
                    os.system('cls')
                    print("Checkout de Hóspede ")
                    hospedeCheckout = int(input("Informe o índice para Checkout: "))
                    checkout(hospedeCheckout)
                
                case _:
                    os.system('cls')
                    print("Opção Inválida. Escolha entre 1 e 5!\n")
    menu()