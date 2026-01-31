produtos = []

def cadastrar():

    id_produto = len(produtos) + 1

    try:
        nome_produto=input('Digite o nome do produto: ')
        quantidade= int(input('Digite a quantidade de produto: '))
    
    except ValueError:
        print('Valor errado')

    lista= {
        'nome_produto': nome_produto,
        'quantidade': quantidade,
        'id': id_produto
    }

    produtos.append(lista)


def listar():
    if len(produtos) == 0:
        print('Lista sem produtos.')
    else:
        print(produtos)

def buscar():
    nome=input('Digite o nome do produto que quer buscar: ')
    nome = nome

    for i in produtos:
        if i['nome_produto'] in nome.lower():
            print(i)

def atualizar_quantidade():
    atualizar=input('Digite o nome do produto que quer atualizar a quantidade: ')

    for i in produtos:
        if i['nome_produto'] in atualizar.lower():
            nova_quantidade= input('Digite a nova quantidade')
            i['quantidade']= nova_quantidade
            print(i)



def remover():
    nome_r=input('Digite o nome do produto a ser removido: ')

#Preciso colocar um código válido que remova determinado produto.
    for i in produtos:
        if i['nome_produto'] in nome_r.lower():
            print(i)

while True:
    print('[1] Cadastrar produto')
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