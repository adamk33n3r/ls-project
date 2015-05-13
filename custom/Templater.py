import os, shutil
from string import Template
class Templater(object):
    def __init__(self, slideshow, outFile = "index.html",baseHTML = "base.html", slideHTML = "slide.html", vSlideHTML = "vSlide.html"):
        self.currentDir = os.path.dirname(os.path.realpath(__file__))
        self.slideshow = slideshow
        self.outDir = "output"
        if os.path.exists(self.outDir):
            shutil.rmtree(self.outDir)
        shutil.copytree(os.path.join(self.currentDir, "reveal"), self.outDir)
        self.outFile = open(os.path.join(self.outDir, outFile), 'w')
        self.baseHTML  = open(os.path.join(self.currentDir, baseHTML)).read()
        self.slideHTML = open(os.path.join(self.currentDir, slideHTML)).read()
        self.vSlideHTML = open(os.path.join(self.currentDir, vSlideHTML)).read()

    def generate(self):
        print("Generating configuration...")
        configString = str(self.slideshow.config)
        configString = configString.replace("'true'", "true")
        configString = configString.replace("'false'", "false")

        print("Generating styling...")
        cssString = ""
        for selector, properties in self.slideshow.formatting.items():
            cssString += ".{} {{\n".format(selector)
            for property, value in properties.items():
                if property == 'bg':
                    cssString += "\t/* {}: {}; */\n".format(property, value)
                else:
                    cssString += "\t{}: {} !important;\n".format(property, value)
            cssString += "}\n"


        print("Generating slides...")
        slidesString = ""
        for slide in self.slideshow.slides:
            slidesString += self._createSlide(slide)
        outputString = Template(self.baseHTML).substitute(config = configString, css = cssString, slides = slidesString)
        self.outFile.write(outputString)
        self.outFile.close()

    def _createSlide(self, slide):
        bg = ""
        if slide.type in self.slideshow.formatting:
            if 'bg' in self.slideshow.formatting[slide.type]:
                bg = self.slideshow.formatting[slide.type]['bg']
        allSlides = Template(self.slideHTML).substitute(title = slide.title, body = slide.body, style = slide.type, bg = bg)
        if len(slide.children) > 0:
            for child in slide.children:
                bg = ""
                if child.type in self.slideshow.formatting:
                    if 'bg' in self.slideshow.formatting[child.type]:
                        bg = self.slideshow.formatting[child.type]['bg']
                allSlides += Template(self.slideHTML).substitute(title = child.title, body = child.body, style = child.type, bg = bg)
            allSlides = Template(self.vSlideHTML).substitute(slides = allSlides)
        return allSlides
