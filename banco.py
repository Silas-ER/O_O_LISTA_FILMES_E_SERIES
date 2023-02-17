class Banco:
    def __init__(self, nome, ano):
        self._nome = nome
        self._ano = ano
        self._likes = 0
    
    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1
    
    @property
    def ano(self):
        return self._ano

    @property
    def nome(self):
        return self._nome 
    
    @nome.setter
    def nome(self,nome):
        self._nome = nome

class filme(Banco):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

class serie(Banco):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
