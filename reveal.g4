grammar reveal;

options {
    language=Python3;
}

slideshow:  config* formatting* slide+ EOF {# slideshow};

slide:      var_title=title {# var_title}NL var_body=body NL* {# var_body};

title:      var_format=(SLIDE | SLIDE2) {# var_format} var_title=text {# var_title};
body:       (text NL)+ {# body};

config:     CONFIG WORD option {#config > option} NL+ {# config};
option:     WORD | ALPHANUM | NUMBER {# option};

formatting: FORMAT WORD NL (setting option NL)+ NL* {# formatting};
setting:    DASHWORD | WORD {# setting};

text:       (WORD | ALPHANUM | SYMBOL)+ {# text};

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
