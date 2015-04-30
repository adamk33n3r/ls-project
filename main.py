#!/usr/bin/env python3

import sys
from antlr4 import *
from antlr.revealLexer import revealLexer
from antlr.revealParser import revealParser
from custom.customListener import CustomRevealListener

from custom.Templater import Templater

def main(argv):
    if len(argv) < 2:
        print("Must pass file to be parsed")
        return
    try:
        inFile = FileStream(argv[1])
    except FileNotFoundError:
        print("File ({}) not found".format(argv[1]))
        return
    lexer = revealLexer(inFile)
    stream = CommonTokenStream(lexer)
    parser = revealParser(stream)
    print("Parsing...")
    tree = parser.slideshow()

    reveal = CustomRevealListener(Templater)
    walker = ParseTreeWalker()
    print("Walking tree to build data structure...")
    walker.walk(reveal, tree)



if __name__ == '__main__':
    main(sys.argv)
