# Criaremos um script que imprimirá na tela o total de horas que uma pessoa estudou durante um determinado período:
# 1. Crie uma variável chamada "nome" e, usando o método input(), atribua a ela um nome;
nome = input('Insira seu nome:')

# 2. Crie uma variável chamada "total_dias" e, usando o método input(), solicite o total de dias dedicados ao estudo por semana;
total_dias = input('Insira o total de dias dedicados essa semana:')
total_dias = int(total_dias)

# 3. Crie uma variável chamada "total_horas" e, usanod o método input(), solicite a média de horas estudada por dia;
total_horas = input('Insira a média de horas estudadas esta semana:')
total_horas = int(total_horas)

# 4. Crie uma variável chamada "curso" e, usando o método input(), solicite o título do curso desejado;
curso = input('Insira seu curso:')

# 5. Imprima na tela uma frase informando o nome da estudante, o total_dias dedicados aos estudos, o total horas semanais e o curso.
print(f'Olá {nome}, você estudou {total_dias} dias com uma média de {total_horas} horas por dia, resultando um total de {total_horas * total_dias}h no curso de {curso}.')