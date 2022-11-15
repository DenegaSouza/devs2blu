from pessoaFisica import PessoaFisica
from pessoaJuridica import PessoaJuridica

contaFisica = PessoaFisica('everton', 123456, 10000)  
print(contaFisica)
segundoTitular = contaFisica.segundo_titular = 'eu tb'
print(f'{contaFisica}\nSegundo titular: {segundoTitular}')


print("----------------------------------------")
contaJuridica = PessoaJuridica('everton', 161456, 5000)    
print(contaJuridica)
segundoTitularJuridica = contaJuridica.segundo_titular = 'eu tb'
print(f'{contaFisica}\nSegundo titular: {segundoTitularJuridica}')