'''
Faça um programa que solicite o nome de um aluno 
solicite também a inserção das últimas três notas 
este cálculo deve realizar a média desse aluno, 
e através desta condição deve ser impresso o nome do aluno , 
as três notas digitadas e a média final, e deve ser impresso se o aluno foi aprovado ou nao!
'''

from controller import cadastrarAluno, os

if __name__ == "__main__":    
    
    def menu():
        
        while True:
            poli = '='*10
            print(f"\n{poli} EXERCICIO 3 {poli}\n1. Cadastro aluno\n2. Mostrar média\n")
        
            opcao = int(input("Por favor, digite o nr. da opção desejada: "))
            
            match opcao:
                case 1:
                    os.system('cls') 
                    cadastrarAluno()
                    
                case 2:
                    os.system('cls')
                    mostrarMedia() 
                              
                case _:
                    os.system('cls')
                    print("Exercício Inválido. Escolha entre 1 e xxxxxxx!\n")
    menu()
