from car import Car
from configurador import Configurador

lCar = Car()
lCar.instalaOpcional('ar_condicionado')
lConfigurador = Configurador()

lConfigurador.addCarro(lCar)
print(lConfigurador)