#!/usr/bin/env python3

import sys
from antlr4 import *
from antlr.revealLexer import revealLexer
from antlr.revealParser import revealParser
from custom.customListener import CustomRevealListener

def main(argv):
    input = FileStream(argv[1])
    lexer = revealLexer(input)
    stream = CommonTokenStream(lexer)
    parser = revealParser(stream)
    tree = parser.slideshow()

    reveal = CustomRevealListener()
    walker = ParseTreeWalker()
    walker.walk(reveal, tree)


if __name__ == '__main__':
    main(sys.argv)
