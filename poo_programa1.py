class Bicicleta:
    def __init__(self, cor, modelo, ano, valor, movimento=False, baixa=False, marcha=0):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.movimento = movimento
        self.baixa = baixa
        self.marcha = marcha
        
    def buzinar(self):
        print("Bibiiiiiiiiii")
        
    def acao(self):
        if (self.movimento == False):
            print("Bike Parada")
        else:
            print("Bike Em Movimento")

    def liberado(self):
        if (self.baixa == False):
            print("Não")
        else:
            print("Sim")

    def cor(self):
        return self.cor

    #def voar(): #TRABALHAR EXPLICITAMENTE
    #    print("Flying")
        
    def trocar_marcha(self, nro_marcha): #NAO ESQUECER SELF
        #print(nro_marcha)
        #print("Marcha Trocada")
        _self = self
        #print(_self)
        
        def _trocar_marcha():
            if nro_marcha > _self.marcha:
                #print(_self.marcha)
                print("Marcha Trocada")
            #pass
            else:
                print("Não Trocada")
                
        _trocar_marcha()

    #def __str__(self):
    #    return f"Bicicleta: Cor={self.cor}, Modelo={self.modelo}, Ano={self.ano}, Valor={self.valor}"

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    
bike_1 = Bicicleta("preta", "bmx", 2023, 1.200)
bike_2 = Bicicleta("rosa", "mountaim", 2020, 1.000, True)

print(bike_1.cor)
bike_1.buzinar()
bike_1.acao()

print()

print(bike_2.cor)
bike_2.buzinar()
Bicicleta.buzinar(bike_2)
#bike_2.movimento = False
bike_2.acao()
print()
print("Liberada? " + str(bike_2.baixa))
bike_2.liberado()
print()
bike_2.baixa = True
print("Liberada? " + str(bike_2.baixa))
bike_2.liberado()
print("Color " + Bicicleta.cor(bike_2))
print(bike_2.cor)
print(bike_2)
#bike_2.voar()
bike_2.trocar_marcha(1)
bike_2.trocar_marcha(0)
