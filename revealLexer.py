# Generated from java-escape by ANTLR 4.5
from antlr4 import *
from io import StringIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2\21")
        buf.write("c\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\3\2\3\2\3\2\5\2%\n\2\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\5\3-\n\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7")
        buf.write("\3\7\3\b\6\b8\n\b\r\b\16\b9\3\t\3\t\3\t\3\t\6\t@\n\t\r")
        buf.write("\t\16\tA\3\n\3\n\6\nF\n\n\r\n\16\nG\3\13\3\13\3\f\6\f")
        buf.write("M\n\f\r\f\16\fN\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\5\16Y\n\16\3\17\3\17\3\20\6\20^\n\20\r\20\16\20_\3\20")
        buf.write("\3\20\2\2\21\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13")
        buf.write("\25\f\27\r\31\16\33\17\35\20\37\21\3\2\6\4\2$$))\4\2C")
        buf.write("\\c|\f\2##%%\'\'*,..\60\61<>@A]`}\177\5\2\13\13\17\17")
        buf.write("\"\"o\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
        buf.write("\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2")
        buf.write("\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33")
        buf.write("\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\3$\3\2\2\2\5,\3\2\2")
        buf.write("\2\7.\3\2\2\2\t\60\3\2\2\2\13\62\3\2\2\2\r\64\3\2\2\2")
        buf.write("\17\67\3\2\2\2\21;\3\2\2\2\23E\3\2\2\2\25I\3\2\2\2\27")
        buf.write("L\3\2\2\2\31P\3\2\2\2\33X\3\2\2\2\35Z\3\2\2\2\37]\3\2")
        buf.write("\2\2!%\7B\2\2\"#\7B\2\2#%\5\23\n\2$!\3\2\2\2$\"\3\2\2")
        buf.write("\2%\4\3\2\2\2&\'\7B\2\2\'-\7B\2\2()\7B\2\2)*\7B\2\2*+")
        buf.write("\3\2\2\2+-\5\23\n\2,&\3\2\2\2,(\3\2\2\2-\6\3\2\2\2./\7")
        buf.write("&\2\2/\b\3\2\2\2\60\61\7(\2\2\61\n\3\2\2\2\62\63\7/\2")
        buf.write("\2\63\f\3\2\2\2\64\65\t\2\2\2\65\16\3\2\2\2\668\5\25\13")
        buf.write("\2\67\66\3\2\2\289\3\2\2\29\67\3\2\2\29:\3\2\2\2:\20\3")
        buf.write("\2\2\2;?\5\17\b\2<=\5\13\6\2=>\5\17\b\2>@\3\2\2\2?<\3")
        buf.write("\2\2\2@A\3\2\2\2A?\3\2\2\2AB\3\2\2\2B\22\3\2\2\2CF\5\17")
        buf.write("\b\2DF\5\27\f\2EC\3\2\2\2ED\3\2\2\2FG\3\2\2\2GE\3\2\2")
        buf.write("\2GH\3\2\2\2H\24\3\2\2\2IJ\t\3\2\2J\26\3\2\2\2KM\5\31")
        buf.write("\r\2LK\3\2\2\2MN\3\2\2\2NL\3\2\2\2NO\3\2\2\2O\30\3\2\2")
        buf.write("\2PQ\4\62;\2Q\32\3\2\2\2RY\t\4\2\2SY\5\13\6\2TY\5\r\7")
        buf.write("\2UY\5\t\5\2VY\5\7\4\2WY\5\3\2\2XR\3\2\2\2XS\3\2\2\2X")
        buf.write("T\3\2\2\2XU\3\2\2\2XV\3\2\2\2XW\3\2\2\2Y\34\3\2\2\2Z[")
        buf.write("\7\f\2\2[\36\3\2\2\2\\^\t\5\2\2]\\\3\2\2\2^_\3\2\2\2_")
        buf.write("]\3\2\2\2_`\3\2\2\2`a\3\2\2\2ab\b\20\2\2b \3\2\2\2\f\2")
        buf.write("$,9AEGNX_\3\b\2\2")
        return buf.getvalue()


class revealLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]


    SLIDE = 1
    SLIDE2 = 2
    CONFIG = 3
    FORMAT = 4
    DASH = 5
    QUOTE = 6
    WORD = 7
    DASHWORD = 8
    ALPHANUM = 9
    LETTER = 10
    NUMBER = 11
    DIGIT = 12
    SYMBOL = 13
    NL = 14
    WS = 15

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
            "'$'", "'&'", "'-'", "'\n'" ]

    symbolicNames = [ u"<INVALID>",
            "SLIDE", "SLIDE2", "CONFIG", "FORMAT", "DASH", "QUOTE", "WORD", 
            "DASHWORD", "ALPHANUM", "LETTER", "NUMBER", "DIGIT", "SYMBOL", 
            "NL", "WS" ]

    ruleNames = [ "SLIDE", "SLIDE2", "CONFIG", "FORMAT", "DASH", "QUOTE", 
                  "WORD", "DASHWORD", "ALPHANUM", "LETTER", "NUMBER", "DIGIT", 
                  "SYMBOL", "NL", "WS" ]

    grammarFileName = "reveal.g4"

    def __init__(self, input=None):
        super().__init__(input)
        self.checkVersion("4.5")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


