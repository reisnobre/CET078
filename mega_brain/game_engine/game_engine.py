import sys
import os
dir = os.path.dirname(__file__)
sys.path.insert(0, dir + '../helpers')

from src_of_expressions import Source_Of_Expressions

class Game_Engine:
    def __init__(self, lives=1, chances=0):
        self.__lives = lives
        self.__chances = chances
        self._expressions = Source_Of_Expressions()
        self._setup()
        self._start()

    def _setup(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def _start(self):
        raise NotImplementedError("Subclass must implement abstract method")

    #
    # def validate_expr(self):
    #     raise NotImplementedError("Subclass must implement abstract method")
    #
    # def end(self):
    #     raise NotImplementedError("Subclass must implement abstract method")
