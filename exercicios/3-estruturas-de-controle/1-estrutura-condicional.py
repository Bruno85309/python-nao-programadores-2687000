# Declare 4 variáveis do tipo numérica
x = 20
y = 10
a = 5
b = 10

# Crie uma estrutura condicional para comparar dois números
if x > y:
  print(f'O número {x} é maior do que o número {y} em {x-y} unidades.')

# Se a condição for verdadeira, imprima na tela uma mensagem informando que a condição foi cumprida e informando o número de maior valor
if b > a:
  print(f'A condição foi cumprida e o maior número é {b}.')

# Se a condição não for cumprida, imprima na tela uma mensagem informando que a condição é negativa e informe o número de maior valor
if a > b:
  print(f'A condição foi cumprida e {a} é maior do que {b}.')
else:
  print(f'A condição não foi cumprida e {a} é menor do que {b}')


# Insira outras condições na estrutura condicional usando o elif
if a == b:
  print(f'O valor de {a} é igual ao valor {b}')
elif b == y:
  print(f'Temos que {b} é igualzinha a {y}')
else:
  print('Nenhuma das condições de igualdade entre as variáveis foram validadas.')

# Incremente a estrutura condicional já existente com expressões lógicas utilizando "and" ou "or"
if (a == b) or (y != x):
  print(f'O valor de {a} é igual ao valor {b} ou {y} é diferente de {x}.')
elif (b == y) and (b > a):
  print(f'Temos que {b} é igualzinha a {y} e {b} é maior do que {a}.')
else:
  print('Nenhuma das condições de igualdade e/ou diferença entre as variáveis foram validadas.')