class Operations:
    def __init__(self, key, value, a, b):
        self._key = key
        self._value = value
        self._a = a
        self._b = b

    def operate(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def expression(self):
        return str(self._a) + self._value + str(self._b)

    def getKey(self):
        return self._key

    def getVal(self):
        return self._value

class SumOf(Operations):
    def __init__(self, a, b):
        Operations.__init__(self, key='a', value='+', a=a, b=b)

    def operate(self):
        return self._a + self._b

class SubOf(Operations):
    def __init__(self, a, b):
        Operations.__init__(self, key='s', value='-', a=a, b=b)

    def operate(self):
        return self._a - self._b

class MulOf(Operations):
    def __init__(self, a, b):
        Operations.__init__(self, key='m', value='*', a=a, b=b)

    def operate(self):
        return self._a * self._b

class DivOf(Operations):
    def __init__(self, a, b):
        Operations.__init__(self, key='d', value='/', a=a, b=b)

    def operate(self):
        return self._a / self._b
