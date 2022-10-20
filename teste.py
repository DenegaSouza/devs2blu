from time import sleep

# sleep(0.02) normal
# sleep(1) pausa

# PARTE 1 - LARISSA
# PARTE 2 - HAIKO
# PARTE 3 - MARCOS
# PARTE 4 - LUCAS
# PARTE 5 - JOÃO
# ESTRUTURAÇÃO E CRIAÇÃO DA QUESTÃO - EVERTON MARCOS LARISSA
# CORREÇÃO ORTOGRÁFICA - LARISSA HAIKO

#DEFINIÇÕES DE VARIÁVEIS
linha= '=' * 125
cont = ''
respostas = {'res1':['ponte', 'trilha'],            # BIBLIOTECA COM AS RESPOSTAS CORRETAS
             'res2': ['morango', 'cereja'],
             'res3': 75,
             'res4': ["'='*5", "'====='"],
             'res5': ["print(f'Seu salário é {salario}')", "print('Seu salário é {}'.format(salario))"]}


# VARIÁVEIS TEMPORÁRIAS
varTemporaria = 'Projeto Era uma Vez - História de Escoteiro'
historia = ''


# CABEÇALHO
print('=' * (len(varTemporaria)+2))
print(f' {varTemporaria}')
print('=' * (len(varTemporaria)+2))

# IDENTIFICAÇÃO DO USUÁRIO
player = str(input('Nome do Player: ')).strip().upper()
print('=' * (len(varTemporaria)+2))


