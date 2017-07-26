import sys
from termcolor import colored, cprint

def resolve(msg, level):
    if level is 0:
        return __success(msg)
    elif level is 1:
        return __alert(msg)
    elif level is 2:
        return __error(msg)
    elif level is 3:
        return __fluffy(msg)

def __success(msg):
    return colored(msg, 'green', attrs=['bold'])
def __alert(msg):
    return colored(msg, 'yellow', attrs=['bold'])
def __error(msg):
    return colored(msg, 'red', attrs=['bold'])
def __fluffy(msg):
    return colored(msg, 'magenta', attrs=['bold'])

# class Print_Machine:
#     def __init__(self, msg, level):
#         self.__msg = msg
#         self.resolve(level)
