import sys
import os
dir = os.path.dirname(__file__)
sys.path.insert(0, dir + '../helpers')

from game_engine import Game_Engine
import print_machine

class Puss_Mode(Game_Engine):
    def __init__(self, lives=5, chances=3):
        Game_Engine.__init__(self, lives=lives, chances=chances)

    def _start(self):
        print('ok')
