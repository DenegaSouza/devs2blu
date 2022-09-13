n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))

media = (n1 + n2) / 2

print(f"Parabéns, você atingiu a média de {media}" if media >=7 else f"Você não atingiu a média. Sua média foi de {media}")