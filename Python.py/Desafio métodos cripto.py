import string #biblioteca onde armazena ascii entre outras strings
import random #biblioteca onde consigo buscar por números aleatorios através de comandos.

#ascii
ascii1= (string.ascii_letters)

def pa():
        a= random.randint(0,9) #Será sorteado um número de 0 a 9 que correspondera ao número inicial (a)
        r=5         #r= razão
        cripto= '' #onde armazenará as letras da criptografia

        for i in palavra:
            soma = shift + a                #[soma % len(ascii1)] *assim que a tabela acabar, voltará para o inicio novamente (fará lopping)
            cripto += ascii1[soma % len(ascii1)] #será adicionado no cripto algumas letras da tabela ascii, que corresponde ao indice identificado pelo resultado da soma
            a += r #a soma da razão com o número inicial(a), resultará no próximo número que se tornará o número inicial(a), e assim sucessivamente, até ser finalizado o for

        print(cripto) #mensagem criptografada

def pg():
        a1= random.randint(0,9)
        r1=2
        cripto2= ''

        for i in palavra:
            soma1= shift + a1
            cripto2 += ascii1[soma1 % len(ascii1)]
            a1= a1*r1 #a multiplicação da razão(r1) com o número inicial(a1), resultará no próximo número que se tornará o número inicial(a1),\n
                        #e assim sucessivamente, até ser finalizado o for.
        print(cripto2)

def np():
    
    #Abaixo farei uma tupla com alguns números primos.
    numeros_primos= (2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139)
    ni=0 #ni (número do índice)
    cripto3= ''

    for i in palavra:
        soma2= shift + numeros_primos[ni]
        cripto3 += ascii1[soma2 % len(ascii1)]
        ni+=1
    print(cripto3)

def fibonacci():
    na=0 #número anterior
    np=1 #número posterior
    cripto4= ''

    for i in palavra:

        soma3= na + np
        cripto4 += ascii1[soma3 % len(ascii1)]
        na = np       #na ganha o valor de np e o np ganha o valor da soma, assim cada um pula uma casa e faz a soma, até o for se encerrar.
        np = soma3     #ex: soma3= na(2) np(3): #na pega o valor de np= 3 e descarta o 2, np pega o valor de soma3 = 5 e atualiza seu valor, para que /
                        # haja a soma do numero anterior (na) com o numero posterior (np), obs: valor anterior sempre é descartado.

        print(soma3)
    print(cripto4)

while True:


    print('[1] PA(Progressão Aritmetica)')
    print('[2] PG(Progressão Geometrica)')
    print('[3] NP(Números Primos)')
    print('[4] Fibonacci')
    print('[5] Sair')

    try:
        opcao= input('Escolha uma das opções acima: ')

        palavra= input('Digite uma palavra: ')

        shift= int(input('Digite o valor de Shift: '))
    
    except ValueError:
         print('Error digite exatamente da maneira que está sendo solicitado.')
         continue
         

    if opcao == '1':
        pa()

    elif opcao == '2':
        pg()

    elif opcao == '3':
        np()

    elif opcao == '4':
         fibonacci()

    elif opcao == '5':
         print('Fechando programa...')
         break
    
    else:
         print('opção inválida, tente novamente.')
         continue

    



    








