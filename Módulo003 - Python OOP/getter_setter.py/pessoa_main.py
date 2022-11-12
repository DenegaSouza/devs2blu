from pessoa import Pessoa

def menu():
    pessoa = Pessoa(
        input("Digite o nome: "),
        input("Digite o cpf: "),
        input("Digite a idade: "),
        input("Digite a altura: ")
        )
    print(f"Nome: {pessoa.nome}\nCPF: {pessoa.cpf}\nIdade: {pessoa.idade}\nAltura: {pessoa.altura}")
    print(pessoa)

    pessoa2 = Pessoa(
        input("Digite o nome: "),
        input("Digite o cpf: "),
        input("Digite a idade: "),
        input("Digite a altura: ")
        )
    print(f"Nome: {pessoa2.nome}\nCPF: {pessoa2.cpf}\nIdade: {pessoa2.idade}")
    print(pessoa2)

menu()