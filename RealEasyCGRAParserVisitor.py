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
    def visitCompilationUnit(self, ctx: EasyCGRAParser.CompilationUnitContext):
        # VectorCGRA can only have one entry block
        #print("Visit Compilation Unit")
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
        # just for VectorCGRA, do not care labe 
        for normalInst in ctx.normalInst():
            normalInsts.append(self.visitNormalInst(normalInst))
        return normalInsts
        
            
    def visitNormalInst(self, ctx: EasyCGRAParser.NormalInstContext):
        if(ctx.opCode()):
            opCode = self.visitOpCode(ctx.opCode())
        else:
            opCode = EasyCGRAParser.MOV
        if(ctx.operandList()):
            inst = instObj()
            srcList = self.visitOperandList(ctx.operandList(0))
            dstList = None
            if(len(ctx.operandList()) == 2):
                dstList = self.visitOperandList(ctx.operandList(1))
            inst.opCode = opCode
            inst.srcOperands = srcList
            inst.dstOperands = dstList
            return inst
        else:
            inst = instObj()
            inst.opCode = opCode
            srcOpr = self.visitOperand(ctx.operand(0))
            dstOpr = self.visitOperand(ctx.operand(1))
            inst.srcOperands = [srcOpr]
            inst.dstOperands = [dstOpr]
            return inst
        
    def visitOperandList(self, ctx: EasyCGRAParser.OperandListContext):
        oprs = []
        for opr in ctx.operand():
            oprs.append(self.visitOperand(opr))
        return oprs
        
    def visitOperand(self, ctx: EasyCGRAParser.OperandContext):
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
        elif(ctx.labelID()):
            opr.operandType = OperandType.LABEL
            opr.value = ctx.labelID().getText()
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
    
    def visitOpCode(self, ctx: EasyCGRAParser.OpCodeContext):
        if(ctx.MOV()):
            return EasyCGRAParser.MOV
        elif(ctx.MUL_CONST_ADD()):
            return EasyCGRAParser.MUL_CONST_ADD
        elif(ctx.ADD()):
            return EasyCGRAParser.ADD
        elif(ctx.ADDI()):
            return EasyCGRAParser.ADDI
        elif(ctx.SUB()):
            return EasyCGRAParser.SUB
        elif(ctx.SUBI()):
            return EasyCGRAParser.SUBI
        elif(ctx.MUL()):
            return EasyCGRAParser.MUL
        elif(ctx.DIV()):
            return EasyCGRAParser.DIV
        elif(ctx.MAC()):
            return EasyCGRAParser.MAC
        elif(ctx.INC()):
            return EasyCGRAParser.INC
        elif(ctx.LLS()):
            return EasyCGRAParser.LLS
        elif(ctx.LRS()):
            return EasyCGRAParser.LRS
        elif(ctx.OR()):
            return EasyCGRAParser.OR
        elif(ctx.AND()):
            return EasyCGRAParser.AND
        elif(ctx.XOR()):
            return EasyCGRAParser.XOR
        elif(ctx.NOT()):
            return EasyCGRAParser.NOT
        elif(ctx.FADD()):
            return EasyCGRAParser.FADD
        elif(ctx.FSUB()):
            return EasyCGRAParser.FSUB
        elif(ctx.FMUL()):
            return EasyCGRAParser.FMUL
        elif(ctx.FDIV()):
            return EasyCGRAParser.FDIV
        else:
            raise ValueError("Invalid opCode")
    
    def visitLabel(self, ctx: EasyCGRAParser.LabelContext):
        assert False, "Label should not be visited in VectorCGRA"
        
    def visitPredTag(self, ctx: EasyCGRAParser.PredTagContext):
        assert False, "PredTag should not be visited in VectorCGRA"
        
        
            
        
