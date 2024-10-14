import antlr4
import sys
import os
import pprint
from antlr4 import *

dir_path = os.path.dirname(os.path.realpath(__file__))

# manual access to schema directory
sys.path.append(os.path.abspath(os.path.join(dir_path,  '../../' +  os.pardir)))
from schemas.samples.Students import Students

# restore parent directory path
sys.path.append(os.path.abspath(os.path.join(dir_path, os.pardir)))

from compiler.analyzer.SQLAnnotate import SQLAnnotate
from compiler.generator.IntermediateCodeGenerator import IntermediateCodeGenerator
from compiler.optimizer.SQLQueryTreeTransformer import SQLQueryTreeTransformer

if __name__ == '__main__':
    inputStream = antlr4.InputStream(sys.argv[1])
    sqlAnnotate = SQLAnnotate(sql = inputStream, schema = Students)
    sqlAnnotate.annotate()
    annotations = sqlAnnotate.getAnnotations()

    code = IntermediateCodeGenerator (annotations)
    queryTree = code.generate().reverse().getResults()

    # feed the query plan to optimer to generate possible queries
    # NOTE: the current transformer do nothing as of the moment
    queryTreeTransformer = SQLQueryTreeTransformer (queryTree)
    transformedTree = queryTreeTransformer.transform ()
    print(transformedTree)