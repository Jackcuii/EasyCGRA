import sys
from antlr4 import *
from EasyCGRALexer import EasyCGRALexer
from EasyCGRAParser import EasyCGRAParser
from RealEasyCGRAParserVisitor import RealEasyCGRAParserVisitor


# from ... import *  # TODO: import the correct file of the opCodes of VectorCGRA
class OPT_MUL_CONST_ADD_DUMMY:
    def __str__(self):
        return "OPT_MUL_CONST_ADD"

class EasyToVectorOpcodeMap:
    opMap = {
        EasyCGRAParser.MUL_CONST_ADD: OPT_MUL_CONST_ADD_DUMMY(),
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
        return pkt

    
class ScriptFactory:
    FromFu = 0
    FromRouting = 1
    def makeVectorCGRAPkts(ScriptInsts, CtrlType,IntraCgraPktType, CgraPayloadType, TileInType, FuOutType, config, fuInCode, id_, FromFuOrRouting = FromRouting): #False means from routing inst
        pkts = []
        for cInst in ScriptInsts:
            #print("cInst: ", cInst)
            pkt = VectorCGRApkt(CtrlType, IntraCgraPktType, CgraPayloadType, TileInType, FuOutType, config, None, fuInCode, id_)
            # find opcode
            for inst in cInst:
                if inst.opCode != EasyCGRAParser.MOV: # not the routing inst
                    pkt.OpCode = EasyToVectorOpcodeMap.opMap[inst.opCode]
            
            if pkt.OpCode is None:
                pkt.OpCode = ... # TODO: alter this with your pure routing inst's opCode
            # update the params
            for inst in cInst:
                if inst.opCode != EasyCGRAParser.MOV:
                    # cope with the srcOperands
                    if FromFuOrRouting == ScriptFactory.FromRouting:
                        #print("inst.srcOperands: ", inst.srcOperands)
                        for idx in range(len(inst.srcOperands)):
                            if len(inst.srcOperands[idx].IDs) == 0:
                                continue
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
                        pkt.FuOutParams[0] = 1
                    elif inst.dstOperands[0].IDs[-1] == "SOUTH":
                        pkt.FuOutParams[1] = 1
                    elif inst.dstOperands[0].IDs[-1] == "WEST":
                        pkt.FuOutParams[2] = 1
                    elif inst.dstOperands[0].IDs[-1] == "EAST":
                        pkt.FuOutParams[3] = 1
                    elif inst.dstOperands[0].IDs[-1] == "$0":
                        pkt.FuOutParams[4] = 1
                    elif inst.dstOperands[0].IDs[-1] == "$1":
                        pkt.FuOutParams[5] = 1
                    elif inst.dstOperands[0].IDs[-1] == "$2":
                        pkt.FuOutParams[6] = 1
                    elif inst.dstOperands[0].IDs[-1] == "$3":
                        pkt.FuOutParams[7] = 1
                        
        
                else: # the routing inst
                    src_route = inst.srcOperands[0].IDs[-1]
                    dst_route = inst.dstOperands[0].IDs[-1]
                    if src_route == "NORTH":
                        src_route_idx = 1
                    elif src_route == "SOUTH":
                        src_route_idx = 2
                    elif src_route == "WEST":
                        src_route_idx = 3
                    elif src_route == "EAST":
                        src_route_idx = 4
                    if dst_route == "NORTH":
                        dst_route_idx = 0
                    elif dst_route == "SOUTH":
                        dst_route_idx = 1
                    elif dst_route == "WEST":
                        dst_route_idx = 2
                    elif dst_route == "EAST":
                        dst_route_idx = 3
                        
                    pkt.TileInParams[dst_route_idx] = src_route_idx
            pkts.append(pkt.makeCtrlPkt())
            
        return pkts
    
                    
    
    @classmethod
    def make(cls, file, CtrlType, IntraCgraPktType, CgraPayloadType, TileInType, FuOutType, config, fuInCode, id_, FromFuOrRouting = FromRouting):
        input_stream = FileStream(file)
        lexer = EasyCGRALexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = EasyCGRAParser(stream)
        tree = parser.compilationUnit()
        #print(type(tree))
        if parser.getNumberOfSyntaxErrors() > 0:
            print(f"Syntax errors in your script {file}.")
            return None
        else:
            vinterp = RealEasyCGRAParserVisitor()
            #print("Tree: ", tree)
            insts = vinterp.visitCompilationUnit(tree)
            #insts = vinterp.visitCompilationUnit(tree)
            #print("Insts: ", insts)
            pkts = ScriptFactory.makeVectorCGRAPkts(insts, CtrlType, IntraCgraPktType, CgraPayloadType, TileInType, FuOutType, config, fuInCode, id_, FromFuOrRouting)
            #print("Pkts: ", pkts)
            return pkts
        