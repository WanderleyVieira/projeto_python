cadastro_aluno= []


def cadastrar_aluno():
    nome= input(f'Digite Seu nome: ')
    idade= int(input(f'Digite sua idade: '))
    n_id= int(input(f'Digite os 6 digitos de seu número de cadastro: '))

    cadastro= {
    'nome': nome,
    'idade': idade,
    'numero_cadastro': n_id
    }

    cadastro_aluno.append(cadastro)

def lista_alunos():
    print(cadastro_aluno)

def deletar_aluno():
    numero = int(input('Digite o número de cadastro do aluno: '))

    for aluno in cadastro_aluno:
        if aluno['numero_cadastro'] == numero:
            cadastro_aluno.remove(aluno)
            print('Aluno removido com sucesso.')
            return

    print('Aluno não encontrado.')
        

    
    

while True:
    try:

        print(f'[1] cadastrar aluno')
        print(f'[2] lista: alunos cadastrados')
        print(f'[3] deletar aluno da lista')

        opcao= int(input('Digite uma das opções acima: '))

    except:
        print('error')

    if opcao == 1:
        cadastrar_aluno()

    if opcao == 2:
        lista_alunos()

    if opcao == 3:
        deletar_aluno()


#correção

cadastro_aluno = []


def cadastrar_aluno():
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    n_id = int(input('Digite os 6 dígitos do número de cadastro: '))

    cadastro = {
        'nome': nome,
        'idade': idade,
        'numero_cadastro': n_id
    }

    cadastro_aluno.append(cadastro)
    print('Aluno cadastrado com sucesso!\n')


def lista_alunos():
    if not cadastro_aluno:
        print('Nenhum aluno cadastrado.\n')
        return

    for aluno in cadastro_aluno:
        print(
            f"Nome: {aluno['nome']} | "
            f"Idade: {aluno['idade']} | "
            f"Cadastro: {aluno['numero_cadastro']}"
        )
    print()


def deletar_aluno():
    numero = int(input('Digite o número de cadastro do aluno: '))

    for aluno in cadastro_aluno:
        if aluno['numero_cadastro'] == numero:
            cadastro_aluno.remove(aluno)
            print('Aluno removido com sucesso!\n')
            return

    print('Aluno não encontrado.\n')


while True:
    try:
        print('[1] Cadastrar aluno')
        print('[2] Listar alunos cadastrados')
        print('[3] Deletar aluno')
        print('[0] Sair')

        opcao = int(input('Digite uma das opções acima: '))

    except ValueError:
        print('Erro: digite apenas números.\n')
        continue

    if opcao == 1:
        cadastrar_aluno()

    elif opcao == 2:
        lista_alunos()

    elif opcao == 3:
        deletar_aluno()

    elif opcao == 0:
        print('Encerrando o programa...')
        break

    else:
        print('Opção inválida.\n')
