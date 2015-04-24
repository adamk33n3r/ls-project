grammar reveal;

@parser::members {
    int lineNumber = 0, expNumber = 1;
    class Slide {
        public String title, body;
        public Slide(String title, String body) {
            this.title = title;
            this.body = body;
        }
    }
    java.util.LinkedList<Slide> slides = new java.util.LinkedList<Slide>();
    private void incrementLineNumber() {
        this.lineNumber++;
    }
    private void printSlides() {
        for (Slide slide : slides)
            System.out.println(String.format("%s:\n%s", slide.title, slide.body));
    }
}

slideshow:  config* format* slide+ EOF { printSlides(); };

slide:      var_title=title NL var_body=body NL* { slides.push(new Slide($var_title.text,$var_body.text)); };

title:      var_format=(SLIDE | SLIDE2) var_title=text { /*System.out.println($var_title.text);*/ };
body:       (text NL)+;

config:     CONFIG WORD option NL+;
option:     WORD | ALPHANUM | NUMBER;

format:     FORMAT WORD NL (setting option NL)+ NL*;
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
