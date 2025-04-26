

class Sanitizer:
    max_simultaneous_mem_read = 1
    max_simultaneous_mem_write = 1
    def __init__(self, max_simultaneous_mem_read, max_simultaneous_mem_write):
        self.max_simultaneous_mem_read = max_simultaneous_mem_read
        self.max_simultaneous_mem_write = max_simultaneous_mem_write
        
    def sanitize(self, insts):
        dsts = []
        
        # check the dsts
        for inst in insts:
            for dst in inst.dstOperands:
                if dst.text in dsts:
                    raise ValueError("Data Race!")
                dsts.append(dst.text)
                
        # check simultaneous read and write to memory
        
        for inst in insts:
            for dst in inst.dstOperands:
                if dst.text in dsts:
                    raise ValueError("Data Race!")
                dsts.append(dst.text)
