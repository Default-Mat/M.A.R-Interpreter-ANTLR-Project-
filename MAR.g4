grammar MAR;

program: line+ EOF;
line: statement | ifBlock | whileBlock;
ifBlock: IF expression block (elseIfBlock | elseBlock)?;
elseIfBlock: ELSE IF expression block (elseIfBlock | elseBlock)?;
elseBlock: ELSE block;
whileBlock: WHILE expression block;
statement: (assignment | functionCall) SC;

assignment: ID EQUALL expression;
functionCall: ID OPP (expression (COMMA expression)*)? CLP;

expression
    : expression ADD term       #addExpression
    | expression SUB term       #subExpression
    | term                      #termExpression
    | expression compareOp expression       #compareExpression
    | expression boolOp expression          #boolExpression
    ;

term
    : term MUL power           #mulExpression
    | term DIV power           #divExpression
    | term MOD power           #modExpression
    | power                     #powerTerm
    ;

power
    : not POW power          #powerExpression
    | not                    #notPower
    ;

not
    : NOT not               #notExpression
    | factor                #factorNot
    ;

factor
    : OPP expression CLP        #paranthesesExpression
    | ID                        #identifierExpression
    | constant                  #constantExpression
    | functionCall              #functionCallExpression
    ;

constant: INTEGER | FLOAT | STRING | BOOL | NULL;
powerOp: POW;
mulOp: MUL | DIV | MOD;
addOp: ADD | SUB;
compareOp: RELOP;
boolOp: BOOL_OP;
block: OPCB line* CLCB;
fragment DIGIT: [0-9];
fragment LETTER: [A-Za-z];

WS: (' ' | '\t' | '\n' | '\r')+ -> skip;
INTEGER: DIGIT+;
FLOAT: (DIGIT+)'.'(DIGIT*);
STRING: '"' .*? '"';
BOOL: 'true' | 'false';
NULL: 'null';
IF: 'if';
ELSE: 'else';
FOR: 'for';
WHILE: 'while';
BOOL_OP: 'and' | 'or';
ID: (LETTER)+(LETTER | DIGIT | '_')*;
NOT: '!';
OPP: '(';
CLP: ')';
COMMA: ',';
EQUALL: '=';
OPCB: '{';
CLCB: '}';
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
POW: '^';
MOD: '%';
RELOP: '<' | '>' | '<=' | '>=' | '==' | '!=' ;
SC: ';';
