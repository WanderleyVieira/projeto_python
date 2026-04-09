def saudacao():
    x=15
    def despedida():
        print(x)

    despedida()

saudacao()

print("bom dia")



import random

txt= 'oi'

t=txt
print(txt)

# criando uma classe
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


# criando um objeto
p = Pessoa("Ana", 20)


print("----- DIR -----")
print(dir(p))   # mostra tudo que existe no objeto


print("\n----- VARS -----")
print(vars(p))  # mostra as variáveis do objeto, resumindo onde foram armazenadas as váriaveis(namespace)

print(help())

#Closure acontece quando uma função filha lembra das variáveis da função pai,
#mesmo depois da função pai ter terminado.
#Para isso, a função pai retorna a função filha.
#Depois armazenamos esse retorno em uma variável e chamamos essa função retornada.
  
def classe(a,b,c):
    print(f'classes A={a} B={b} e C={c}')
    def alunos_classe():
        print(a)

    return alunos_classe

funcao=classe(3,4,6)

funcao()



    