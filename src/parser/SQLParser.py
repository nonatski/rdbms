# Generated from ./src/parser/SQL.g4 by ANTLR 4.13.2
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
        4,1,27,151,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,1,0,1,0,3,0,32,8,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,4,1,45,8,1,11,1,12,1,46,1,1,3,1,50,8,1,3,1,52,8,1,1,2,1,2,1,2,
        1,2,3,2,58,8,2,1,3,1,3,1,3,1,3,3,3,64,8,3,1,3,1,3,1,3,1,4,1,4,1,
        4,1,4,5,4,73,8,4,10,4,12,4,76,9,4,3,4,78,8,4,1,5,1,5,1,5,1,5,5,5,
        84,8,5,10,5,12,5,87,9,5,1,5,1,5,1,6,1,6,1,6,1,6,5,6,95,8,6,10,6,
        12,6,98,9,6,1,6,1,6,1,7,1,7,1,7,1,8,1,8,4,8,107,8,8,11,8,12,8,108,
        1,8,1,8,4,8,113,8,8,11,8,12,8,114,3,8,117,8,8,1,9,1,9,1,9,1,9,1,
        10,1,10,1,10,5,10,126,8,10,10,10,12,10,129,9,10,1,11,4,11,132,8,
        11,11,11,12,11,133,1,11,1,11,4,11,138,8,11,11,11,12,11,139,5,11,
        142,8,11,10,11,12,11,145,9,11,1,12,1,12,1,13,1,13,1,13,0,0,14,0,
        2,4,6,8,10,12,14,16,18,20,22,24,26,0,4,1,0,13,14,2,0,9,9,24,24,2,
        0,20,20,25,26,1,0,3,8,155,0,31,1,0,0,0,2,36,1,0,0,0,4,53,1,0,0,0,
        6,59,1,0,0,0,8,77,1,0,0,0,10,79,1,0,0,0,12,90,1,0,0,0,14,101,1,0,
        0,0,16,116,1,0,0,0,18,118,1,0,0,0,20,122,1,0,0,0,22,131,1,0,0,0,
        24,146,1,0,0,0,26,148,1,0,0,0,28,32,3,2,1,0,29,32,3,4,2,0,30,32,
        3,6,3,0,31,28,1,0,0,0,31,29,1,0,0,0,31,30,1,0,0,0,32,33,1,0,0,0,
        33,34,5,15,0,0,34,35,5,0,0,1,35,1,1,0,0,0,36,37,5,10,0,0,37,51,3,
        8,4,0,38,44,5,11,0,0,39,45,3,22,11,0,40,41,5,22,0,0,41,42,3,2,1,
        0,42,43,5,23,0,0,43,45,1,0,0,0,44,39,1,0,0,0,44,40,1,0,0,0,45,46,
        1,0,0,0,46,44,1,0,0,0,46,47,1,0,0,0,47,49,1,0,0,0,48,50,3,14,7,0,
        49,48,1,0,0,0,49,50,1,0,0,0,50,52,1,0,0,0,51,38,1,0,0,0,51,52,1,
        0,0,0,52,3,1,0,0,0,53,54,5,16,0,0,54,55,5,11,0,0,55,57,3,22,11,0,
        56,58,3,14,7,0,57,56,1,0,0,0,57,58,1,0,0,0,58,5,1,0,0,0,59,60,5,
        17,0,0,60,61,5,18,0,0,61,63,3,22,11,0,62,64,3,12,6,0,63,62,1,0,0,
        0,63,64,1,0,0,0,64,65,1,0,0,0,65,66,5,19,0,0,66,67,3,10,5,0,67,7,
        1,0,0,0,68,78,5,1,0,0,69,74,3,20,10,0,70,71,5,2,0,0,71,73,3,20,10,
        0,72,70,1,0,0,0,73,76,1,0,0,0,74,72,1,0,0,0,74,75,1,0,0,0,75,78,
        1,0,0,0,76,74,1,0,0,0,77,68,1,0,0,0,77,69,1,0,0,0,78,9,1,0,0,0,79,
        80,5,22,0,0,80,85,3,24,12,0,81,82,5,2,0,0,82,84,3,24,12,0,83,81,
        1,0,0,0,84,87,1,0,0,0,85,83,1,0,0,0,85,86,1,0,0,0,86,88,1,0,0,0,
        87,85,1,0,0,0,88,89,5,23,0,0,89,11,1,0,0,0,90,91,5,22,0,0,91,96,
        3,20,10,0,92,93,5,2,0,0,93,95,3,20,10,0,94,92,1,0,0,0,95,98,1,0,
        0,0,96,94,1,0,0,0,96,97,1,0,0,0,97,99,1,0,0,0,98,96,1,0,0,0,99,100,
        5,23,0,0,100,13,1,0,0,0,101,102,5,12,0,0,102,103,3,16,8,0,103,15,
        1,0,0,0,104,117,3,18,9,0,105,107,3,18,9,0,106,105,1,0,0,0,107,108,
        1,0,0,0,108,106,1,0,0,0,108,109,1,0,0,0,109,112,1,0,0,0,110,111,
        7,0,0,0,111,113,3,18,9,0,112,110,1,0,0,0,113,114,1,0,0,0,114,112,
        1,0,0,0,114,115,1,0,0,0,115,117,1,0,0,0,116,104,1,0,0,0,116,106,
        1,0,0,0,117,17,1,0,0,0,118,119,3,20,10,0,119,120,3,26,13,0,120,121,
        3,24,12,0,121,19,1,0,0,0,122,127,7,1,0,0,123,124,5,2,0,0,124,126,
        7,1,0,0,125,123,1,0,0,0,126,129,1,0,0,0,127,125,1,0,0,0,127,128,
        1,0,0,0,128,21,1,0,0,0,129,127,1,0,0,0,130,132,5,24,0,0,131,130,
        1,0,0,0,132,133,1,0,0,0,133,131,1,0,0,0,133,134,1,0,0,0,134,143,
        1,0,0,0,135,137,5,2,0,0,136,138,5,24,0,0,137,136,1,0,0,0,138,139,
        1,0,0,0,139,137,1,0,0,0,139,140,1,0,0,0,140,142,1,0,0,0,141,135,
        1,0,0,0,142,145,1,0,0,0,143,141,1,0,0,0,143,144,1,0,0,0,144,23,1,
        0,0,0,145,143,1,0,0,0,146,147,7,2,0,0,147,25,1,0,0,0,148,149,7,3,
        0,0,149,27,1,0,0,0,18,31,44,46,49,51,57,63,74,77,85,96,108,114,116,
        127,133,139,143
    ]

