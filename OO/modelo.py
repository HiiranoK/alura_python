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

    def __str__(self):
        return  f'nome: {self.nome} - Ano: {self.ano} - likes: {self.like}'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome,ano)
        self.duracao = duracao

    def __str__(self):
        return f'nome: {self.nome} - Ano: {self.ano} - duração: {self.duracao} - likes: {self.like}'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome,ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'nome: {self.nome} - Ano: {self.ano} - temporadas: {self.temporadas}- likes: {self.like}'

class Playlist:
    def __init__(self,nome,programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self,item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)
        
homem_aranha = Filme('Homem-Aranha - Sem Volta Para Casa', 2021, 120)
atlanta = Serie('Atlanta',2018, 2)
tmep = Filme('Todo mundo em pânico', 1999, 100)
demolidor = Serie('Demolidor', 2016, 2)

homem_aranha.nome = "spider-man - no way home"
homem_aranha.dar_like()
homem_aranha.dar_like()
atlanta.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
demolidor.dar_like()
demolidor.dar_like()
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()

filmes_e_series = [homem_aranha,atlanta,demolidor,tmep]

playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

for programa in playlist_fim_de_semana:
    print(programa)

print(homem_aranha in playlist_fim_de_semana)
print(playlist_fim_de_semana[1])
print(f'tamanho do playlist: {len(playlist_fim_de_semana)}')
