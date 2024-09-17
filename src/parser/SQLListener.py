# Generated from ./src/parser/SQL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SQLParser import SQLParser
else:
    from SQLParser import SQLParser

# This class defines a complete listener for a parse tree produced by SQLParser.
class SQLListener(ParseTreeListener):

    # Enter a parse tree produced by SQLParser#sql_statement.
    def enterSql_statement(self, ctx:SQLParser.Sql_statementContext):
        pass

    # Exit a parse tree produced by SQLParser#sql_statement.
    def exitSql_statement(self, ctx:SQLParser.Sql_statementContext):
        pass


    # Enter a parse tree produced by SQLParser#select_statement.
    def enterSelect_statement(self, ctx:SQLParser.Select_statementContext):
        pass

    # Exit a parse tree produced by SQLParser#select_statement.
    def exitSelect_statement(self, ctx:SQLParser.Select_statementContext):
        pass


    # Enter a parse tree produced by SQLParser#delete_statement.
    def enterDelete_statement(self, ctx:SQLParser.Delete_statementContext):
        pass

    # Exit a parse tree produced by SQLParser#delete_statement.
    def exitDelete_statement(self, ctx:SQLParser.Delete_statementContext):
        pass


    # Enter a parse tree produced by SQLParser#insert_statement.
    def enterInsert_statement(self, ctx:SQLParser.Insert_statementContext):
        pass

    # Exit a parse tree produced by SQLParser#insert_statement.
    def exitInsert_statement(self, ctx:SQLParser.Insert_statementContext):
        pass


    # Enter a parse tree produced by SQLParser#table_list.
    def enterTable_list(self, ctx:SQLParser.Table_listContext):
        pass

    # Exit a parse tree produced by SQLParser#table_list.
    def exitTable_list(self, ctx:SQLParser.Table_listContext):
        pass


    # Enter a parse tree produced by SQLParser#column_list.
    def enterColumn_list(self, ctx:SQLParser.Column_listContext):
        pass

    # Exit a parse tree produced by SQLParser#column_list.
    def exitColumn_list(self, ctx:SQLParser.Column_listContext):
        pass


    # Enter a parse tree produced by SQLParser#values_list.
    def enterValues_list(self, ctx:SQLParser.Values_listContext):
        pass

    # Exit a parse tree produced by SQLParser#values_list.
    def exitValues_list(self, ctx:SQLParser.Values_listContext):
        pass


    # Enter a parse tree produced by SQLParser#insert_column_list.
    def enterInsert_column_list(self, ctx:SQLParser.Insert_column_listContext):
        pass

    # Exit a parse tree produced by SQLParser#insert_column_list.
    def exitInsert_column_list(self, ctx:SQLParser.Insert_column_listContext):
        pass


    # Enter a parse tree produced by SQLParser#where_clause.
    def enterWhere_clause(self, ctx:SQLParser.Where_clauseContext):
        pass

    # Exit a parse tree produced by SQLParser#where_clause.
    def exitWhere_clause(self, ctx:SQLParser.Where_clauseContext):
        pass


    # Enter a parse tree produced by SQLParser#condition_list.
    def enterCondition_list(self, ctx:SQLParser.Condition_listContext):
        pass

    # Exit a parse tree produced by SQLParser#condition_list.
    def exitCondition_list(self, ctx:SQLParser.Condition_listContext):
        pass


    # Enter a parse tree produced by SQLParser#expression.
    def enterExpression(self, ctx:SQLParser.ExpressionContext):
        pass

    # Exit a parse tree produced by SQLParser#expression.
    def exitExpression(self, ctx:SQLParser.ExpressionContext):
        pass


    # Enter a parse tree produced by SQLParser#column.
    def enterColumn(self, ctx:SQLParser.ColumnContext):
        pass

    # Exit a parse tree produced by SQLParser#column.
    def exitColumn(self, ctx:SQLParser.ColumnContext):
        pass


    # Enter a parse tree produced by SQLParser#value.
    def enterValue(self, ctx:SQLParser.ValueContext):
        pass

    # Exit a parse tree produced by SQLParser#value.
    def exitValue(self, ctx:SQLParser.ValueContext):
        pass


    # Enter a parse tree produced by SQLParser#operator.
    def enterOperator(self, ctx:SQLParser.OperatorContext):
        pass

    # Exit a parse tree produced by SQLParser#operator.
    def exitOperator(self, ctx:SQLParser.OperatorContext):
        pass



del SQLParser