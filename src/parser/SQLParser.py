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
        1,2,1,2,3,2,71,8,2,1,3,1,3,1,3,1,3,3,3,77,8,3,1,3,1,3,1,3,1,4,4,
        4,83,8,4,11,4,12,4,84,1,4,1,4,4,4,89,8,4,11,4,12,4,90,5,4,93,8,4,
        10,4,12,4,96,9,4,1,5,1,5,1,5,1,5,5,5,102,8,5,10,5,12,5,105,9,5,3,
        5,107,8,5,1,6,1,6,1,6,1,6,5,6,113,8,6,10,6,12,6,116,9,6,1,6,1,6,
        1,7,1,7,1,7,1,7,5,7,124,8,7,10,7,12,7,127,9,7,1,7,1,7,1,8,1,8,1,
        8,1,9,1,9,4,9,136,8,9,11,9,12,9,137,1,9,1,9,4,9,142,8,9,11,9,12,
        9,143,3,9,146,8,9,1,10,1,10,1,10,1,10,1,11,1,11,1,11,5,11,155,8,
        11,10,11,12,11,158,9,11,1,12,1,12,1,13,1,13,1,13,0,0,14,0,2,4,6,
        8,10,12,14,16,18,20,22,24,26,0,4,1,0,13,14,2,0,9,9,24,26,2,0,20,
        20,25,26,1,0,3,8,172,0,31,1,0,0,0,2,49,1,0,0,0,4,66,1,0,0,0,6,72,
        1,0,0,0,8,82,1,0,0,0,10,106,1,0,0,0,12,108,1,0,0,0,14,119,1,0,0,
        0,16,130,1,0,0,0,18,145,1,0,0,0,20,147,1,0,0,0,22,151,1,0,0,0,24,
        159,1,0,0,0,26,161,1,0,0,0,28,32,3,2,1,0,29,32,3,4,2,0,30,32,3,6,
        3,0,31,28,1,0,0,0,31,29,1,0,0,0,31,30,1,0,0,0,32,43,1,0,0,0,33,37,
        5,15,0,0,34,38,3,2,1,0,35,38,3,4,2,0,36,38,3,6,3,0,37,34,1,0,0,0,
        37,35,1,0,0,0,37,36,1,0,0,0,38,39,1,0,0,0,39,37,1,0,0,0,39,40,1,
        0,0,0,40,42,1,0,0,0,41,33,1,0,0,0,42,45,1,0,0,0,43,41,1,0,0,0,43,
        44,1,0,0,0,44,46,1,0,0,0,45,43,1,0,0,0,46,47,5,15,0,0,47,48,5,0,
        0,1,48,1,1,0,0,0,49,50,5,10,0,0,50,64,3,10,5,0,51,57,5,11,0,0,52,
        58,3,8,4,0,53,54,5,22,0,0,54,55,3,2,1,0,55,56,5,23,0,0,56,58,1,0,
        0,0,57,52,1,0,0,0,57,53,1,0,0,0,58,59,1,0,0,0,59,57,1,0,0,0,59,60,
        1,0,0,0,60,62,1,0,0,0,61,63,3,16,8,0,62,61,1,0,0,0,62,63,1,0,0,0,
        63,65,1,0,0,0,64,51,1,0,0,0,64,65,1,0,0,0,65,3,1,0,0,0,66,67,5,16,
        0,0,67,68,5,11,0,0,68,70,3,8,4,0,69,71,3,16,8,0,70,69,1,0,0,0,70,
        71,1,0,0,0,71,5,1,0,0,0,72,73,5,17,0,0,73,74,5,18,0,0,74,76,3,8,
        4,0,75,77,3,14,7,0,76,75,1,0,0,0,76,77,1,0,0,0,77,78,1,0,0,0,78,
        79,5,19,0,0,79,80,3,12,6,0,80,7,1,0,0,0,81,83,5,24,0,0,82,81,1,0,
        0,0,83,84,1,0,0,0,84,82,1,0,0,0,84,85,1,0,0,0,85,94,1,0,0,0,86,88,
        5,1,0,0,87,89,5,24,0,0,88,87,1,0,0,0,89,90,1,0,0,0,90,88,1,0,0,0,
        90,91,1,0,0,0,91,93,1,0,0,0,92,86,1,0,0,0,93,96,1,0,0,0,94,92,1,
        0,0,0,94,95,1,0,0,0,95,9,1,0,0,0,96,94,1,0,0,0,97,107,5,2,0,0,98,
        103,3,22,11,0,99,100,5,1,0,0,100,102,3,22,11,0,101,99,1,0,0,0,102,
        105,1,0,0,0,103,101,1,0,0,0,103,104,1,0,0,0,104,107,1,0,0,0,105,
        103,1,0,0,0,106,97,1,0,0,0,106,98,1,0,0,0,107,11,1,0,0,0,108,109,
        5,22,0,0,109,114,3,24,12,0,110,111,5,1,0,0,111,113,3,24,12,0,112,
        110,1,0,0,0,113,116,1,0,0,0,114,112,1,0,0,0,114,115,1,0,0,0,115,
        117,1,0,0,0,116,114,1,0,0,0,117,118,5,23,0,0,118,13,1,0,0,0,119,
        120,5,22,0,0,120,125,3,22,11,0,121,122,5,1,0,0,122,124,3,22,11,0,
        123,121,1,0,0,0,124,127,1,0,0,0,125,123,1,0,0,0,125,126,1,0,0,0,
        126,128,1,0,0,0,127,125,1,0,0,0,128,129,5,23,0,0,129,15,1,0,0,0,
        130,131,5,12,0,0,131,132,3,18,9,0,132,17,1,0,0,0,133,146,3,20,10,
        0,134,136,3,20,10,0,135,134,1,0,0,0,136,137,1,0,0,0,137,135,1,0,
        0,0,137,138,1,0,0,0,138,141,1,0,0,0,139,140,7,0,0,0,140,142,3,20,
        10,0,141,139,1,0,0,0,142,143,1,0,0,0,143,141,1,0,0,0,143,144,1,0,
        0,0,144,146,1,0,0,0,145,133,1,0,0,0,145,135,1,0,0,0,146,19,1,0,0,
        0,147,148,3,22,11,0,148,149,3,26,13,0,149,150,3,24,12,0,150,21,1,
        0,0,0,151,156,7,1,0,0,152,153,5,1,0,0,153,155,7,1,0,0,154,152,1,
        0,0,0,155,158,1,0,0,0,156,154,1,0,0,0,156,157,1,0,0,0,157,23,1,0,
        0,0,158,156,1,0,0,0,159,160,7,2,0,0,160,25,1,0,0,0,161,162,7,3,0,
        0,162,27,1,0,0,0,21,31,37,39,43,57,59,62,64,70,76,84,90,94,103,106,
        114,125,137,143,145,156
    ]

