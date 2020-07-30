class Worker:
    def __init__(self, name, cpf, address):
        self._name = name
        self._cpf = cpf
        self._address = address
    def gains(self):              # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")

class WageEarner(Worker):
    def __init__(self, name, cpf, address, weekWage):
        Worker.__init__(self, name=name, cpf=cpf, address=address)
        self._weekWage = weekWage

    def gains(self):
        return self._weekWage

class Freelancer(Worker):
    def __init__(self, name, cpf, address, hourWage, workedHours):
        Worker.__init__(self, name=name, cpf=cpf, address=address)
        self.__hourWage = hourWage
        self.__workedHours = workedHours

    def gains(self):
        if self.__workedHours <= 40:
            return self.__workedHours * self.__hourWage
        else:
            return (40 * self.__hourWage + (self.__workedHours - 40) * 1.5)

class Commissioned(Worker):
    def __init__(self, name, cpf, address, grossSales, rate):
        Worker.__init__(self, name=name, cpf=cpf, address=address)
        self._grossSales = grossSales
        self._rate = rate

    def gains(self):
        return self._rate * (self._grossSales / 100)

class WageEarnerComisioned(WageEarner, Commissioned):
    def __init__(self, name, cpf, address, weekWage, grossSales, rate):
        WageEarner.__init__(self, name, cpf, address, weekWage)
        Commissioned.__init__(self, name, cpf, address, grossSales, rate)

    def gains(self):
        return (self._rate * self._grossSales / 100) + self._weekWage
