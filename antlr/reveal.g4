grammar reveal;

options {
    language=Python3;
}

slideshow:  config* formatting* slide+ EOF;

slide:      var_title=title NL var_body=body NL*;

title:      var_type=(SLIDE | SLIDE2) SPACE+ var_string=string;
body:       (string NL)+;

config:     CONFIG var_option=WORD SPACE var_value=option NL*;
option:     WORD | ALPHANUM | NUMBER;

formatting: FORMAT var_name=WORD NL (var_setting=setting SPACE var_option=option NL)+ NL*;
setting:    DASHWORD | WORD;

string:     (WORD | ALPHANUM | SYMBOL | SPACE)+;

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

SPACE:      ' ';
WS:         [\t\r]+ -> skip;
