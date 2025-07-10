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
    : fator (fator + sub_fator)*
    ;

sub_fator
    : (SQRT | POW | SUBIND)+ fator
    ;

fator
    : icognita
    | numero
    | funcao
    | IDENT
    | LBRACE sub_equation RBRACE
    ;

icognita
    : '-'? ICOG
    ;

numero
    : '-'? (NUM | INF)
    ;

funcao
    : funcao_nao_exp
    | funcao_exp (POW fator)? fator
    | derivada_parcial
    ;

funcao_nao_exp
    : limite
    | integral
    | derivada
    | torio
    ;

opfunc 
    : COS  
    | SIN   
    | TAN   
    | SEC   
    | CSC   
    | COT   
    | log   
    | LN 
    ;

log
    : LOG LBRACK fator RBRACK
    ;

limite
    : LIM LBRACK ICOG TENDER numero RBRACK fator
    ;

integral
    : INT LBRACK (sub_equation TO sub_equation)? RBRACK fator D_DIFF ICOG
    ;

derivada
    : DER LBRACK ICOG RBRACK fator
    ;

torio
    : (PROD | SUM) LBRACK ((equation TO)? sub_equation)? RBRACK fator
    ;

derivada_parcial
    : DER (POW fator)? LBRACK ICOG(POW fator)? RBRACK fator