from parser import ScriptFactory

with open("./gemm.ecgra",'r') as f:
    ScriptFactory.make(f)