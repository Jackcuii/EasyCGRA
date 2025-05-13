# Generated from EasyCGRAParser.g4 by ANTLR 4.13.2
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
        4,1,56,147,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,5,0,
        28,8,0,10,0,12,0,31,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,
        1,2,1,2,1,2,3,2,46,8,2,1,3,5,3,49,8,3,10,3,12,3,52,9,3,1,4,1,4,5,
        4,56,8,4,10,4,12,4,59,9,4,1,4,1,4,1,4,3,4,64,8,4,1,5,1,5,1,5,1,6,
        1,6,1,7,1,7,1,7,1,7,1,7,3,7,76,8,7,1,7,1,7,1,7,1,7,3,7,82,8,7,1,
        8,1,8,1,8,5,8,87,8,8,10,8,12,8,90,9,8,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,
        9,130,8,9,1,10,1,10,1,10,5,10,135,8,10,10,10,12,10,138,9,10,1,11,
        1,11,1,11,3,11,143,8,11,1,12,1,12,1,12,0,0,13,0,2,4,6,8,10,12,14,
        16,18,20,22,24,0,1,2,0,1,19,21,22,153,0,29,1,0,0,0,2,34,1,0,0,0,
        4,45,1,0,0,0,6,50,1,0,0,0,8,63,1,0,0,0,10,65,1,0,0,0,12,68,1,0,0,
        0,14,81,1,0,0,0,16,83,1,0,0,0,18,129,1,0,0,0,20,131,1,0,0,0,22,142,
        1,0,0,0,24,144,1,0,0,0,26,28,3,2,1,0,27,26,1,0,0,0,28,31,1,0,0,0,
        29,27,1,0,0,0,29,30,1,0,0,0,30,32,1,0,0,0,31,29,1,0,0,0,32,33,5,
        0,0,1,33,1,1,0,0,0,34,35,3,4,2,0,35,36,5,43,0,0,36,37,3,6,3,0,37,
        38,5,44,0,0,38,3,1,0,0,0,39,40,5,25,0,0,40,46,5,26,0,0,41,42,5,25,
        0,0,42,43,3,16,8,0,43,44,5,26,0,0,44,46,1,0,0,0,45,39,1,0,0,0,45,
        41,1,0,0,0,46,5,1,0,0,0,47,49,3,8,4,0,48,47,1,0,0,0,49,52,1,0,0,
        0,50,48,1,0,0,0,50,51,1,0,0,0,51,7,1,0,0,0,52,50,1,0,0,0,53,57,5,
        43,0,0,54,56,3,14,7,0,55,54,1,0,0,0,56,59,1,0,0,0,57,55,1,0,0,0,
        57,58,1,0,0,0,58,60,1,0,0,0,59,57,1,0,0,0,60,64,5,44,0,0,61,64,3,
        14,7,0,62,64,3,10,5,0,63,53,1,0,0,0,63,61,1,0,0,0,63,62,1,0,0,0,
        64,9,1,0,0,0,65,66,3,12,6,0,66,67,5,50,0,0,67,11,1,0,0,0,68,69,5,
        56,0,0,69,13,1,0,0,0,70,71,3,24,12,0,71,72,5,48,0,0,72,75,3,16,8,
        0,73,74,5,27,0,0,74,76,3,16,8,0,75,73,1,0,0,0,75,76,1,0,0,0,76,82,
        1,0,0,0,77,78,3,18,9,0,78,79,5,27,0,0,79,80,3,18,9,0,80,82,1,0,0,
        0,81,70,1,0,0,0,81,77,1,0,0,0,82,15,1,0,0,0,83,88,3,18,9,0,84,85,
        5,48,0,0,85,87,3,18,9,0,86,84,1,0,0,0,87,90,1,0,0,0,88,86,1,0,0,
        0,88,89,1,0,0,0,89,17,1,0,0,0,90,88,1,0,0,0,91,92,3,22,11,0,92,93,
        5,45,0,0,93,94,3,20,10,0,94,95,5,46,0,0,95,130,1,0,0,0,96,97,5,28,
        0,0,97,98,5,45,0,0,98,99,5,30,0,0,99,130,5,46,0,0,100,101,5,28,0,
        0,101,102,5,45,0,0,102,103,5,32,0,0,103,130,5,46,0,0,104,105,5,28,
        0,0,105,106,5,45,0,0,106,107,5,31,0,0,107,130,5,46,0,0,108,109,5,
        28,0,0,109,110,5,45,0,0,110,111,5,33,0,0,111,130,5,46,0,0,112,113,
        5,28,0,0,113,114,5,45,0,0,114,115,5,34,0,0,115,130,5,46,0,0,116,
        117,3,22,11,0,117,118,5,29,0,0,118,119,5,45,0,0,119,120,3,20,10,
        0,120,121,5,46,0,0,121,130,1,0,0,0,122,123,3,22,11,0,123,124,5,29,
        0,0,124,125,5,45,0,0,125,126,5,31,0,0,126,127,5,46,0,0,127,130,1,
        0,0,0,128,130,3,12,6,0,129,91,1,0,0,0,129,96,1,0,0,0,129,100,1,0,
        0,0,129,104,1,0,0,0,129,108,1,0,0,0,129,112,1,0,0,0,129,116,1,0,
        0,0,129,122,1,0,0,0,129,128,1,0,0,0,130,19,1,0,0,0,131,136,5,56,
        0,0,132,133,5,48,0,0,133,135,5,56,0,0,134,132,1,0,0,0,135,138,1,
        0,0,0,136,134,1,0,0,0,136,137,1,0,0,0,137,21,1,0,0,0,138,136,1,0,
        0,0,139,143,5,51,0,0,140,143,5,52,0,0,141,143,1,0,0,0,142,139,1,
        0,0,0,142,140,1,0,0,0,142,141,1,0,0,0,143,23,1,0,0,0,144,145,7,0,
        0,0,145,25,1,0,0,0,11,29,45,50,57,63,75,81,88,129,136,142
    ]

