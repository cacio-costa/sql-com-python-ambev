print('Olá, Mundo Python com SQL')
# A função `print` escreve o texto na saída do sistema operacional

# Programa que calcula a média de idade de uma família

print( (40 + 37 + 0.5) / 3 ) # Saída -> 25.833333
# Operadores matemáticos
#   +  -> Adição
#   -  -> Subtração
#   *  -> Multiplicação
#   /  -> Divisão
#   %  -> Módulo (resto da divisão)
#   ** -> Exponenciação
#   // -> Divisão inteira
#   
#   Parênteses, numa expressão, indicam a precedência


# Versão coom variáveis

idade_do_pai = 40 
# a partir desse momento, o programa conhece
# o nome "idade_do_pai" com o valor 40

idade_da_mae = 37
idade_do_filho = 0.5

soma_das_idades = (idade_do_pai + idade_da_mae + idade_do_filho) 
media = soma_das_idades / 3

print(f'A média das idades é {media}')
# SAÍDA: A média das idades é 25.833333333333332

# Lista com as notas de um aluno
notas = [8.9, 9.4, 7.8]


# Tupla representando um registro lido do banco de dados
fornecedor = ('47.508.411/0001-86', "Distribuidora Água Viva Bebidas", '(11) 2564-7890')


# Elementos das listas e tuplas são acessados pelo índice.
# Começa pelo índice ZERO (0).
print(notas[1]) # SAÍDA -> 9.4
print(fornecedor[0]) # SAÍDA -> 47.508.411/0001-86


# Dicionário representando um produto
coca_cola = {
  'codigo': 2,
  'nome': 'Coca Cola',
  'preco': 4.99
}


# O acesso aos valores dos dicionários se dá pela CHAVE
print(coca_cola['preco'])

# Avalia a bebida: está barata se o preço for menor que 5 reais
coca_cola = {
	'codigo': 2,
	'nome': 'Coca Cola',
	'preco': 4.99
}

if coca_cola['preco'] < 5:
	print('Está barata')
else:
	print('Me rouba logo!!!')

# SAÍDA: -> Está barata, porque o preço da Coca (4.99) < 5


# Exibir todos os dados do fornecedor
fornecedor = ('47.508.411/0001-86', "Distribuidora Água Viva Bebidas", '(11) 2564-7890')

for campo in fornecedor:
	print(campo)

# SAÍDA (cada informação é impressa em uma nova linha)
#   -> 47.508.411/0001-86
#   -> Distribuidora Água Viva Bebidas
#   -> (11) 2564-7890
	

# Cria função para calcular a média final nas disciplinas da escola.
#
#  -> Precisa receber 3 parâmetros para realizar o cálculo.
#  -> Retorna o valor da média ao ponto em que foi invocada.

def calcula_media_final(nota1, nota2, nota3):
    soma_das_notas = nota1 + nota2 + nota3
    
    media = soma_das_notas / 3
    return media


# Parâmetros seguem a ordem em que são passados: nota1=5.7, nota2=6.8 e nota3=3.4
media_do_joao = calcula_media_final(5.7, 6.8, 3.4) 

media_da_maria = calcula_media_final(nota1=8.8, nota2=8.5, nota3=9.9)

print(media_do_joao) # Saída -> 5.3
print(media_da_maria) # Saída -> 9.06