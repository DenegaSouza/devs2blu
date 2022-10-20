from controller import soma
from controller import subtracao
from controller import multiplicacao
from controller import divisao
import os

if __name__ == "__main__":
    while True:
        n1 = n2 = t1 = t2 = None
        poli = '='*10
        print(f"\n{poli} MENU DA CALCULADORA {poli}\n1. SOMA\n2. SUBTRAÇÃO\n3. MULTIPLICAÇÃO\n4. DIVISÃO\n5. SAIR")
        operacao = int(input("Por favor, digite o nr. da operação desejada: "))
        
        if operacao == 1:
            print("O resultado da SOMA é:", soma(n1, n2),"\nRetornando ao menu principal...")  
        elif operacao == 2:
            print("O resultado da SUBTRAÇÃO é:",subtracao(n1, n2),"\nRetornando ao menu principal...")
        elif operacao == 3:
            print("O resultado da MULTIPLICAÇÃO é:", multiplicacao(n1, n2),"\nRetornando ao menu principal...")
        elif operacao == 4:
            print("O resultado da DIVISÃO é:", divisao(n1, n2),"\nRetornando ao menu principal...")
        elif operacao == 5:
            os.system('cls')
            print("\nPrograma encerrado.\n")
            break
        else:
            os.system('cls')
            print("Opção Inválida. Escolha entre 1 e 5!\n")