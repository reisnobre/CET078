class Paciente:
    def __init__(self, nome, sexo, altura, peso, idade):
        self.__nome = nome
        self.__sexo = sexo
        self.__altura = altura
        self.__peso = peso
        self.__idade = idade
        self.__calIngerida = 0
        
    
    def calculaKcaloria(self):
        if(self.__sexo == "masculino"):
            return 66.437 + (5.0033 * self.__altura) + (13.7516 * self.__peso) - (6.755 * self.__idade)
        else:
            return 655.0955 + (1.8496 * self.__altura) + (9.5634 * self.__peso) - (4.6756 * self.__idade)
    
    def consomeKcaloria(self, qtd):
        if((qtd + self.__calIngerida) < self.calculaKcaloria()):
            self.__calIngerida += qtd
            print("Calorias ingeridas com sucesso, faltam {:.2f} calorias para atingir o limite diário permitido de {:.2f} calorias".format(self.calculaKcaloria() - self.__calIngerida, self.calculaKcaloria()))
        else:
             print("Não é mais permitido ingerir calorias, {:.2f} calorias consumidas de um total de {:.2f} calorias permitidas".format(self.__calIngerida, self.calculaKcaloria()))