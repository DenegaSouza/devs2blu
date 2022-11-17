from pessoaFisica import PessoaFisica
from pessoaJuridica import PessoaJuridica

contaFisica = PessoaFisica('everton', 123456, 10000)  
contaFisica.segundo_titular = 'eu tb'
print(contaFisica)


print("----------------------------------------")
contaJuridica = PessoaJuridica('everton', 161456, 5000)    
contaJuridica.segundo_titular = 'eu tb'
print(contaFisica)