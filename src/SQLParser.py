# Generated from SQL.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,49,118,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,1,0,1,0,3,0,32,8,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,3,1,42,8,
        1,1,2,1,2,1,2,1,2,3,2,48,8,2,1,3,1,3,1,3,1,3,3,3,54,8,3,1,3,1,3,
        1,3,1,4,1,4,1,4,1,4,5,4,63,8,4,10,4,12,4,66,9,4,3,4,68,8,4,1,5,1,
        5,1,5,1,5,5,5,74,8,5,10,5,12,5,77,9,5,1,5,1,5,1,6,1,6,1,6,1,6,5,
        6,85,8,6,10,6,12,6,88,9,6,1,6,1,6,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,1,8,3,8,104,8,8,1,9,1,9,1,9,1,9,1,10,1,10,1,11,1,11,
        1,12,1,12,1,13,1,13,1,13,0,0,14,0,2,4,6,8,10,12,14,16,18,20,22,24,
        26,0,4,1,0,5,25,1,0,26,30,1,0,47,48,1,0,31,36,114,0,31,1,0,0,0,2,
        36,1,0,0,0,4,43,1,0,0,0,6,49,1,0,0,0,8,67,1,0,0,0,10,69,1,0,0,0,
        12,80,1,0,0,0,14,91,1,0,0,0,16,103,1,0,0,0,18,105,1,0,0,0,20,109,
        1,0,0,0,22,111,1,0,0,0,24,113,1,0,0,0,26,115,1,0,0,0,28,32,3,2,1,
        0,29,32,3,4,2,0,30,32,3,6,3,0,31,28,1,0,0,0,31,29,1,0,0,0,31,30,
        1,0,0,0,32,33,1,0,0,0,33,34,5,42,0,0,34,35,5,0,0,1,35,1,1,0,0,0,
        36,37,5,37,0,0,37,38,3,8,4,0,38,39,5,38,0,0,39,41,3,22,11,0,40,42,
        3,14,7,0,41,40,1,0,0,0,41,42,1,0,0,0,42,3,1,0,0,0,43,44,5,43,0,0,
        44,45,5,38,0,0,45,47,3,22,11,0,46,48,3,14,7,0,47,46,1,0,0,0,47,48,
        1,0,0,0,48,5,1,0,0,0,49,50,5,44,0,0,50,51,5,45,0,0,51,53,3,22,11,
        0,52,54,3,12,6,0,53,52,1,0,0,0,53,54,1,0,0,0,54,55,1,0,0,0,55,56,
        5,46,0,0,56,57,3,10,5,0,57,7,1,0,0,0,58,68,5,1,0,0,59,64,3,20,10,
        0,60,61,5,2,0,0,61,63,3,20,10,0,62,60,1,0,0,0,63,66,1,0,0,0,64,62,
        1,0,0,0,64,65,1,0,0,0,65,68,1,0,0,0,66,64,1,0,0,0,67,58,1,0,0,0,
        67,59,1,0,0,0,68,9,1,0,0,0,69,70,5,3,0,0,70,75,3,24,12,0,71,72,5,
        2,0,0,72,74,3,24,12,0,73,71,1,0,0,0,74,77,1,0,0,0,75,73,1,0,0,0,
        75,76,1,0,0,0,76,78,1,0,0,0,77,75,1,0,0,0,78,79,5,4,0,0,79,11,1,
        0,0,0,80,81,5,3,0,0,81,86,3,20,10,0,82,83,5,2,0,0,83,85,3,20,10,
        0,84,82,1,0,0,0,85,88,1,0,0,0,86,84,1,0,0,0,86,87,1,0,0,0,87,89,
        1,0,0,0,88,86,1,0,0,0,89,90,5,4,0,0,90,13,1,0,0,0,91,92,5,39,0,0,
        92,93,3,16,8,0,93,15,1,0,0,0,94,104,3,18,9,0,95,96,3,18,9,0,96,97,
        5,40,0,0,97,98,3,18,9,0,98,104,1,0,0,0,99,100,3,18,9,0,100,101,5,
        41,0,0,101,102,3,18,9,0,102,104,1,0,0,0,103,94,1,0,0,0,103,95,1,
        0,0,0,103,99,1,0,0,0,104,17,1,0,0,0,105,106,3,20,10,0,106,107,3,
        26,13,0,107,108,3,24,12,0,108,19,1,0,0,0,109,110,7,0,0,0,110,21,
        1,0,0,0,111,112,7,1,0,0,112,23,1,0,0,0,113,114,7,2,0,0,114,25,1,
        0,0,0,115,116,7,3,0,0,116,27,1,0,0,0,9,31,41,47,53,64,67,75,86,103
    ]

