from os import *

class console:
    @staticmethod
    def clear():
        system('cls' if name == 'nt' else 'clear')

    @staticmethod
    def pause():
        system('pause')
