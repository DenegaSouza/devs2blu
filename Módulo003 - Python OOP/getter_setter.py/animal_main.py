from animal import Animal

def menu():
    animal = Animal(
        input("Digite a espécie: "),
        input("Digite a raça: "),
        input("Digite o porte: "),
        input("Digite a cor: ")
        )
    print(f"Espécie: {animal.especie}\nRaça: {animal.raca}\nPorte: {animal.porte}\nCor: {animal.cor}")
    print(animal)

    animal2 = Animal(
        input("Digite a espécie: "),
        input("Digite a raça: "),
        input("Digite o porte: "),
        input("Digite a cor: ")
        )
    print(f"Espécie: {animal2.especie}\nRaça: {animal2.raca}\nCor: {animal2.cor}")
    print(animal2)
    
menu()