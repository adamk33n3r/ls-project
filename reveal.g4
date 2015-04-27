grammar reveal;

options {
    language=Python3;
}

@parser::members {
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

    
}

slideshow:  config* formatting* slide+ EOF {self.globals.printSlides()};

slide:      var_title=title NL var_body=body NL* {self.globals.slideshow.addSlide(self.globals.Slide($var_title.text,$var_body.text))};

title:      var_format=(SLIDE | SLIDE2) var_title=text {#System.out.println($var_title.text)};
body:       (text NL)+;

config:     CONFIG WORD option NL+;
option:     WORD | ALPHANUM | NUMBER;

formatting:     FORMAT WORD NL (setting option NL)+ NL*;
setting:    DASHWORD | WORD;

text:       (WORD | ALPHANUM | SYMBOL)+;

SLIDE:      '@' | '@' ALPHANUM;
SLIDE2:     '@@' | '@@' ALPHANUM;
CONFIG:     '$';
FORMAT:     '&';
DASH:       '-';
QUOTE:      '\'' | '"';
WORD:       LETTER+;
DASHWORD:   WORD (DASH WORD)+;
ALPHANUM:   (WORD | NUMBER)+;
LETTER:     'a'..'z' | 'A'..'Z';
NUMBER:     DIGIT+;
DIGIT:      '0'..'9';
SYMBOL:     [,.!#%^*()[\]{}\\|<>/?;:] | DASH | QUOTE | FORMAT | CONFIG | SLIDE;
NL:         '\n';

WS:         [ \t\r]+ -> skip;
