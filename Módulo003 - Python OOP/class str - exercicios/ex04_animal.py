'''
EXERCICIO-03 
crie um documento instanciando uma classe chamada Animal com atributos espécie, cor, raça. 
Crie  um método str  com a variável referência que acessa os atributos da classe no espaço alocado de memória. 
insira os atributos na função através da variável referência padrão, e use f string para adicionar ao return. 
crie um segundo documento main com variável referência animal 1, animal 2, animal 3 e 
insira valores diferentes para cada objeto, imprima no terminal os dados inseridos
'''

class Animal():
    especie = ''
    cor = ''
    raca = ''
    
    def __str__(self):
        return f'Especie: {self.especie} / Cor: {self.cor} / Raca: {self.raca}'