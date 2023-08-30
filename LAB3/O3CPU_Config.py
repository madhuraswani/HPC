from gem5.components.processors.simple_processor import SimpleProcessor
from gem5.components.processors.cpu_types import CPUTypes
from gem5.isas import ISA
from m5.objects.BranchPredictor import *

class TournamentBP_O3Processor(SimpleProcessor):
    def __init__(self,width, rob_size, num_regs):
        super().__init__(cpu_type=CPUTypes.O3,num_cores=1, isa=ISA.X86)

        self.cores[0].core.branchPred = TournamentBP()
    
class LOCALBP_O3Processor(SimpleProcessor):
    def __init__(self,width, rob_size, num_regs):
        super().__init__(cpu_type=CPUTypes.O3,num_cores=1, isa=ISA.X86)
        
        self.cores[0].core.branchPred = LocalBP()

class BiMode_O3Processor(SimpleProcessor):
    def __init__(self,width, rob_size, num_regs):
        super().__init__(cpu_type=CPUTypes.O3,num_cores=1, isa=ISA.X86)

        self.cores[0].core.branchPred = BiModeBP()