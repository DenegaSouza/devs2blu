
from model.pessoaFisica import PessoaFisica
from model.pessoaJuridica import PessoaJuridica
from controller.juridico import create_pj, read_pj
from controller.fisico import create_psf, read_psf
import os

# Crie uma funcao menu()
def menu():
    # Dentro da função menu() crie uma variável com nome de menu recebendo valor 1
    menu = 1
    # Crie um while, abrindo parênteses  atribua à variável menu diferente de zero.
    while (menu != 0):
        # Crie um print descritivo solicitando ao usuário para digitar a opção desejada
        print('='*10, "MENU BANCÁRIO", '='*10)
        # Crie uma variável menu_inicial recebendo um int() e dentro do int um input solicitando ao usuário opção 1 ou opção 2, 
        # estas opções devem ser relacionadas à pessoa física e pessoa jurídica
        menu_inicial = int(input(('\nPor favor, digite a opção desejada:\n1. Pessoa Física\n2. Pessoa Jurídica\n9. Encerrar\n> ')))
                           
        # Crie um match recendo a variável menu_incial:
        match menu_inicial:
            # Crie um case 1: opção de escolha para pessoa física.
            case 1:
                os.system('cls')
                print("Você selecionou a Opção 1 - Menu de Pessoa Física")
                menu = int(input('Digite 1 para Criar Conta Pessoa Física\nDigite 2 para Listar Contas de Pessoa Física\nDigite 9 para sair\n> '))
                match menu:
                    case 1:
                        os.system('cls')
                        print("Você selecionou a Opção 1 - Criar Conta Pessoa Física")
                        conta = PessoaFisica()                        
                        conta.titular = 'Everton Souza'
                        conta.cpf = '06146'
                        conta.saldo_inicial = '5000'
                        os.system('cls')
                        print(f"Cadastro concluído!\nTitular: {conta.titular}\nCPF: {conta.cpf}\nSaldo Inicial: {conta.saldo_inicial}\n")
                        segundo_titular = int(input("Deseja cadastrar o Segundo Titular da conta?\nDigite 1 para SIM ou 2 para NÃO\n> "))
                        if segundo_titular == 1:
                            conta.segundo_titular = input('Digite o nome do segundo titular: ')
                            create_psf(conta)
                            print(conta)
                        elif segundo_titular == 2:
                            print("Ok, cadastro concluído sem Segundo Titular")
                            create_psf(conta)
                            
                    case 2:
                        os.system('cls')
                        print("Você selecionou a Opção 2 - Listar Conta Pessoa Física")
                        lista_contas_psf = read_psf()
                        for c in lista_contas_psf:
                            print(c)   
                    case 9:
                        break
                    case _:
                        print("Opção Inválida. Tente novamente.")   
                                    
                            
                
            # Crie um case 2: opção de escolha para pessoa juridica
            case 2:
                os.system('cls')
                print("Você selecionou a Opção 1 - Menu de Pessoa Jurídica")
                menu = int(input('Digite 1 para Criar Conta Pessoa Jurídica\nDigite 2 para Listar Contas de Pessoa Jurídica: \n> '))
                match menu:
                    case 1:
                        os.system('cls')
                        print("Você selecionou a Opção 1 - Criar Conta Pessoa Jurídica")
                        conta = PessoaJuridica()                        
                        conta.titular = 'Everton Souza'
                        conta.cnpj = '16146657'
                        conta.saldo_inicial = '10000'
                        os.system('cls')
                        print(f"Cadastro concluído!\nTitular: {conta.titular}\nCNPJ: {conta.cnpj}\nSaldo Inicial: {conta.saldo_inicial}\n")
                        segundo_titular = int(input("Deseja cadastrar o Segundo Titular da conta?\nDigite 1 para SIM ou 2 para NÃO\n> "))
                        if segundo_titular == 1:
                            conta.segundo_titular = input('Digite o nome do segundo titular: ')
                            create_pj(conta)
                            print(conta)
                        elif segundo_titular == 2:
                            print("Ok, cadastro concluído sem Segundo Titular")
                            create_pj(conta)
                                                   
                    case 2:
                        os.system('cls')
                        print("Você selecionou a Opção 2 - Listar Conta Pessoa Jurídica")
                        lista_contas_pj = read_pj()
                        for c in lista_contas_pj:
                            print(c)
                    case _:
                        print("Opção Inválida. Tente novamente.")   
                        break                  
            case 9:
                break
            case _:
                print("Opção Inválida. Tente novamente.")   
                  