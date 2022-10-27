import os

def cadastrarAluno():
    print("CADASTRO DE ALUNOS")
    cadastroAluno = {}
    cadastroAluno['nome'] = str(input("Digite o nome do aluno: ")) 
    cadastroAluno['nota1'] = int(input("Digite a primeira nota: "))
    cadastroAluno['nota2'] = int(input("Digite a segunda nota: "))
    cadastroAluno['nota3'] = int(input("Digite a terceira nota: "))
    print(f"Aluno cadastrado com os seguintes dados {cadastroAluno}")
    
def mediaAluno():
    

==