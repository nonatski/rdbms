import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(os.path.join(dir_path, os.pardir)))

class SQLQueryTreeTransformer:
    def __init__ (self, queryTree):
        self.queries         =      []
        self.queryTree       =      queryTree
    
    def transform (self):
        if 'data' in self.queryTree:
            self.queries.append (self.queryTree['data'])

        return { 'trees' : self.queries }