# Generated from java-escape by ANTLR 4.5
# encoding: utf-8
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .revealListener import revealListener
else:
    from revealListener import revealListener
def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\23")
        buf.write("e\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\7\2\26\n\2\f\2\16\2\31\13\2\3")
        buf.write("\2\7\2\34\n\2\f\2\16\2\37\13\2\3\2\6\2\"\n\2\r\2\16\2")
        buf.write("#\3\2\3\2\3\3\3\3\3\3\3\3\7\3,\n\3\f\3\16\3/\13\3\3\4")
        buf.write("\3\4\6\4\63\n\4\r\4\16\4\64\3\4\3\4\3\5\3\5\3\5\6\5<\n")
        buf.write("\5\r\5\16\5=\3\6\3\6\3\6\3\6\3\6\7\6E\n\6\f\6\16\6H\13")
        buf.write("\6\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\6\bT\n\b\r")
        buf.write("\b\16\bU\3\b\7\bY\n\b\f\b\16\b\\\13\b\3\t\3\t\3\n\6\n")
        buf.write("a\n\n\r\n\16\nb\3\n\2\2\13\2\4\6\b\n\f\16\20\22\2\6\3")
        buf.write("\2\3\4\5\2\t\t\13\f\16\16\3\2\t\n\6\2\t\t\f\f\20\20\22")
        buf.write("\22e\2\27\3\2\2\2\4\'\3\2\2\2\6\60\3\2\2\2\b;\3\2\2\2")
        buf.write("\n?\3\2\2\2\fI\3\2\2\2\16K\3\2\2\2\20]\3\2\2\2\22`\3\2")
        buf.write("\2\2\24\26\5\n\6\2\25\24\3\2\2\2\26\31\3\2\2\2\27\25\3")
        buf.write("\2\2\2\27\30\3\2\2\2\30\35\3\2\2\2\31\27\3\2\2\2\32\34")
        buf.write("\5\16\b\2\33\32\3\2\2\2\34\37\3\2\2\2\35\33\3\2\2\2\35")
        buf.write("\36\3\2\2\2\36!\3\2\2\2\37\35\3\2\2\2 \"\5\4\3\2! \3\2")
        buf.write("\2\2\"#\3\2\2\2#!\3\2\2\2#$\3\2\2\2$%\3\2\2\2%&\7\2\2")
        buf.write("\3&\3\3\2\2\2\'(\5\6\4\2()\7\21\2\2)-\5\b\5\2*,\7\21\2")
        buf.write("\2+*\3\2\2\2,/\3\2\2\2-+\3\2\2\2-.\3\2\2\2.\5\3\2\2\2")
        buf.write("/-\3\2\2\2\60\62\t\2\2\2\61\63\7\22\2\2\62\61\3\2\2\2")
        buf.write("\63\64\3\2\2\2\64\62\3\2\2\2\64\65\3\2\2\2\65\66\3\2\2")
        buf.write("\2\66\67\5\22\n\2\67\7\3\2\2\289\5\22\n\29:\7\21\2\2:")
        buf.write("<\3\2\2\2;8\3\2\2\2<=\3\2\2\2=;\3\2\2\2=>\3\2\2\2>\t\3")
        buf.write("\2\2\2?@\7\5\2\2@A\7\t\2\2AB\7\22\2\2BF\5\f\7\2CE\7\21")
        buf.write("\2\2DC\3\2\2\2EH\3\2\2\2FD\3\2\2\2FG\3\2\2\2G\13\3\2\2")
        buf.write("\2HF\3\2\2\2IJ\t\3\2\2J\r\3\2\2\2KL\7\6\2\2LM\7\t\2\2")
        buf.write("MS\7\21\2\2NO\5\20\t\2OP\7\22\2\2PQ\5\f\7\2QR\7\21\2\2")
        buf.write("RT\3\2\2\2SN\3\2\2\2TU\3\2\2\2US\3\2\2\2UV\3\2\2\2VZ\3")
        buf.write("\2\2\2WY\7\21\2\2XW\3\2\2\2Y\\\3\2\2\2ZX\3\2\2\2Z[\3\2")
        buf.write("\2\2[\17\3\2\2\2\\Z\3\2\2\2]^\t\4\2\2^\21\3\2\2\2_a\t")
        buf.write("\5\2\2`_\3\2\2\2ab\3\2\2\2b`\3\2\2\2bc\3\2\2\2c\23\3\2")
        buf.write("\2\2\f\27\35#-\64=FUZb")
        return buf.getvalue()


class revealParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"'$'", u"'&'", 
                     u"'-'", u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"'\n'", u"' '" ]

    symbolicNames = [ u"<INVALID>", u"SLIDE", u"SLIDE2", u"CONFIG", u"FORMAT", 
                      u"DASH", u"QUOTE", u"WORD", u"DASHWORD", u"COLOR", 
                      u"ALPHANUM", u"LETTER", u"NUMBER", u"DIGIT", u"SYMBOL", 
                      u"NL", u"SPACE", u"WS" ]

    RULE_slideshow = 0
    RULE_slide = 1
    RULE_title = 2
    RULE_body = 3
    RULE_config = 4
    RULE_option = 5
    RULE_formatting = 6
    RULE_setting = 7
    RULE_string = 8

    ruleNames =  [ "slideshow", "slide", "title", "body", "config", "option", 
                   "formatting", "setting", "string" ]

    EOF = Token.EOF
    SLIDE=1
    SLIDE2=2
    CONFIG=3
    FORMAT=4
    DASH=5
    QUOTE=6
    WORD=7
    DASHWORD=8
    COLOR=9
    ALPHANUM=10
    LETTER=11
    NUMBER=12
    DIGIT=13
    SYMBOL=14
    NL=15
    SPACE=16
    WS=17

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.5")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class SlideshowContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(revealParser.EOF, 0)

        def config(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(revealParser.ConfigContext)
            else:
                return self.getTypedRuleContext(revealParser.ConfigContext,i)


        def formatting(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(revealParser.FormattingContext)
            else:
                return self.getTypedRuleContext(revealParser.FormattingContext,i)


        def slide(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(revealParser.SlideContext)
            else:
                return self.getTypedRuleContext(revealParser.SlideContext,i)


        def getRuleIndex(self):
            return revealParser.RULE_slideshow

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, revealListener ):
                listener.enterSlideshow(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, revealListener ):
                listener.exitSlideshow(self)




    def slideshow(self):

        localctx = revealParser.SlideshowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_slideshow)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==revealParser.CONFIG:
                self.state = 18
                self.config()
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==revealParser.FORMAT:
                self.state = 24
                self.formatting()
                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 31 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 30
                self.slide()
                self.state = 33 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==revealParser.SLIDE or _la==revealParser.SLIDE2):
                    break

            self.state = 35
            self.match(revealParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SlideContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.var_title = None # TitleContext
            self.var_body = None # BodyContext

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(revealParser.NL)
            else:
                return self.getToken(revealParser.NL, i)

        def title(self):
            return self.getTypedRuleContext(revealParser.TitleContext,0)


        def body(self):
            return self.getTypedRuleContext(revealParser.BodyContext,0)


        def getRuleIndex(self):
            return revealParser.RULE_slide

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, revealListener ):
                listener.enterSlide(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, revealListener ):
                listener.exitSlide(self)




    def slide(self):

        localctx = revealParser.SlideContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_slide)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            localctx.var_title = self.title()
            self.state = 38
            self.match(revealParser.NL)
            self.state = 39
            localctx.var_body = self.body()
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==revealParser.NL:
                self.state = 40
                self.match(revealParser.NL)
                self.state = 45
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TitleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.var_type = None # Token
            self.var_string = None # StringContext

        def string(self):
            return self.getTypedRuleContext(revealParser.StringContext,0)


        def SLIDE(self):
            return self.getToken(revealParser.SLIDE, 0)

        def SLIDE2(self):
            return self.getToken(revealParser.SLIDE2, 0)

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(revealParser.SPACE)
            else:
                return self.getToken(revealParser.SPACE, i)

        def getRuleIndex(self):
            return revealParser.RULE_title

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, revealListener ):
                listener.enterTitle(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, revealListener ):
                listener.exitTitle(self)




    def title(self):

        localctx = revealParser.TitleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_title)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            localctx.var_type = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==revealParser.SLIDE or _la==revealParser.SLIDE2):
                localctx.var_type = self._errHandler.recoverInline(self)
            else:
                self.consume()
            self.state = 48 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 47
                    self.match(revealParser.SPACE)

                else:
                    raise NoViableAltException(self)
                self.state = 50 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

            self.state = 52
            localctx.var_string = self.string()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def string(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(revealParser.StringContext)
            else:
                return self.getTypedRuleContext(revealParser.StringContext,i)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(revealParser.NL)
            else:
                return self.getToken(revealParser.NL, i)

        def getRuleIndex(self):
            return revealParser.RULE_body

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, revealListener ):
                listener.enterBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, revealListener ):
                listener.exitBody(self)




    def body(self):

        localctx = revealParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 54
                self.string()
                self.state = 55
                self.match(revealParser.NL)
                self.state = 59 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << revealParser.WORD) | (1 << revealParser.ALPHANUM) | (1 << revealParser.SYMBOL) | (1 << revealParser.SPACE))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConfigContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.var_option = None # Token
            self.var_value = None # OptionContext

        def CONFIG(self):
            return self.getToken(revealParser.CONFIG, 0)

        def SPACE(self):
            return self.getToken(revealParser.SPACE, 0)

        def WORD(self):
            return self.getToken(revealParser.WORD, 0)

        def option(self):
            return self.getTypedRuleContext(revealParser.OptionContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(revealParser.NL)
            else:
                return self.getToken(revealParser.NL, i)

        def getRuleIndex(self):
            return revealParser.RULE_config

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, revealListener ):
                listener.enterConfig(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, revealListener ):
                listener.exitConfig(self)




    def config(self):

        localctx = revealParser.ConfigContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_config)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(revealParser.CONFIG)
            self.state = 62
            localctx.var_option = self.match(revealParser.WORD)
            self.state = 63
            self.match(revealParser.SPACE)
            self.state = 64
            localctx.var_value = self.option()
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==revealParser.NL:
                self.state = 65
                self.match(revealParser.NL)
                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OptionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLOR(self):
            return self.getToken(revealParser.COLOR, 0)

        def WORD(self):
            return self.getToken(revealParser.WORD, 0)

        def ALPHANUM(self):
            return self.getToken(revealParser.ALPHANUM, 0)

        def NUMBER(self):
            return self.getToken(revealParser.NUMBER, 0)

        def getRuleIndex(self):
            return revealParser.RULE_option

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, revealListener ):
                listener.enterOption(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, revealListener ):
                listener.exitOption(self)




    def option(self):

        localctx = revealParser.OptionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_option)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << revealParser.WORD) | (1 << revealParser.COLOR) | (1 << revealParser.ALPHANUM) | (1 << revealParser.NUMBER))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FormattingContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.var_name = None # Token
            self.var_setting = None # SettingContext
            self.var_option = None # OptionContext

        def FORMAT(self):
            return self.getToken(revealParser.FORMAT, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(revealParser.NL)
            else:
                return self.getToken(revealParser.NL, i)

        def WORD(self):
            return self.getToken(revealParser.WORD, 0)

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(revealParser.SPACE)
            else:
                return self.getToken(revealParser.SPACE, i)

        def setting(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(revealParser.SettingContext)
            else:
                return self.getTypedRuleContext(revealParser.SettingContext,i)


        def option(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(revealParser.OptionContext)
            else:
                return self.getTypedRuleContext(revealParser.OptionContext,i)


        def getRuleIndex(self):
            return revealParser.RULE_formatting

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, revealListener ):
                listener.enterFormatting(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, revealListener ):
                listener.exitFormatting(self)




    def formatting(self):

        localctx = revealParser.FormattingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_formatting)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(revealParser.FORMAT)
            self.state = 74
            localctx.var_name = self.match(revealParser.WORD)
            self.state = 75
            self.match(revealParser.NL)
            self.state = 81 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 76
                localctx.var_setting = self.setting()
                self.state = 77
                self.match(revealParser.SPACE)
                self.state = 78
                localctx.var_option = self.option()
                self.state = 79
                self.match(revealParser.NL)
                self.state = 83 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==revealParser.WORD or _la==revealParser.DASHWORD):
                    break

            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==revealParser.NL:
                self.state = 85
                self.match(revealParser.NL)
                self.state = 90
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SettingContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DASHWORD(self):
            return self.getToken(revealParser.DASHWORD, 0)

        def WORD(self):
            return self.getToken(revealParser.WORD, 0)

        def getRuleIndex(self):
            return revealParser.RULE_setting

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, revealListener ):
                listener.enterSetting(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, revealListener ):
                listener.exitSetting(self)




    def setting(self):

        localctx = revealParser.SettingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_setting)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            _la = self._input.LA(1)
            if not(_la==revealParser.WORD or _la==revealParser.DASHWORD):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StringContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(revealParser.WORD)
            else:
                return self.getToken(revealParser.WORD, i)

        def ALPHANUM(self, i:int=None):
            if i is None:
                return self.getTokens(revealParser.ALPHANUM)
            else:
                return self.getToken(revealParser.ALPHANUM, i)

        def SYMBOL(self, i:int=None):
            if i is None:
                return self.getTokens(revealParser.SYMBOL)
            else:
                return self.getToken(revealParser.SYMBOL, i)

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(revealParser.SPACE)
            else:
                return self.getToken(revealParser.SPACE, i)

        def getRuleIndex(self):
            return revealParser.RULE_string

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, revealListener ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, revealListener ):
                listener.exitString(self)




    def string(self):

        localctx = revealParser.StringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_string)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 93
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << revealParser.WORD) | (1 << revealParser.ALPHANUM) | (1 << revealParser.SYMBOL) | (1 << revealParser.SPACE))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 96 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << revealParser.WORD) | (1 << revealParser.ALPHANUM) | (1 << revealParser.SYMBOL) | (1 << revealParser.SPACE))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx




