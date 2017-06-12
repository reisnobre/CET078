class Transaction:
    def __init__(self, value):
        self.value = value
    
    def getTransactionTotal(self):
        return self.value
        
class SplitTransaction(Transaction):
    def __init__(self, splits, interestRate, value):
        super().__init__(value)
        self.__splits = splits
        self.__interestRate = interestRate
        
    def getTransactionTotal(self):
        return (self.value * (1 + self.__interestRate/100 ** self.__splits))
        
class CashTransaction(Transaction):
    def __init__(self, discount, value):
        super().__init__(value)
        self.__discount = discount
        
    def getTransactionTotal(self):
        return (self.value - self.value / self.__discount)