from antlr4 import *
import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(os.path.join(dir_path, os.pardir)))

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
