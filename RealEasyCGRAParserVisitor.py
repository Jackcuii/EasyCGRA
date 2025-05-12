from EasyCGRAParser import EasyCGRAParser
from EasyCGRAParserVisitor import EasyCGRAParserVisitor

# enum
class OperandType:
    IMM = 0
    MEM_DYN = 1
    MEM_STATIC = 2
    ID = 3
    LABEL = 4

class oprObj:
    predTag = None
    IDs = []
    operandType = None
    value = None
    
class instObj:
    opCode = None
    srcOperands = []
    dstOperands = []



class RealEasyCGRAParserVisitor(EasyCGRAParserVisitor):
    
    # override them
    def visitCompilationUnit(self, ctx):
        # VectorCGRA can only have one entry block
        assert len(ctx.entryBlock()) == 1, "VectorCGRA can only have one entry block"
        return self.visitEntryBlock(ctx.entryBlock(0))
    
    def visitEntryBlock(self, ctx: EasyCGRAParser.EntryBlockContext):
        # VectorCGRA do not care the entryHead
        return self.visitInstList(ctx.instList())
        
    def visitInstList(self, ctx: EasyCGRAParser.InstListContext):
        insts = []
        for inst in ctx.inst():
            insts.append(self.visitInst(inst))
        return insts
    
    def visitInst(self, ctx: EasyCGRAParser.InstContext):
        normalInsts = []
        for normalInst in ctx.normalInst():
            normalInsts.append(self.visitNormalInst(normalInst))
        for label in ctx.label():
            self.visitLabel(label)
            
    def visitNormalInst(self, ctx: EasyCGRAParser.NormalInstContext):
        if(ctx.opCode()):
            opCode = ctx.opCode().getText()
        else:
            opCode = EasyCGRAParser.MOV
        if(len(ctx.operandList()) == 2):
            return (opCode, ctx.operandList(0), ctx.operandList(1))
        elif(len(ctx.operandList()) == 1):
            return (opCode, None, ctx.operandList(0))
        else:
            raise ValueError("Invalid operand list")
        
    def visitOperandList(self, ctx: EasyCGRAParser.OperandListContext):
        opr = oprObj()
        if(ctx.IMM()):
            opr.operandType = OperandType.IMM
            # change the imm to int
            if(ctx.DECIMAL_LITERAL()):
                opr.value = int(ctx.DECIMAL_LITERAL().getText())
            elif(ctx.OCT_LITERAL()):
                opr.value = int(ctx.OCT_LITERAL().getText(), 8)
            elif(ctx.HEX_LITERAL()):
                opr.value = int(ctx.HEX_LITERAL().getText(), 16)
            elif(ctx.BINARY_LITERAL()):
                opr.value = int(ctx.BINARY_LITERAL().getText(), 2)
            elif(ctx.FLOAT_LITERAL()):
                opr.value = float(ctx.FLOAT_LITERAL().getText())
            else:
                raise ValueError("Invalid immediate value")
        elif(ctx.MEM()):
            if(ctx.idList()):
                opr.operandType = OperandType.MEM_DYN
                ids = self.visitIdList(ctx.idList())
                opr.IDs = ids
                opr.predTag = ctx.predTag()
            elif(ctx.HEX_LITERAL()):
                opr.operandType = OperandType.MEM_STATIC
                opr.value = int(ctx.HEX_LITERAL().getText(), 16)
                opr.predTag = ctx.predTag()
            else:
                raise ValueError("Invalid memory address")
        elif(ctx.label()):
            opr.operandType = OperandType.LABEL
            opr.value = ctx.label().getText()
        else:
            opr.operandType = OperandType.ID
            opr.IDs = self.visitIdList(ctx.idList())
            opr.predTag = ctx.predTag()
        return opr
    
    def visitIdList(self, ctx: EasyCGRAParser.IdListContext):
        ids = []
        for id in ctx.IDENTIFIER():
            ids.append(id.getText())
        return ids
        
        
            
        
