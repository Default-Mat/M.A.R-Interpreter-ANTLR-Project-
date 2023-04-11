grammar MAR;

program: line+ EOF;
line: statement | ifBlock | whileBlock;
ifBlock: IF expression block (ELSE block)?;
whileBlock: WHILE expression block;
statement: (assignment | functionCall) SC;
assignment: ID EQUALL expression;
functionCall: ID OPP (expression (COMMA expression)*)? CLP;
expression:
    constant |
    ID |
    expression mulOp expression |       #mulExpression
    expression addOp expression |
    expression compareOp expression |
    expression boolOp expression
;
constant: INTEGER | FLOAT | STRING | BOOL | NULL;
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
MOD: '%';
RELOP: '<' | '>' | '<=' | '>=' | '==' | '!=' ;
SC: ';';