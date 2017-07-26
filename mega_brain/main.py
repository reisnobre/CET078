import sys
import os
dir = os.path.dirname(__file__)
sys.path.insert(0, dir + './game_engine')
sys.path.insert(0, dir + './helpers')

import print_machine
from puss_mode import Puss_Mode
from iron_man import Iron_Man
from src_of_expressions import Source_Of_Expressions

expressions = Source_Of_Expressions()
def menu():
    print(print_machine.resolve(msg='**________________***________________**\n', level=1))
    print(print_machine.resolve(msg='Escolha um nível de Jogo\n', level=0))
    print(print_machine.resolve(msg='1. Iron Man\n2. Puss Mode\n3. Sair', level=2))
    return int(input())

def start():
    print(print_machine.resolve(msg='Bem vindo ao Mega Mind\n', level=1))
    ctrl = menu()
    while (ctrl is not 3):
        load_game(ctrl)
        ctrl = menu()

def load_game(level=1):
    if level is 1:
        print(print_machine.resolve(msg='______________________\n', level=1))
        print(print_machine.resolve(msg='Let the Games Begin!\n', level=2))
        ge = Iron_Man()
    else:
        print(print_machine.resolve(msg='______________________\n', level=1))
        print(print_machine.resolve(msg='Bem vindo a terra dos Unicórnios!\n', level=3))
        ge = Iron_Man()

def end(status):
    print("Até a proxima")

start()
# print(colored('grey', 'grey', attrs=['bold']))
# print(colored('red', 'red', attrs=['bold']))
# print(colored('green', 'green', attrs=['bold']))
# print(colored('yellow', 'yellow', attrs=['bold']))
# print(colored('blue', 'blue', attrs=['bold']))
# print(colored('magenta', 'magenta', attrs=['bold']))
# print(colored('cyan', 'cyan', attrs=['bold']))
# print(colored('white', 'white', attrs=['bold']))
