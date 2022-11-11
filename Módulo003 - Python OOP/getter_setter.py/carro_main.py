from carro import Carro

carro = Carro('Marca', 'Modelo', 'Cor', 'Categoria')

print(f"Marca: {carro.get_marca()}\nModelo: {carro.get_modelo()}\nCor: {carro.get_cor()}\nCategoria: {carro.get_categoria()}")
print(carro)

carro2 = Carro(
    input("Digite a marca do carro: "), 
    input("Digite o modelo: "),
    input("Digite a cor: "),
    input("Digite a categoria: ")    
)
print(f"Marca: {carro2.get_marca()}\nModelo: {carro2.get_modelo()}\nCategoria: {carro2.get_categoria()}")
print(carro2)