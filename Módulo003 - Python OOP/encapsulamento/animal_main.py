from animal import Animal

animal = Animal('Especie', 'Raca', 'Porte', 'Cor')

print(f"Especie: {animal.get_especie()}\nRaca: {animal.get_raca()}\nPorte: {animal.get_porte()}\nCor: {animal.get_cor()}")
print("==============")
print(animal)

animal2 = Animal(
    input("Digite a espécie: "), 
    input("Digite a raca: "),
    input("Digite o porte: "),
    input("Digite a cor: ")    
)
print(f"Especie: {animal2.get_especie()}\nRaca: {animal2.get_raca()}\nCor: {animal2.get_cor()}")
print("==============")
print(animal2)