// Generated from /home/amirreza/amir/M.A.R-Interpreter-ANTLR-Project-/MAR.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class MARLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		WS=1, INTEGER=2, FLOAT=3, STRING=4, BOOL=5, NULL=6, IF=7, ELSE=8, FOR=9, 
		WHILE=10, BOOL_OP=11, ID=12, NOT=13, OPP=14, CLP=15, COMMA=16, EQUALL=17, 
		OPCB=18, CLCB=19, ADD=20, SUB=21, MUL=22, DIV=23, MOD=24, RELOP=25, SC=26;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"DIGIT", "LETTER", "WS", "INTEGER", "FLOAT", "STRING", "BOOL", "NULL", 
			"IF", "ELSE", "FOR", "WHILE", "BOOL_OP", "ID", "NOT", "OPP", "CLP", "COMMA", 
			"EQUALL", "OPCB", "CLCB", "ADD", "SUB", "MUL", "DIV", "MOD", "RELOP", 
			"SC"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, null, null, null, "'null'", "'if'", "'else'", "'for'", 
			"'while'", null, null, "'!'", "'('", "')'", "','", "'='", "'{'", "'}'", 
			"'+'", "'-'", "'*'", "'/'", "'%'", null, "';'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "WS", "INTEGER", "FLOAT", "STRING", "BOOL", "NULL", "IF", "ELSE", 
			"FOR", "WHILE", "BOOL_OP", "ID", "NOT", "OPP", "CLP", "COMMA", "EQUALL", 
			"OPCB", "CLCB", "ADD", "SUB", "MUL", "DIV", "MOD", "RELOP", "SC"
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


	public MARLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "MAR.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\34\u00bb\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31"+
		"\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\3\2\3\2\3\3\3\3\3\4\6\4"+
		"A\n\4\r\4\16\4B\3\4\3\4\3\5\6\5H\n\5\r\5\16\5I\3\6\6\6M\n\6\r\6\16\6N"+
		"\3\6\3\6\7\6S\n\6\f\6\16\6V\13\6\3\7\3\7\7\7Z\n\7\f\7\16\7]\13\7\3\7\3"+
		"\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\bj\n\b\3\t\3\t\3\t\3\t\3\t\3"+
		"\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3"+
		"\r\3\r\3\16\3\16\3\16\3\16\3\16\5\16\u0088\n\16\3\17\6\17\u008b\n\17\r"+
		"\17\16\17\u008c\3\17\3\17\3\17\7\17\u0092\n\17\f\17\16\17\u0095\13\17"+
		"\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26"+
		"\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\34\3\34"+
		"\3\34\3\34\3\34\3\34\3\34\5\34\u00b8\n\34\3\35\3\35\3[\2\36\3\2\5\2\7"+
		"\3\t\4\13\5\r\6\17\7\21\b\23\t\25\n\27\13\31\f\33\r\35\16\37\17!\20#\21"+
		"%\22\'\23)\24+\25-\26/\27\61\30\63\31\65\32\67\339\34\3\2\6\3\2\62;\4"+
		"\2C\\c|\5\2\13\f\17\17\"\"\4\2>>@@\2\u00c7\2\7\3\2\2\2\2\t\3\2\2\2\2\13"+
		"\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2"+
		"\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2"+
		"!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3"+
		"\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2"+
		"\29\3\2\2\2\3;\3\2\2\2\5=\3\2\2\2\7@\3\2\2\2\tG\3\2\2\2\13L\3\2\2\2\r"+
		"W\3\2\2\2\17i\3\2\2\2\21k\3\2\2\2\23p\3\2\2\2\25s\3\2\2\2\27x\3\2\2\2"+
		"\31|\3\2\2\2\33\u0087\3\2\2\2\35\u008a\3\2\2\2\37\u0096\3\2\2\2!\u0098"+
		"\3\2\2\2#\u009a\3\2\2\2%\u009c\3\2\2\2\'\u009e\3\2\2\2)\u00a0\3\2\2\2"+
		"+\u00a2\3\2\2\2-\u00a4\3\2\2\2/\u00a6\3\2\2\2\61\u00a8\3\2\2\2\63\u00aa"+
		"\3\2\2\2\65\u00ac\3\2\2\2\67\u00b7\3\2\2\29\u00b9\3\2\2\2;<\t\2\2\2<\4"+
		"\3\2\2\2=>\t\3\2\2>\6\3\2\2\2?A\t\4\2\2@?\3\2\2\2AB\3\2\2\2B@\3\2\2\2"+
		"BC\3\2\2\2CD\3\2\2\2DE\b\4\2\2E\b\3\2\2\2FH\5\3\2\2GF\3\2\2\2HI\3\2\2"+
		"\2IG\3\2\2\2IJ\3\2\2\2J\n\3\2\2\2KM\5\3\2\2LK\3\2\2\2MN\3\2\2\2NL\3\2"+
		"\2\2NO\3\2\2\2OP\3\2\2\2PT\7\60\2\2QS\5\3\2\2RQ\3\2\2\2SV\3\2\2\2TR\3"+
		"\2\2\2TU\3\2\2\2U\f\3\2\2\2VT\3\2\2\2W[\7$\2\2XZ\13\2\2\2YX\3\2\2\2Z]"+
		"\3\2\2\2[\\\3\2\2\2[Y\3\2\2\2\\^\3\2\2\2][\3\2\2\2^_\7$\2\2_\16\3\2\2"+
		"\2`a\7v\2\2ab\7t\2\2bc\7w\2\2cj\7g\2\2de\7h\2\2ef\7c\2\2fg\7n\2\2gh\7"+
		"u\2\2hj\7g\2\2i`\3\2\2\2id\3\2\2\2j\20\3\2\2\2kl\7p\2\2lm\7w\2\2mn\7n"+
		"\2\2no\7n\2\2o\22\3\2\2\2pq\7k\2\2qr\7h\2\2r\24\3\2\2\2st\7g\2\2tu\7n"+
		"\2\2uv\7u\2\2vw\7g\2\2w\26\3\2\2\2xy\7h\2\2yz\7q\2\2z{\7t\2\2{\30\3\2"+
		"\2\2|}\7y\2\2}~\7j\2\2~\177\7k\2\2\177\u0080\7n\2\2\u0080\u0081\7g\2\2"+
		"\u0081\32\3\2\2\2\u0082\u0083\7c\2\2\u0083\u0084\7p\2\2\u0084\u0088\7"+
		"f\2\2\u0085\u0086\7q\2\2\u0086\u0088\7t\2\2\u0087\u0082\3\2\2\2\u0087"+
		"\u0085\3\2\2\2\u0088\34\3\2\2\2\u0089\u008b\5\5\3\2\u008a\u0089\3\2\2"+
		"\2\u008b\u008c\3\2\2\2\u008c\u008a\3\2\2\2\u008c\u008d\3\2\2\2\u008d\u0093"+
		"\3\2\2\2\u008e\u0092\5\5\3\2\u008f\u0092\5\3\2\2\u0090\u0092\7a\2\2\u0091"+
		"\u008e\3\2\2\2\u0091\u008f\3\2\2\2\u0091\u0090\3\2\2\2\u0092\u0095\3\2"+
		"\2\2\u0093\u0091\3\2\2\2\u0093\u0094\3\2\2\2\u0094\36\3\2\2\2\u0095\u0093"+
		"\3\2\2\2\u0096\u0097\7#\2\2\u0097 \3\2\2\2\u0098\u0099\7*\2\2\u0099\""+
		"\3\2\2\2\u009a\u009b\7+\2\2\u009b$\3\2\2\2\u009c\u009d\7.\2\2\u009d&\3"+
		"\2\2\2\u009e\u009f\7?\2\2\u009f(\3\2\2\2\u00a0\u00a1\7}\2\2\u00a1*\3\2"+
		"\2\2\u00a2\u00a3\7\177\2\2\u00a3,\3\2\2\2\u00a4\u00a5\7-\2\2\u00a5.\3"+
		"\2\2\2\u00a6\u00a7\7/\2\2\u00a7\60\3\2\2\2\u00a8\u00a9\7,\2\2\u00a9\62"+
		"\3\2\2\2\u00aa\u00ab\7\61\2\2\u00ab\64\3\2\2\2\u00ac\u00ad\7\'\2\2\u00ad"+
		"\66\3\2\2\2\u00ae\u00b8\t\5\2\2\u00af\u00b0\7>\2\2\u00b0\u00b8\7?\2\2"+
		"\u00b1\u00b2\7@\2\2\u00b2\u00b8\7?\2\2\u00b3\u00b4\7?\2\2\u00b4\u00b8"+
		"\7?\2\2\u00b5\u00b6\7#\2\2\u00b6\u00b8\7?\2\2\u00b7\u00ae\3\2\2\2\u00b7"+
		"\u00af\3\2\2\2\u00b7\u00b1\3\2\2\2\u00b7\u00b3\3\2\2\2\u00b7\u00b5\3\2"+
		"\2\2\u00b88\3\2\2\2\u00b9\u00ba\7=\2\2\u00ba:\3\2\2\2\16\2BINT[i\u0087"+
		"\u008c\u0091\u0093\u00b7\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}