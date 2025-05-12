// Generated from /home/jackcui/Arch/zeo-2.0/EasyCGRA/EasyCGRAParser.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class EasyCGRAParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		ADD=1, ADDI=2, SUB=3, SUBI=4, MUL=5, DIV=6, MAC=7, INC=8, LLS=9, LRS=10, 
		OR=11, AND=12, XOR=13, NOT=14, FADD=15, FSUB=16, FMUL=17, FDIV=18, FMAC=19, 
		BEQ=20, MOV=21, MAC_CONST_ADD=22, LOAD=23, STORE=24, ENTRY=25, ENTRY_ARROW=26, 
		RIGHT_ARROW=27, N=28, IMM=29, MEM=30, DECIMAL_LITERAL=31, HEX_LITERAL=32, 
		OCT_LITERAL=33, BINARY_LITERAL=34, FLOAT_LITERAL=35, HEX_FLOAT_LITERAL=36, 
		BOOL_LITERAL=37, CHAR_LITERAL=38, STRING_LITERAL=39, TEXT_BLOCK=40, NULL_LITERAL=41, 
		LPAREN=42, RPAREN=43, LBRACE=44, RBRACE=45, LBRACK=46, RBRACK=47, SEMI=48, 
		COMMA=49, DOT=50, COLON=51, AND_PRED=52, OR_PRED=53, WS=54, COMMENT=55, 
		LINE_COMMENT=56, IDENTIFIER=57;
	public static final int
		RULE_compilationUnit = 0, RULE_entryBlock = 1, RULE_entryHead = 2, RULE_instList = 3, 
		RULE_inst = 4, RULE_label = 5, RULE_normalInst = 6, RULE_operandList = 7, 
		RULE_operand = 8, RULE_idList = 9, RULE_predTag = 10, RULE_opCode = 11;
	private static String[] makeRuleNames() {
		return new String[] {
			"compilationUnit", "entryBlock", "entryHead", "instList", "inst", "label", 
			"normalInst", "operandList", "operand", "idList", "predTag", "opCode"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'ADD'", "'ADDI'", "'SUB'", "'SUBI'", "'MUL'", "'DIV'", "'MAC'", 
			"'INC'", "'LLS'", "'LRS'", "'OR'", "'AND'", "'XOR'", "'NOT'", "'FADD'", 
			"'FSUB'", "'FMUL'", "'FDIV'", "'FMAC'", "'BEQ'", "'MOV'", "'MAC_CONST_ADD'", 
			"'LOAD'", "'STORE'", "'Entry'", "'=>'", "'->'", "'\\n'", "'IMM'", "'MEM'", 
			null, null, null, null, null, null, null, null, null, null, "'null'", 
			"'('", "')'", "'{'", "'}'", "'['", "']'", "';'", "','", "'.'", "':'", 
			"'!'", "'^'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "ADD", "ADDI", "SUB", "SUBI", "MUL", "DIV", "MAC", "INC", "LLS", 
			"LRS", "OR", "AND", "XOR", "NOT", "FADD", "FSUB", "FMUL", "FDIV", "FMAC", 
			"BEQ", "MOV", "MAC_CONST_ADD", "LOAD", "STORE", "ENTRY", "ENTRY_ARROW", 
			"RIGHT_ARROW", "N", "IMM", "MEM", "DECIMAL_LITERAL", "HEX_LITERAL", "OCT_LITERAL", 
			"BINARY_LITERAL", "FLOAT_LITERAL", "HEX_FLOAT_LITERAL", "BOOL_LITERAL", 
			"CHAR_LITERAL", "STRING_LITERAL", "TEXT_BLOCK", "NULL_LITERAL", "LPAREN", 
			"RPAREN", "LBRACE", "RBRACE", "LBRACK", "RBRACK", "SEMI", "COMMA", "DOT", 
			"COLON", "AND_PRED", "OR_PRED", "WS", "COMMENT", "LINE_COMMENT", "IDENTIFIER"
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
	public String getGrammarFileName() { return "EasyCGRAParser.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public EasyCGRAParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CompilationUnitContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(EasyCGRAParser.EOF, 0); }
		public List<EntryBlockContext> entryBlock() {
			return getRuleContexts(EntryBlockContext.class);
		}
		public EntryBlockContext entryBlock(int i) {
			return getRuleContext(EntryBlockContext.class,i);
		}
		public CompilationUnitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_compilationUnit; }
	}

	public final CompilationUnitContext compilationUnit() throws RecognitionException {
		CompilationUnitContext _localctx = new CompilationUnitContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_compilationUnit);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(27);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ENTRY) {
				{
				{
				setState(24);
				entryBlock();
				}
				}
				setState(29);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(30);
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
	public static class EntryBlockContext extends ParserRuleContext {
		public EntryHeadContext entryHead() {
			return getRuleContext(EntryHeadContext.class,0);
		}
		public TerminalNode LBRACE() { return getToken(EasyCGRAParser.LBRACE, 0); }
		public InstListContext instList() {
			return getRuleContext(InstListContext.class,0);
		}
		public TerminalNode RBRACE() { return getToken(EasyCGRAParser.RBRACE, 0); }
		public EntryBlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_entryBlock; }
	}

	public final EntryBlockContext entryBlock() throws RecognitionException {
		EntryBlockContext _localctx = new EntryBlockContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_entryBlock);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(32);
			entryHead();
			setState(33);
			match(LBRACE);
			setState(34);
			instList();
			setState(35);
			match(RBRACE);
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
	public static class EntryHeadContext extends ParserRuleContext {
		public TerminalNode ENTRY() { return getToken(EasyCGRAParser.ENTRY, 0); }
		public TerminalNode ENTRY_ARROW() { return getToken(EasyCGRAParser.ENTRY_ARROW, 0); }
		public OperandListContext operandList() {
			return getRuleContext(OperandListContext.class,0);
		}
		public EntryHeadContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_entryHead; }
	}

	public final EntryHeadContext entryHead() throws RecognitionException {
		EntryHeadContext _localctx = new EntryHeadContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_entryHead);
		try {
			setState(43);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(37);
				match(ENTRY);
				setState(38);
				match(ENTRY_ARROW);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(39);
				match(ENTRY);
				setState(40);
				operandList();
				setState(41);
				match(ENTRY_ARROW);
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
	public static class InstListContext extends ParserRuleContext {
		public List<InstContext> inst() {
			return getRuleContexts(InstContext.class);
		}
		public InstContext inst(int i) {
			return getRuleContext(InstContext.class,i);
		}
		public InstListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_instList; }
	}

	public final InstListContext instList() throws RecognitionException {
		InstListContext _localctx = new InstListContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_instList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(48);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 157713949506142206L) != 0)) {
				{
				{
				setState(45);
				inst();
				}
				}
				setState(50);
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
	public static class InstContext extends ParserRuleContext {
		public TerminalNode LBRACE() { return getToken(EasyCGRAParser.LBRACE, 0); }
		public TerminalNode RBRACE() { return getToken(EasyCGRAParser.RBRACE, 0); }
		public List<NormalInstContext> normalInst() {
			return getRuleContexts(NormalInstContext.class);
		}
		public NormalInstContext normalInst(int i) {
			return getRuleContext(NormalInstContext.class,i);
		}
		public LabelContext label() {
			return getRuleContext(LabelContext.class,0);
		}
		public InstContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_inst; }
	}

	public final InstContext inst() throws RecognitionException {
		InstContext _localctx = new InstContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_inst);
		int _la;
		try {
			setState(61);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(51);
				match(LBRACE);
				setState(55);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 157696357320097790L) != 0)) {
					{
					{
					setState(52);
					normalInst();
					}
					}
					setState(57);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(58);
				match(RBRACE);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(59);
				normalInst();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(60);
				label();
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
	public static class LabelContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(EasyCGRAParser.IDENTIFIER, 0); }
		public TerminalNode COLON() { return getToken(EasyCGRAParser.COLON, 0); }
		public LabelContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_label; }
	}

	public final LabelContext label() throws RecognitionException {
		LabelContext _localctx = new LabelContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_label);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(63);
			match(IDENTIFIER);
			setState(64);
			match(COLON);
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
	public static class NormalInstContext extends ParserRuleContext {
		public OpCodeContext opCode() {
			return getRuleContext(OpCodeContext.class,0);
		}
		public TerminalNode COMMA() { return getToken(EasyCGRAParser.COMMA, 0); }
		public List<OperandListContext> operandList() {
			return getRuleContexts(OperandListContext.class);
		}
		public OperandListContext operandList(int i) {
			return getRuleContext(OperandListContext.class,i);
		}
		public TerminalNode RIGHT_ARROW() { return getToken(EasyCGRAParser.RIGHT_ARROW, 0); }
		public NormalInstContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_normalInst; }
	}

	public final NormalInstContext normalInst() throws RecognitionException {
		NormalInstContext _localctx = new NormalInstContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_normalInst);
		try {
			setState(80);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(66);
				opCode();
				setState(67);
				match(COMMA);
				setState(68);
				operandList();
				setState(69);
				match(RIGHT_ARROW);
				setState(70);
				operandList();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(72);
				operandList();
				setState(73);
				match(RIGHT_ARROW);
				setState(74);
				operandList();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(76);
				opCode();
				setState(77);
				match(COMMA);
				setState(78);
				operandList();
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
	public static class OperandListContext extends ParserRuleContext {
		public List<OperandContext> operand() {
			return getRuleContexts(OperandContext.class);
		}
		public OperandContext operand(int i) {
			return getRuleContext(OperandContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(EasyCGRAParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(EasyCGRAParser.COMMA, i);
		}
		public OperandListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_operandList; }
	}

	public final OperandListContext operandList() throws RecognitionException {
		OperandListContext _localctx = new OperandListContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_operandList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(82);
			operand();
			setState(87);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(83);
				match(COMMA);
				setState(84);
				operand();
				}
				}
				setState(89);
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
	public static class OperandContext extends ParserRuleContext {
		public PredTagContext predTag() {
			return getRuleContext(PredTagContext.class,0);
		}
		public TerminalNode LBRACK() { return getToken(EasyCGRAParser.LBRACK, 0); }
		public IdListContext idList() {
			return getRuleContext(IdListContext.class,0);
		}
		public TerminalNode RBRACK() { return getToken(EasyCGRAParser.RBRACK, 0); }
		public TerminalNode IMM() { return getToken(EasyCGRAParser.IMM, 0); }
		public TerminalNode DECIMAL_LITERAL() { return getToken(EasyCGRAParser.DECIMAL_LITERAL, 0); }
		public TerminalNode OCT_LITERAL() { return getToken(EasyCGRAParser.OCT_LITERAL, 0); }
		public TerminalNode HEX_LITERAL() { return getToken(EasyCGRAParser.HEX_LITERAL, 0); }
		public TerminalNode BINARY_LITERAL() { return getToken(EasyCGRAParser.BINARY_LITERAL, 0); }
		public TerminalNode FLOAT_LITERAL() { return getToken(EasyCGRAParser.FLOAT_LITERAL, 0); }
		public TerminalNode MEM() { return getToken(EasyCGRAParser.MEM, 0); }
		public LabelContext label() {
			return getRuleContext(LabelContext.class,0);
		}
		public OperandContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_operand; }
	}

	public final OperandContext operand() throws RecognitionException {
		OperandContext _localctx = new OperandContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_operand);
		try {
			setState(128);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(90);
				predTag();
				setState(91);
				match(LBRACK);
				setState(92);
				idList();
				setState(93);
				match(RBRACK);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(95);
				match(IMM);
				setState(96);
				match(LBRACK);
				setState(97);
				match(DECIMAL_LITERAL);
				setState(98);
				match(RBRACK);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(99);
				match(IMM);
				setState(100);
				match(LBRACK);
				setState(101);
				match(OCT_LITERAL);
				setState(102);
				match(RBRACK);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(103);
				match(IMM);
				setState(104);
				match(LBRACK);
				setState(105);
				match(HEX_LITERAL);
				setState(106);
				match(RBRACK);
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(107);
				match(IMM);
				setState(108);
				match(LBRACK);
				setState(109);
				match(BINARY_LITERAL);
				setState(110);
				match(RBRACK);
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(111);
				match(IMM);
				setState(112);
				match(LBRACK);
				setState(113);
				match(FLOAT_LITERAL);
				setState(114);
				match(RBRACK);
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(115);
				predTag();
				setState(116);
				match(MEM);
				setState(117);
				match(LBRACK);
				setState(118);
				idList();
				setState(119);
				match(RBRACK);
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(121);
				predTag();
				setState(122);
				match(MEM);
				setState(123);
				match(LBRACK);
				setState(124);
				match(HEX_LITERAL);
				setState(125);
				match(RBRACK);
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(127);
				label();
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
	public static class IdListContext extends ParserRuleContext {
		public List<TerminalNode> IDENTIFIER() { return getTokens(EasyCGRAParser.IDENTIFIER); }
		public TerminalNode IDENTIFIER(int i) {
			return getToken(EasyCGRAParser.IDENTIFIER, i);
		}
		public List<TerminalNode> COMMA() { return getTokens(EasyCGRAParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(EasyCGRAParser.COMMA, i);
		}
		public IdListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_idList; }
	}

	public final IdListContext idList() throws RecognitionException {
		IdListContext _localctx = new IdListContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_idList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(130);
			match(IDENTIFIER);
			setState(135);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(131);
				match(COMMA);
				setState(132);
				match(IDENTIFIER);
				}
				}
				setState(137);
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
	public static class PredTagContext extends ParserRuleContext {
		public TerminalNode AND_PRED() { return getToken(EasyCGRAParser.AND_PRED, 0); }
		public TerminalNode OR_PRED() { return getToken(EasyCGRAParser.OR_PRED, 0); }
		public PredTagContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_predTag; }
	}

	public final PredTagContext predTag() throws RecognitionException {
		PredTagContext _localctx = new PredTagContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_predTag);
		try {
			setState(141);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case AND_PRED:
				enterOuterAlt(_localctx, 1);
				{
				setState(138);
				match(AND_PRED);
				}
				break;
			case OR_PRED:
				enterOuterAlt(_localctx, 2);
				{
				setState(139);
				match(OR_PRED);
				}
				break;
			case MEM:
			case LBRACK:
				enterOuterAlt(_localctx, 3);
				{
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
	public static class OpCodeContext extends ParserRuleContext {
		public TerminalNode ADD() { return getToken(EasyCGRAParser.ADD, 0); }
		public TerminalNode ADDI() { return getToken(EasyCGRAParser.ADDI, 0); }
		public TerminalNode SUB() { return getToken(EasyCGRAParser.SUB, 0); }
		public TerminalNode SUBI() { return getToken(EasyCGRAParser.SUBI, 0); }
		public TerminalNode MUL() { return getToken(EasyCGRAParser.MUL, 0); }
		public TerminalNode DIV() { return getToken(EasyCGRAParser.DIV, 0); }
		public TerminalNode MAC() { return getToken(EasyCGRAParser.MAC, 0); }
		public TerminalNode INC() { return getToken(EasyCGRAParser.INC, 0); }
		public TerminalNode LLS() { return getToken(EasyCGRAParser.LLS, 0); }
		public TerminalNode LRS() { return getToken(EasyCGRAParser.LRS, 0); }
		public TerminalNode OR() { return getToken(EasyCGRAParser.OR, 0); }
		public TerminalNode AND() { return getToken(EasyCGRAParser.AND, 0); }
		public TerminalNode XOR() { return getToken(EasyCGRAParser.XOR, 0); }
		public TerminalNode NOT() { return getToken(EasyCGRAParser.NOT, 0); }
		public TerminalNode FADD() { return getToken(EasyCGRAParser.FADD, 0); }
		public TerminalNode FSUB() { return getToken(EasyCGRAParser.FSUB, 0); }
		public TerminalNode FMUL() { return getToken(EasyCGRAParser.FMUL, 0); }
		public TerminalNode FDIV() { return getToken(EasyCGRAParser.FDIV, 0); }
		public TerminalNode FMAC() { return getToken(EasyCGRAParser.FMAC, 0); }
		public TerminalNode MOV() { return getToken(EasyCGRAParser.MOV, 0); }
		public TerminalNode MAC_CONST_ADD() { return getToken(EasyCGRAParser.MAC_CONST_ADD, 0); }
		public OpCodeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_opCode; }
	}

	public final OpCodeContext opCode() throws RecognitionException {
		OpCodeContext _localctx = new OpCodeContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_opCode);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(143);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 7340030L) != 0)) ) {
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
		"\u0004\u00019\u0092\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0001"+
		"\u0000\u0005\u0000\u001a\b\u0000\n\u0000\f\u0000\u001d\t\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0003\u0002,\b\u0002\u0001\u0003\u0005\u0003/\b\u0003\n\u0003\f\u0003"+
		"2\t\u0003\u0001\u0004\u0001\u0004\u0005\u00046\b\u0004\n\u0004\f\u0004"+
		"9\t\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0003\u0004>\b\u0004\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0003\u0006Q\b"+
		"\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0005\u0007V\b\u0007\n\u0007"+
		"\f\u0007Y\t\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0001\b\u0001\b\u0001\b\u0003\b\u0081\b\b\u0001\t\u0001\t\u0001"+
		"\t\u0005\t\u0086\b\t\n\t\f\t\u0089\t\t\u0001\n\u0001\n\u0001\n\u0003\n"+
		"\u008e\b\n\u0001\u000b\u0001\u000b\u0001\u000b\u0000\u0000\f\u0000\u0002"+
		"\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0000\u0001\u0002\u0000"+
		"\u0001\u0013\u0015\u0016\u0099\u0000\u001b\u0001\u0000\u0000\u0000\u0002"+
		" \u0001\u0000\u0000\u0000\u0004+\u0001\u0000\u0000\u0000\u00060\u0001"+
		"\u0000\u0000\u0000\b=\u0001\u0000\u0000\u0000\n?\u0001\u0000\u0000\u0000"+
		"\fP\u0001\u0000\u0000\u0000\u000eR\u0001\u0000\u0000\u0000\u0010\u0080"+
		"\u0001\u0000\u0000\u0000\u0012\u0082\u0001\u0000\u0000\u0000\u0014\u008d"+
		"\u0001\u0000\u0000\u0000\u0016\u008f\u0001\u0000\u0000\u0000\u0018\u001a"+
		"\u0003\u0002\u0001\u0000\u0019\u0018\u0001\u0000\u0000\u0000\u001a\u001d"+
		"\u0001\u0000\u0000\u0000\u001b\u0019\u0001\u0000\u0000\u0000\u001b\u001c"+
		"\u0001\u0000\u0000\u0000\u001c\u001e\u0001\u0000\u0000\u0000\u001d\u001b"+
		"\u0001\u0000\u0000\u0000\u001e\u001f\u0005\u0000\u0000\u0001\u001f\u0001"+
		"\u0001\u0000\u0000\u0000 !\u0003\u0004\u0002\u0000!\"\u0005,\u0000\u0000"+
		"\"#\u0003\u0006\u0003\u0000#$\u0005-\u0000\u0000$\u0003\u0001\u0000\u0000"+
		"\u0000%&\u0005\u0019\u0000\u0000&,\u0005\u001a\u0000\u0000\'(\u0005\u0019"+
		"\u0000\u0000()\u0003\u000e\u0007\u0000)*\u0005\u001a\u0000\u0000*,\u0001"+
		"\u0000\u0000\u0000+%\u0001\u0000\u0000\u0000+\'\u0001\u0000\u0000\u0000"+
		",\u0005\u0001\u0000\u0000\u0000-/\u0003\b\u0004\u0000.-\u0001\u0000\u0000"+
		"\u0000/2\u0001\u0000\u0000\u00000.\u0001\u0000\u0000\u000001\u0001\u0000"+
		"\u0000\u00001\u0007\u0001\u0000\u0000\u000020\u0001\u0000\u0000\u0000"+
		"37\u0005,\u0000\u000046\u0003\f\u0006\u000054\u0001\u0000\u0000\u0000"+
		"69\u0001\u0000\u0000\u000075\u0001\u0000\u0000\u000078\u0001\u0000\u0000"+
		"\u00008:\u0001\u0000\u0000\u000097\u0001\u0000\u0000\u0000:>\u0005-\u0000"+
		"\u0000;>\u0003\f\u0006\u0000<>\u0003\n\u0005\u0000=3\u0001\u0000\u0000"+
		"\u0000=;\u0001\u0000\u0000\u0000=<\u0001\u0000\u0000\u0000>\t\u0001\u0000"+
		"\u0000\u0000?@\u00059\u0000\u0000@A\u00053\u0000\u0000A\u000b\u0001\u0000"+
		"\u0000\u0000BC\u0003\u0016\u000b\u0000CD\u00051\u0000\u0000DE\u0003\u000e"+
		"\u0007\u0000EF\u0005\u001b\u0000\u0000FG\u0003\u000e\u0007\u0000GQ\u0001"+
		"\u0000\u0000\u0000HI\u0003\u000e\u0007\u0000IJ\u0005\u001b\u0000\u0000"+
		"JK\u0003\u000e\u0007\u0000KQ\u0001\u0000\u0000\u0000LM\u0003\u0016\u000b"+
		"\u0000MN\u00051\u0000\u0000NO\u0003\u000e\u0007\u0000OQ\u0001\u0000\u0000"+
		"\u0000PB\u0001\u0000\u0000\u0000PH\u0001\u0000\u0000\u0000PL\u0001\u0000"+
		"\u0000\u0000Q\r\u0001\u0000\u0000\u0000RW\u0003\u0010\b\u0000ST\u0005"+
		"1\u0000\u0000TV\u0003\u0010\b\u0000US\u0001\u0000\u0000\u0000VY\u0001"+
		"\u0000\u0000\u0000WU\u0001\u0000\u0000\u0000WX\u0001\u0000\u0000\u0000"+
		"X\u000f\u0001\u0000\u0000\u0000YW\u0001\u0000\u0000\u0000Z[\u0003\u0014"+
		"\n\u0000[\\\u0005.\u0000\u0000\\]\u0003\u0012\t\u0000]^\u0005/\u0000\u0000"+
		"^\u0081\u0001\u0000\u0000\u0000_`\u0005\u001d\u0000\u0000`a\u0005.\u0000"+
		"\u0000ab\u0005\u001f\u0000\u0000b\u0081\u0005/\u0000\u0000cd\u0005\u001d"+
		"\u0000\u0000de\u0005.\u0000\u0000ef\u0005!\u0000\u0000f\u0081\u0005/\u0000"+
		"\u0000gh\u0005\u001d\u0000\u0000hi\u0005.\u0000\u0000ij\u0005 \u0000\u0000"+
		"j\u0081\u0005/\u0000\u0000kl\u0005\u001d\u0000\u0000lm\u0005.\u0000\u0000"+
		"mn\u0005\"\u0000\u0000n\u0081\u0005/\u0000\u0000op\u0005\u001d\u0000\u0000"+
		"pq\u0005.\u0000\u0000qr\u0005#\u0000\u0000r\u0081\u0005/\u0000\u0000s"+
		"t\u0003\u0014\n\u0000tu\u0005\u001e\u0000\u0000uv\u0005.\u0000\u0000v"+
		"w\u0003\u0012\t\u0000wx\u0005/\u0000\u0000x\u0081\u0001\u0000\u0000\u0000"+
		"yz\u0003\u0014\n\u0000z{\u0005\u001e\u0000\u0000{|\u0005.\u0000\u0000"+
		"|}\u0005 \u0000\u0000}~\u0005/\u0000\u0000~\u0081\u0001\u0000\u0000\u0000"+
		"\u007f\u0081\u0003\n\u0005\u0000\u0080Z\u0001\u0000\u0000\u0000\u0080"+
		"_\u0001\u0000\u0000\u0000\u0080c\u0001\u0000\u0000\u0000\u0080g\u0001"+
		"\u0000\u0000\u0000\u0080k\u0001\u0000\u0000\u0000\u0080o\u0001\u0000\u0000"+
		"\u0000\u0080s\u0001\u0000\u0000\u0000\u0080y\u0001\u0000\u0000\u0000\u0080"+
		"\u007f\u0001\u0000\u0000\u0000\u0081\u0011\u0001\u0000\u0000\u0000\u0082"+
		"\u0087\u00059\u0000\u0000\u0083\u0084\u00051\u0000\u0000\u0084\u0086\u0005"+
		"9\u0000\u0000\u0085\u0083\u0001\u0000\u0000\u0000\u0086\u0089\u0001\u0000"+
		"\u0000\u0000\u0087\u0085\u0001\u0000\u0000\u0000\u0087\u0088\u0001\u0000"+
		"\u0000\u0000\u0088\u0013\u0001\u0000\u0000\u0000\u0089\u0087\u0001\u0000"+
		"\u0000\u0000\u008a\u008e\u00054\u0000\u0000\u008b\u008e\u00055\u0000\u0000"+
		"\u008c\u008e\u0001\u0000\u0000\u0000\u008d\u008a\u0001\u0000\u0000\u0000"+
		"\u008d\u008b\u0001\u0000\u0000\u0000\u008d\u008c\u0001\u0000\u0000\u0000"+
		"\u008e\u0015\u0001\u0000\u0000\u0000\u008f\u0090\u0007\u0000\u0000\u0000"+
		"\u0090\u0017\u0001\u0000\u0000\u0000\n\u001b+07=PW\u0080\u0087\u008d";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}