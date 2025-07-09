parser grammar md_equationsParser;

options { tokenVocab = md_equationsLexer; }

document
    : (block | equationBlock)* EOF
    ;

block
    : (TEXT_CONTENT | SINGLE_DOLLAR)+
    ;

equationBlock
    : OPEN_DOLLAR (IDENT ATRIB)? equation CLOSE_DOLLAR
    ;

equation
    : sub_equation (COMP sub_equation)*
    ;

sub_equation
    : parem (OP parem)* 
    | div
    ;

div
    : LBRACE sub_equation DIV sub_equation RBRACE
    ;

parem
    : LPAREN sub_equation RPAREN 
    | parcela
    ;

parcela
    : (fator_uni)*
    ;

fator_uni
    : (SQRT | COS | SIN | TAN | SEC | CSC | COT | LOG | LN | POW | SUBIND)+ fator
    ;

fator
    : icognita
    | numero
    | func
    | IDENT
    | LBRACE sub_equation RBRACE
    ;

icognita
    : '-'? ICOG
    ;

numero
    : '-'? (NUM | INF)
    ;

func
    : limite
    | integral
    | derivada
    | torio
    ;

limite
    : LIM LBRACK ICOG TENDER numero RBRACK fator
    ;

integral
    : INT LBRACK (sub_equation VIRGULA sub_equation)? RBRACK fator D_DIFF ICOG
    ;

derivada
    : (DER | PDER) LBRACK ICOG RBRACK fator
    ;

torio
    : (PROD | SUM) LBRACK (sub_equation (VIRGULA sub_equation)?)? RBRACK fator
    ;