grammar calculadora;

prog:   stat+ ;

stat:   expr NEWLINE                # printExpr
    |   ID '=' expr NEWLINE         # assign
    |   'for' ID 'in' expr 'to' expr ':' stat+ 'end' NEWLINE  # forStat
    |   'if' expr 'then' NEWLINE stat+ ('else' NEWLINE stat+)? 'end' NEWLINE  # ifStat
    |   'while' expr 'do' NEWLINE stat+ 'end' NEWLINE  # whileStat
    |   'print' expr NEWLINE        # print
    |   'def' ID '(' params? ')' ':' stat+ 'end' NEWLINE # functionDef
    |   ID '(' args? ')' NEWLINE    # functionCall
    |   NEWLINE                     # blank
    ;

params: ID (',' ID)* ;

expr:   ('!'+|'-') expr             # unary
    |   expr '++'                   # increment
    |   expr '--'                   # decrement
    |   expr op=('+'|'-') expr      # AddSub
    |   expr op=('*'|'/') expr      # MulDiv
    |   expr '**' expr              # Power
    |   expr ROOT expr              # Root
    |   expr '%' expr               # Mod
    |   expr op=('=='|'!='|'<'|'>'|'<='|'>=') expr  # comparison
    |   NOT expr                    # negacion
    |   BOOL                        # bool
    |   FLOAT                       # float
    |   INT                         # int
    |   STRING                      # string
    |   ID                          # id
    |   '(' expr ')'                # parens
    |   SEN '(' expr ')'            # sinFunction
    |   COS '(' expr ')'            # cosFunction
    |   TAN '(' expr ')'            # tanFunction
    |   matrix                      # matrixExpr
    |   expr '[' 'T' ']'            # transposeExpr
    |   expr '[' 'I' ']'            # inverseExpr
    |   expr '.' 'head' '(' ')'     # dataframeHead
    |   expr '.' 'mean' '(' ')'     # dataframeMean
    |   expr '.' 'describe' '(' ')' # dataframeDescribe
    |   expr '.' 'series' '(' expr ')'  # dataframeSeries
    |   expr '.' 'append' '(' expr ')'  # listAppend
    |   expr '.' 'remove' '(' expr ')'  # listRemove
    |   expr '.' 'index' '(' expr ')'   # listIndex
    |   expr '.' 'len' '(' ')'          # listLen
    |   expr '.' 'pop' '(' ')'          # listPop
    |	expr '.' 'get_key' '(' expr ')'  # getDictKey
    |	expr '.' 'get_value' '(' expr ')'  # getDictValue
    |	expr '.' 'add_entry' '(' expr ',' expr ')'  # addDictEntry
    |	expr '.' 'remove_entry' '(' expr ')'  # removeDictEntry
    |   expr '.' 'plot' '(' 'line' ')' # graficaLineas
    |   expr '.' 'plot' '(' 'bar' ')' # graficaBarras
    |   expr '.' 'plot' '(' 'scatter' ')' # graficaPuntos
    |   expr '.' 'plot' '(' 'hist' ')' # graficaHistograma
    |   expr '.' 'plot' '(' 'box' ')' # graficaCaja
    |   list                        # listExpr
    |   tupla                       # tupleExpr
    |   dicti                        # dictExpr
    |   dataframe                   # dataframeExpr
    |   'open' '(' expr ',' expr ')'  # openFile
    |   ID '.' 'write' '(' expr ')' # writeFile
    |   ID '.' 'writelines' '(' expr ')' #writelinesFile
    |   ID '.' 'read' '(' ')'         # readFile
    |   ID '.' 'delete' '(' ')'       # deleteFile
    |   ID '.' 'close'  '(' ')'       # closeFile
    |   expr '.' 'csv' '(' STRING ')'   # crearCsv
    |   ID '.' 'leer_csv' '(' STRING ')'  # leerCsv
    |   'return' expr                  # return
    |   'factorial' '(' INT ')'      # factorial
    |   'euclides' '(' expr ',' expr ')'  # euclidesFunction
    |   'repetida' '(' expr ')'       # repetida
    ;

matrix: '[' matrix_contents ']' ;

matrix_contents: row (',' row)* ;

row: '[' expr (',' expr)* ']' ;



list: '[' list_contents? ']' ;

tupla: '(' list_contents? ')' ;

list_contents: expr (',' expr)* ;

dicti: '{' dict_contents? '}' ;

dict_contents: dict_entry (',' dict_entry)* ;

dict_access: ID '[' ID ']' ;

dict_entry: expr ':' expr
          | expr '[' expr ']' ':' list ;



dataframe: 'DataFrame' '(' expr ')' ;


args: expr (',' expr)* ;

NOT: '!';
INCREMENT: '++';
DECREMENT: '--';

MUL :   '*' ;
DIV :   '/' ;
ADD :   '+' ;
SUB :   '-' ;
MOD :   '%' ;
ROOT:   '^' ;

EQ : '==' ;
NEQ: '!=' ;
LT : '<' ;
GT : '>' ;
LE : '<=' ;
GE : '>=' ;

TAN :   'tan' ;
COS :   'cos' ;
SEN :   'sen' ;
BOOL:   'true' | 'false' ;   // Coincide con booleanos
ID  :   [a-zA-Z]+ ;      // Coincide con identificadores
INT :   [0-9]+ ;         // Coincide con enteros
FLOAT:  [0-9]+ '.' [0-9]+ ;    // Coincide con flotantes
STRING: '"' .*? '"' ;         // Coincide con strings
NEWLINE:'\r'? '\n' ;     // Retorna nuevas líneas al analizador (es una señal de fin de declaración)
WS  :   [ \t]+ -> skip ; // Ignora los espacios en blanco
