palavra_secreta= ''
letras_acertadas= ''
letras_digitadas= ''

while True:
    while True:

        palavra_chave= str(input('Digite uma palavra: '))
        confirmando_palavra= input(f'Ceteza que quer utilizar está palavra: "{palavra_chave}"?\n Digite [1] SIM ou [2] NÃO')

        if confirmando_palavra in ('1','Sim','SIM','sim','S','s'):
            palavra_secreta += palavra_chave
            print('Sua palavra foi adicionada')
        
        
        elif confirmando_palavra in ('2','Não','NÃO','não','N','n'):
            print('Digite uma nova palavra.')
            continue

        else:
            print('Você precisa digitar [1] para Sim ou [2] para não. Voltaremos ao ínicio...')

        while True:

            letra_escolhida= input('Digite uma letra: ')
            if len(letra_escolhida) == 1:
                if letra_escolhida not in letras_digitadas:
                    letras_digitadas += letra_escolhida

                elif letra_escolhida in letras_digitadas:
                    print(f'Letra já digitada: Letras Digitadas {letras_digitadas}')

                if letra_escolhida in palavra_secreta:
                    letras_acertadas += letra_escolhida

                palavra_formada= ''
                for letra_chave in palavra_secreta:
                    if letra_chave in letras_acertadas:
                        palavra_formada += letra_chave

                    else:
                        palavra_formada += '*'

                print(f'palavra formada: {palavra_formada}')

                if palavra_formada ==  palavra_secreta:
                    print(f'parabéns palavra secreta decifrada: palavra secreta = {palavra_secreta}')
                    print('Fim de jogo')

                    palavra_formada= ''
                    letras_acertadas= ''
                    letras_digitadas= ''
                    palavra_secreta= ''

                    break


            






        




    

