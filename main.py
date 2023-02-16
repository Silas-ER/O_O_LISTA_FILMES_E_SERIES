from banco_de_filmes import filmes
from banco_de_series import series

Vingadores = filmes('Vingadores - Guerra Infinita', 2019, 190)
Vikings = series('Vikings', 2016, 6)

print("Nome: {} - Ano: {} - Duração: {} - Likes: {}".format(Vingadores.nome, Vingadores.ano, Vingadores.duracao, Vingadores.likes))
print(Vikings.nome)