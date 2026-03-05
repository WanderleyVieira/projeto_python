import string # armazena ascii entre outras strings
import random #consigo gerar números aleátorios

#ascii
ascii1= (string.ascii_letters+string.digits+string.punctuation+' ')

def pa(palavra, shift):
        a= random.randint(0,9) #Será sorteado um número de 0 a 9 que correspondera ao número inicial (a)
        r=5         #r= razão
        cripto= '' #onde armazenará as letras da criptografia

        for i in palavra:
            soma = shift + a                #[soma % len(ascii1)] *assim que a tabela acabar, voltará para o inicio novamente (fará lopping)
            cripto += ascii1[soma % len(ascii1)] #será adicionado no cripto algumas letras da tabela ascii, que corresponde ao indice identificado pelo resultado da soma
            a += r #a soma da razão com o número inicial(a), resultará no próximo número que se tornará o número inicial(a), e assim sucessivamente, até ser finalizado o for

        print(f'criptografia = {cripto}') #mensagem criptografada

def pg(palavra, shift):
        a1= random.randint(0,9)
        r1=2
        cripto1= ''

        for i in palavra:
            soma1= shift + a1
            cripto1 += ascii1[soma1 % len(ascii1)]
            a1= a1*r1 #a multiplicação da razão(r1) com o número inicial(a1), resultará no próximo número que se tornará o número inicial(a1),\n
                        #e assim sucessivamente, até ser finalizado o for.
        print(f'criptografia = {cripto1}')

def np(palavra, shift):
    
    #Abaixo farei uma tupla com alguns números primos.
    numeros_primos= (2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139)
    ni=0 #ni (número do índice)
    cripto2= ''

    for i in palavra:
        soma2= shift + numeros_primos[ni % len(numeros_primos)]
        cripto2 += ascii1[soma2 % len(ascii1)]
        ni+=1
    print(f'criptografia = {cripto2}')

def fibonacci(palavra, shift):
    na=0 #número anterior
    np=1 #número posterior
    cripto3= ''

    for i in palavra:

        soma3= na + np
        resultado= soma3 + shift
        cripto3 += ascii1[resultado % len(ascii1)]
        na = np       #na ganha o valor de np e o np ganha o valor da soma, assim cada um pula uma casa e faz a soma, até o for se encerrar.
        np = soma3     #ex: soma3= na(2) np(3): #na pega o valor de np= 3 e descarta o 2, np pega o valor de soma3 = 5 e atualiza seu valor, para que /
                        # haja a soma do numero anterior (na) com o numero posterior (np), obs: valor anterior sempre é descartado.

    print(f'criptografia = {cripto3}')

while True:


    print('\n[1] PA(Progressão Aritmetica)')
    print('[2] PG(Progressão Geometrica)')
    print('[3] NP(Números Primos)')
    print('[4] Fibonacci')
    print('[5] Sair')

    try:
        opcao= input('Escolha uma das opções acima: ')
        
        if opcao == '5':
            print('Fechando programa...')
            break

        palavra= input('Digite uma palavra: ')

        shift= int(input('Digite o valor de Shift: ')) #o shift vem para mudar o calculo
    
    except ValueError:
         print('Erro: digite exatamente da maneira que está sendo solicitado.')
         continue
         

    if opcao == '1':
        pa(palavra, shift)

    elif opcao == '2':
        pg(palavra, shift)

    elif opcao == '3':
        np(palavra, shift)

    elif opcao == '4':
         fibonacci(palavra, shift)
    
    else:
         print('opção inválida, tente novamente.')
         continue

    



    








