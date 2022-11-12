from carro import Carro

def menu():
    carro = Carro(
        input("Digite a marca: "),
        input("Digite o modelo: "),
        input("Digite a cor: "),
        input("Digite a cotegoria: ")
        )
    print(f"Marca: {carro.marca}\nModelo: {carro.modelo}\nCor: {carro.cor}\nCategoria: {carro.categoria}")
    print(carro)

    carro2 = Carro(
        input("Digite a marca: "),
        input("Digite o modelo: "),
        input("Digite a cor: "),
        input("Digite a cotegoria: ")
        )
    print(f"Marca: {carro2.marca} \nModelo: {carro2.modelo} \nCategoria: {carro2.categoria}")
    print(carro2)
    
menu()