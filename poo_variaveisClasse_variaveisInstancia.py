class Estudante:
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f"{self.nome} ({self.matricula}) - {self.escola}"

def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

aluno_1 = Estudante("Marcinho", 1)
aluno_2 = Estudante("Darlan", 2)

#print(aluno_1)
#print(aluno_2)
mostrar_valores(aluno_1, aluno_2)

aluno_1.matricula = 3

print("")
#print(aluno_1)
mostrar_valores(aluno_1, aluno_2)

print("")
Estudante.escola = "Python"
aluno_3 = Estudante("Joazinho", 4)
aluno_3.escola = "DIO"

mostrar_valores(aluno_1, aluno_2, aluno_3)
