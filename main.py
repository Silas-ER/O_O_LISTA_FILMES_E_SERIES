import random
from banco import Banco, filme, serie

Vingadores = filme('Vingadores - Guerra Infinita', 2019, 190)
Vikings = serie('Vikings', 2016, 6)
Vinland = serie('Vinland Saga', 2013, 2)
Megan = filme('Megan', 2023, 120)

for i in range(1,10):
    Vingadores.dar_like()
    Vikings.dar_like()
    Vinland.dar_like()
    Megan.dar_like()

