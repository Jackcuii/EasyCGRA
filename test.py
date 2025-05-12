from parser import ScriptFactory

class OPT_MUL_CONST_ADD_DUMMY:
    def __str__(self):
        return "OPT_MUL_CONST_ADD"
    
    
class CgraPayloadTypeDummy:
    def __init__(self, config, ctrl_addr, ctrl):
        self.config = config
        self.ctrl_addr = ctrl_addr
        self.ctrl = ctrl
        
    def __str__(self):
        return f"CgraPayloadType({self.config}, ctrl_addr = {self.ctrl_addr},\n ctrl = {self.ctrl})"
    
class IntraCgraPktTypeDummy:
    def __init__(self, first, second, payload):
        self.first = first
        self.second = second
        self.payload = payload
        
    def __str__(self):
        return f"IntraCgraPktType({self.first}, {self.second}, payload = {self.payload})"

class CtrlTypeDummy:
    def __init__(self, op_code, second, fu_in_code, tile_in, fu_out):
        self.op_code = op_code
        self.second = second
        self.fu_in_code = fu_in_code
        self.tile_in = tile_in
        self.fu_out = fu_out
        
    def __str__(self):
        return f"CtrlType({self.op_code}, {self.second},\n fu_in_code = {self.fu_in_code},\n tile_in = {self.tile_in},\n fu_out = {self.fu_out})"

class TileInTypeDummy:
    def __init__(self, params):
        self.params = params
        
    def __str__(self):
        return f"TileInType({self.params})"
    
class FuOutTypeDummy:
    def __init__(self, params):
        self.params = params
        
    def __str__(self):
        return f"FuOutType({self.params})"

class FuInCodeDummy:
    def __str__(self):
        return "fu_in_code"

if __name__ == "__main__":
    print("Test the Basic Functionality of the ScriptFactory")

    with open("./asms/tile4.ecgra",'r') as f:
        pkts = ScriptFactory.make(f, CgraPayloadTypeDummy, IntraCgraPktTypeDummy, CtrlTypeDummy, TileInTypeDummy, FuOutTypeDummy, "CMD_CONFIG", FuInCodeDummy, 4, FromFuOrRouting = ScriptFactory.FromFu)
        print(pkts)