class EasyCGRAParser ( Parser ):

    grammarFileName = "EasyCGRAParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'ADD'", "'ADDI'", "'SUB'", "'SUBI'", 
                     "'MUL'", "'DIV'", "'MAC'", "'INC'", "'LLS'", "'LRS'", 
                     "'OR'", "'AND'", "'XOR'", "'NOT'", "'FADD'", "'FSUB'", 
                     "'FMUL'", "'FDIV'", "'FMAC'", "'BEQ'", "'MOV'", "'MUL_CONST_ADD'", 
                     "'LOAD'", "'STORE'", "'Entry'", "'=>'", "'->'", "'IMM'", 
                     "'MEM'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'null'", "'('", "')'", "'{'", 
                     "'}'", "'['", "']'", "';'", "','", "'.'", "':'", "'!'", 
                     "'^'" ]

    symbolicNames = [ "<INVALID>", "ADD", "ADDI", "SUB", "SUBI", "MUL", 
                      "DIV", "MAC", "INC", "LLS", "LRS", "OR", "AND", "XOR", 
                      "NOT", "FADD", "FSUB", "FMUL", "FDIV", "FMAC", "BEQ", 
                      "MOV", "MUL_CONST_ADD", "LOAD", "STORE", "ENTRY", 
                      "ENTRY_ARROW", "RIGHT_ARROW", "IMM", "MEM", "DECIMAL_LITERAL", 
                      "HEX_LITERAL", "OCT_LITERAL", "BINARY_LITERAL", "FLOAT_LITERAL", 
                      "HEX_FLOAT_LITERAL", "BOOL_LITERAL", "CHAR_LITERAL", 
                      "STRING_LITERAL", "TEXT_BLOCK", "NULL_LITERAL", "LPAREN", 
                      "RPAREN", "LBRACE", "RBRACE", "LBRACK", "RBRACK", 
                      "SEMI", "COMMA", "DOT", "COLON", "AND_PRED", "OR_PRED", 
                      "WS", "COMMENT", "LINE_COMMENT", "IDENTIFIER" ]

    RULE_compilationUnit = 0
    RULE_entryBlock = 1
    RULE_entryHead = 2
    RULE_instList = 3
    RULE_inst = 4
    RULE_label = 5
    RULE_labelID = 6
    RULE_normalInst = 7
    RULE_operandList = 8
    RULE_operand = 9
    RULE_idList = 10
    RULE_predTag = 11
    RULE_opCode = 12

    ruleNames =  [ "compilationUnit", "entryBlock", "entryHead", "instList", 
                   "inst", "label", "labelID", "normalInst", "operandList", 
                   "operand", "idList", "predTag", "opCode" ]

    EOF = Token.EOF
    ADD=1
    ADDI=2
    SUB=3
    SUBI=4
    MUL=5
    DIV=6
    MAC=7
    INC=8
    LLS=9
    LRS=10
    OR=11
    AND=12
    XOR=13
    NOT=14
    FADD=15
    FSUB=16
    FMUL=17
    FDIV=18
    FMAC=19
    BEQ=20
    MOV=21
    MUL_CONST_ADD=22
    LOAD=23
    STORE=24
    ENTRY=25
    ENTRY_ARROW=26
    RIGHT_ARROW=27
    IMM=28
    MEM=29
    DECIMAL_LITERAL=30
    HEX_LITERAL=31
    OCT_LITERAL=32
    BINARY_LITERAL=33
    FLOAT_LITERAL=34
    HEX_FLOAT_LITERAL=35
    BOOL_LITERAL=36
    CHAR_LITERAL=37
    STRING_LITERAL=38
    TEXT_BLOCK=39
    NULL_LITERAL=40
    LPAREN=41
    RPAREN=42
    LBRACE=43
    RBRACE=44
    LBRACK=45
    RBRACK=46
    SEMI=47
    COMMA=48
    DOT=49
    COLON=50
    AND_PRED=51
    OR_PRED=52
    WS=53
    COMMENT=54
    LINE_COMMENT=55
    IDENTIFIER=56

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CompilationUnitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(EasyCGRAParser.EOF, 0)

        def entryBlock(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EasyCGRAParser.EntryBlockContext)
            else:
                return self.getTypedRuleContext(EasyCGRAParser.EntryBlockContext,i)


        def getRuleIndex(self):
            return EasyCGRAParser.RULE_compilationUnit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompilationUnit" ):
                listener.enterCompilationUnit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompilationUnit" ):
                listener.exitCompilationUnit(self)




    def compilationUnit(self):

        localctx = EasyCGRAParser.CompilationUnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_compilationUnit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 26
                self.entryBlock()
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 32
            self.match(EasyCGRAParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EntryBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def entryHead(self):
            return self.getTypedRuleContext(EasyCGRAParser.EntryHeadContext,0)


        def LBRACE(self):
            return self.getToken(EasyCGRAParser.LBRACE, 0)

        def instList(self):
            return self.getTypedRuleContext(EasyCGRAParser.InstListContext,0)


        def RBRACE(self):
            return self.getToken(EasyCGRAParser.RBRACE, 0)

        def getRuleIndex(self):
            return EasyCGRAParser.RULE_entryBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntryBlock" ):
                listener.enterEntryBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntryBlock" ):
                listener.exitEntryBlock(self)




    def entryBlock(self):

        localctx = EasyCGRAParser.EntryBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_entryBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.entryHead()
            self.state = 35
            self.match(EasyCGRAParser.LBRACE)
            self.state = 36
            self.instList()
            self.state = 37
            self.match(EasyCGRAParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EntryHeadContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENTRY(self):
            return self.getToken(EasyCGRAParser.ENTRY, 0)

        def ENTRY_ARROW(self):
            return self.getToken(EasyCGRAParser.ENTRY_ARROW, 0)

        def operandList(self):
            return self.getTypedRuleContext(EasyCGRAParser.OperandListContext,0)


        def getRuleIndex(self):
            return EasyCGRAParser.RULE_entryHead

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntryHead" ):
                listener.enterEntryHead(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntryHead" ):
                listener.exitEntryHead(self)




    def entryHead(self):

        localctx = EasyCGRAParser.EntryHeadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_entryHead)
        try:
            self.state = 45
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                self.match(EasyCGRAParser.ENTRY)
                self.state = 40
                self.match(EasyCGRAParser.ENTRY_ARROW)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 41
                self.match(EasyCGRAParser.ENTRY)
                self.state = 42
                self.operandList()
                self.state = 43
                self.match(EasyCGRAParser.ENTRY_ARROW)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def inst(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EasyCGRAParser.InstContext)
            else:
                return self.getTypedRuleContext(EasyCGRAParser.InstContext,i)


        def getRuleIndex(self):
            return EasyCGRAParser.RULE_instList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstList" ):
                listener.enterInstList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstList" ):
                listener.exitInstList(self)




    def instList(self):

        localctx = EasyCGRAParser.InstListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_instList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 78856974756741118) != 0):
                self.state = 47
                self.inst()
                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(EasyCGRAParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(EasyCGRAParser.RBRACE, 0)

        def normalInst(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EasyCGRAParser.NormalInstContext)
            else:
                return self.getTypedRuleContext(EasyCGRAParser.NormalInstContext,i)


        def label(self):
            return self.getTypedRuleContext(EasyCGRAParser.LabelContext,0)


        def getRuleIndex(self):
            return EasyCGRAParser.RULE_inst

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInst" ):
                listener.enterInst(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInst" ):
                listener.exitInst(self)




    def inst(self):

        localctx = EasyCGRAParser.InstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_inst)
        self._la = 0 # Token type
        try:
            self.state = 63
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 53
                self.match(EasyCGRAParser.LBRACE)
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 78848178663718910) != 0):
                    self.state = 54
                    self.normalInst()
                    self.state = 59
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 60
                self.match(EasyCGRAParser.RBRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 61
                self.normalInst()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 62
                self.label()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LabelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def labelID(self):
            return self.getTypedRuleContext(EasyCGRAParser.LabelIDContext,0)


        def COLON(self):
            return self.getToken(EasyCGRAParser.COLON, 0)

        def getRuleIndex(self):
            return EasyCGRAParser.RULE_label

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabel" ):
                listener.enterLabel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabel" ):
                listener.exitLabel(self)




    def label(self):

        localctx = EasyCGRAParser.LabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.labelID()
            self.state = 66
            self.match(EasyCGRAParser.COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LabelIDContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(EasyCGRAParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return EasyCGRAParser.RULE_labelID

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabelID" ):
                listener.enterLabelID(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabelID" ):
                listener.exitLabelID(self)




    def labelID(self):

        localctx = EasyCGRAParser.LabelIDContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_labelID)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(EasyCGRAParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NormalInstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def opCode(self):
            return self.getTypedRuleContext(EasyCGRAParser.OpCodeContext,0)


        def COMMA(self):
            return self.getToken(EasyCGRAParser.COMMA, 0)

        def operandList(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EasyCGRAParser.OperandListContext)
            else:
                return self.getTypedRuleContext(EasyCGRAParser.OperandListContext,i)


        def RIGHT_ARROW(self):
            return self.getToken(EasyCGRAParser.RIGHT_ARROW, 0)

        def operand(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EasyCGRAParser.OperandContext)
            else:
                return self.getTypedRuleContext(EasyCGRAParser.OperandContext,i)


        def getRuleIndex(self):
            return EasyCGRAParser.RULE_normalInst

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNormalInst" ):
                listener.enterNormalInst(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNormalInst" ):
                listener.exitNormalInst(self)




    def normalInst(self):

        localctx = EasyCGRAParser.NormalInstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_normalInst)
        self._la = 0 # Token type
        try:
            self.state = 81
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 70
                self.opCode()
                self.state = 71
                self.match(EasyCGRAParser.COMMA)
                self.state = 72
                self.operandList()
                self.state = 75
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==27:
                    self.state = 73
                    self.match(EasyCGRAParser.RIGHT_ARROW)
                    self.state = 74
                    self.operandList()


                pass
            elif token in [28, 29, 45, 51, 52, 56]:
                self.enterOuterAlt(localctx, 2)
                self.state = 77
                self.operand()
                self.state = 78
                self.match(EasyCGRAParser.RIGHT_ARROW)
                self.state = 79
                self.operand()
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


    class OperandListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(EasyCGRAParser.OperandContext)
            else:
                return self.getTypedRuleContext(EasyCGRAParser.OperandContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(EasyCGRAParser.COMMA)
            else:
                return self.getToken(EasyCGRAParser.COMMA, i)

        def getRuleIndex(self):
            return EasyCGRAParser.RULE_operandList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperandList" ):
                listener.enterOperandList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperandList" ):
                listener.exitOperandList(self)




    def operandList(self):

        localctx = EasyCGRAParser.OperandListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_operandList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.operand()
            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 84
                self.match(EasyCGRAParser.COMMA)
                self.state = 85
                self.operand()
                self.state = 90
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def predTag(self):
            return self.getTypedRuleContext(EasyCGRAParser.PredTagContext,0)


        def LBRACK(self):
            return self.getToken(EasyCGRAParser.LBRACK, 0)

        def idList(self):
            return self.getTypedRuleContext(EasyCGRAParser.IdListContext,0)


        def RBRACK(self):
            return self.getToken(EasyCGRAParser.RBRACK, 0)

        def IMM(self):
            return self.getToken(EasyCGRAParser.IMM, 0)

        def DECIMAL_LITERAL(self):
            return self.getToken(EasyCGRAParser.DECIMAL_LITERAL, 0)

        def OCT_LITERAL(self):
            return self.getToken(EasyCGRAParser.OCT_LITERAL, 0)

        def HEX_LITERAL(self):
            return self.getToken(EasyCGRAParser.HEX_LITERAL, 0)

        def BINARY_LITERAL(self):
            return self.getToken(EasyCGRAParser.BINARY_LITERAL, 0)

        def FLOAT_LITERAL(self):
            return self.getToken(EasyCGRAParser.FLOAT_LITERAL, 0)

        def MEM(self):
            return self.getToken(EasyCGRAParser.MEM, 0)

        def labelID(self):
            return self.getTypedRuleContext(EasyCGRAParser.LabelIDContext,0)


        def getRuleIndex(self):
            return EasyCGRAParser.RULE_operand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperand" ):
                listener.enterOperand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperand" ):
                listener.exitOperand(self)




    def operand(self):

        localctx = EasyCGRAParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_operand)
        try:
            self.state = 129
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 91
                self.predTag()
                self.state = 92
                self.match(EasyCGRAParser.LBRACK)
                self.state = 93
                self.idList()
                self.state = 94
                self.match(EasyCGRAParser.RBRACK)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 96
                self.match(EasyCGRAParser.IMM)
                self.state = 97
                self.match(EasyCGRAParser.LBRACK)
                self.state = 98
                self.match(EasyCGRAParser.DECIMAL_LITERAL)
                self.state = 99
                self.match(EasyCGRAParser.RBRACK)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 100
                self.match(EasyCGRAParser.IMM)
                self.state = 101
                self.match(EasyCGRAParser.LBRACK)
                self.state = 102
                self.match(EasyCGRAParser.OCT_LITERAL)
                self.state = 103
                self.match(EasyCGRAParser.RBRACK)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 104
                self.match(EasyCGRAParser.IMM)
                self.state = 105
                self.match(EasyCGRAParser.LBRACK)
                self.state = 106
                self.match(EasyCGRAParser.HEX_LITERAL)
                self.state = 107
                self.match(EasyCGRAParser.RBRACK)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 108
                self.match(EasyCGRAParser.IMM)
                self.state = 109
                self.match(EasyCGRAParser.LBRACK)
                self.state = 110
                self.match(EasyCGRAParser.BINARY_LITERAL)
                self.state = 111
                self.match(EasyCGRAParser.RBRACK)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 112
                self.match(EasyCGRAParser.IMM)
                self.state = 113
                self.match(EasyCGRAParser.LBRACK)
                self.state = 114
                self.match(EasyCGRAParser.FLOAT_LITERAL)
                self.state = 115
                self.match(EasyCGRAParser.RBRACK)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 116
                self.predTag()
                self.state = 117
                self.match(EasyCGRAParser.MEM)
                self.state = 118
                self.match(EasyCGRAParser.LBRACK)
                self.state = 119
                self.idList()
                self.state = 120
                self.match(EasyCGRAParser.RBRACK)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 122
                self.predTag()
                self.state = 123
                self.match(EasyCGRAParser.MEM)
                self.state = 124
                self.match(EasyCGRAParser.LBRACK)
                self.state = 125
                self.match(EasyCGRAParser.HEX_LITERAL)
                self.state = 126
                self.match(EasyCGRAParser.RBRACK)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 128
                self.labelID()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(EasyCGRAParser.IDENTIFIER)
            else:
                return self.getToken(EasyCGRAParser.IDENTIFIER, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(EasyCGRAParser.COMMA)
            else:
                return self.getToken(EasyCGRAParser.COMMA, i)

        def getRuleIndex(self):
            return EasyCGRAParser.RULE_idList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdList" ):
                listener.enterIdList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdList" ):
                listener.exitIdList(self)




    def idList(self):

        localctx = EasyCGRAParser.IdListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_idList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(EasyCGRAParser.IDENTIFIER)
            self.state = 136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 132
                self.match(EasyCGRAParser.COMMA)
                self.state = 133
                self.match(EasyCGRAParser.IDENTIFIER)
                self.state = 138
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PredTagContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND_PRED(self):
            return self.getToken(EasyCGRAParser.AND_PRED, 0)

        def OR_PRED(self):
            return self.getToken(EasyCGRAParser.OR_PRED, 0)

        def getRuleIndex(self):
            return EasyCGRAParser.RULE_predTag

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPredTag" ):
                listener.enterPredTag(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPredTag" ):
                listener.exitPredTag(self)




    def predTag(self):

        localctx = EasyCGRAParser.PredTagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_predTag)
        try:
            self.state = 142
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [51]:
                self.enterOuterAlt(localctx, 1)
                self.state = 139
                self.match(EasyCGRAParser.AND_PRED)
                pass
            elif token in [52]:
                self.enterOuterAlt(localctx, 2)
                self.state = 140
                self.match(EasyCGRAParser.OR_PRED)
                pass
            elif token in [29, 45]:
                self.enterOuterAlt(localctx, 3)

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


    class OpCodeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(EasyCGRAParser.ADD, 0)

        def ADDI(self):
            return self.getToken(EasyCGRAParser.ADDI, 0)

        def SUB(self):
            return self.getToken(EasyCGRAParser.SUB, 0)

        def SUBI(self):
            return self.getToken(EasyCGRAParser.SUBI, 0)

        def MUL(self):
            return self.getToken(EasyCGRAParser.MUL, 0)

        def DIV(self):
            return self.getToken(EasyCGRAParser.DIV, 0)

        def MAC(self):
            return self.getToken(EasyCGRAParser.MAC, 0)

        def INC(self):
            return self.getToken(EasyCGRAParser.INC, 0)

        def LLS(self):
            return self.getToken(EasyCGRAParser.LLS, 0)

        def LRS(self):
            return self.getToken(EasyCGRAParser.LRS, 0)

        def OR(self):
            return self.getToken(EasyCGRAParser.OR, 0)

        def AND(self):
            return self.getToken(EasyCGRAParser.AND, 0)

        def XOR(self):
            return self.getToken(EasyCGRAParser.XOR, 0)

        def NOT(self):
            return self.getToken(EasyCGRAParser.NOT, 0)

        def FADD(self):
            return self.getToken(EasyCGRAParser.FADD, 0)

        def FSUB(self):
            return self.getToken(EasyCGRAParser.FSUB, 0)

        def FMUL(self):
            return self.getToken(EasyCGRAParser.FMUL, 0)

        def FDIV(self):
            return self.getToken(EasyCGRAParser.FDIV, 0)

        def FMAC(self):
            return self.getToken(EasyCGRAParser.FMAC, 0)

        def MOV(self):
            return self.getToken(EasyCGRAParser.MOV, 0)

        def MUL_CONST_ADD(self):
            return self.getToken(EasyCGRAParser.MUL_CONST_ADD, 0)

        def getRuleIndex(self):
            return EasyCGRAParser.RULE_opCode

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpCode" ):
                listener.enterOpCode(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpCode" ):
                listener.exitOpCode(self)




    def opCode(self):

        localctx = EasyCGRAParser.OpCodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_opCode)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7340030) != 0)):
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





