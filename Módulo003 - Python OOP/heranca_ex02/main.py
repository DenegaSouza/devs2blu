from pessoaFisica import PessoaFisica
from pessoaJuridica import PessoaJuridica

contaFisica = PessoaFisica(
    input("Digite o titular: "),
    input("Digite o cpf: "),
    input("Digite o saldo inicial: "),
    input("Digite o segundo titular: ")
)    
print(contaFisica)
print("----------------------------------------")
contaJuridica = PessoaJuridica('Everton', 161456, 5000, 'Denega')    
print(contaJuridica)