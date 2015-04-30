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
        slidesString = ""
        for slide in self.slideshow.slides:
            slidesString += self._createSlide(slide)
        outputString = Template(self.baseHTML).substitute(config = str(self.slideshow.config), slides = slidesString)
        self.outFile.write(outputString)
        self.outFile.close()

    def _createSlide(self, slide):
        if len(slide.children) > 0:
            slides = Template(self.slideHTML).substitute(title = slide.title, body = slide.body)
            for child in slide.children:
                slides += Template(self.slideHTML).substitute(title = child.title, body = child.body)
            return Template(self.vSlideHTML).substitute(slides = slides)
        else:
            return Template(self.slideHTML).substitute(title = slide.title, body = slide.body)
