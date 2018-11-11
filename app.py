"""
    TicTacToeParser
    Copyright(C) Simon Raichl 2018
    MIT License
"""


from core import Core

again = None
while again is None or again == "y":
    print(Core().get_board())
    again = input("Again? Y/N\n").lower()
