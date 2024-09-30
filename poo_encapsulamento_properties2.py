class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento
        #self.idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        #logica modificar nome
        pass
    
    @nome.deleter
    def nome(self):
        self._nome = "Cadastre Nova Pessoa"

    @property
    def idade(self):
        _ano_atual = 2024
        #_mes_atual = 9
        return _ano_atual - self._ano_nascimento

    def get_nome(self):
        return self._nome
    
    def get_idade(self):
        return 2024 - self._ano_nascimento

pessoa = Pessoa("M", 1992)
print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")
print(f"Nome: {pessoa.get_nome()} \tIdade: {pessoa.get_idade()}")
del pessoa.nome
print(pessoa.nome)
