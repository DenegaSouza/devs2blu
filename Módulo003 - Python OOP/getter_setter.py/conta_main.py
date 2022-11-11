from conta import Conta

conta = Conta(123456, "Everton", 5000, 10000)

print(f"Titular: {conta.get_titular()}\nNr. da conta: {conta.get_numero()}\nSaldo: {conta.get_saldo()}")

conta2 = Conta(
    input("Digite o nr. da conta: "), 
    input("Digite o nome do titular: "),
    input("Digite o saldo da conta: "),
    input("Digite o limite da conta: ")    
)
print(f"Titular: {conta2.get_titular()}\nNr. da conta: {conta2.get_numero()}\nSaldo: {conta2.get_saldo()}")