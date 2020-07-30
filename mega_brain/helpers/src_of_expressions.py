import sys
import os
dir = os.path.dirname(__file__)
sys.path.insert(0, dir + '../')

import csv
from expression import Expression
import generator

class Source_Of_Expressions:
    def __init__(self):
        self.__expressions = self.__getExpressions()

    def __getExpressions(self):
        expressions = []
        with open("expressions.txt") as src:
            for expr in csv.reader(src, dialect="excel-tab"):
                obj = Expression(difficulty=expr[0], category=expr[1], expression=expr[2], answer=expr[3])
                expressions.append(obj)
        return sorted(expressions, key=lambda expr : expr.difficulty())

    def get(self):
        return self.__expressions