class SQLParser ( Parser ):

    grammarFileName = "SQL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'*'", "','", "'='", "'<>'", "'<'", "'>'", 
                     "'<='", "'>='", "<INVALID>", "'select'", "'from'", 
                     "'where'", "'and'", "'or'", "';'", "'delete'", "'insert'", 
                     "'into'", "'values'", "'null'", "'.'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "TCNAME", "SELECT", "FROM", "WHERE", 
                      "AND", "OR", "SEMICOLON", "DELETE", "INSERT", "INTO", 
                      "VALUES", "NULL", "DOT", "OPENPAR", "CLOSEPAR", "WORD", 
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
    TCNAME=9
    SELECT=10
    FROM=11
    WHERE=12
    AND=13
    OR=14
    SEMICOLON=15
    DELETE=16
    INSERT=17
    INTO=18
    VALUES=19
    NULL=20
    DOT=21
    OPENPAR=22
    CLOSEPAR=23
    WORD=24
    NUMBER=25
    STRING=26
    WS=27

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
            if token in [10]:
                self.state = 28
                self.select_statement()
                pass
            elif token in [16]:
                self.state = 29
                self.delete_statement()
                pass
            elif token in [17]:
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

        def table(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.TableContext)
            else:
                return self.getTypedRuleContext(SQLParser.TableContext,i)


        def OPENPAR(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.OPENPAR)
            else:
                return self.getToken(SQLParser.OPENPAR, i)

        def select_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.Select_statementContext)
            else:
                return self.getTypedRuleContext(SQLParser.Select_statementContext,i)


        def CLOSEPAR(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.CLOSEPAR)
            else:
                return self.getToken(SQLParser.CLOSEPAR, i)

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
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 38
                self.match(SQLParser.FROM)
                self.state = 44 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 44
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [24]:
                        self.state = 39
                        self.table()
                        pass
                    elif token in [22]:
                        self.state = 40
                        self.match(SQLParser.OPENPAR)
                        self.state = 41
                        self.select_statement()
                        self.state = 42
                        self.match(SQLParser.CLOSEPAR)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 46 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==22 or _la==24):
                        break

                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==12:
                    self.state = 48
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
            self.state = 53
            self.match(SQLParser.DELETE)
            self.state = 54
            self.match(SQLParser.FROM)
            self.state = 55
            self.table()
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 56
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
            self.state = 59
            self.match(SQLParser.INSERT)
            self.state = 60
            self.match(SQLParser.INTO)
            self.state = 61
            self.table()
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 62
                self.insert_column_list()


            self.state = 65
            self.match(SQLParser.VALUES)
            self.state = 66
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
            self.state = 77
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 68
                self.match(SQLParser.T__0)
                pass
            elif token in [9, 24]:
                self.enterOuterAlt(localctx, 2)
                self.state = 69
                self.column()
                self.state = 74
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 70
                    self.match(SQLParser.T__1)
                    self.state = 71
                    self.column()
                    self.state = 76
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

        def OPENPAR(self):
            return self.getToken(SQLParser.OPENPAR, 0)

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.ValueContext)
            else:
                return self.getTypedRuleContext(SQLParser.ValueContext,i)


        def CLOSEPAR(self):
            return self.getToken(SQLParser.CLOSEPAR, 0)

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
            self.state = 79
            self.match(SQLParser.OPENPAR)
            self.state = 80
            self.value()
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 81
                self.match(SQLParser.T__1)
                self.state = 82
                self.value()
                self.state = 87
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 88
            self.match(SQLParser.CLOSEPAR)
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

        def OPENPAR(self):
            return self.getToken(SQLParser.OPENPAR, 0)

        def column(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.ColumnContext)
            else:
                return self.getTypedRuleContext(SQLParser.ColumnContext,i)


        def CLOSEPAR(self):
            return self.getToken(SQLParser.CLOSEPAR, 0)

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
            self.state = 90
            self.match(SQLParser.OPENPAR)
            self.state = 91
            self.column()
            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 92
                self.match(SQLParser.T__1)
                self.state = 93
                self.column()
                self.state = 98
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 99
            self.match(SQLParser.CLOSEPAR)
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
            self.state = 101
            self.match(SQLParser.WHERE)
            self.state = 102
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


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.AND)
            else:
                return self.getToken(SQLParser.AND, i)

        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.OR)
            else:
                return self.getToken(SQLParser.OR, i)

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
        self._la = 0 # Token type
        try:
            self.state = 116
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 104
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 106 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 105
                    self.expression()
                    self.state = 108 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==9 or _la==24):
                        break

                self.state = 112 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 110
                    _la = self._input.LA(1)
                    if not(_la==13 or _la==14):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 111
                    self.expression()
                    self.state = 114 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==13 or _la==14):
                        break

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
            self.state = 118
            self.column()
            self.state = 119
            self.operator()
            self.state = 120
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

        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.WORD)
            else:
                return self.getToken(SQLParser.WORD, i)

        def TCNAME(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.TCNAME)
            else:
                return self.getToken(SQLParser.TCNAME, i)

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
            self.state = 122
            _la = self._input.LA(1)
            if not(_la==9 or _la==24):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 127
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 123
                    self.match(SQLParser.T__1)
                    self.state = 124
                    _la = self._input.LA(1)
                    if not(_la==9 or _la==24):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume() 
                self.state = 129
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

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

        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.WORD)
            else:
                return self.getToken(SQLParser.WORD, i)

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
            self.state = 131 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 130
                    self.match(SQLParser.WORD)

                else:
                    raise NoViableAltException(self)
                self.state = 133 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 135
                self.match(SQLParser.T__1)
                self.state = 137 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 136
                        self.match(SQLParser.WORD)

                    else:
                        raise NoViableAltException(self)
                    self.state = 139 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

                self.state = 145
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def NULL(self):
            return self.getToken(SQLParser.NULL, 0)

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
            self.state = 146
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 101711872) != 0)):
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
            self.state = 148
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 504) != 0)):
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





