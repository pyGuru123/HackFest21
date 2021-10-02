"""
Use Patterns.Alphabets_pattern file from the current project
which contains printer logic such as printA, printB, etc functions

These functions have been mapped with the printer alphabets
which will print out the given input by the user
"""
from Patterns.Alphabets_pattern import *

characters = 'abcdefghijklmnopqrstuvwxyz'
text = input('Enter what you want to print:\n').lower()
for character in text:
    if character == 'a':
        printA(character)
    elif character == 'b':
        printB(character)
    elif character == 'c':
        printC(character)
    elif character == 'd':
        printD(character)
    elif character == 'e':
        printE(character)
    elif character == 'f':
        printF(character)
    elif character == 'g':
        printG(character)
    elif character == 'h':
        printH(character)
    elif character == 'i':
        printI(character)
    elif character == 'j':
        printJ(character)
    elif character == 'k':
        printK(character)
    elif character == 'l':
        printL(character)
    elif character == 'm':
        printM(character)
    elif character == 'n':
        printN(character)
    elif character == 'o':
        printO(character)
    elif character == 'p':
        printP(character)
    elif character == 'q':
        printQ(character)
    elif character == 'r':
        printR(character)
    elif character == 's':
        printS(character)
    elif character == 't':
        printT(character)
    elif character == 'u':
        printU(character)
    elif character == 'v':
        printV(character)
    elif character == 'w':
        printW(character)
    elif character == 'x':
        printX(character)
    elif character == 'y':
        printY(character)
    elif character == 'z':
        printZ(character)
