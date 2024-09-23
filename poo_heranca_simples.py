class Veiculo:
    def __init__(self, cor, placa, qtde_rodas):
        self.cor = cor
        self.placa = placa
        self.qtde_rodas= qtde_rodas

    def ligar_motor(self):
        print("Ligando o Motor")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
 

class Carro(Veiculo):
    pass

class Motocicleta(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, qtde_rodas, carga):
        super().__init__(cor, placa, qtde_rodas)
        self.carga = carga
        #print(self.carga)
        
    def esta_carregado(self, carga):
        self.carga = carga
        print(self.carga)
        print(f"{'Sim' if self.carga else 'Não'}")
        #if carga == True:
        #    print("Sim")
        #else:
        #    print("Não")

    #def __str__(self):
        #return self.cor


moto1 = Motocicleta("Preta", "CV-001", 2)
moto1.ligar_motor()
#print(moto1)

carro1 = Carro("Branco", "XXV-5246", 4)
carro1.ligar_motor()

caminhao1= Caminhao("Rosa", "JGH-45652", 10, False)
caminhao1.ligar_motor()
caminhao1.esta_carregado(True)
caminhao1.esta_carregado(False)
print(caminhao1)
print(moto1)
print(carro1)
