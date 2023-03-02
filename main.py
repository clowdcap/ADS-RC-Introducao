# Exercício de fixação 1:
# Elabore um algoritmo que solicite dois números ao usuário e exiba a soma deles

def exercicio_1():
    def soma_numeros(n1, n2):
        return n1 + n2

    print("Digite o primeiro número: ")
    numero1 = float(input())

    print("Digite o segundo número: ")
    numero2 = float(input())

    return print('Soma:', soma_numeros(numero1, numero2))


exercicio_1()

#########################################################################################
# Exercício de fixação 2:
# Elabore um algoritmo que solicite ao usuário seu ano de nascimento e calcule sua idade
# com relação ao ano de 2020, sendo que o usuário já fez aniversário nesse ano.

def exercicio_2():
    ano_atual = 2023

    def calcular_idade(ano_nasc):
        return ano_atual - ano_nasc

    print("Digite o seu ano de nascimento: ")
    ano_de_nascimento = int(input())

    return print('Sua idade é de:', calcular_idade(ano_de_nascimento), 'anos')


exercicio_2()

#########################################################################################
# Exercício de fixação 3:
# Elabore um algoritmo que solicite ao usuário o nome de uma disciplina e
# suas quatro notas bimestrais.
# O algoritmo deve calcular a média dessas notas
# e exibir uma mensagem informando que a média da disciplina nome é média.

def exercicio_3():
    lista_de_notas = []

    def pega_dados(numero_de_notas):
        for nota, index in enumerate(range(numero_de_notas)):
            nota = float(input(f"Digite a nota {index + 1}: "))
            lista_de_notas.append(nota)

    def soma_notas(notas):
        return sum(notas)

    def media_notas(soma):
        return soma / quantidade_de_notas

    def imprime_na_tela():
        return print(f'Disciplina: {nome_da_disciplina} \n'
                     f'Média: {media_notas(soma_notas(lista_de_notas))}')

    nome_da_disciplina = str(input(f"Qual Disciplina: "))
    quantidade_de_notas = int(input(f"Quantas notas vão ser analizadas: "))
    pega_dados(quantidade_de_notas)

    return imprime_na_tela()


exercicio_3()

#########################################################################################
# Exercício de fixação 4:
# Elabore um algoritmo que solicits o nome de um produto, seu valor e quantidade,
# informando o valor de compra calculado.

def exercicio_4():
    nome_do_produto = str(input('Qual o nome do produto ?: '))
    valor_do_produto = float(input('Qual o valor do produto ?: '))
    quantidade_do_produto = int(input('Qual a quantidade do produto ?: '))

    valor_da_compra = valor_do_produto * quantidade_do_produto

    return print(f'Produto: {nome_do_produto}\n'
                 f'Valor do Produto: R${valor_do_produto:.2f}\n'
                 f'Quantidade: {quantidade_do_produto}\n'
                 f'Valor da compra: R${valor_da_compra:.2f}')


exercicio_4()

#########################################################################################
# Exercício de fixação 5:
# Elabore um algoritmo que solicits o nome de um produto, seu valor e quantidade,
# informando o valor de compra calculado.

def exercicio_5():
    nome_do_produto = str(input('Qual o nome do produto ?: '))
    valor_do_produto = float(input('Qual o valor do produto ?: '))
    quantidade_do_produto = int(input('Qual a quantidade do produto ?: '))
    desconto_na_compra = 0.15

    valor_da_compra = (valor_do_produto * quantidade_do_produto) - (
            valor_do_produto * quantidade_do_produto) * desconto_na_compra

    return print(f'Produto: {nome_do_produto}\n'
                 f'Valor do Produto: R${valor_do_produto:.2f}\n'
                 f'Quantidade: {quantidade_do_produto}\n'
                 f'Valor da compra: R${valor_da_compra:.2f} com desconto de 15%')

exercicio_5()

#########################################################################################
