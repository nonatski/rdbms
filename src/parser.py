from antlr4 import *
from SQLLexer import SQLLexer
from SQLParser import SQLParser

def parse_sql(sql_query):
    input_stream = InputStream(sql_query)
    lexer = SQLLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SQLParser(stream)
    tree = parser.sql_statement()
    print(tree.toStringTree(recog=parser))

# Example SQL query
query = "insert into student (studno, birthday) values ('hello', 1);"
query = query.lower()
parse_sql(query)
