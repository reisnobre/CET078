class Frac:
    def __init__(self, num, den):
        self.__num = num
        self.__den = den
        
    def gcd(self, x, y):
        while y != 0:
            (x, y) = (y, x % y)
        return x
        
    def lcm(self, x, y):
        return x * y // self.gcd(x, y)
    
    def soma(self, obj):
        lLcm = self.lcm(self.__den, obj.__den)
        res = {}
        res['__num'] = (self.__num * (lLcm / self.__den)) + (obj.__num * (lLcm / obj.__den))
        res['__den'] = lLcm
        print("Soma {}/{}".format(res['__num'], res['__den']))
        
    def subtracao(self, obj):
        lLcm = self.lcm(self.__den, obj.__den)
        res = {}
        res['__num'] = (self.__num * (lLcm / self.__den)) - (obj.__num * (lLcm / obj.__den))
        res['__den'] = lLcm
        print("Subtração {}/{}".format(res['__num'], res['__den']))
    
    def produto(self, obj):
        res = {}
        res['__num'] = self.__num * obj.__num
        res['__den'] = self.__den * obj.__den
        print("Produto {}/{}".format(res['__num'], res['__den']))
    def divisao(self, obj):
        res = {}
        res['__num'] = self.__num * obj.__den
        res['__den'] = self.__den * obj.__num
        print("Divisão {}/{}".format(res['__num'], res['__den']))
        
    def recGcd(self, a, b):
        if b == 0: 
            return a 
        else: 
            return self.recGcd(b, a % b)