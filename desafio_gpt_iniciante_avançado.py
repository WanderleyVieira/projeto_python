produtos = []

def cadastrar():

    while True:
        id_produto = len(produtos) + 1
    
        try:
            nome_produto=input('Digite o nome do produto: ')
            quantidade= int(input('Digite a quantidade de produto: '))
            if len(produtos) >= 1:
                for i in produtos:
                    if i ['nome_produto'] == nome_produto:
                        print('Erro: Produto já está na lista.')
                        break


        except ValueError:
            print('Valor errado, tente novamente \n')
            continue

        lista= {
            'nome_produto': nome_produto,
            'quantidade': quantidade,
            'id': id_produto
        }

        produtos.append(lista)
        print(f'{nome_produto} adicionado a lista.')
        break
    
def listar():
    if len(produtos) == 0:
        print('Lista sem produtos.')
    else:
        print(produtos)

def buscar():
    nome=input('Digite o nome do produto que quer buscar: ')

    x=False
    for i in produtos:
        if i['nome_produto'] in nome.lower():
            print(i)
            x=True
    if x == False:
        print('Produto não identificado.')
    

def atualizar_quantidade():
    atualizar=input('Digite o nome do produto que quer atualizar a quantidade: ')

    for i in produtos:
        
        if i['nome_produto'] in atualizar.lower():
            nova_quantidade= input('Digite a nova quantidade')
            i['quantidade']= nova_quantidade
            print(i)
    if i['nome_produto'] not in atualizar.lower():
        print('Produto não identificado.')



def remover():
    contador=0
    nome_r=input('Digite o nome do produto a ser removido: ')
    for r in produtos:
        
        if r['nome_produto'] in nome_r:
            del produtos[contador]
            print(f'"{nome_r}" foi removido')
        
        contador += 1

    if r['nome_produto'] not in nome_r:
        print('Produto não identificado.')

        
            

while True:
    print('\n[1] Cadastrar produto')
    print('[2] Listar produtos')
    print('[3] Buscar produto por nome')
    print('[4] Atualizar quantidade')
    print('[5] Remover produto')
    print('[6] Sair')

    opcao = input('Escolha: ')

    if opcao == '1':
        cadastrar()

    elif opcao == '2':
        listar()
    
    elif opcao == '3':
        buscar()

    elif opcao == '4':
        atualizar_quantidade()

    elif opcao == '5':
        remover()

    elif opcao == '6':
        print('Encerrando programa...')
        break