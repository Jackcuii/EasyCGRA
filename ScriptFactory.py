import sys
from antlr4 import *
from EasyCGRALexer import EasyCGRALexer
from EasyCGRAParser import EasyCGRAParser
from RealEasyCGRAParserVisitor import RealEasyCGRAParserVisitor


from ... import *  # TODO: import the correct file of the opCodes of VectorCGRA
from test import *

class EasyToVectorOpcodeMap:
    opMap = {
        EasyCGRAParser.MAC_CONST_ADD: OPT_MUL_CONST_ADD_DUMMY(),
        EasyCGRAParser.ADD: ...,
        EasyCGRAParser.ADDI: ...,
        EasyCGRAParser.SUB: ...,
        EasyCGRAParser.SUBI: ...,
        EasyCGRAParser.MUL: ...,
        EasyCGRAParser.DIV: ...,
        EasyCGRAParser.MAC: ...,
    }


class VectorCGRApkt:

    def __init__(self, CtrlType, IntraCgraPktType, CgraPayloadType, TileInType, FuOutType, config, OpCode, fuInCode, id_):
        self.IntraCgraPktType = IntraCgraPktType
        self.CgraPayloadType = CgraPayloadType
        self.TileInType = TileInType
        self.FuOutType = FuOutType
        self.TileInParams = [0, 0, 0, 0, 0, 0, 0, 0]
        self.FuOutParams = [0, 0, 0, 0, 0, 0, 0, 0]
        self.config = config
        self.OpCode = OpCode
        self.fuInCode = fuInCode
        self.id_ = id_
        self.CtrlType = CtrlType
        
    def makeCtrlPkt(self):
        TileIn = [ self.TileInType(self.TileInParams[idx]) for idx in range(8) ]
        FuOut = [ self.FuOutType(self.FuOutParams[idx]) for idx in range(8) ]
        ctrl = self.CtrlType(self.OpCode, 0, self.fuInCode, TileIn, FuOut)
        payload = self.CgraPayloadType(self.config, ctrl_addr = 0, ctrl = ctrl)
        pkt = self.IntraCgraPktType(0, self.id_, payload)
        return ctrl

    
class ScriptFactory:
    FromFu = 0
    FromRouting = 1
    def makeVectorCGRAPkts(ScriptInsts, CtrlType,IntraCgraPktType, CgraPayloadType, TileInType, FuOutType, config, fuInCode, id_, FromFuOrRouting = FromFu): #False means from routing inst
        pkts = []
        for cInst in ScriptInsts:
            pkt = VectorCGRApkt(CtrlType, IntraCgraPktType, CgraPayloadType, TileInType, FuOutType, config, None, fuInCode, id_)
            # find opcode
            for inst in cInst.inst:
                if inst != EasyCGRAParser.MOV: # not the routing inst
                    pkt.OpCode = EasyToVectorOpcodeMap.opMap[inst]
            
            if pkt.OpCode is None:
                pkt.OpCode = ... # TODO: alter this with your pure routing inst's opCode
            # update the params
            
            for inst in cInst.inst:
                if inst != EasyCGRAParser.MOV:
                    # cope with the srcOperands
                    if FromFuOrRouting == ScriptFactory.FromRouting:
                        for idx in range(len(inst.srcOperands)):
                            if inst.srcOperands[idx].IDs[-1] == "NORTH":
                                pkt.TileInParams[idx + 4] = 1
                            elif inst.srcOperands[idx].IDs[-1] == "SOUTH":
                                pkt.TileInParams[idx + 4] = 2
                            elif inst.srcOperands[idx].IDs[-1] == "WEST":
                                pkt.TileInParams[idx + 4] = 3
                            elif inst.srcOperands[idx].IDs[-1] == "EAST":
                                pkt.TileInParams[idx + 4] = 4
                    elif FromFuOrRouting == ScriptFactory.FromFu:
                        for idx in range(len(inst.srcOperands)):
                            ... 
                        
                    
                    # TODO: only one dstOperand?
                    if inst.dstOperands[0].IDs[-1] == "NORTH":
                        pkt.TileInParams[0] = 1
                    elif inst.dstOperands[0].IDs[-1] == "SOUTH":
                        pkt.TileInParams[1] = 1
                    elif inst.dstOperands[0].IDs[-1] == "WEST":
                        pkt.TileInParams[2] = 1
                    elif inst.dstOperands[0].IDs[-1] == "EAST":
                        pkt.TileInParams[3] = 1
                    elif inst.dstOperands[0].IDs[-1] == "$0":
                        pkt.TileInParams[4] = 1
                    elif inst.dstOperands[0].IDs[-1] == "$1":
                        pkt.TileInParams[5] = 1
                    elif inst.dstOperands[0].IDs[-1] == "$2":
                        pkt.TileInParams[6] = 1
                    elif inst.dstOperands[0].IDs[-1] == "$3":
                        pkt.TileInParams[7] = 1
                        
        
                else: # the routing inst
                    src_route = inst.srcOperands[0].IDs[-1]
                    dst_route = inst.dstOperands[0].IDs[-1]
                    if src_route == "NORTH":
                        pkt.TileInParams[0] = 1
                    elif src_route == "SOUTH":
                        pkt.TileInParams[0] = 2
                    elif src_route == "WEST":
                        pkt.TileInParams[0] = 3
                    elif src_route == "EAST":
                        pkt.TileInParams[0] = 4
                    if dst_route == "NORTH":
                        pkt.TileInParams[0] = 1
                    elif dst_route == "SOUTH":
                        pkt.TileInParams[0] = 2
                    elif dst_route == "WEST":
                        pkt.TileInParams[0] = 3
                    elif dst_route == "EAST":
                        pkt.TileInParams[0] = 4
                        
                    pkt.TileInParams[src_route] = dst_route
                    
    
    @classmethod
    def make(cls, file, CtrlType, IntraCgraPktType, CgraPayloadType, TileInType, FuOutType, config, fuInCode, id_, FromFuOrRouting = FromFu):
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
            insts = vinterp.visit(tree)
            pkts = ScriptFactory.makeVectorCGRAPkts(insts, CtrlType, IntraCgraPktType, CgraPayloadType, TileInType, FuOutType, config, fuInCode, id_, FromFuOrRouting)
            return pkts
        