#letras = len("python")
#listas = len([10, 20, 30])

#print(letras)
#print(listas)

class Passaro:
    def voar(self): #pass
        #print("Voando...")
        print("Pardal Pode Voar")

class Pardal(Passaro):
    def voar(self):
        #print("Pardal Voa")
        return super().voar()

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz Não Voa")

# FIXME: Exemplo ruim do uso de herança para "ganhar" o método voar
class Aviao(Passaro):
    def voar(self):
        print("Avião Está Decolando...")

#def plano_de_voo(passaro):
#    passaro.voar()

def plano_de_voo(obj):
    obj.voar()

#plano_de_voo(Pardal())
#plano_de_voo(Avestruz())

p1 = Pardal()
a1 = Avestruz()
plano_de_voo(p1)
plano_de_voo(a1)
plano_de_voo(Aviao())
