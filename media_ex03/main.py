"""
Faça um programa que solicite o nome de um aluno 
solicite também a inserção das últimas três notas 
este cálculo deve realizar a média desse aluno, 
e através desta condição deve ser impresso o nome do aluno , 
as três notas digitadas e a média final, e deve ser impresso se o aluno foi aprovado ou nao!
"""

from controller import mediaAluno

if __name__ == "__main__":    
    
    def menu():
        print("EXERCICIO 3 - MÉDIA")

        nome = str(input("Digite o nome do aluno: "))
        n1 = float(input("Digite a primeira nota: "))
        n2 = float(input("Digite a segunda nota: "))
        n3 = float(input("Digite a terceira nota: "))
        n4 = float(input("Digite a quarta nota: "))
        mediaAluno(n1, n2, n3, n4)
    menu()
