while True:  # jogo inteiro
    letras_acertadas = ''
    letras_digitadas = ''
    palavra_secreta = ''

    while True:  # escolha da palavra
        palavra_chave = input('Digite uma palavra: ')
        confirmando_palavra = input(
            f'Certeza que quer utilizar esta palavra: "{palavra_chave}"?\nDigite [S,s]im ou [N,n]ão '
        )

        if confirmando_palavra.lower() == 's':
            palavra_secreta = palavra_chave
            print('Sua palavra foi adicionada')
            break
        elif confirmando_palavra.lower() == 'n':
            print('Digite uma nova palavra.')
        else:
            print('Você precisa digitar [S,s]im ou [N,n]ão.')

    while True:  # rodada do jogo
        letra_escolhida = input('Digite uma letra: ')

        if len(letra_escolhida) != 1:
            print('Digite apenas uma letra.')
            continue

        if letra_escolhida in letras_digitadas:
            print(f'Letra já digitada: {letras_digitadas}')
            continue

        letras_digitadas += letra_escolhida

        if letra_escolhida in palavra_secreta:
            letras_acertadas += letra_escolhida

        palavra_formada = ''
        for letra_chave in palavra_secreta:
            if letra_chave in letras_acertadas:
                palavra_formada += letra_chave
            else:
                palavra_formada += '*'

        print(f'Palavra formada: {palavra_formada}')

        if palavra_formada == palavra_secreta:
            print(f'\n Parabéns! Palavra secreta decifrada: {palavra_secreta}')
            print('Reiniciando jogo...\n')
            break 


            






        




    

