import string
import random


ascii1= (string.ascii_letters)

print(ascii1)

def pa():
        a= random.randint(0,9)
        r=5
        cripto= ''

        for i in palavra:
            soma = shift + a
            cripto += ascii1[soma % len(ascii1)]
            a += r

        print(cripto)

def pg():
        a1= random.randint(0,9)
        q=2
        cripto2= ''

        for i in palavra:
            soma1= shift + a1
            cripto2 += ascii1[soma1 % len(ascii1)]
            a1= a1*q
        
        print(cripto2)

def np():
    
    #preciso identificar uma formula para localizar os possíveis números primos.
    numeros_primos= (2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139)
    n=0

    cripto3= ''
    for i in palavra:
        soma2= shift + numeros_primos[n]
        cripto3 += ascii1[soma2 % len(ascii1)]
        n+=1
    print(cripto3)

def fibonacci():
    n=0
    j=1
    cripto4= ''

    for i in palavra:
        tabela_fibonacci= range(0,1000)
        soma3= tabela_fibonacci[n]+ tabela_fibonacci[j]
        cripto4 += ascii1[soma3 % len(ascii1)]
        n+=1
        j+=1
    print(cripto4)


             
while True:


    print('[1] PA')
    print('[2} PG')
    print('[3] NP')
    print('[4] Fibonacci')

    opcao= input('Escolha uma das opções acima: ')

    palavra= input('Digite uma palavra com até 15 caracteres e sem acentuo ')

    shift= int(input('Digite o valor de Shift: '))

    if opcao == '1':
        pa()

        
    if opcao == '2':
        pg()

    if opcao == '3':
        np()

    if opcao == '4':
         fibonacci()

    



    








