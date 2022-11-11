'''
EXERCICIO-03 
crie um documento instanciando uma classe chamada pessoa, 
crie a função construtor, 
com a variável referência que acessa os atributos da classe no espaço alocado de memória.  
defina os atributos diretamente na função construtor nome, SobreNome, idade, cpf, 
crie um segundo documento main com variável pessoa 1, pessoa 2, pessoa 3 , 
insira valores diferentes para cada objeto, 
imprima no terminal o espaço  alocado de memória do objeto principal , do objeto principal  e de cada variável de referência para o objeto!
'''

class Pessoa:
    nome = ''
    altura = 0
    idade = 0
    cpf = ''
    
    def __str__(self):
        return f'{self.nome} - {self.altura} - {self.idade} - {self.cpf}'

pessoa1 = Pessoa()
pessoa1.nome = 'everton'
pessoa1.cpf = '000.000.000-00'
pessoa1.idade = 30
pessoa1.altura = 1.8

print(pessoa1.altura)

