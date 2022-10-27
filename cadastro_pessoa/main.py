
"""
EXERCICIO 2
Crie um programa que leia nome, sexo e idade de várias pessoas, 
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. 
No final, mostre: 
A) Quantas pessoas foram cadastradas; 
B) A média de idade do grupo; 
C) Uma lista com todas as mulheres; 
D) Uma lista com todas as pessoas com idade acima da média.
"""

from controller import *

if __name__ == "__main__":    
    
    def menu():
        
        while True:
            poli = '='*10
            print(f"\n{poli} EXERCICIOS {poli}\n1. Cadastrar pessoa\n2. Mostrar dados\n3. Qtd cadastros\n4. Media de Idade")
        
            opcao = int(input("Por favor, digite o nr. da opção desejada: "))
            
            match opcao:
                case 1:
                    os.system('cls') 
                    cadastrarPessoa()
                    
                case 2:
                    os.system('cls') 
                    
                
                case 3:
                    os.system('cls') 
                    qtdCadastrados()
                
                case 4:
                    os.system('cls') 
                    mediaIdade()                  
                    
                                                                                                                                 
                case 9:
                    os.system('cls')
                    print("\nAtendimento encerrado.\n") 
                    break                            
                
                                
                case _:
                    os.system('cls')
                    print("Exercício Inválido. Escolha entre 1 e xxxxxxx!\n")
    menu()