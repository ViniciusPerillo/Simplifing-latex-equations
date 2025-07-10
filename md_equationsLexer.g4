lexer grammar md_equationsLexer;

OPEN_DOLLAR    : '$$' -> pushMode(EQUATION_MODE);
SINGLE_DOLLAR  : '$' ;
TEXT_CONTENT   : ~[$]+ ; 

mode EQUATION_MODE;
    CLOSE_DOLLAR : '$$' -> popMode;
    WS           : [ \t\n\r]+ -> skip;
    COMMENT      : '<!--' .*? '>' -> skip;
    
    // Brackets & Operators
    LBRACK  : '[' ;
    RBRACK  : ']' ;
    LBRACE  : '{' ;
    RBRACE  : '}' ;
    LPAREN  : '(' ;
    RPAREN  : ')' ;
    COMP    : '=' | '>=' | '<=' | '~' | '==' | '+-' | '!=' ;
    DIV     : '/';
    MINUS   : '-';
    OP      : '+' | MINUS | '*' | DIV ;
    VIRGULA : ';' ;
    TENDER  : '->' ;
    ATE     : 'to';
    ATRIB   : '<-' ;
    FAT     : '!' ;
    INF     : 'inf' ;
    MOD     : '|';
    
    // Functions & Operators
    SQRT  : 'sqrt' ;
    COS   : 'cos' ;
    SIN   : 'sin' ;
    TAN   : 'tan' ;
    SEC   : 'sec' ;
    CSC   : 'csc' ;
    COT   : 'cot' ;
    LOG   : 'log' ;
    LN    : 'ln' ;
    LIM   : 'lim' ;
    INT   : 'int' ;
    DER   : 'der' ;
    PDER  : 'pder' ;
    SUM   : 'sum' ;
    PROD  : 'prod' ;
    POW   : '^' ;
    SUBIND: '_' ;
    D_DIFF: 'd' ;  
    
    // Literals
    NUM  : [0-9]+ (',' [0-9]+)? ;
    ICOG : [a-zA-Z] | 'alpha' | 'beta' | 'gamma' | 'delta' | 'Delta' | 'epsilon' | 'zeta' | 'eta' | 'theta'
       | 'iota' | 'kappa' | 'lambda' | 'mu' | 'nu' | 'xi' | 'pi' | 'rho' | 'sigma' | 'tau'
       | 'upsilon' | 'phi' | 'chi' | 'psi' | 'omega' | 'Omega' | 'nabla' ;          
    IDENT: '('[a-zA-Z_][a-zA-Z0-9_]* ')' ; 