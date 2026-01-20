



#Tabela: informações do IMC;

cadastro_imc= []

tabela= {
    'Abaixo de 17' : 'Muito baixo do peso ideal',
    'Entre 17 e 18,49' : 'Abaixo do peso',
    'Entre 18,5 e 24,99' : 'Peso normal',
    'Entre 25 e 29,99' : 'Acima do peso',
    'Entre 30 e 34,99' : 'Obesidade grau 1',
    'Entre 35 e 39,99'  : 'Obesidade grau 2',
    'Acima de 40' : 'Obesidade grau 3 (mórbida)'
    }

#Saudação para o usuário;

#Menu de opções;
def menu():

    print('        Seja Bem-Vindo!         \n')
    
    print(f'[1] Realizar Cálculo do IMC')
    print(f'[2] Visualizar Tabela do IMC')
    print(f'[3] Lista de IMC cadastrados: ')
    print(f'[4] Sair do programa')

#Onde será calculado o IMC de acordo com informações solicitada pelo sistema/
#como peso e altura;


def calculo_imc():

    id= len(cadastro_imc) + 1

    try:
        nome= input('Digite seu nome: ')
        idade= int(input('Qual sua idade ? '))
        peso= float(input('Qual seu seu peso em kg?  '))
        altura= float(input('Qual sua altura? '))

    except ValueError:
        print('Erro de digitação, lembre-se \n' \
              'idade,peso e altura são números')
        return

    resultado_imc= peso / (altura * altura) 
    print(f'Seu IMC= {resultado_imc:.2f}')

    dic_imc= {
        'nome' : nome,
        'imc': resultado_imc,
        'id': id
    }
    
    cadastro_imc.append(dic_imc)

    #Será válidado o resultado com a tabela de acordo com as opções abaixo;

    if resultado_imc < 17:
        print(tabela['menor que 17'])           

    elif resultado_imc < 18.49:
        print(tabela['Entre 18,5 e 24,99'])

    elif resultado_imc < 24.99:
        print(tabela['Entre 18,5 e 24,99'])
    
    elif resultado_imc < 29.99:
        print(tabela['Entre 25 e 29,99'])
    
    elif resultado_imc < 34.99:
        print(tabela['Entre 30 e 34,99'])
    
    elif resultado_imc < 39.99 :
        print(tabela['Entre 35 e 39,99'])

    else:
        print(tabela['Acima de 40'])


# Apenas onde será visualizado a tabela;

def tabela_imc():

     print(tabela)

#Iniciando laço;

while True:

    menu()

    opcao= int(input('Escolha uma das opções acima: '))

    if opcao == 1:
        calculo_imc()

    elif opcao == 2:
        tabela_imc()

    elif opcao == 3:
        if len(cadastro_imc) == 0:
            print('Sem cadastros\n')
        else:
            print(cadastro_imc)

    elif opcao == 4:
        print('Encerrando programa...\n')
        break

    else:
        print('Opção invalida, tente novamente\n')
        continue




#Informações sobre o que é IMC:

'''def imc_info():
    print('O IMC (Índice de Massa Corporal) é um cálculo matemático usado para indicar se uma pessoa está com peso adequado,\n magreza, sobrepeso ou obesidade. É um índice universal, validado pela Organização Mundial da Saúde (OMS), mas não \n avalia sozinho o estado nutricional, devendo ser interpretado por um profissional de saúde junto com outros fatores,\n como idade, sexo e percentual de gordura.\n'
    'A fórmula foi criada por Adolphe Quételet no século XVIII, revisada por Ancel Keys em 1972 e reconhecida como padrão\n internacional pela OMS em 1980.')'''

