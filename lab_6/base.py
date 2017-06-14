from worker import Commissioned, Freelancer, WageEarner, WageEarnerComisioned

lComi = Commissioned('Eduardo', '05158724580', 'my address', 200, rate=5)
lFree = Freelancer('Jorge', '01234567890', 'my address', hourWage=23, workedHours=30)
lWageEarner = WageEarner(name='Lucas', cpf='01234567890', address='my address', weekWage=300)
lWageEarnerComissioned = WageEarnerComisioned(name='George', cpf='01234567890', address='my address', weekWage=200, grossSales=300, rate=5)

workers = [lComi, lFree, lWageEarner, lWageEarnerComissioned]

for worker in workers:
    print(worker.gains())
