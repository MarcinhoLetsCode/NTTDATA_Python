class Conta:
    def __init__(self, nro_agencia, saldo=0):
        self._saldo = saldo
        self.nro_agencia = nro_agencia

    def depositar(self, valor):
        #...
        self._saldo += valor
    
    def sacar(self, valor):
        #...
        self._saldo -= valor

    def mostrar_saldo(self):
        #...
        return self._saldo

conta1 = Conta("0001",100)
#conta1._saldo += 100 Errado
conta1.depositar(100)
#print(conta1._saldo) Errado
print(conta1.nro_agencia)
print(conta1.mostrar_saldo())



