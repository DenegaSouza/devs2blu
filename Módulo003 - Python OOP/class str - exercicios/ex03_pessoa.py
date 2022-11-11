'''
EXERCICIO-03 
crie um documento instanciando uma classe chamada Pessoa com atributos nome, cpf, idade. 
Crie  um método str  com a variável referência que acessa os atributos da classe no espaço alocado de memória.  
insira os atributos na função através da variável referência padrão, e use f string para adicionar ao return. 
crie um segundo documento main com variável referência pessoa 1, pessoa 2, pessoa 3  
insira valores diferentes para cada objeto, imprima no terminal os dados inseridos
'''

class Pessoa():
    nome = ''
    cpf = ''
    idade = 0
    
    def __str__(self):
        return f'Nome: {self.nome} / CPF: {self.cpf} / Idade: {self.idade}'
    
    