# PLAY
while True:
    vd = 3            # Se o jogador quiser jogar novamente, ele volta a ter 3 vidas.
    print(f'Olá {player} você possui {vd} tentativas\n')

    # Alteração da variável temporária
    historia = f"Era uma vez um escoteiro chamado {player}, " \
               "que resolveu sair para caminhar pela floresta. \n" \
               "Depois de duas horas andando, ele chegou numa bifurcação, onde uma iria para uma ponte, \n" \
               "e a outra entrava mais na floresta, indo para um local escuro.\n"
               

    # INTRODUÇÃO DA HISTÓRIA E PARTE 1              # POR PADRÃO O PYTHON GUARDA OS DADOS QUE RECEBE  (buffer)
    for c in range(0, len(historia)):               # E SÓ EXIBE ATÉ QUE RECEBE O COMANDO DE NOVA LINHA \n
        print(historia[c], end='')      # ESSE ERRO INICIOU NO PYTHON 3.3
        sleep(0.02)

    # Alteração da variável temporária
    historia = "Como o escoteiro irá continuar? \n" \
               "Digite 'PONTE' para ir pela ponte \n" \
                "Digite 'TRILHA' para ir pela trilha\n"


    while True:
        # LARISSA
        #VALIDAÇÃO DA RESPOSTA parte 1
        while vd >0 :
            for c in range(0, len(historia)):
                print(historia[c], end='', flush=True)
                sleep(0.02)
            resposta = str(input()).strip().lower()
            print()

            if resposta in respostas['res1']:
                sleep(1)
                if respostas['res1'][1] in resposta:
                    # Alteração da variável temporária
                    historia = f'Essa era a escolha mais segura, e você entrou na floresta escurecida e ' \
                               f'ainda possui {vd} tentativas para continuar a história'

                    for c in range(0, len(historia)):
                        print(historia[c], end='', flush=True)
                        sleep(0.02)
                    print('\n', end='\n')
                    print(linha)
                    break
                else:
                    vd -= 1
                    print('Você escolheu errado, e acabou morrendo!\n'
                          f'Você possui mais {vd} tentativas para terminar a história.\n')
                    sleep(1)
            if vd == 0:
                break         # VALIDAÇÃO NÚMERO DE TENTATIVAS
        if vd == 0:
            break

        
        # HAIKO
        print()
        sleep(1)
        # INTRODUÇÃ da variável temporária
        historia = "Ao continuar na trilha você acaba encontrando um lobo, " \
                   "que para não te devorar te oferece um desafio:\n" \
                   "Adivinhe a palavra secreta dentre as duas: "

        for c in range(0, len(historia)):
            print(historia[c], end='', flush=True)
            sleep(0.02)

        # Alteração da variável temporária
        historia = "\nDigite a sua opção: Morango ou Cereja:"

        # VALIDAÇÃO DA RESPOSTA parte 2
        while True:
            for c in range(0, len(historia)):
                print(historia[c], end='', flush=True)
                sleep(0.02)
            print()
            resposta = str(input()).strip().lower()

            if resposta in respostas['res2']:
                sleep(1)
                if resposta == respostas['res2'][0]:
                    for c in range(0, 3):
                        sleep(0.7)
                        print('. ', end='', flush=True)
                    sleep(1)
                    print(f"\nVocê segue caminho, pois sobreviveu e possui {vd} tentativas!")
                    print(end='\n')
                    print(f'{linha}\n')
                    break
                else:
                    sleep(1)
                    vd -= 1
                    print('\nVocê escolheu errado e acabou morrendo!')
                    print(f'Você possui mais {vd} tentativas para terminar a história.')
                    sleep(1)
            if vd == 0:
                break               # VALIDAÇÃO NÚMERO DE TENTATIVAS
        if vd == 0 :
            break


        # MARCOS
        # INTRODUÇÃO DA HISTÓRIA E PARTE 3
        # Alteração da variável temporária
        historia = f'Você passou pelo lobo e começou a ouvir transito distante, e ' \
                   f'ficou animado, pois está cansado e com vontade de ir para casa. \n' \
                   f'Seguindo o som, você encontra uma cabana onde uma senhora mora e em troca ' \
                   f'de café e pão, \nela pede para você que você resolva o seguinte cálculo ' \
                   f'matemático "(81/3 + 6*8)" cujo a resposta é a sua idade.'

        for c in range(0, len(historia)):
            print(historia[c], end='', flush=True)
            sleep(0.02)
        print(end='\n')

        # VALIDAÇÃO DA RESPOSTA parte 3
        # Alteração da variável temporária
        historia = 'Digite a idade da senhora:'
        while vd > 0:
            sleep(0.5)
            for c in range(0, len(historia)):
                print(historia[c], end='', flush=True)
                sleep(0.02)
            print()
            resposta = int(input())

            if resposta != respostas['res3']:
                vd -= 1
                sleep(1)
                print(f'\nVocê errou e perdeu uma vida! Agora você possui {vd} vida(s)!')
            else:
                sleep(1)
                print(f'\nParabéns, você acertou!! \nVocê possui {vd} tentativa(s).')
                sleep(1)
                print(end='\n')
                print(f'{linha}\n')
                break
            if vd == 0:
                break               # VALIDAÇÃO NÚMERO DE TENTATIVAS
        if vd == 0:
            break

        
        # LUCAS
        # INTRODUÇÃO DA HISTÓRIA E PARTE 4
        # Alteração da variável temporária
        historia = "Você está alimentado e animado, e após andar 1h você encontrou a estrada, " \
                   "e foi socorrido por um mago chamado professor André.\n" \
                   "André chega perto e faz uma pergunta."

        # estrura para imrimir o texto letra por letra
        for c in range(0, len(historia)):
            print(historia[c], end='')
            sleep(0.02)
        print(end='\n')

        # Alteração da variável temporária
        historia = "\nQual exemplo de polimorfismo está correto?\n" \
                    "'=====' \nou \n" \
                    "'='*5 \n" \
                    "Responda digitando EXATAMENTE como citado acima!"
                    
        while vd > 0:
            # VALIDAÇÃO DA RESPOSTA parte 4
            for c in range(0, len(historia)):
                print(historia[c], end='', flush=True)
                sleep(0.02)
            print(end='\n')
            resposta = str(input()).strip()

            if resposta in respostas['res4']:
                if resposta != respostas['res4'][0]:
                    vd -= 1
                    print(f"\nVocê errou e perdeu uma vida, tente novamente!\nVocê possui {vd} vida(s)")
                else:
                    sleep(1)
                    print(f'\nParabéns, você acertou!! \nVocê possui {vd} tentativa(s).')
                    sleep(0.2)
                    print(end='\n')
                    print(f'{linha}\n')
                    break
                if vd == 0:
                    break           # VALIDAÇÃO NÚMERO DE TENTATIVAS
        if vd == 0:
            break


        # JOÃO
        # Alteração da variável temporária
        historia = "Apos uma longa conversa com o mago professor André, você chega em uma grande montanha...\n" \
                   "Você avista um inimigo poderoso, seu nome é..."

        for c in range(0, len(historia)):
            print(historia[c], end="", flush=True)
            sleep(0.02)

        sleep(3)
        # Alteração da variável temporária
        historia = " NICOLAS"

        for c in range(0, len(historia)):
            print(historia[c], end='', flush=True)
            sleep(1)

        sleep(1)

        # VALIDAÇÃO DA RESPOSTA parte 5
        # Alteração da variável temporária
        historia = "\nEle te pergunta: Qual desses é um exemplo correto de interpolação??!!\n" \
                   "print(f'Seu salário é {salario}')\n" \
                   "ou \n" \
                   "print('Seu salário é {}'.format(salario))\n" \
                   "Responda digitando EXATAMENTE como citado acima!"

        while vd > 0:
            sleep(1)
            for c in range(0, len(historia)):
                print(historia[c], end='', flush=True)
                sleep(0.02)
            print()
            resposta = str(input()).strip()

            if resposta in respostas['res5']:
                sleep(1)
                if resposta == respostas['res5'][0]:
                    print(f"\nVocê derrota Nicolas e ainda ",
                        f"possui {vd} tentativa!" if vd == 1 else f"restavam {vd} tentativas")
                    break
                else:
                    sleep(1)
                    vd -= 1
                    print(f"\nProfessor André fica decepcionado e te dá um cascudo! Você ainda possui {vd}",
                              "tentativa!\n" if vd == 1 else "tentativas!")
                if vd == 0:
                    break           # VALIDAÇÃO NÚMERO DE TENTATIVAS
        break


        # FIM DO JOGO

    if vd > 0 :
        sleep(1)
        varTemporaria = 'Parabéns! Você completou o jogo!'
        print('=' * (len(varTemporaria) + 2))
        print(f' {varTemporaria}')
        print('=' * (len(varTemporaria) + 2))
    else :
        sleep(0.02)
        varTemporaria = 'Você perdeu!'
        print('=' * (len(varTemporaria) + 2))
        print(f' {varTemporaria}')
        print('=' * (len(varTemporaria) + 2))

    sleep(1)
    while True:                     # CONTINUE
        cont = str(input('Jogar novamente? [SIM/NÃO]: ')).strip().upper()
        if cont in 'SIMNÃONAO':
            sleep(0.02)
            break
    if cont in 'NÃONAO':
        sleep(0.02)
        break
    print(linha)

varTemporaria = f'Fim do Jogo - Você terminou o jogo com {vd} vidas!'
print('=' * (len(varTemporaria) + 2))
print(f' {varTemporaria}')
print('=' * (len(varTemporaria) + 2))