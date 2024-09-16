# RDBMS
Basic Relational Database Management System


## Parser (Antlr4)
### Build from Source
> antlr4 -Dlanguage=Python3 ./src/parser/SQL.g4

### Inspecting Parse Tree
> antlr4-parse ./src/parser/SQL.g4 sql_statement  -gui ./src/parser/tests/select.txt