"""
EXERCICIO 1
Crie um programa que leia nome, ano de nascimento e carteira de trabalho de uma pessoa 
e cadastre-os através de um dicionário em um input , 
se o número da carteira de trabalho for diferente de ZERO, 
o dicionário receberá através de uma condicional também os dados do primeiro ano de contratação e o salário. 
ao final do programa imprima os dados solicitados, esta construção deve ser feita através de funções
"""

from controller import cadastrarFunc
from controller import os

if __name__ == "__main__":    
    
    def menu():
        
        while True:
            poli = '='*10
            print(f"\n{poli} EXERCICIO 1 {poli}\n1. Cadastrar\n2. Sair")
            opcao = int(input("Por favor, digite o nr. da opção desejada: "))
            
            match opcao:
                case 1:
                    os.system('cls') 
                    cadastrarFunc()
                    
                case 2:
                    os.system('cls') 
                    print("\nAtendimento encerrado.\n") 
                
                case _:
                    os.system('cls')
                    print("Exercício Inválido. Escolha entre 1 e 3!\n")
    menu()