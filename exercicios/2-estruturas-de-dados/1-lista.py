# Crie uma lista apenas com elementos numéricos
num = [1, 2, 3, 4, 5]
print(num)

# Crie uma lista contendo todos os tipos e estrutura de dados que você aprendeu até agora
mix = [1, 2.5, True, 'aula', 5, 7, 20, 80]
print(mix)

# Imprima na tela apenas os 5 primeiros elementos da lista
print(mix[0:5])

# Crie um slice na lista para que imprima na tela os elementos de índice par
print(mix[::2])

# Remova da lista o último item
mix.pop()

# Insira na lista um novo item
mix.append('Arroz')

# Remova da lista um item específico
mix.remove(20)

print(mix)