# Generated from ./src/parser/SQL.g4 by ANTLR 4.13.2
from antlr4 import *
import pprint

if "." in __name__:
    from .SQLParser import SQLParser
else:
    from SQLParser import SQLParser

# This class defines a complete generic visitor for a parse tree produced by SQLParser.

class SQLVisitor(ParseTreeVisitor):

    def __init__(self):
        super().__init__()
        self.schema = None
        self.errors = []
        self.annotations = {}
        self.debug = False

    def loadSchema (self, Schema):
        if Schema != None:
            self.schema = Schema()
    
    def debugData (self, data, query = ''):
        if data and self.debug:
            print("\r\n---------ORIGINAL QUERY--------------------")
            print(f"({query})")
            print("-------------------------------------------\r\n")
            print("---------DEBUG START-----------------------")
            pprint.PrettyPrinter(indent=1).pprint(data)
            print('---------DEBUG END-------------------------')
    
    def setDebug (self, allowDebug = False):
        if allowDebug:
            self.debug = True
        else:
            self.debug = False
        
        return self

    # Visit a parse tree produced by SQLParser#sql_statement.
    def visitSql_statement(self, ctx:SQLParser.Sql_statementContext):
        select_statement = ctx.select_statement ()
        delete_statement = ctx.delete_statement()

        select_list_nodes = []
        delete_list_nodes = []

        # select statement
        if isinstance(select_statement, list):
            for select in select_statement:
                select_list_nodes.append(self.visit(select))
        else:
            select_list_nodes.append(self.visit(select_statement))
        
        # delete statement
        if isinstance(delete_statement, list):
            for delete in delete_statement:
                delete_list_nodes.append(self.visit(delete))
        else:
            delete_list_nodes.append(self.visit(delete_statement))
                        
        return {
            'select_statement'  :   select_list_nodes,
            'delete_statement'  :   delete_statement
        }


    # Visit a parse tree produced by SQLParser#select_statement.
    def visitSelect_statement(self, ctx:SQLParser.Select_statementContext):
        select_tables = ctx.table_list()
        select_columns = ctx.column_list ()
        where_clause = ctx.where_clause ()

        table_list_nodes = []
        column_list_nodes = []
        select_list_nodes = []
        where_list_nodes = []

        table_list_name = []
   
        
        # list tables
        if isinstance(select_tables, list):
            for select in select_tables:
                table_list_nodes.append(self.visit(select))
        else:
            table_list_nodes.append(self.visit(select_tables))


        # list of columns
        if isinstance(select_columns, list):
            
            for columns in select_columns:
                column_list_nodes.append(self.visit(columns))
        else:
            column_list_nodes.append(self.visit(select_columns))
        
        # get all VALID table names in string and push to list        
        for tb in table_list_nodes:
            for name in tb:
                if tb[name]['valid']:
                    table_list_name.append(name)

        # get all columns
        for cl in column_list_nodes:
            for name in cl:       
                # use cl[name]["name"] instead of name since the namee field might contain different
                # format such as table.column
                if cl[name]["type"] == "string":
                    cl[name]["error"] = None
                    cl[name]["valid"] = True

                if cl[name]["type"] == "table":
                    if ("tableName" and "columnName") in cl[name]:
                        tableName = cl[name]["tableName"]
                        columnName = cl[name]["columnName"]
                        
                        if self.schema.isTableExists (tableName):
                            if self.schema.isColumnExists (tableName, columnName):
                               if tableName in table_list_name:
                                    #print(name, '------')
                                    cl[name]["error"] = f"Column name {name} does not exists in {tableName}"
                                    cl[name]["valid"] = False   
                                    cl[name]["error"] = None
                                    cl[name]["valid"] = True
   
                if cl[name]["type"] == "column":
                    # get all fields in database if * is given
                    if not cl[name]['name'] == '*':
                        existsInTables = []
                        
                        for tl in table_list_name:
                            if self.schema.isColumnExists (tl, name):
                                    # convert regular columName to table.columnName format to allow
                                    # matching of parent columns to the columns of its subquery
                                    cl[name]["name"] = f"{tl}.{name}"
                                    cl[name]["tableName"] = f"{tl}"
                                    cl[name]["columnName"] = f"{name}"
                                    existsInTables.append(tl)
                            else:
                                cl[name]["error"] = f"Column name {name} does not exists in {tl}"
                                cl[name]["valid"] = False
                        
                        # if the column name exists in multiple tables, it is considered ambigous
                        # unless the tableName is explicitely specified
                        # SELECT id FROM student_info, enrollment
                        if len (existsInTables) > 1:
                            cl[name]["error"] = f"Column name {name} is ambigous"
                            cl[name]["valid"] = False
                    
                    else:
                        # get all fields from the database
                        # SELECT * from database
                        newColumnList = []

                        for table in table_list_nodes:
                            for name in table:
                                if table[name]['valid']:
                                    cols = self.schema.getColumns (name)
                                    for colName in cols:
                                        col = {}
                                        col[colName] = {}
                                        col[colName]['name'] = f"{name}.{colName}"
                                        col[colName]['valid'] = True
                                        col[colName]['error'] = None
                                        col[colName]['type'] = 'table'
                                        col[colName]['columnName'] = colName
                                        col[colName]['tableName'] = name
                                        newColumnList.append(col)

                        # replace * with all columns
                        if len(newColumnList) > 0:
                            column_list_nodes = newColumnList
                       

        # where clause
        if isinstance(where_clause, list):
            for where in where_clause:
                if where != None:
                    where_list_nodes.append(self.visit(where))
        else:
            if where_clause == None:
                pass
            else:
                where_list_nodes.append(self.visit(where_clause))
        
        # check if column exists in table
        for where_list in where_list_nodes:
            for condition_list in where_list["condition_list"]:
                for expression_list in condition_list["expression_list"]:
                    for tl in table_list_name:
                        for name in expression_list['column']:
                            if self.schema.isColumnExists (tl, name):
                                #expression_list['column'][name]["error"] = f"Column name {name} does not exists in {tl}"
                                #expression_list['column'][name]["valid"] = False
                                expression_list['column'][name]["error"] = None
                                expression_list['column'][name]["valid"] = True
                        
        
        # get subqueries
        select_statements_nodes = ctx.select_statement()
        for select_statement in select_statements_nodes:
            if isinstance(select_statement, list):
                pass
            else:
               select_list_nodes.append(self.visit(select_statement))
        
        
        # ensure that column exists in subquery
        # for instance, the select statement below will produce an empty table_list
        # since it has been replaced with subquery
        # SELECT a, b, name, 'test' FROM (SELECT name from student_info);

        subquery_column_name = []
        for subquery_select_node in select_list_nodes:
            for column in subquery_select_node['column_list']:
                for name in column:
                    #if column[name]['valid'] == True:
                    # use the property ["name"] instead of name since the name field might contain different
                    # format such as table.column
                    subquery_column_name.append(column[name])

        # get all columns from parent query and match to subquery if there is no table
        if(len(table_list_name) <= 0):
            for col in column_list_nodes:
                for name in col:

                    if col[name]['type'] == 'string':
                        # do nothing since string by default in column_list  is valid
                        col[name]["error"] = None
                        col[name]["valid"] = True
                    else:
                        existsInTables = []
                        
                        for query in subquery_column_name:
                            if query['type'] == 'string':
                                # string column_list must always be valid
                                col[name]["error"] = None
                                col[name]["valid"] = True
                            else:

                                if name == '*':
                                    #col[name]["error"] = None
                                    #col[name]["valid"] = True
                                    newColumnList = []

                                    if len(subquery_column_name) > 0:
                                        for sq in subquery_column_name:
                                            col = {}
                                            col[sq['name']] = sq
                                            newColumnList.append(col)

                                        # replace * with all columns
                                        column_list_nodes = newColumnList
                                else:

                                # column type = table
                                    if col[name]['type'] == 'table':
                                        if col[name]['name'] == query['name']:
                                            col[name]["error"] = None
                                            col[name]["valid"] = True
                                            existsInTables.append (query['name'])

                                    else:
                                        # get column name in the table.column to match columnName
                                        # columnName = name
                                        # student.name
                                        tableColumn = query['name'].split('.')
                                        if len (tableColumn) >=2:
                                            if col[name]['name'] == tableColumn[1]:
                                                col[name]["error"] = None
                                                col[name]["valid"] = True
                                                existsInTables.append (query['name'])
                            
    
                            
                        # this ensure that column will not be ambigous
                        # columnName = name
                        # ['student_enrollment.name', 'student_info.name']                
                        if len(existsInTables) > 1:
                            col[name]["error"] = f"Column {col[name]['name']} is ambigous"
                            col[name]["valid"] = False

        # verify clause if column exists
        for where_nodes in where_list_nodes:
            for condition_list in where_nodes['condition_list']:
                for expression in condition_list['expression_list']:
                    for expressionName in expression['column']:
                        existsInTables = []
                        
                        # read all columns
                        for col in column_list_nodes:
                            for name in col:

                                # for an expression of col = value
                                # ensure that it will match all the columns in the list 
                                # example: name in [table1.name, table2.name]
                                if expression['column'][expressionName]['type'] == 'column':
                                    if col[name]['type'] == 'table':
                                        tableColumn = col[name]['name'].split('.')

                                        if len (tableColumn) >=2:
                                            if expression['column'][expressionName]['name'] == tableColumn[1]:
                                                # put it the the list of matched column
                                                existsInTables.append(col[name]['name'])
                                    else:
                                        # if column is not a table, match the whole name
                                        if col[name]['name'] == expression['column'][expressionName]['name']:
                                            existsInTables.append(col[name]['name'])
                                else:
                                    # for wehere clause with table.column format
                                    # where student_info.name='test'
                                    if col[name]['name'] == expression['column'][expressionName]['name']:
                                        existsInTables.append(col[name]['name'])
                                    

                        
                        # this ensure that column will not be ambigous
                        # columnName = name
                        # ['student_enrollment.name', 'student_info.name']    
                        if len(existsInTables) == 0 :
                            expression['column'][expressionName]["error"] = f"Column {expressionName} does not exists"
                            expression['column'][expressionName]["valid"] = False

                        elif len(existsInTables) == 1 :
                            expression['column'][expressionName]["error"] = None
                            expression['column'][expressionName]["valid"] = True
                        else:
                            expression['column'][expressionName]["error"] = f"Column {expressionName} is ambigous"
                            expression['column'][expressionName]["valid"] = False
                            

        # return data
        data = {
            'table_list'    :   table_list_nodes,
            'column_list'   :   column_list_nodes,
            'where_clause'  :   where_list_nodes,
            'subquery'      :   select_list_nodes,
        }
        
        self.debugData (data, ctx.getText())

        return data

    # Visit a parse tree produced by SQLParser#delete_statement.
    def visitDelete_statement(self, ctx:SQLParser.Delete_statementContext):
        delete_tables = ctx.table_list ()
        where_clause = ctx.where_clause ()

        table_list_nodes = []
        where_list_nodes = []
        table_list_name = []

        # list tables
        if isinstance(delete_tables, list):
            for select in delete_tables:
                table_list_nodes.append(self.visit(select))
        else:
            table_list_nodes.append(self.visit(delete_tables))

        
        # get all VALID table names in string and push to list        
        for tb in table_list_nodes:
            for name in tb:
                if tb[name]['valid']:
                    table_list_name.append(name)  

        # where clause
        if isinstance(where_clause, list):
            for where in where_clause:
                if where != None:
                    where_list_nodes.append(self.visit(where))
        else:
            if where_clause == None:
                pass
            else:
                where_list_nodes.append(self.visit(where_clause))
        
        # verify clause if column exists
        for where_nodes in where_list_nodes:
            for condition_list in where_nodes['condition_list']:
                for expression in condition_list['expression_list']:
                    for expressionName in expression['column']:
                        for tb in table_list_name:
                                # for an expression of col = value
                                # ensure that it belongs to the table
                                # example: table.name in [table1, table2]
                                if expression['column'][expressionName]['type'] == 'table':
                                    
                                    tableColumn = expression['column'][expressionName]['name'].split('.')

                                    if len (tableColumn) >=2:
                                        if self.schema.isColumnExists(tb, tableColumn[1]):
                                            expression['column'][expressionName]['error'] = None
                                            expression['column'][expressionName]['valid'] = True
                                else:
                                    # column name does not contain a table information
                                    # thus, just confirm its existence
                                    if self.schema.isColumnExists(tb, expression['column'][expressionName]['name']):
                                        expression['column'][expressionName]['error'] = None
                                        expression['column'][expressionName]['valid'] = True

        data = {
            'table_list'    :   table_list_nodes,
            'where_clause'  :   where_list_nodes,
        }

        self.debugData (data)

        return data


    # Visit a parse tree produced by SQLParser#insert_statement.
    def visitInsert_statement(self, ctx:SQLParser.Insert_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#table_list.
    def visitTable_list(self, ctx:SQLParser.Table_listContext):
        
        # check if table exists in the database
        self.annotations = {}

        for child in ctx.getChildren():
               # skp semicolon for multiple tables
               if not child.getText() == ',':
                    self.annotations[child.getText()] =  {
                        "name": child.getText(),
                        "error": None,
                        "valid": True,
                    }

                    if not self.schema.isTableExists(child.getText()):
                        self.annotations[child.getText()] =  {
                            "name": child.getText(),
                            "error": f"Table {child.getText()} not found",
                            "valid": False,
                        }

        return self.annotations


    # Visit a parse tree produced by SQLParser#column_list.
    def visitColumn_list(self, ctx:SQLParser.Column_listContext):

        self.annotation = {}

        for column in ctx.getChildren():

                columns = column.getText().split(',')
                for columnName in columns:
                    self.annotation[columnName] =  {
                        "name": columnName,
                        "error": f"Column {columnName} does not exists",
                        "valid": False,
                        "type": "column"
                    }

                    # if the columName is a string 
                    # example statement: SELECT "a"
                    if columnName[0] == "'" or columnName[0] == '"':
                        self.annotation[columnName]["type"] = "string"
                    else:
                        
                        # detect if the columName contains dot
                        # table.column
                        tableColumnName = columnName.split('.')
  
                        if len(tableColumnName) >= 2:
                            # check if column exists
                            self.annotation[columnName]["type"] = "table"
                            self.annotation[columnName]["tableName"] = tableColumnName[0]
                            self.annotation[columnName]["columnName"] = tableColumnName[1]

        return self.annotation


    # Visit a parse tree produced by SQLParser#values_list.
    def visitValues_list(self, ctx:SQLParser.Values_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#insert_column_list.
    def visitInsert_column_list(self, ctx:SQLParser.Insert_column_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#where_clause.
    def visitWhere_clause(self, ctx:SQLParser.Where_clauseContext):

        condition_list = ctx.condition_list()
        condition_list_nodes = []

        if isinstance (condition_list, list):
            for conditions in condition_list:
                condition_list_nodes.append(self.visit(conditions))
        else:
            condition_list_nodes.append(self.visit(condition_list))
        
        return {
            "condition_list"    :   condition_list_nodes
        }
            
    # Visit a parse tree produced by SQLParser#condition_list.
    def visitCondition_list(self, ctx:SQLParser.Condition_listContext):
        expression_list = ctx.expression ()
        expression_list_nodes = []

        if isinstance (expression_list, list):
            for expression in expression_list:
                expression_list_nodes.append(self.visit(expression))
        else:
            expression_list_nodes.append(self.visit(expression_list))
        
        return {
            "expression_list"    :   expression_list_nodes
        }

    # Visit a parse tree produced by SQLParser#expression.
    def visitExpression(self, ctx:SQLParser.ExpressionContext):
        column = ctx.column ()
        operator = ctx.operator ()
        value = ctx.value ()
        column_node = None
        operator_node = None
        value_node = None
        
        column_node = self.visit(column)
        operator_node = self.visit(operator)
        value_node = self.visit (value)
       
        return {
            "column"    :   column_node,
            "operator"  :   operator_node,
            "value"     :   value_node,
        }
    

    # Visit a parse tree produced by SQLParser#column.
    def visitColumn(self, ctx:SQLParser.ColumnContext):
        self.annotation = {}
        for column in ctx.getChildren():

            columns = column.getText().split(',')

            for columnName in columns:
                self.annotation[columnName] =  {
                    "name": columnName,
                    "error": f"Column {columnName} does not exists",
                    "valid": False,
                    "type": "column"
                }

                # if the columName is a string 
                # example statement: SELECT "a"
                if columnName[0] == "'" or columnName[0] == '"':
                    self.annotation[columnName]["type"] = "string"
                else:
                    
                    # detect if the columName contains dot
                    # table.column
                    tableColumnName = columnName.split('.')

                    if len(tableColumnName) >= 2:
                        # check if column exists
                        self.annotation[columnName]["type"] = "table"
                        self.annotation[columnName]["tableName"] = tableColumnName[0]
                        self.annotation[columnName]["columnName"] = tableColumnName[1]

        return self.annotation


    # Visit a parse tree produced by SQLParser#value.
    def visitValue(self, ctx:SQLParser.ValueContext):
        self.annotation = {}
        self.annotation[ctx.getChild(0).getText()] =  {
            "name": ctx.getChild(0).getText(),
            "error": None,
            "valid": True,
        }

        return self.annotation


    # Visit a parse tree produced by SQLParser#operator.
    def visitOperator(self, ctx:SQLParser.OperatorContext):
        self.annotation = {}
        self.annotation[ctx.getChild(0).getText()] =  {
            "name": ctx.getChild(0).getText(),
            "error": None,
            "valid": True,
        }
        return self.annotation



del SQLParser