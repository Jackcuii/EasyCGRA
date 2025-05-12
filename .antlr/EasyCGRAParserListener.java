// Generated from /home/jackcui/Arch/zeo-2.0/EasyCGRA/EasyCGRAParser.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link EasyCGRAParser}.
 */
public interface EasyCGRAParserListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link EasyCGRAParser#compilationUnit}.
	 * @param ctx the parse tree
	 */
	void enterCompilationUnit(EasyCGRAParser.CompilationUnitContext ctx);
	/**
	 * Exit a parse tree produced by {@link EasyCGRAParser#compilationUnit}.
	 * @param ctx the parse tree
	 */
	void exitCompilationUnit(EasyCGRAParser.CompilationUnitContext ctx);
	/**
	 * Enter a parse tree produced by {@link EasyCGRAParser#entryBlock}.
	 * @param ctx the parse tree
	 */
	void enterEntryBlock(EasyCGRAParser.EntryBlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link EasyCGRAParser#entryBlock}.
	 * @param ctx the parse tree
	 */
	void exitEntryBlock(EasyCGRAParser.EntryBlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link EasyCGRAParser#entryHead}.
	 * @param ctx the parse tree
	 */
	void enterEntryHead(EasyCGRAParser.EntryHeadContext ctx);
	/**
	 * Exit a parse tree produced by {@link EasyCGRAParser#entryHead}.
	 * @param ctx the parse tree
	 */
	void exitEntryHead(EasyCGRAParser.EntryHeadContext ctx);
	/**
	 * Enter a parse tree produced by {@link EasyCGRAParser#instList}.
	 * @param ctx the parse tree
	 */
	void enterInstList(EasyCGRAParser.InstListContext ctx);
	/**
	 * Exit a parse tree produced by {@link EasyCGRAParser#instList}.
	 * @param ctx the parse tree
	 */
	void exitInstList(EasyCGRAParser.InstListContext ctx);
	/**
	 * Enter a parse tree produced by {@link EasyCGRAParser#inst}.
	 * @param ctx the parse tree
	 */
	void enterInst(EasyCGRAParser.InstContext ctx);
	/**
	 * Exit a parse tree produced by {@link EasyCGRAParser#inst}.
	 * @param ctx the parse tree
	 */
	void exitInst(EasyCGRAParser.InstContext ctx);
	/**
	 * Enter a parse tree produced by {@link EasyCGRAParser#label}.
	 * @param ctx the parse tree
	 */
	void enterLabel(EasyCGRAParser.LabelContext ctx);
	/**
	 * Exit a parse tree produced by {@link EasyCGRAParser#label}.
	 * @param ctx the parse tree
	 */
	void exitLabel(EasyCGRAParser.LabelContext ctx);
	/**
	 * Enter a parse tree produced by {@link EasyCGRAParser#normalInst}.
	 * @param ctx the parse tree
	 */
	void enterNormalInst(EasyCGRAParser.NormalInstContext ctx);
	/**
	 * Exit a parse tree produced by {@link EasyCGRAParser#normalInst}.
	 * @param ctx the parse tree
	 */
	void exitNormalInst(EasyCGRAParser.NormalInstContext ctx);
	/**
	 * Enter a parse tree produced by {@link EasyCGRAParser#operandList}.
	 * @param ctx the parse tree
	 */
	void enterOperandList(EasyCGRAParser.OperandListContext ctx);
	/**
	 * Exit a parse tree produced by {@link EasyCGRAParser#operandList}.
	 * @param ctx the parse tree
	 */
	void exitOperandList(EasyCGRAParser.OperandListContext ctx);
	/**
	 * Enter a parse tree produced by {@link EasyCGRAParser#operand}.
	 * @param ctx the parse tree
	 */
	void enterOperand(EasyCGRAParser.OperandContext ctx);
	/**
	 * Exit a parse tree produced by {@link EasyCGRAParser#operand}.
	 * @param ctx the parse tree
	 */
	void exitOperand(EasyCGRAParser.OperandContext ctx);
	/**
	 * Enter a parse tree produced by {@link EasyCGRAParser#idList}.
	 * @param ctx the parse tree
	 */
	void enterIdList(EasyCGRAParser.IdListContext ctx);
	/**
	 * Exit a parse tree produced by {@link EasyCGRAParser#idList}.
	 * @param ctx the parse tree
	 */
	void exitIdList(EasyCGRAParser.IdListContext ctx);
	/**
	 * Enter a parse tree produced by {@link EasyCGRAParser#predTag}.
	 * @param ctx the parse tree
	 */
	void enterPredTag(EasyCGRAParser.PredTagContext ctx);
	/**
	 * Exit a parse tree produced by {@link EasyCGRAParser#predTag}.
	 * @param ctx the parse tree
	 */
	void exitPredTag(EasyCGRAParser.PredTagContext ctx);
	/**
	 * Enter a parse tree produced by {@link EasyCGRAParser#opCode}.
	 * @param ctx the parse tree
	 */
	void enterOpCode(EasyCGRAParser.OpCodeContext ctx);
	/**
	 * Exit a parse tree produced by {@link EasyCGRAParser#opCode}.
	 * @param ctx the parse tree
	 */
	void exitOpCode(EasyCGRAParser.OpCodeContext ctx);
}