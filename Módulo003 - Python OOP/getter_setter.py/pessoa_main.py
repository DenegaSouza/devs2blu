from pessoa import Pessoa

pessoa = Pessoa("Everton", "061466", 30, 183)

print(f"Nome: {pessoa.get_nome()}\nNr. CPF: {pessoa.get_cpf()}\nIdade: {pessoa.get_idade()}\nAltura: {pessoa.get_altura()}")

pessoa2 = Pessoa(
    input("Digite o nome da pessoa: "), 
    input("Digite o CPF: "),
    input("Digite a idade: "),
    input("Digite a altura em cm: ")    
)
print(f"Nome: {pessoa2.get_nome()}\nNr. CPF: {pessoa2.get_cpf()}\nIdade: {pessoa2.get_idade()}")
print(pessoa2)