# RDBMS

This **Basic Relational Database Management System** will support data management, retrieval, and storage. Only `INSERT`, `SELECT`, and `DELETE` operations are allowed by the system. Consequently, query clauses will not be allowed, with the exception of the `WHERE` clause, which may contain up to two conditions (with the conditions concatenated using `AND` and `OR`).


## Parser (Antlr4)
### Building from Source
> antlr4 -Dlanguage=Python3 ./src/parser/SQL.g4

### Inspecting Parse Tree
> antlr4-parse ./src/parser/SQL.g4 sql_statement  -gui ./src/parser/tests/select.txt