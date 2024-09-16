// Generated from /Applications/XAMPP/xamppfiles/htdocs/rdbms/src/parser/SQL.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class SQLParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, TCNAME=9, 
		SELECT=10, FROM=11, WHERE=12, AND=13, OR=14, SEMICOLON=15, DELETE=16, 
		INSERT=17, INTO=18, VALUES=19, NULL=20, DOT=21, OPENPAR=22, CLOSEPAR=23, 
		WORD=24, NUMBER=25, STRING=26, WS=27;
	public static final int
		RULE_sql_statement = 0, RULE_select_statement = 1, RULE_delete_statement = 2, 
		RULE_insert_statement = 3, RULE_column_list = 4, RULE_values_list = 5, 
		RULE_insert_column_list = 6, RULE_where_clause = 7, RULE_condition = 8, 
		RULE_expression = 9, RULE_column = 10, RULE_table = 11, RULE_value = 12, 
		RULE_operator = 13;
	private static String[] makeRuleNames() {
		return new String[] {
			"sql_statement", "select_statement", "delete_statement", "insert_statement", 
			"column_list", "values_list", "insert_column_list", "where_clause", "condition", 
			"expression", "column", "table", "value", "operator"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'*'", "','", "'='", "'<>'", "'<'", "'>'", "'<='", "'>='", null, 
			"'select'", "'from'", "'where'", "'and'", "'or'", "';'", "'delete'", 
			"'insert'", "'into'", "'values'", "'null'", "'.'", "'('", "')'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, "TCNAME", "SELECT", 
			"FROM", "WHERE", "AND", "OR", "SEMICOLON", "DELETE", "INSERT", "INTO", 
			"VALUES", "NULL", "DOT", "OPENPAR", "CLOSEPAR", "WORD", "NUMBER", "STRING", 
			"WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "SQL.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public SQLParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Sql_statementContext extends ParserRuleContext {
		public TerminalNode SEMICOLON() { return getToken(SQLParser.SEMICOLON, 0); }
		public TerminalNode EOF() { return getToken(SQLParser.EOF, 0); }
		public Select_statementContext select_statement() {
			return getRuleContext(Select_statementContext.class,0);
		}
		public Delete_statementContext delete_statement() {
			return getRuleContext(Delete_statementContext.class,0);
		}
		public Insert_statementContext insert_statement() {
			return getRuleContext(Insert_statementContext.class,0);
		}
		public Sql_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sql_statement; }
	}

	public final Sql_statementContext sql_statement() throws RecognitionException {
		Sql_statementContext _localctx = new Sql_statementContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_sql_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(31);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case SELECT:
				{
				setState(28);
				select_statement();
				}
				break;
			case DELETE:
				{
				setState(29);
				delete_statement();
				}
				break;
			case INSERT:
				{
				setState(30);
				insert_statement();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(33);
			match(SEMICOLON);
			setState(34);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Select_statementContext extends ParserRuleContext {
		public TerminalNode SELECT() { return getToken(SQLParser.SELECT, 0); }
		public Column_listContext column_list() {
			return getRuleContext(Column_listContext.class,0);
		}
		public TerminalNode FROM() { return getToken(SQLParser.FROM, 0); }
		public List<TableContext> table() {
			return getRuleContexts(TableContext.class);
		}
		public TableContext table(int i) {
			return getRuleContext(TableContext.class,i);
		}
		public List<TerminalNode> OPENPAR() { return getTokens(SQLParser.OPENPAR); }
		public TerminalNode OPENPAR(int i) {
			return getToken(SQLParser.OPENPAR, i);
		}
		public List<Select_statementContext> select_statement() {
			return getRuleContexts(Select_statementContext.class);
		}
		public Select_statementContext select_statement(int i) {
			return getRuleContext(Select_statementContext.class,i);
		}
		public List<TerminalNode> CLOSEPAR() { return getTokens(SQLParser.CLOSEPAR); }
		public TerminalNode CLOSEPAR(int i) {
			return getToken(SQLParser.CLOSEPAR, i);
		}
		public Where_clauseContext where_clause() {
			return getRuleContext(Where_clauseContext.class,0);
		}
		public Select_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_select_statement; }
	}

	public final Select_statementContext select_statement() throws RecognitionException {
		Select_statementContext _localctx = new Select_statementContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_select_statement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(36);
			match(SELECT);
			setState(37);
			column_list();
			setState(51);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==FROM) {
				{
				setState(38);
				match(FROM);
				setState(44); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					setState(44);
					_errHandler.sync(this);
					switch (_input.LA(1)) {
					case WORD:
						{
						setState(39);
						table();
						}
						break;
					case OPENPAR:
						{
						setState(40);
						match(OPENPAR);
						setState(41);
						select_statement();
						setState(42);
						match(CLOSEPAR);
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					}
					setState(46); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==OPENPAR || _la==WORD );
				setState(49);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==WHERE) {
					{
					setState(48);
					where_clause();
					}
				}

				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Delete_statementContext extends ParserRuleContext {
		public TerminalNode DELETE() { return getToken(SQLParser.DELETE, 0); }
		public TerminalNode FROM() { return getToken(SQLParser.FROM, 0); }
		public TableContext table() {
			return getRuleContext(TableContext.class,0);
		}
		public Where_clauseContext where_clause() {
			return getRuleContext(Where_clauseContext.class,0);
		}
		public Delete_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_delete_statement; }
	}

	public final Delete_statementContext delete_statement() throws RecognitionException {
		Delete_statementContext _localctx = new Delete_statementContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_delete_statement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(53);
			match(DELETE);
			setState(54);
			match(FROM);
			setState(55);
			table();
			setState(57);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WHERE) {
				{
				setState(56);
				where_clause();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Insert_statementContext extends ParserRuleContext {
		public TerminalNode INSERT() { return getToken(SQLParser.INSERT, 0); }
		public TerminalNode INTO() { return getToken(SQLParser.INTO, 0); }
		public TableContext table() {
			return getRuleContext(TableContext.class,0);
		}
		public TerminalNode VALUES() { return getToken(SQLParser.VALUES, 0); }
		public Values_listContext values_list() {
			return getRuleContext(Values_listContext.class,0);
		}
		public Insert_column_listContext insert_column_list() {
			return getRuleContext(Insert_column_listContext.class,0);
		}
		public Insert_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_insert_statement; }
	}

	public final Insert_statementContext insert_statement() throws RecognitionException {
		Insert_statementContext _localctx = new Insert_statementContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_insert_statement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(59);
			match(INSERT);
			setState(60);
			match(INTO);
			setState(61);
			table();
			setState(63);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==OPENPAR) {
				{
				setState(62);
				insert_column_list();
				}
			}

			setState(65);
			match(VALUES);
			setState(66);
			values_list();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Column_listContext extends ParserRuleContext {
		public List<ColumnContext> column() {
			return getRuleContexts(ColumnContext.class);
		}
		public ColumnContext column(int i) {
			return getRuleContext(ColumnContext.class,i);
		}
		public Column_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_column_list; }
	}

	public final Column_listContext column_list() throws RecognitionException {
		Column_listContext _localctx = new Column_listContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_column_list);
		int _la;
		try {
			setState(77);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__0:
				enterOuterAlt(_localctx, 1);
				{
				setState(68);
				match(T__0);
				}
				break;
			case TCNAME:
			case WORD:
				enterOuterAlt(_localctx, 2);
				{
				setState(69);
				column();
				setState(74);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__1) {
					{
					{
					setState(70);
					match(T__1);
					setState(71);
					column();
					}
					}
					setState(76);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Values_listContext extends ParserRuleContext {
		public TerminalNode OPENPAR() { return getToken(SQLParser.OPENPAR, 0); }
		public List<ValueContext> value() {
			return getRuleContexts(ValueContext.class);
		}
		public ValueContext value(int i) {
			return getRuleContext(ValueContext.class,i);
		}
		public TerminalNode CLOSEPAR() { return getToken(SQLParser.CLOSEPAR, 0); }
		public Values_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_values_list; }
	}

	public final Values_listContext values_list() throws RecognitionException {
		Values_listContext _localctx = new Values_listContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_values_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(79);
			match(OPENPAR);
			setState(80);
			value();
			setState(85);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__1) {
				{
				{
				setState(81);
				match(T__1);
				setState(82);
				value();
				}
				}
				setState(87);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(88);
			match(CLOSEPAR);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Insert_column_listContext extends ParserRuleContext {
		public TerminalNode OPENPAR() { return getToken(SQLParser.OPENPAR, 0); }
		public List<ColumnContext> column() {
			return getRuleContexts(ColumnContext.class);
		}
		public ColumnContext column(int i) {
			return getRuleContext(ColumnContext.class,i);
		}
		public TerminalNode CLOSEPAR() { return getToken(SQLParser.CLOSEPAR, 0); }
		public Insert_column_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_insert_column_list; }
	}

	public final Insert_column_listContext insert_column_list() throws RecognitionException {
		Insert_column_listContext _localctx = new Insert_column_listContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_insert_column_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(90);
			match(OPENPAR);
			setState(91);
			column();
			setState(96);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__1) {
				{
				{
				setState(92);
				match(T__1);
				setState(93);
				column();
				}
				}
				setState(98);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(99);
			match(CLOSEPAR);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Where_clauseContext extends ParserRuleContext {
		public TerminalNode WHERE() { return getToken(SQLParser.WHERE, 0); }
		public ConditionContext condition() {
			return getRuleContext(ConditionContext.class,0);
		}
		public Where_clauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_where_clause; }
	}

	public final Where_clauseContext where_clause() throws RecognitionException {
		Where_clauseContext _localctx = new Where_clauseContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_where_clause);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(101);
			match(WHERE);
			setState(102);
			condition();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ConditionContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public List<TerminalNode> AND() { return getTokens(SQLParser.AND); }
		public TerminalNode AND(int i) {
			return getToken(SQLParser.AND, i);
		}
		public List<TerminalNode> OR() { return getTokens(SQLParser.OR); }
		public TerminalNode OR(int i) {
			return getToken(SQLParser.OR, i);
		}
		public ConditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condition; }
	}

	public final ConditionContext condition() throws RecognitionException {
		ConditionContext _localctx = new ConditionContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_condition);
		int _la;
		try {
			setState(116);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(104);
				expression();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(106); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(105);
					expression();
					}
					}
					setState(108); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==TCNAME || _la==WORD );
				setState(112); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(110);
					_la = _input.LA(1);
					if ( !(_la==AND || _la==OR) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(111);
					expression();
					}
					}
					setState(114); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==AND || _la==OR );
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpressionContext extends ParserRuleContext {
		public ColumnContext column() {
			return getRuleContext(ColumnContext.class,0);
		}
		public OperatorContext operator() {
			return getRuleContext(OperatorContext.class,0);
		}
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(118);
			column();
			setState(119);
			operator();
			setState(120);
			value();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ColumnContext extends ParserRuleContext {
		public List<TerminalNode> WORD() { return getTokens(SQLParser.WORD); }
		public TerminalNode WORD(int i) {
			return getToken(SQLParser.WORD, i);
		}
		public List<TerminalNode> TCNAME() { return getTokens(SQLParser.TCNAME); }
		public TerminalNode TCNAME(int i) {
			return getToken(SQLParser.TCNAME, i);
		}
		public ColumnContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_column; }
	}

	public final ColumnContext column() throws RecognitionException {
		ColumnContext _localctx = new ColumnContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_column);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(122);
			_la = _input.LA(1);
			if ( !(_la==TCNAME || _la==WORD) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(127);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,14,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(123);
					match(T__1);
					setState(124);
					_la = _input.LA(1);
					if ( !(_la==TCNAME || _la==WORD) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					}
					} 
				}
				setState(129);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,14,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TableContext extends ParserRuleContext {
		public List<TerminalNode> WORD() { return getTokens(SQLParser.WORD); }
		public TerminalNode WORD(int i) {
			return getToken(SQLParser.WORD, i);
		}
		public TableContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_table; }
	}

	public final TableContext table() throws RecognitionException {
		TableContext _localctx = new TableContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_table);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(131); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					{
					setState(130);
					match(WORD);
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(133); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,15,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
			setState(143);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__1) {
				{
				{
				setState(135);
				match(T__1);
				setState(137); 
				_errHandler.sync(this);
				_alt = 1;
				do {
					switch (_alt) {
					case 1:
						{
						{
						setState(136);
						match(WORD);
						}
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					setState(139); 
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,16,_ctx);
				} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
				}
				}
				setState(145);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ValueContext extends ParserRuleContext {
		public TerminalNode STRING() { return getToken(SQLParser.STRING, 0); }
		public TerminalNode NUMBER() { return getToken(SQLParser.NUMBER, 0); }
		public TerminalNode NULL() { return getToken(SQLParser.NULL, 0); }
		public ValueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_value; }
	}

	public final ValueContext value() throws RecognitionException {
		ValueContext _localctx = new ValueContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_value);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(146);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 101711872L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OperatorContext extends ParserRuleContext {
		public OperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_operator; }
	}

	public final OperatorContext operator() throws RecognitionException {
		OperatorContext _localctx = new OperatorContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_operator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(148);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 504L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u001b\u0097\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001"+
		"\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004"+
		"\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007"+
		"\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b"+
		"\u0002\f\u0007\f\u0002\r\u0007\r\u0001\u0000\u0001\u0000\u0001\u0000\u0003"+
		"\u0000 \b\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0004\u0001-\b\u0001\u000b\u0001\f\u0001.\u0001\u0001\u0003\u0001"+
		"2\b\u0001\u0003\u00014\b\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0003\u0002:\b\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0003\u0003@\b\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0005\u0004I\b\u0004\n\u0004"+
		"\f\u0004L\t\u0004\u0003\u0004N\b\u0004\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0005\u0005T\b\u0005\n\u0005\f\u0005W\t\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0005\u0006"+
		"_\b\u0006\n\u0006\f\u0006b\t\u0006\u0001\u0006\u0001\u0006\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0004\bk\b\b\u000b\b\f\bl\u0001"+
		"\b\u0001\b\u0004\bq\b\b\u000b\b\f\br\u0003\bu\b\b\u0001\t\u0001\t\u0001"+
		"\t\u0001\t\u0001\n\u0001\n\u0001\n\u0005\n~\b\n\n\n\f\n\u0081\t\n\u0001"+
		"\u000b\u0004\u000b\u0084\b\u000b\u000b\u000b\f\u000b\u0085\u0001\u000b"+
		"\u0001\u000b\u0004\u000b\u008a\b\u000b\u000b\u000b\f\u000b\u008b\u0005"+
		"\u000b\u008e\b\u000b\n\u000b\f\u000b\u0091\t\u000b\u0001\f\u0001\f\u0001"+
		"\r\u0001\r\u0001\r\u0000\u0000\u000e\u0000\u0002\u0004\u0006\b\n\f\u000e"+
		"\u0010\u0012\u0014\u0016\u0018\u001a\u0000\u0004\u0001\u0000\r\u000e\u0002"+
		"\u0000\t\t\u0018\u0018\u0002\u0000\u0014\u0014\u0019\u001a\u0001\u0000"+
		"\u0003\b\u009b\u0000\u001f\u0001\u0000\u0000\u0000\u0002$\u0001\u0000"+
		"\u0000\u0000\u00045\u0001\u0000\u0000\u0000\u0006;\u0001\u0000\u0000\u0000"+
		"\bM\u0001\u0000\u0000\u0000\nO\u0001\u0000\u0000\u0000\fZ\u0001\u0000"+
		"\u0000\u0000\u000ee\u0001\u0000\u0000\u0000\u0010t\u0001\u0000\u0000\u0000"+
		"\u0012v\u0001\u0000\u0000\u0000\u0014z\u0001\u0000\u0000\u0000\u0016\u0083"+
		"\u0001\u0000\u0000\u0000\u0018\u0092\u0001\u0000\u0000\u0000\u001a\u0094"+
		"\u0001\u0000\u0000\u0000\u001c \u0003\u0002\u0001\u0000\u001d \u0003\u0004"+
		"\u0002\u0000\u001e \u0003\u0006\u0003\u0000\u001f\u001c\u0001\u0000\u0000"+
		"\u0000\u001f\u001d\u0001\u0000\u0000\u0000\u001f\u001e\u0001\u0000\u0000"+
		"\u0000 !\u0001\u0000\u0000\u0000!\"\u0005\u000f\u0000\u0000\"#\u0005\u0000"+
		"\u0000\u0001#\u0001\u0001\u0000\u0000\u0000$%\u0005\n\u0000\u0000%3\u0003"+
		"\b\u0004\u0000&,\u0005\u000b\u0000\u0000\'-\u0003\u0016\u000b\u0000()"+
		"\u0005\u0016\u0000\u0000)*\u0003\u0002\u0001\u0000*+\u0005\u0017\u0000"+
		"\u0000+-\u0001\u0000\u0000\u0000,\'\u0001\u0000\u0000\u0000,(\u0001\u0000"+
		"\u0000\u0000-.\u0001\u0000\u0000\u0000.,\u0001\u0000\u0000\u0000./\u0001"+
		"\u0000\u0000\u0000/1\u0001\u0000\u0000\u000002\u0003\u000e\u0007\u0000"+
		"10\u0001\u0000\u0000\u000012\u0001\u0000\u0000\u000024\u0001\u0000\u0000"+
		"\u00003&\u0001\u0000\u0000\u000034\u0001\u0000\u0000\u00004\u0003\u0001"+
		"\u0000\u0000\u000056\u0005\u0010\u0000\u000067\u0005\u000b\u0000\u0000"+
		"79\u0003\u0016\u000b\u00008:\u0003\u000e\u0007\u000098\u0001\u0000\u0000"+
		"\u00009:\u0001\u0000\u0000\u0000:\u0005\u0001\u0000\u0000\u0000;<\u0005"+
		"\u0011\u0000\u0000<=\u0005\u0012\u0000\u0000=?\u0003\u0016\u000b\u0000"+
		">@\u0003\f\u0006\u0000?>\u0001\u0000\u0000\u0000?@\u0001\u0000\u0000\u0000"+
		"@A\u0001\u0000\u0000\u0000AB\u0005\u0013\u0000\u0000BC\u0003\n\u0005\u0000"+
		"C\u0007\u0001\u0000\u0000\u0000DN\u0005\u0001\u0000\u0000EJ\u0003\u0014"+
		"\n\u0000FG\u0005\u0002\u0000\u0000GI\u0003\u0014\n\u0000HF\u0001\u0000"+
		"\u0000\u0000IL\u0001\u0000\u0000\u0000JH\u0001\u0000\u0000\u0000JK\u0001"+
		"\u0000\u0000\u0000KN\u0001\u0000\u0000\u0000LJ\u0001\u0000\u0000\u0000"+
		"MD\u0001\u0000\u0000\u0000ME\u0001\u0000\u0000\u0000N\t\u0001\u0000\u0000"+
		"\u0000OP\u0005\u0016\u0000\u0000PU\u0003\u0018\f\u0000QR\u0005\u0002\u0000"+
		"\u0000RT\u0003\u0018\f\u0000SQ\u0001\u0000\u0000\u0000TW\u0001\u0000\u0000"+
		"\u0000US\u0001\u0000\u0000\u0000UV\u0001\u0000\u0000\u0000VX\u0001\u0000"+
		"\u0000\u0000WU\u0001\u0000\u0000\u0000XY\u0005\u0017\u0000\u0000Y\u000b"+
		"\u0001\u0000\u0000\u0000Z[\u0005\u0016\u0000\u0000[`\u0003\u0014\n\u0000"+
		"\\]\u0005\u0002\u0000\u0000]_\u0003\u0014\n\u0000^\\\u0001\u0000\u0000"+
		"\u0000_b\u0001\u0000\u0000\u0000`^\u0001\u0000\u0000\u0000`a\u0001\u0000"+
		"\u0000\u0000ac\u0001\u0000\u0000\u0000b`\u0001\u0000\u0000\u0000cd\u0005"+
		"\u0017\u0000\u0000d\r\u0001\u0000\u0000\u0000ef\u0005\f\u0000\u0000fg"+
		"\u0003\u0010\b\u0000g\u000f\u0001\u0000\u0000\u0000hu\u0003\u0012\t\u0000"+
		"ik\u0003\u0012\t\u0000ji\u0001\u0000\u0000\u0000kl\u0001\u0000\u0000\u0000"+
		"lj\u0001\u0000\u0000\u0000lm\u0001\u0000\u0000\u0000mp\u0001\u0000\u0000"+
		"\u0000no\u0007\u0000\u0000\u0000oq\u0003\u0012\t\u0000pn\u0001\u0000\u0000"+
		"\u0000qr\u0001\u0000\u0000\u0000rp\u0001\u0000\u0000\u0000rs\u0001\u0000"+
		"\u0000\u0000su\u0001\u0000\u0000\u0000th\u0001\u0000\u0000\u0000tj\u0001"+
		"\u0000\u0000\u0000u\u0011\u0001\u0000\u0000\u0000vw\u0003\u0014\n\u0000"+
		"wx\u0003\u001a\r\u0000xy\u0003\u0018\f\u0000y\u0013\u0001\u0000\u0000"+
		"\u0000z\u007f\u0007\u0001\u0000\u0000{|\u0005\u0002\u0000\u0000|~\u0007"+
		"\u0001\u0000\u0000}{\u0001\u0000\u0000\u0000~\u0081\u0001\u0000\u0000"+
		"\u0000\u007f}\u0001\u0000\u0000\u0000\u007f\u0080\u0001\u0000\u0000\u0000"+
		"\u0080\u0015\u0001\u0000\u0000\u0000\u0081\u007f\u0001\u0000\u0000\u0000"+
		"\u0082\u0084\u0005\u0018\u0000\u0000\u0083\u0082\u0001\u0000\u0000\u0000"+
		"\u0084\u0085\u0001\u0000\u0000\u0000\u0085\u0083\u0001\u0000\u0000\u0000"+
		"\u0085\u0086\u0001\u0000\u0000\u0000\u0086\u008f\u0001\u0000\u0000\u0000"+
		"\u0087\u0089\u0005\u0002\u0000\u0000\u0088\u008a\u0005\u0018\u0000\u0000"+
		"\u0089\u0088\u0001\u0000\u0000\u0000\u008a\u008b\u0001\u0000\u0000\u0000"+
		"\u008b\u0089\u0001\u0000\u0000\u0000\u008b\u008c\u0001\u0000\u0000\u0000"+
		"\u008c\u008e\u0001\u0000\u0000\u0000\u008d\u0087\u0001\u0000\u0000\u0000"+
		"\u008e\u0091\u0001\u0000\u0000\u0000\u008f\u008d\u0001\u0000\u0000\u0000"+
		"\u008f\u0090\u0001\u0000\u0000\u0000\u0090\u0017\u0001\u0000\u0000\u0000"+
		"\u0091\u008f\u0001\u0000\u0000\u0000\u0092\u0093\u0007\u0002\u0000\u0000"+
		"\u0093\u0019\u0001\u0000\u0000\u0000\u0094\u0095\u0007\u0003\u0000\u0000"+
		"\u0095\u001b\u0001\u0000\u0000\u0000\u0012\u001f,.139?JMU`lrt\u007f\u0085"+
		"\u008b\u008f";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}