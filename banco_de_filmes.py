class filmes:
    def __init__ (self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0
    
    @property
    def likes(self):
        return self.__likes

    @property
    def nome(self):
        return self.__nome
        
    def dar_like(self):
        self.__likes += 1