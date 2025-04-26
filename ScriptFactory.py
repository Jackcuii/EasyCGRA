import sys
from antlr4 import *
from EasyCGRALexer import EasyCGRALexer
from EasyCGRAParser import EasyCGRAParser
from RealEasyCGRAParserVisitor import RealEasyCGRAParserVisitor


class ScriptFactory:
    def makeVectorCGRAInst(ScriptInsts, CtrlPktType):
        for inst in ScriptInsts:
            CtrlPktType(...) # TODO        
        
    
    @classmethod
    def make(cls, file):
        input_stream = FileStream(file)
        lexer = EasyCGRALexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = EasyCGRAParser(stream)
        tree = parser.start_()
        if parser.getNumberOfSyntaxErrors() > 0:
            print(f"Syntax errors in your script {file}.")
            return None
        else:
            vinterp = RealEasyCGRAParserVisitor()
            vinterp.visit(tree)
            
            return vinterp.insts
        