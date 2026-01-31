cadastros = []

def cadastrar():
    
    while True:
        

        nome= input('Digite seu nome: ')
        idade= input('Digite sua idade: ')
        peso= input('Digite seu peso: ')
        altura= input('Digite sua altura: ')

        try:
            idade= int(idade)
            peso= float(peso)
            altura= float(altura)
        
            if idade < 18:
                print('O resultado do calculo do IMC foi feito para maiores de 18 anos.')
                break

        except:
            print('Valor digitado está errado, tente novamente.')
            continue

        imc= peso / (altura+altura)
        imc= f'Seu imc é {imc:.2f}'
        print(imc)

        novo_id = len(cadastros) + 1

        lista_nova ={
            'id': novo_id,
            'nome': nome,
            'idade': idade,
            'imc': imc
            }
        
        print (lista_nova)
        cadastros.append(lista_nova)
        break

def listar():
    if len(cadastros) == 0:
        print('Não há conteúdo nesta lista.\n') 
    else:
        print(cadastros)

while True:

    print('[1] Cadastrar pessoa')
    print('[2] Listar cadastros')
    print('[3] Sair')                   

    opcao= input('Escolha uma das opções acima: ')

    if opcao == '1':
        cadastrar()

    elif opcao == '2':
        listar()

    elif opcao == '3':
        print('Encerrando programa...')
        break

    else:
        print('Opção digitada é inválida, tente novamente.')