class SQLParser ( Parser ):

    grammarFileName = "SQL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'*'", "','", "'('", "')'", "'studno'", 
                     "'studentname'", "'birthday'", "'degree'", "'major'", 
                     "'unitsearned'", "'description'", "'action'", "'datefiled'", 
                     "'dateresolved'", "'cno'", "'ctitle'", "'cdesc'", "'noofunits'", 
                     "'haslab'", "'semoffered'", "'semester'", "'acadyear'", 
                     "'section'", "'time'", "'maxstud'", "'student'", "'studenthistory'", 
                     "'course'", "'courseoffering'", "'studcourse'", "'='", 
                     "'<>'", "'<'", "'>'", "'<='", "'>='", "'select'", "'from'", 
                     "'where'", "'and'", "'or'", "';'", "'delete'", "'insert'", 
                     "'into'", "'values'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "SELECT", "FROM", "WHERE", "AND", "OR", 
                      "SEMICOLON", "DELETE", "INSERT", "INTO", "VALUES", 
                      "NUMBER", "STRING", "WS" ]

    RULE_sql_statement = 0
    RULE_select_statement = 1
    RULE_delete_statement = 2
    RULE_insert_statement = 3
    RULE_column_list = 4
    RULE_values_list = 5
    RULE_insert_column_list = 6
    RULE_where_clause = 7
    RULE_condition = 8
    RULE_expression = 9
    RULE_column = 10
    RULE_table = 11
    RULE_value = 12
    RULE_operator = 13

    ruleNames =  [ "sql_statement", "select_statement", "delete_statement", 
                   "insert_statement", "column_list", "values_list", "insert_column_list", 
                   "where_clause", "condition", "expression", "column", 
                   "table", "value", "operator" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    SELECT=37
    FROM=38
    WHERE=39
    AND=40
    OR=41
    SEMICOLON=42
    DELETE=43
    INSERT=44
    INTO=45
    VALUES=46
    NUMBER=47
    STRING=48
    WS=49

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Sql_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self):
            return self.getToken(SQLParser.SEMICOLON, 0)

        def EOF(self):
            return self.getToken(SQLParser.EOF, 0)

        def select_statement(self):
            return self.getTypedRuleContext(SQLParser.Select_statementContext,0)


        def delete_statement(self):
            return self.getTypedRuleContext(SQLParser.Delete_statementContext,0)


        def insert_statement(self):
            return self.getTypedRuleContext(SQLParser.Insert_statementContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_sql_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSql_statement" ):
                listener.enterSql_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSql_statement" ):
                listener.exitSql_statement(self)




    def sql_statement(self):

        localctx = SQLParser.Sql_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_sql_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [37]:
                self.state = 28
                self.select_statement()
                pass
            elif token in [43]:
                self.state = 29
                self.delete_statement()
                pass
            elif token in [44]:
                self.state = 30
                self.insert_statement()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 33
            self.match(SQLParser.SEMICOLON)
            self.state = 34
            self.match(SQLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Select_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SELECT(self):
            return self.getToken(SQLParser.SELECT, 0)

        def column_list(self):
            return self.getTypedRuleContext(SQLParser.Column_listContext,0)


        def FROM(self):
            return self.getToken(SQLParser.FROM, 0)

        def table(self):
            return self.getTypedRuleContext(SQLParser.TableContext,0)


        def where_clause(self):
            return self.getTypedRuleContext(SQLParser.Where_clauseContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_select_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelect_statement" ):
                listener.enterSelect_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelect_statement" ):
                listener.exitSelect_statement(self)




    def select_statement(self):

        localctx = SQLParser.Select_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_select_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(SQLParser.SELECT)
            self.state = 37
            self.column_list()
            self.state = 38
            self.match(SQLParser.FROM)
            self.state = 39
            self.table()
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==39:
                self.state = 40
                self.where_clause()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Delete_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DELETE(self):
            return self.getToken(SQLParser.DELETE, 0)

        def FROM(self):
            return self.getToken(SQLParser.FROM, 0)

        def table(self):
            return self.getTypedRuleContext(SQLParser.TableContext,0)


        def where_clause(self):
            return self.getTypedRuleContext(SQLParser.Where_clauseContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_delete_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDelete_statement" ):
                listener.enterDelete_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDelete_statement" ):
                listener.exitDelete_statement(self)




    def delete_statement(self):

        localctx = SQLParser.Delete_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_delete_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(SQLParser.DELETE)
            self.state = 44
            self.match(SQLParser.FROM)
            self.state = 45
            self.table()
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==39:
                self.state = 46
                self.where_clause()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Insert_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INSERT(self):
            return self.getToken(SQLParser.INSERT, 0)

        def INTO(self):
            return self.getToken(SQLParser.INTO, 0)

        def table(self):
            return self.getTypedRuleContext(SQLParser.TableContext,0)


        def VALUES(self):
            return self.getToken(SQLParser.VALUES, 0)

        def values_list(self):
            return self.getTypedRuleContext(SQLParser.Values_listContext,0)


        def insert_column_list(self):
            return self.getTypedRuleContext(SQLParser.Insert_column_listContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_insert_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInsert_statement" ):
                listener.enterInsert_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInsert_statement" ):
                listener.exitInsert_statement(self)




    def insert_statement(self):

        localctx = SQLParser.Insert_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_insert_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(SQLParser.INSERT)
            self.state = 50
            self.match(SQLParser.INTO)
            self.state = 51
            self.table()
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 52
                self.insert_column_list()


            self.state = 55
            self.match(SQLParser.VALUES)
            self.state = 56
            self.values_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Column_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def column(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.ColumnContext)
            else:
                return self.getTypedRuleContext(SQLParser.ColumnContext,i)


        def getRuleIndex(self):
            return SQLParser.RULE_column_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumn_list" ):
                listener.enterColumn_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumn_list" ):
                listener.exitColumn_list(self)




    def column_list(self):

        localctx = SQLParser.Column_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_column_list)
        self._la = 0 # Token type
        try:
            self.state = 67
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 58
                self.match(SQLParser.T__0)
                pass
            elif token in [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]:
                self.enterOuterAlt(localctx, 2)
                self.state = 59
                self.column()
                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 60
                    self.match(SQLParser.T__1)
                    self.state = 61
                    self.column()
                    self.state = 66
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Values_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.ValueContext)
            else:
                return self.getTypedRuleContext(SQLParser.ValueContext,i)


        def getRuleIndex(self):
            return SQLParser.RULE_values_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValues_list" ):
                listener.enterValues_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValues_list" ):
                listener.exitValues_list(self)




    def values_list(self):

        localctx = SQLParser.Values_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_values_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(SQLParser.T__2)
            self.state = 70
            self.value()
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 71
                self.match(SQLParser.T__1)
                self.state = 72
                self.value()
                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 78
            self.match(SQLParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Insert_column_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def column(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.ColumnContext)
            else:
                return self.getTypedRuleContext(SQLParser.ColumnContext,i)


        def getRuleIndex(self):
            return SQLParser.RULE_insert_column_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInsert_column_list" ):
                listener.enterInsert_column_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInsert_column_list" ):
                listener.exitInsert_column_list(self)




    def insert_column_list(self):

        localctx = SQLParser.Insert_column_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_insert_column_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(SQLParser.T__2)
            self.state = 81
            self.column()
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 82
                self.match(SQLParser.T__1)
                self.state = 83
                self.column()
                self.state = 88
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 89
            self.match(SQLParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Where_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHERE(self):
            return self.getToken(SQLParser.WHERE, 0)

        def condition(self):
            return self.getTypedRuleContext(SQLParser.ConditionContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_where_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhere_clause" ):
                listener.enterWhere_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhere_clause" ):
                listener.exitWhere_clause(self)




    def where_clause(self):

        localctx = SQLParser.Where_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_where_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(SQLParser.WHERE)
            self.state = 92
            self.condition()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SQLParser.ExpressionContext,i)


        def AND(self):
            return self.getToken(SQLParser.AND, 0)

        def OR(self):
            return self.getToken(SQLParser.OR, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)




    def condition(self):

        localctx = SQLParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_condition)
        try:
            self.state = 103
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 94
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 95
                self.expression()
                self.state = 96
                self.match(SQLParser.AND)
                self.state = 97
                self.expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 99
                self.expression()
                self.state = 100
                self.match(SQLParser.OR)
                self.state = 101
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def column(self):
            return self.getTypedRuleContext(SQLParser.ColumnContext,0)


        def operator(self):
            return self.getTypedRuleContext(SQLParser.OperatorContext,0)


        def value(self):
            return self.getTypedRuleContext(SQLParser.ValueContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = SQLParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.column()
            self.state = 106
            self.operator()
            self.state = 107
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColumnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SQLParser.RULE_column

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumn" ):
                listener.enterColumn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumn" ):
                listener.exitColumn(self)




    def column(self):

        localctx = SQLParser.ColumnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_column)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 67108832) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SQLParser.RULE_table

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTable" ):
                listener.enterTable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTable" ):
                listener.exitTable(self)




    def table(self):

        localctx = SQLParser.TableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_table)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2080374784) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(SQLParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(SQLParser.NUMBER, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = SQLParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            _la = self._input.LA(1)
            if not(_la==47 or _la==48):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SQLParser.RULE_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperator" ):
                listener.enterOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperator" ):
                listener.exitOperator(self)




    def operator(self):

        localctx = SQLParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 135291469824) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





