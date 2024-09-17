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
        4,1,27,164,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,1,0,1,0,3,0,32,8,0,1,0,1,0,1,0,1,0,4,0,38,8,0,11,0,12,0,39,5,
        0,42,8,0,10,0,12,0,45,9,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,4,1,58,8,1,11,1,12,1,59,1,1,3,1,63,8,1,3,1,65,8,1,1,2,1,2,
        1,2,1,2,3,2,71,8,2,1,3,1,3,1,3,1,3,3,3,77,8,3,1,3,1,3,1,3,1,4,1,
        4,1,4,1,4,5,4,86,8,4,10,4,12,4,89,9,4,3,4,91,8,4,1,5,1,5,1,5,1,5,
        5,5,97,8,5,10,5,12,5,100,9,5,1,5,1,5,1,6,1,6,1,6,1,6,5,6,108,8,6,
        10,6,12,6,111,9,6,1,6,1,6,1,7,1,7,1,7,1,8,1,8,4,8,120,8,8,11,8,12,
        8,121,1,8,1,8,4,8,126,8,8,11,8,12,8,127,3,8,130,8,8,1,9,1,9,1,9,
        1,9,1,10,1,10,1,10,5,10,139,8,10,10,10,12,10,142,9,10,1,11,4,11,
        145,8,11,11,11,12,11,146,1,11,1,11,4,11,151,8,11,11,11,12,11,152,
        5,11,155,8,11,10,11,12,11,158,9,11,1,12,1,12,1,13,1,13,1,13,0,0,
        14,0,2,4,6,8,10,12,14,16,18,20,22,24,26,0,4,1,0,13,14,2,0,9,9,24,
        24,2,0,20,20,25,26,1,0,3,8,172,0,31,1,0,0,0,2,49,1,0,0,0,4,66,1,
        0,0,0,6,72,1,0,0,0,8,90,1,0,0,0,10,92,1,0,0,0,12,103,1,0,0,0,14,
        114,1,0,0,0,16,129,1,0,0,0,18,131,1,0,0,0,20,135,1,0,0,0,22,144,
        1,0,0,0,24,159,1,0,0,0,26,161,1,0,0,0,28,32,3,2,1,0,29,32,3,4,2,
        0,30,32,3,6,3,0,31,28,1,0,0,0,31,29,1,0,0,0,31,30,1,0,0,0,32,43,
        1,0,0,0,33,37,5,15,0,0,34,38,3,2,1,0,35,38,3,4,2,0,36,38,3,6,3,0,
        37,34,1,0,0,0,37,35,1,0,0,0,37,36,1,0,0,0,38,39,1,0,0,0,39,37,1,
        0,0,0,39,40,1,0,0,0,40,42,1,0,0,0,41,33,1,0,0,0,42,45,1,0,0,0,43,
        41,1,0,0,0,43,44,1,0,0,0,44,46,1,0,0,0,45,43,1,0,0,0,46,47,5,15,
        0,0,47,48,5,0,0,1,48,1,1,0,0,0,49,50,5,10,0,0,50,64,3,8,4,0,51,57,
        5,11,0,0,52,58,3,22,11,0,53,54,5,22,0,0,54,55,3,2,1,0,55,56,5,23,
        0,0,56,58,1,0,0,0,57,52,1,0,0,0,57,53,1,0,0,0,58,59,1,0,0,0,59,57,
        1,0,0,0,59,60,1,0,0,0,60,62,1,0,0,0,61,63,3,14,7,0,62,61,1,0,0,0,
        62,63,1,0,0,0,63,65,1,0,0,0,64,51,1,0,0,0,64,65,1,0,0,0,65,3,1,0,
        0,0,66,67,5,16,0,0,67,68,5,11,0,0,68,70,3,22,11,0,69,71,3,14,7,0,
        70,69,1,0,0,0,70,71,1,0,0,0,71,5,1,0,0,0,72,73,5,17,0,0,73,74,5,
        18,0,0,74,76,3,22,11,0,75,77,3,12,6,0,76,75,1,0,0,0,76,77,1,0,0,
        0,77,78,1,0,0,0,78,79,5,19,0,0,79,80,3,10,5,0,80,7,1,0,0,0,81,91,
        5,1,0,0,82,87,3,20,10,0,83,84,5,2,0,0,84,86,3,20,10,0,85,83,1,0,
        0,0,86,89,1,0,0,0,87,85,1,0,0,0,87,88,1,0,0,0,88,91,1,0,0,0,89,87,
        1,0,0,0,90,81,1,0,0,0,90,82,1,0,0,0,91,9,1,0,0,0,92,93,5,22,0,0,
        93,98,3,24,12,0,94,95,5,2,0,0,95,97,3,24,12,0,96,94,1,0,0,0,97,100,
        1,0,0,0,98,96,1,0,0,0,98,99,1,0,0,0,99,101,1,0,0,0,100,98,1,0,0,
        0,101,102,5,23,0,0,102,11,1,0,0,0,103,104,5,22,0,0,104,109,3,20,
        10,0,105,106,5,2,0,0,106,108,3,20,10,0,107,105,1,0,0,0,108,111,1,
        0,0,0,109,107,1,0,0,0,109,110,1,0,0,0,110,112,1,0,0,0,111,109,1,
        0,0,0,112,113,5,23,0,0,113,13,1,0,0,0,114,115,5,12,0,0,115,116,3,
        16,8,0,116,15,1,0,0,0,117,130,3,18,9,0,118,120,3,18,9,0,119,118,
        1,0,0,0,120,121,1,0,0,0,121,119,1,0,0,0,121,122,1,0,0,0,122,125,
        1,0,0,0,123,124,7,0,0,0,124,126,3,18,9,0,125,123,1,0,0,0,126,127,
        1,0,0,0,127,125,1,0,0,0,127,128,1,0,0,0,128,130,1,0,0,0,129,117,
        1,0,0,0,129,119,1,0,0,0,130,17,1,0,0,0,131,132,3,20,10,0,132,133,
        3,26,13,0,133,134,3,24,12,0,134,19,1,0,0,0,135,140,7,1,0,0,136,137,
        5,2,0,0,137,139,7,1,0,0,138,136,1,0,0,0,139,142,1,0,0,0,140,138,
        1,0,0,0,140,141,1,0,0,0,141,21,1,0,0,0,142,140,1,0,0,0,143,145,5,
        24,0,0,144,143,1,0,0,0,145,146,1,0,0,0,146,144,1,0,0,0,146,147,1,
        0,0,0,147,156,1,0,0,0,148,150,5,2,0,0,149,151,5,24,0,0,150,149,1,
        0,0,0,151,152,1,0,0,0,152,150,1,0,0,0,152,153,1,0,0,0,153,155,1,
        0,0,0,154,148,1,0,0,0,155,158,1,0,0,0,156,154,1,0,0,0,156,157,1,
        0,0,0,157,23,1,0,0,0,158,156,1,0,0,0,159,160,7,2,0,0,160,25,1,0,
        0,0,161,162,7,3,0,0,162,27,1,0,0,0,21,31,37,39,43,57,59,62,64,70,
        76,87,90,98,109,121,127,129,140,146,152,156
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

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.SEMICOLON)
            else:
                return self.getToken(SQLParser.SEMICOLON, i)

        def EOF(self):
            return self.getToken(SQLParser.EOF, 0)

        def select_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.Select_statementContext)
            else:
                return self.getTypedRuleContext(SQLParser.Select_statementContext,i)


        def delete_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.Delete_statementContext)
            else:
                return self.getTypedRuleContext(SQLParser.Delete_statementContext,i)


        def insert_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.Insert_statementContext)
            else:
                return self.getTypedRuleContext(SQLParser.Insert_statementContext,i)


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
        self._la = 0 # Token type
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

            self.state = 43
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 33
                    self.match(SQLParser.SEMICOLON)
                    self.state = 37 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 37
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [10]:
                            self.state = 34
                            self.select_statement()
                            pass
                        elif token in [16]:
                            self.state = 35
                            self.delete_statement()
                            pass
                        elif token in [17]:
                            self.state = 36
                            self.insert_statement()
                            pass
                        else:
                            raise NoViableAltException(self)

                        self.state = 39 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 197632) != 0)):
                            break
             
                self.state = 45
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 46
            self.match(SQLParser.SEMICOLON)
            self.state = 47
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
            self.state = 49
            self.match(SQLParser.SELECT)
            self.state = 50
            self.column_list()
            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 51
                self.match(SQLParser.FROM)
                self.state = 57 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 57
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [24]:
                        self.state = 52
                        self.table()
                        pass
                    elif token in [22]:
                        self.state = 53
                        self.match(SQLParser.OPENPAR)
                        self.state = 54
                        self.select_statement()
                        self.state = 55
                        self.match(SQLParser.CLOSEPAR)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 59 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==22 or _la==24):
                        break

                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==12:
                    self.state = 61
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
            self.state = 66
            self.match(SQLParser.DELETE)
            self.state = 67
            self.match(SQLParser.FROM)
            self.state = 68
            self.table()
            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 69
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
            self.state = 72
            self.match(SQLParser.INSERT)
            self.state = 73
            self.match(SQLParser.INTO)
            self.state = 74
            self.table()
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 75
                self.insert_column_list()


            self.state = 78
            self.match(SQLParser.VALUES)
            self.state = 79
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
            self.state = 90
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 81
                self.match(SQLParser.T__0)
                pass
            elif token in [9, 24]:
                self.enterOuterAlt(localctx, 2)
                self.state = 82
                self.column()
                self.state = 87
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 83
                    self.match(SQLParser.T__1)
                    self.state = 84
                    self.column()
                    self.state = 89
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
            self.state = 92
            self.match(SQLParser.OPENPAR)
            self.state = 93
            self.value()
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 94
                self.match(SQLParser.T__1)
                self.state = 95
                self.value()
                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 101
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
            self.state = 103
            self.match(SQLParser.OPENPAR)
            self.state = 104
            self.column()
            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 105
                self.match(SQLParser.T__1)
                self.state = 106
                self.column()
                self.state = 111
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 112
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
            self.state = 114
            self.match(SQLParser.WHERE)
            self.state = 115
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
            self.state = 129
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 119 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 118
                    self.expression()
                    self.state = 121 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==9 or _la==24):
                        break

                self.state = 125 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 123
                    _la = self._input.LA(1)
                    if not(_la==13 or _la==14):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 124
                    self.expression()
                    self.state = 127 
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
            self.state = 131
            self.column()
            self.state = 132
            self.operator()
            self.state = 133
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
            self.state = 135
            _la = self._input.LA(1)
            if not(_la==9 or _la==24):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 140
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 136
                    self.match(SQLParser.T__1)
                    self.state = 137
                    _la = self._input.LA(1)
                    if not(_la==9 or _la==24):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume() 
                self.state = 142
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

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
            self.state = 144 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 143
                    self.match(SQLParser.WORD)

                else:
                    raise NoViableAltException(self)
                self.state = 146 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 148
                self.match(SQLParser.T__1)
                self.state = 150 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 149
                        self.match(SQLParser.WORD)

                    else:
                        raise NoViableAltException(self)
                    self.state = 152 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

                self.state = 158
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
            self.state = 159
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
            self.state = 161
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





