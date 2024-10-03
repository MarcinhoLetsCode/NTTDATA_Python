class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    #def criar_de_partir_data_nascimento(self, ano, mes, dia, nome):
    @classmethod
    def criar_de_partir_data_nascimento(cls, ano, mes, dia, nome):
        print(cls)
        mes_atual = 10
        ano_atual = 2024
        if (mes_atual < mes):
            idade = ano_atual - ano - 1
        else:
            idade = 2024 - ano
        #return Pessoa(nome, idade)
        return cls(nome, idade)

    @staticmethod
    def e_maior_de_idade(idade):
        return idade >= 18

p = Pessoa("Marcinho", 31)
print(p.nome, p.idade)

#p2 = Pessoa().criar_de_partir_data_nascimento(1992, 12, 23, "Marcinho")
p2 = Pessoa.criar_de_partir_data_nascimento(1992, 12, 23, "Marcinho")
print(p2.nome, p2.idade)

p3 = Pessoa.criar_de_partir_data_nascimento(1992, 12, 23, "Darlan")
print(p3.e_maior_de_idade(p3.idade))

print(Pessoa.e_maior_de_idade(10))
print(Pessoa.e_maior_de_idade(20))
