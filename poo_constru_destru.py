#METODO CONSTRUTOR
#__init__


class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando Instancia")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Destruindo Instancia")

def criar_chachorro():
    c = Cachorro("Tiglo", "Black")
    print(c.nome)

c = Cachorro("Bigle", "White")
print(c.nome)
#del c
print(c)

print()
criar_chachorro()
