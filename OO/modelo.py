class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._like = 0

    def dar_like(self):
        self._like += 1

    @property
    def like(self):
        return self._like

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome,ano)
        self.duracao = duracao


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome,ano)
        self.temporadas = temporadas

homem_aranha = Filme('Homem-Aranha - Sem Volta Para Casa', 2021, 120)
atlanta = Serie('Atlanta',2018, 2)
homem_aranha.nome = "spider-man - no way home"
homem_aranha.dar_like()
homem_aranha.dar_like()
print(f'nome: {homem_aranha.nome} - Ano: {homem_aranha.ano} - duração:{homem_aranha.duracao} minutos - likes: {homem_aranha.like}')
atlanta.dar_like()
print(f'nome: {atlanta.nome} - ano: {atlanta.ano} - temporadas: {atlanta.temporadas} - likes: {atlanta.like}')
print(homem_aranha.nome)