# Nesse desafio você verificará dentro de uma lista se o item estar contido nela, caso verdadeiro deverá imprimir na tela essa informação, além disso deverá solicitar avaliação para o item e armazená-la em um dicionário.
# 1. Crie uma lista com 5 diferentes cursos do LinkedIn Learning
lista = ['Python', 'Java', 'ADM', 'Moda', 'Cinema']
nota = {}

if 'Python' in lista:
  print('Pyhon está presente na lista')
  nota['Python'] = int(input('Qual sua nota para o curso?'))
  print(f'Sua nota para Python é {list(nota.values())[0]}.')
# 2. Crie 3 variáveis do tipo string e associe 1 curso a cada uma delas
# 3. Crie um dicionário vazio para armazenar a nota do curso
# 4. Crie uma estrutura condicional para verificar se cada variável está contida na lista
# 5. Se o curso estiver na lista, solicite uma nota para avaliação
# 6. Armazene essa nota no dicionário, sendo a chave o título do curso e o valor a nota
