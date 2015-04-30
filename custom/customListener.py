from antlr.revealListener import revealListener

from custom.Slideshow import Slideshow
from custom.Slide import Slide

class CustomRevealListener(revealListener):

    def __init__(self, templaterClass):
        self.slideshow = Slideshow()
        self.templater = templaterClass(self.slideshow)

    # Exit a parse tree produced by revealParser#slideshow.
    def exitSlideshow(self, ctx):
        #print(self.slideshow.config)
        #print(self.slideshow.formatting)
        print("Done parsing slides")
        #self.slideshow.printSlides()
        print("Generating output...")
        self.templater.generate()


    # Enter a parse tree produced by revealParser#slide.
    def enterSlide(self, ctx):
        slideType = ctx.var_title.var_type.text
        slideTitle = ctx.var_title.var_string.getText()
        slideBody = ctx.var_body.getText()

        self.slideshow.addSlide(Slide(slideType, slideTitle, slideBody))

    # Enter a parse tree produced by revealParser#config.
    def enterConfig(self, ctx):
        option = ctx.var_option.text
        value = ctx.var_value.getText()
        self.slideshow.setConfig(option, value)

    # Enter a parse tree produced by revealParser#formatting.
    def enterFormatting(self, ctx):
        name = ctx.var_name.text
        for setting, option in zip(ctx.setting(), ctx.option()):
            self.slideshow.addFormatting(name, setting.getText(), option.getText())

    # Enter a parse tree produced by revealParser#setting.
    def enterSetting(self, ctx):
        self.currentSetting = ctx.getText()
