grammar SQL;

// parser rules
sql_statement: (select_statement | delete_statement | insert_statement) SEMICOLON EOF;

select_statement: SELECT column_list FROM table where_clause?;
delete_statement: DELETE FROM table where_clause?;
insert_statement: INSERT INTO table insert_column_list? VALUES values_list;

column_list: '*' | column (',' column)*;
values_list: '('value (',' value)*')';
insert_column_list: '('column (',' column)*')';

where_clause: WHERE condition;
condition: expression | expression AND expression | expression OR expression;

expression: column operator value;

column: 'studno' | 'studentname' | 'birthday' | 'degree' | 'major' | 'unitsearned' | 'description' | 'action' | 'datefiled' | 'dateresolved' | 'cno' | 'ctitle' | 'cdesc' | 'noofunits' | 'haslab' | 'semoffered' | 'semester' | 'acadyear' | 'section' | 'time' | 'maxstud';
table: 'student' | 'studenthistory' | 'course' | 'courseoffering' | 'studcourse';
value: STRING | NUMBER;

operator: '=' | '!=' | '<' | '>' | '<=' | '>=';

// lexer rules
SELECT: 'select';
FROM: 'from';
WHERE: 'where';
AND: 'and';
OR: 'or';
SEMICOLON: ';';
DELETE: 'delete';
INSERT: 'insert';
INTO: 'into';
VALUES: 'values';

NUMBER: [0-9]+;
STRING: '\'' .*? '\'';

WS: [ \t\n\r]+ -> skip;
