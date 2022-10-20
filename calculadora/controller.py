import os

def soma(n1, n2):
    os.system('cls')
    print("Você escolheu a opção SOMA\n")
    n1 = float(input("Digite o primeiro número a ser somado: "))
    n2 = float(input("Digite o segundo número a ser somado: "))
    return n1 + n2
    
def subtracao(n1, n2):
    os.system('cls')
    print("Você escolheu a opção SUBTRAÇÃO\n")
    n1 = float(input("Digite o primeiro número a ser subtraído: "))
    n2 = float(input("Digite o segundo número a ser subtraido: "))
    return n1 - n2

def multiplicacao(n1, n2):
    os.system('cls')
    print("Você escolheu a opção MULTIPLICAÇÃO\n")
    n1 = float(input("Digite o primeiro número a ser multiplicado: "))
    n2 = float(input("Digite o segundo número a ser multiplicado: "))
    return n1 * n2

def divisao(n1, n2):
    os.system('cls')
    print("Você escolheu a opção DIVISÃO\n")
    n1 = float(input("Digite o primeiro número a ser dividido: "))
    n2 = float(input("Digite o segundo número a ser dividido: "))
    return n1 / n2

def somaSal(sal1, sal2, sal3, sal4):
    return sal1+sal2+sal3+sal4