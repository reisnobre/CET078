class Car:
    optionals = ['ar_condicionado', 'vidro_eletrico', 'direcao_hidraulica', 'sensor_estacionamento','teto_solar', 'roda_liga']
    optionalsValues = [1500, 600, 1150, 4000, 2850, 300]
    opitionalsQtd = [0]*6
    base = 29000
    def __init__(self):
        self.__optionals = [0]*6

    def instalaOpcional(self, item):
        if item in self.optionals:
            if(self.__optionals[self.optionals.index(item)] is 0):
                self.__optionals[self.optionals.index(item)] += 1
                self.opitionalsQtd[self.optionals.index(item)] += 1
                
    def getValor(self):
        value = self.base
        for index, item in enumerate(self.__optionals):
            if(item is not 0):
                value += self.optionalsValues[index]
        print(value)