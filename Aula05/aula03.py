#ESTRUTURA DE DECISÃO

n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))

media = (n1 + n2) / 2

print(f"Sua média é {media}")

if media > 7:
    print("Você está acima da média")

elif media == 7:
    print(f"Você atingiu a média {media}")

else: #não recebe variável pois é a condição de saída.
    print("Você não atingiu a média")