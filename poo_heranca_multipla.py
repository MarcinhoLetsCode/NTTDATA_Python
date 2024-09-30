class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        super().__init__(nro_patas=kw["nro_patas"])
        self.cor_pelo = cor_pelo
        #super().__init__(**kw)
        #print(kw)
        #print(kw["nro_patas"])

    def __str__(self):
        return "Mamifero42"

class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        super().__init__(nro_patas=kw["nro_patas"], cor_pelo=kw["cor_pelo"])
        self.cor_bico = cor_bico
        #print(kw["cor_pelo"])
    
    def __str__(self):
        #return self.__class__.__name__
        return "Ave"

class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    pass

class FalarMixin:
    def falar(self):
        return "Estou Falando"

class Leao(Mamifero):
    pass

class Ornitorrinco(Ave, Mamifero, FalarMixin):
    def __init__(self, cor_bico, cor_pelo, nro_patas):
        #print(Ornitorrinco.__mro__)
        print(Ornitorrinco.mro())
        
        super().__init__(cor_bico=cor_bico, cor_pelo=cor_pelo, nro_patas=nro_patas)

    def __str__(self):
        return "Ornitorrinco"

#gato1 = Gato(4, "Preto")
#print(gato1)

gato1 = Gato(nro_patas=4, cor_pelo="Preto")
print(gato1)

ornitorrinco1 = Ornitorrinco(nro_patas=2, cor_pelo="Vermelho", cor_bico="Laranja")
print(ornitorrinco1)
print(ornitorrinco1.falar())
