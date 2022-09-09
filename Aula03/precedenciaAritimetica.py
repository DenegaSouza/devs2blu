n1 = float(input("Digite sua nota 1: "))
n2 = float(input("Digite sua nota 2: "))

media = (n1 + n2) / 2 

print("A média entre {} e {} é de {}" .format(n1, n2, media))

# Ordem de precedência aritimética. Em parêntenses possui prioridade de primeiro nível, vai ser calculado primeiro.
# Caracteres * / ** % tem prioridade de segundo nível em cálculos matemáticos.
# Caracteres + e - tem prioridade em terceiro nível.