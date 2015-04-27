import sys
from antlr4 import *
from revealLexer import revealLexer
from revealParser import revealParser

def main(argv):
    input = FileStream(argv[1])
    lexer = revealLexer(input)
    stream = CommonTokenStream(lexer)
    parser = revealParser(stream)
    tree = parser.slideshow()


if __name__ == '__main__':
    main(sys.argv)
