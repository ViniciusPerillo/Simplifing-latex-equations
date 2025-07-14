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
    : parcela (operator parcela)* 
    ;

operator
    : PLUS_MINUS
    | PLUS
    | MINUS
    | MUL
    | DIV
    ;

sub_equation_brac
    : LPAREN sub_equation RPAREN
    | MOD sub_equation MOD
    ;

parcela
    : (sub_fator)+
    ;

sub_fator
    : (SQRT | POW | SUBIND) apply_func
    | fator FAT
    | MINUS? fator
    ;

fator
    : ICOG
    | numero
    | div
    | funcao
    | sub_equation_brac
    | IDENT
    ;

numero
    : NUM | INF 
    ;

div
    : LBRACE sub_equation DIV sub_equation RBRACE
    ;

funcao
    : funcao_nao_exp
    | funcao_exp (POW fator)? apply_func
    | derivada_parcial
    ;

funcao_nao_exp
    : limite
    | integral
    | derivada
    | torio
    ;

funcao_exp 
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
    : LOG (LBRACK apply_func RBRACK)?
    ;

limite
    : LIM LBRACK ICOG TENDER numero RBRACK apply_func
    ;

integral
    : INT (LBRACK sub_equation ATE sub_equation RBRACK)? apply_func D_DIFF ICOG
    ;

derivada
    : DER LBRACK ICOG RBRACK apply_func
    ;

torio
    : (PROD | SUM) (LBRACK equation (ATE sub_equation)? RBRACK)? apply_func
    ;

derivada_parcial
    : PDER (POW fator)? LBRACK ICOG(POW fator)? RBRACK apply_func
    ;

apply_func
    : fator
    | LBRACE sub_equation RBRACE
    ;