from conta import Conta

def menu():
    conta = Conta(123456, "Everton", 5000, 10000)

    print(f"Titular: {conta.titular}\nNr. da conta: {conta.numero}\nSaldo: {conta.saldo}")
    print(conta)

    conta2 = Conta(
        input("Digite o nr. da conta: "), 
        input("Digite o nome do titular: "),
        input("Digite o saldo da conta: "),
        input("Digite o limite da conta: ")    
    )
    print(f"Titular: {conta2.titular}\nNr. da conta: {conta2.numero}\nSaldo: {conta2.saldo}")
    print(conta2)
    
menu()