class SQLParser ( Parser ):

    grammarFileName = "SQL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "'*'", "'='", "'<>'", "'<'", "'>'", 
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
    RULE_table_list = 4
    RULE_column_list = 5
    RULE_values_list = 6
    RULE_insert_column_list = 7
    RULE_where_clause = 8
    RULE_condition_list = 9
    RULE_expression = 10
    RULE_column = 11
    RULE_value = 12
    RULE_operator = 13

    ruleNames =  [ "sql_statement", "select_statement", "delete_statement", 
                   "insert_statement", "table_list", "column_list", "values_list", 
                   "insert_column_list", "where_clause", "condition_list", 
                   "expression", "column", "value", "operator" ]

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSql_statement" ):
                return visitor.visitSql_statement(self)
            else:
                return visitor.visitChildren(self)




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

        def table_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.Table_listContext)
            else:
                return self.getTypedRuleContext(SQLParser.Table_listContext,i)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelect_statement" ):
                return visitor.visitSelect_statement(self)
            else:
                return visitor.visitChildren(self)




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
                        self.table_list()
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

        def table_list(self):
            return self.getTypedRuleContext(SQLParser.Table_listContext,0)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDelete_statement" ):
                return visitor.visitDelete_statement(self)
            else:
                return visitor.visitChildren(self)




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
            self.table_list()
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

        def table_list(self):
            return self.getTypedRuleContext(SQLParser.Table_listContext,0)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInsert_statement" ):
                return visitor.visitInsert_statement(self)
            else:
                return visitor.visitChildren(self)




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
            self.table_list()
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


    class Table_listContext(ParserRuleContext):
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
            return SQLParser.RULE_table_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTable_list" ):
                listener.enterTable_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTable_list" ):
                listener.exitTable_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTable_list" ):
                return visitor.visitTable_list(self)
            else:
                return visitor.visitChildren(self)




    def table_list(self):

        localctx = SQLParser.Table_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_table_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 81
                    self.match(SQLParser.WORD)

                else:
                    raise NoViableAltException(self)
                self.state = 84 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 86
                self.match(SQLParser.T__0)
                self.state = 88 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 87
                        self.match(SQLParser.WORD)

                    else:
                        raise NoViableAltException(self)
                    self.state = 90 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

                self.state = 96
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColumn_list" ):
                return visitor.visitColumn_list(self)
            else:
                return visitor.visitChildren(self)




    def column_list(self):

        localctx = SQLParser.Column_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_column_list)
        self._la = 0 # Token type
        try:
            self.state = 106
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 97
                self.match(SQLParser.T__1)
                pass
            elif token in [9, 24, 25, 26]:
                self.enterOuterAlt(localctx, 2)
                self.state = 98
                self.column()
                self.state = 103
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==1:
                    self.state = 99
                    self.match(SQLParser.T__0)
                    self.state = 100
                    self.column()
                    self.state = 105
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValues_list" ):
                return visitor.visitValues_list(self)
            else:
                return visitor.visitChildren(self)




    def values_list(self):

        localctx = SQLParser.Values_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_values_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(SQLParser.OPENPAR)
            self.state = 109
            self.value()
            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 110
                self.match(SQLParser.T__0)
                self.state = 111
                self.value()
                self.state = 116
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 117
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInsert_column_list" ):
                return visitor.visitInsert_column_list(self)
            else:
                return visitor.visitChildren(self)




    def insert_column_list(self):

        localctx = SQLParser.Insert_column_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_insert_column_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(SQLParser.OPENPAR)
            self.state = 120
            self.column()
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 121
                self.match(SQLParser.T__0)
                self.state = 122
                self.column()
                self.state = 127
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 128
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

        def condition_list(self):
            return self.getTypedRuleContext(SQLParser.Condition_listContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_where_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhere_clause" ):
                listener.enterWhere_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhere_clause" ):
                listener.exitWhere_clause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhere_clause" ):
                return visitor.visitWhere_clause(self)
            else:
                return visitor.visitChildren(self)




    def where_clause(self):

        localctx = SQLParser.Where_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_where_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(SQLParser.WHERE)
            self.state = 131
            self.condition_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Condition_listContext(ParserRuleContext):
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
            return SQLParser.RULE_condition_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition_list" ):
                listener.enterCondition_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition_list" ):
                listener.exitCondition_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition_list" ):
                return visitor.visitCondition_list(self)
            else:
                return visitor.visitChildren(self)




    def condition_list(self):

        localctx = SQLParser.Condition_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_condition_list)
        self._la = 0 # Token type
        try:
            self.state = 145
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 135 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 134
                    self.expression()
                    self.state = 137 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 117441024) != 0)):
                        break

                self.state = 141 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 139
                    _la = self._input.LA(1)
                    if not(_la==13 or _la==14):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 140
                    self.expression()
                    self.state = 143 
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = SQLParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.column()
            self.state = 148
            self.operator()
            self.state = 149
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

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.STRING)
            else:
                return self.getToken(SQLParser.STRING, i)

        def TCNAME(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.TCNAME)
            else:
                return self.getToken(SQLParser.TCNAME, i)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.NUMBER)
            else:
                return self.getToken(SQLParser.NUMBER, i)

        def getRuleIndex(self):
            return SQLParser.RULE_column

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumn" ):
                listener.enterColumn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumn" ):
                listener.exitColumn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColumn" ):
                return visitor.visitColumn(self)
            else:
                return visitor.visitChildren(self)




    def column(self):

        localctx = SQLParser.ColumnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_column)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 117441024) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 156
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 152
                    self.match(SQLParser.T__0)
                    self.state = 153
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 117441024) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume() 
                self.state = 158
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperator" ):
                return visitor.visitOperator(self)
            else:
                return visitor.visitChildren(self)




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





