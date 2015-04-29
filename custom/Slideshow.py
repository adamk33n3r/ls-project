class Slideshow(object):
    def __init__(self):
        self.config = {}
        self.formatting = {}
        self.slides = []

    def setConfig(self, option, value):
        self.config[option] = value

    def addFormatting(self, name, option, value):
        if name not in self.formatting:
            self.formatting[name] = {}
        self.formatting[name][option] = value

    def addSlide(self, slide):
        slide.type = slide.type[1:]
        if len(slide.type) > 0:
            if slide.type[0] == '@': # Is child
                if len(self.slides) == 0:
                    raise Exception("No slides to become a child of")
                else:
                    self.slides[-1].children.append(slide)
            else:
                self.slides.append(slide)
        else:
            slide.type = None
            self.slides.append(slide)

    def printSlides(self):
        for slide in self.slides:
            #print("{}:\n{}".format(slide.title, slide.body))
            print(slide)
            for child in slide.children:
                print("\t{}:\n\t{}".format(child.title, child.body))

