"""
EXERCICIO 1
Crie um programa que leia nome, ano de nascimento e carteira de trabalho de uma pessoa 
e cadastre-os através de um dicionário em um input , 
se o número da carteira de trabalho for diferente de ZERO, 
o dicionário receberá através de uma condicional também os dados do primeiro ano de contratação e o salário. 
ao final do programa imprima os dados solicitados, esta construção deve ser feita através de funções
"""

'''
Crie um programa que leia nome, sexo e idade de várias pessoas, 
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. 
No final, mostre: 
A) Quantas pessoas foram cadastradas; 
B) A média de idade do grupo; 
C) Uma lista com todas as mulheres; 
D) Uma lista com todas as pessoas com idade acima da média.
'''

from controller import *

if __name__ == "__main__":    
    
    def menu():
        
        while True:
            poli = '='*10
            print(f"\n{poli} EXERCICIOS {poli}\n1. Exercício 1\n2. Exercício 2\n")
        
            opcao = int(input("Por favor, digite o nr. da opção desejada: "))
            
            match opcao:
                case 1:
                    os.system('cls') 
                    cadastrarFunc()
                            
                case 2:
                    os.system('cls') 
                    cadastrarPessoa()


                case 5:
                    os.system('cls')
                    print("\nAtendimento encerrado.\n")
 
                
                case _:
                    os.system('cls')
                    print("Exercício Inválido. Escolha entre 1 e xxxxxxx!\n")
    menu()