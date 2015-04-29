from antlr.revealListener import revealListener

from custom.Slideshow import Slideshow
from custom.Slide import Slide

class CustomRevealListener(revealListener):

    def __init__(self):
        self.slideshow = Slideshow()

    # Enter a parse tree produced by revealParser#slideshow.
    def enterSlideshow(self, ctx):
        print("Parsing...")

    # Exit a parse tree produced by revealParser#slideshow.
    def exitSlideshow(self, ctx):
        print(self.slideshow.config)
        print(self.slideshow.formatting)
        print("Final slides")
        self.slideshow.printSlides()


    # Enter a parse tree produced by revealParser#slide.
    def enterSlide(self, ctx):
        slideType = ctx.var_title.var_type.text
        slideTitle = ctx.var_title.var_string.getText()
        slideBody = ctx.var_body.getText()

        self.slideshow.addSlide(Slide(slideType, slideTitle, slideBody))

    # Exit a parse tree produced by revealParser#slide.
    def exitSlide(self, ctx):
        pass


    # Enter a parse tree produced by revealParser#title.
    def enterTitle(self, ctx):
        pass

    # Exit a parse tree produced by revealParser#title.
    def exitTitle(self, ctx):
        pass


    # Enter a parse tree produced by revealParser#body.
    def enterBody(self, ctx):
        pass

    # Exit a parse tree produced by revealParser#body.
    def exitBody(self, ctx):
        pass


    # Enter a parse tree produced by revealParser#config.
    def enterConfig(self, ctx):
        option = ctx.var_option.text
        value = ctx.var_value.getText()
        self.slideshow.setConfig(option, value)

    # Exit a parse tree produced by revealParser#config.
    def exitConfig(self, ctx):
        pass


    # Enter a parse tree produced by revealParser#option.
    def enterOption(self, ctx):
        pass

    # Exit a parse tree produced by revealParser#option.
    def exitOption(self, ctx):
        pass


    # Enter a parse tree produced by revealParser#formatting.
    def enterFormatting(self, ctx):
        name = ctx.var_name.text
        for setting, option in zip(ctx.setting(), ctx.option()):
            self.slideshow.addFormatting(name, setting.getText(), option.getText())

    # Exit a parse tree produced by revealParser#formatting.
    def exitFormatting(self, ctx):
        pass


    # Enter a parse tree produced by revealParser#setting.
    def enterSetting(self, ctx):
        self.currentSetting = ctx.getText()

    # Exit a parse tree produced by revealParser#setting.
    def exitSetting(self, ctx):
        pass


    # Enter a parse tree produced by revealParser#text.
    def enterString(self, ctx):
        pass

    # Exit a parse tree produced by revealParser#text.
    def exitString(self, ctx):
        pass

