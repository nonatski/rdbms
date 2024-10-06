import antlr4
from antlr4 import *
import sys
import os
import pprint

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(os.path.join(dir_path, os.pardir)))

from SQLAnnotate import SQLAnnotate
from schemas.samples.Students import Students

def main(argv):
    inputStream = antlr4.InputStream(argv[1])
    sqlAnnotate = SQLAnnotate(sql = inputStream, schema = Students)
    sqlAnnotate.annotate()

    results = sqlAnnotate.getAnnotations()

    if '--pretty' in argv:
        pprint.PrettyPrinter(indent=1).pprint(results)
    else:
        print(results)
    
if __name__ == '__main__':
    main(sys.argv)