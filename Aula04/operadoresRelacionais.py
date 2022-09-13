
validador = True
validador = False
idade = int(input("Digite sua Idade: "))

print("Expressão de igualdade", " "*5 )
validador = ( idade == 18)
print(validador)

print(" "*5, "Expressão de diferença", " "*5 )
validador = ( idade != 18)
print(validador)

print(" "*5, "Expressão de maior", " "*5 )
validador = ( idade > 18)
print(validador)

print(" "*5, "Expressão de menor", " "*5 )
validador = ( idade < 18)
print(validador)

print(" "*5, "Expressão de maior e igual", " "*5 )
validador = ( idade >= 18)
print(validador)

print(" "*5, "Expressão de menor e igual", " "*5 )
validador = ( idade <= 18)
print(validador)
