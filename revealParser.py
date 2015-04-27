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
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\21")
        buf.write("a\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\7\2\26\n\2\f\2\16\2\31\13\2\3")
        buf.write("\2\7\2\34\n\2\f\2\16\2\37\13\2\3\2\6\2\"\n\2\r\2\16\2")
        buf.write("#\3\2\3\2\3\2\3\3\3\3\3\3\3\3\7\3-\n\3\f\3\16\3\60\13")
        buf.write("\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\6\5;\n\5\r\5\16")
        buf.write("\5<\3\6\3\6\3\6\3\6\6\6C\n\6\r\6\16\6D\3\7\3\7\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\6\bP\n\b\r\b\16\bQ\3\b\7\bU\n\b\f")
        buf.write("\b\16\bX\13\b\3\t\3\t\3\n\6\n]\n\n\r\n\16\n^\3\n\2\2\13")
        buf.write("\2\4\6\b\n\f\16\20\22\2\6\3\2\3\4\5\2\t\t\13\13\r\r\3")
        buf.write("\2\t\n\5\2\t\t\13\13\17\17`\2\27\3\2\2\2\4(\3\2\2\2\6")
        buf.write("\63\3\2\2\2\b:\3\2\2\2\n>\3\2\2\2\fF\3\2\2\2\16H\3\2\2")
        buf.write("\2\20Y\3\2\2\2\22\\\3\2\2\2\24\26\5\n\6\2\25\24\3\2\2")
        buf.write("\2\26\31\3\2\2\2\27\25\3\2\2\2\27\30\3\2\2\2\30\35\3\2")
        buf.write("\2\2\31\27\3\2\2\2\32\34\5\16\b\2\33\32\3\2\2\2\34\37")
        buf.write("\3\2\2\2\35\33\3\2\2\2\35\36\3\2\2\2\36!\3\2\2\2\37\35")
        buf.write("\3\2\2\2 \"\5\4\3\2! \3\2\2\2\"#\3\2\2\2#!\3\2\2\2#$\3")
        buf.write("\2\2\2$%\3\2\2\2%&\7\2\2\3&\'\b\2\1\2\'\3\3\2\2\2()\5")
        buf.write("\6\4\2)*\7\20\2\2*.\5\b\5\2+-\7\20\2\2,+\3\2\2\2-\60\3")
        buf.write("\2\2\2.,\3\2\2\2./\3\2\2\2/\61\3\2\2\2\60.\3\2\2\2\61")
        buf.write("\62\b\3\1\2\62\5\3\2\2\2\63\64\t\2\2\2\64\65\5\22\n\2")
        buf.write("\65\66\b\4\1\2\66\7\3\2\2\2\678\5\22\n\289\7\20\2\29;")
        buf.write("\3\2\2\2:\67\3\2\2\2;<\3\2\2\2<:\3\2\2\2<=\3\2\2\2=\t")
        buf.write("\3\2\2\2>?\7\5\2\2?@\7\t\2\2@B\5\f\7\2AC\7\20\2\2BA\3")
        buf.write("\2\2\2CD\3\2\2\2DB\3\2\2\2DE\3\2\2\2E\13\3\2\2\2FG\t\3")
        buf.write("\2\2G\r\3\2\2\2HI\7\6\2\2IJ\7\t\2\2JO\7\20\2\2KL\5\20")
        buf.write("\t\2LM\5\f\7\2MN\7\20\2\2NP\3\2\2\2OK\3\2\2\2PQ\3\2\2")
        buf.write("\2QO\3\2\2\2QR\3\2\2\2RV\3\2\2\2SU\7\20\2\2TS\3\2\2\2")
        buf.write("UX\3\2\2\2VT\3\2\2\2VW\3\2\2\2W\17\3\2\2\2XV\3\2\2\2Y")
        buf.write("Z\t\4\2\2Z\21\3\2\2\2[]\t\5\2\2\\[\3\2\2\2]^\3\2\2\2^")
        buf.write("\\\3\2\2\2^_\3\2\2\2_\23\3\2\2\2\13\27\35#.<DQV^")
        return buf.getvalue()


class revealParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"'$'", u"'&'", 
                     u"'-'", u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"'\n'" ]

    symbolicNames = [ u"<INVALID>", u"SLIDE", u"SLIDE2", u"CONFIG", u"FORMAT", 
                      u"DASH", u"QUOTE", u"WORD", u"DASHWORD", u"ALPHANUM", 
                      u"LETTER", u"NUMBER", u"DIGIT", u"SYMBOL", u"NL", 
                      u"WS" ]

    RULE_slideshow = 0
    RULE_slide = 1
    RULE_title = 2
    RULE_body = 3
    RULE_config = 4
    RULE_option = 5
    RULE_formatting = 6
    RULE_setting = 7
    RULE_text = 8

    ruleNames =  [ "slideshow", "slide", "title", "body", "config", "option", 
                   "formatting", "setting", "text" ]

    EOF = Token.EOF
    SLIDE=1
    SLIDE2=2
    CONFIG=3
    FORMAT=4
    DASH=5
    QUOTE=6
    WORD=7
    DASHWORD=8
    ALPHANUM=9
    LETTER=10
    NUMBER=11
    DIGIT=12
    SYMBOL=13
    NL=14
    WS=15

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.5")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



        class Globals:
            def __init__(self):
            
                class Slideshow:
                    def __init__(self):
                        self.slides = []
                    def addSlide(self, slide):
                        slide.title = slide.title[1:]
                        if (slide.title[0] == '@'): # Is child
                            self.slides[-1].child = slide
                        else:
                            self.slides.append(slide)

                self.Slideshow = Slideshow
                self.slideshow = self.Slideshow()

                class Slide:
                    def __init__(self, title, body):
                        self.title = title
                        self.body = body
                        self.child = None
                self.Slide = Slide

            def printSlides(self):
                for slide in self.slideshow.slides:
                    print("{}:\n{}".format(slide.title, slide.body))
                    if slide.child:
                            print("\t{}:\n\t{}".format(slide.child.title, slide.child.body))
        self.globals = Globals()

        


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
            self.globals.printSlides()
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
            self.state = 38
            localctx.var_title = self.title()
            self.state = 39
            self.match(revealParser.NL)
            self.state = 40
            localctx.var_body = self.body()
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==revealParser.NL:
                self.state = 41
                self.match(revealParser.NL)
                self.state = 46
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.globals.slideshow.addSlide(self.globals.Slide((None if localctx.var_title is None else self._input.getText((localctx.var_title.start,localctx.var_title.stop))),(None if localctx.var_body is None else self._input.getText((localctx.var_body.start,localctx.var_body.stop)))))
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
            self.var_format = None # Token
            self.var_title = None # TextContext

        def text(self):
            return self.getTypedRuleContext(revealParser.TextContext,0)


        def SLIDE(self):
            return self.getToken(revealParser.SLIDE, 0)

        def SLIDE2(self):
            return self.getToken(revealParser.SLIDE2, 0)

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
            self.state = 49
            localctx.var_format = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==revealParser.SLIDE or _la==revealParser.SLIDE2):
                localctx.var_format = self._errHandler.recoverInline(self)
            else:
                self.consume()
            self.state = 50
            localctx.var_title = self.text()
            #System.out.println((None if localctx.var_title is None else self._input.getText((localctx.var_title.start,localctx.var_title.stop))))
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

        def text(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(revealParser.TextContext)
            else:
                return self.getTypedRuleContext(revealParser.TextContext,i)


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
            self.state = 56 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 53
                self.text()
                self.state = 54
                self.match(revealParser.NL)
                self.state = 58 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << revealParser.WORD) | (1 << revealParser.ALPHANUM) | (1 << revealParser.SYMBOL))) != 0)):
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

        def CONFIG(self):
            return self.getToken(revealParser.CONFIG, 0)

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
            self.state = 60
            self.match(revealParser.CONFIG)
            self.state = 61
            self.match(revealParser.WORD)
            self.state = 62
            self.option()
            self.state = 64 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 63
                self.match(revealParser.NL)
                self.state = 66 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==revealParser.NL):
                    break

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
            self.state = 68
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << revealParser.WORD) | (1 << revealParser.ALPHANUM) | (1 << revealParser.NUMBER))) != 0)):
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

        def FORMAT(self):
            return self.getToken(revealParser.FORMAT, 0)

        def WORD(self):
            return self.getToken(revealParser.WORD, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(revealParser.NL)
            else:
                return self.getToken(revealParser.NL, i)

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
            self.state = 70
            self.match(revealParser.FORMAT)
            self.state = 71
            self.match(revealParser.WORD)
            self.state = 72
            self.match(revealParser.NL)
            self.state = 77 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 73
                self.setting()
                self.state = 74
                self.option()
                self.state = 75
                self.match(revealParser.NL)
                self.state = 79 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==revealParser.WORD or _la==revealParser.DASHWORD):
                    break

            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==revealParser.NL:
                self.state = 81
                self.match(revealParser.NL)
                self.state = 86
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
            self.state = 87
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

    class TextContext(ParserRuleContext):

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

        def getRuleIndex(self):
            return revealParser.RULE_text

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, revealListener ):
                listener.enterText(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, revealListener ):
                listener.exitText(self)




    def text(self):

        localctx = revealParser.TextContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_text)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 89
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << revealParser.WORD) | (1 << revealParser.ALPHANUM) | (1 << revealParser.SYMBOL))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 92 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << revealParser.WORD) | (1 << revealParser.ALPHANUM) | (1 << revealParser.SYMBOL))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx




