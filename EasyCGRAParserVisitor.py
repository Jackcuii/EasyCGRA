# Generated from EasyCGRAParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .EasyCGRAParser import EasyCGRAParser
else:
    from EasyCGRAParser import EasyCGRAParser

# This class defines a complete generic visitor for a parse tree produced by EasyCGRAParser.

class EasyCGRAParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by EasyCGRAParser#compilationUnit.
    def visitCompilationUnit(self, ctx:EasyCGRAParser.CompilationUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EasyCGRAParser#entryBlock.
    def visitEntryBlock(self, ctx:EasyCGRAParser.EntryBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EasyCGRAParser#entryHead.
    def visitEntryHead(self, ctx:EasyCGRAParser.EntryHeadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EasyCGRAParser#instList.
    def visitInstList(self, ctx:EasyCGRAParser.InstListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EasyCGRAParser#inst.
    def visitInst(self, ctx:EasyCGRAParser.InstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EasyCGRAParser#label.
    def visitLabel(self, ctx:EasyCGRAParser.LabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EasyCGRAParser#normalInst.
    def visitNormalInst(self, ctx:EasyCGRAParser.NormalInstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EasyCGRAParser#operandList.
    def visitOperandList(self, ctx:EasyCGRAParser.OperandListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EasyCGRAParser#operand.
    def visitOperand(self, ctx:EasyCGRAParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EasyCGRAParser#idList.
    def visitIdList(self, ctx:EasyCGRAParser.IdListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EasyCGRAParser#predTag.
    def visitPredTag(self, ctx:EasyCGRAParser.PredTagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EasyCGRAParser#opCode.
    def visitOpCode(self, ctx:EasyCGRAParser.OpCodeContext):
        return self.visitChildren(ctx)



del EasyCGRAParser