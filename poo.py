class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def latir(self):
        print("Auau")
        
    def dormir(self):
        #self.acordado = False
        if (self.acordado == False):
            print("Zzzzzzz...")
        else:
            print("Acordado")


cao_1 = Cachorro("chappie", "amarelo", False)
cao_2 = Cachorro("Aladim", "branco e preto")

print(cao_1.nome)
cao_1.latir()

print()
print(cao_2.acordado)
cao_2.dormir()
cao_2.acordado = False
print(cao_2.acordado)
cao_2.dormir()
