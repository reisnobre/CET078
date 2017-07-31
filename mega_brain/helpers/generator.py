import sys
import os
import io
dir = os.path.dirname(__file__)
sys.path.insert(0, dir + '../')

import random
from operations import SumOf, SubOf, MulOf, DivOf
from expression import Expression

def generate(size=1):
    expressions = []
    problems = []
    while size:
        ctrl = random.randint(1, 4)
        a = random.randint(-100, 100)
        b = random.randint(-100, 100)
        d = random.randint(1, 5)
        op = None
        if ctrl is 1:
            op = SumOf(a=a,b=b)
        elif ctrl is 2:
            op = SubOf(a=a,b=b)
        elif ctrl is 3:
            op = MulOf(a=a,b=b)
        elif ctrl is 4:
            op = DivOf(a=a,b=b)

        expressions.append(Expression(difficulty=d, category=op.getKey(), expression=op.expression(), answer=op.operate()))
        size -= 1

    s_expressions = sorted(expressions, key=lambda expr : expr.difficulty())
    for e in expressions:
        problems.append(e.problem())
    output_expressions(problems) # return s_expressions

def output_expressions(expression):
    try:
        with open('expressions.txt', mode='a', encoding='utf-8') as f:
            f.write('\n'.join(expression))
            f.close()
    except OSError as err:
        with open('expressions.txt', mode='wt', encoding='utf-8') as f:
            f.write('\n'.join(expression))
            f.close()
