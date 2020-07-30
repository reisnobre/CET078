import sys
import os
dir = os.path.dirname(__file__)
sys.path.insert(0, dir + '../')

from expression import Expression

def generate(amount):
    expressions = []
    while amount:
        
        amount--
