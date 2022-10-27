"""
Faça um programa que tenha uma função chamada contador(),
que receba três parâmetros: inicio, fim e passo e realize a contagem.
Seu programa tem que realizar três contagens através da função criada:
A) De 1 até 10, de 1 em 1
B) De 10 até 0, de 2 em 2
C) Uma contagem personalizada
"""

from controller import contador
from controller import sleep
import os

if __name__ == "__main__":    
    
    def menu():
        
        while True:
            poli = '='*10
            print(f"\n{poli} EXERCICIO 4 - CONTADOR {poli}\n1. De 1 até 10, de 1 em 1\n2. De 10 até 0, de 2 em 2\n3. contagem personalizada")
            opcao = int(input("Por favor, digite o nr. da opção desejada: "))
            
            match opcao:
                case 1:
                    os.system('cls')                    
                    contador(1, 10, 1)
                    
                case 2:
                    os.system('cls')
                    contador(10, 1, 2)

                case 3:
                    os.system('cls')
                    contador(int(input("Digite o Nr Inicial: ")),int(input("Digite o Nr final: ")),int(input("Digite o Passo: "))) 

                
                case _:
                    print("Exercício Inválido. Escolha entre 1 e 3!\n")
    menu()
