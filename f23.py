#!/usr/bin/env python
# Write f23() that takes a list of three lists of len 3, and returns who won in 
# tic-tac-toe (you can expect all moves to have been legal, made turn-by-turn)
# you can expect there is a winner. Print the x or o and the type of win:
# "col1", "col2", "row3", "falling_back_diag", "falling_front_diag" 
# Ex. of rows
# row1 = ["o","x",""]
# row2 = ["","x",""]
# row3 = ["o","x",""]
# Ex. of print: x, col2
###############################################################################


def f23(lists_):
    pass






###############################################################################


def main():
    print f23([["o","o","x"],["x","o","x"],["o","","x"]])
    print f23([["o","","o"],["x","o","x"],["o","x","x"]])
    print f23([["o","o","x"],["x","x","x"],["o","","o"]])

if __name__ == "__main__":
    main()