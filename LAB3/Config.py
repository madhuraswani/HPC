from gem5.components.boards.simple_board import SimpleBoard

from gem5.isas import ISA
from gem5.components.cachehierarchies.classic.no_cache import NoCache
from gem5.components.memory.single_channel import SingleChannelDDR3_1600
from gem5.components.processors.cpu_types import CPUTypes
from gem5.components.processors.simple_processor import SimpleProcessor
from shutil import copyfile
import os
from gem5.resources.resource import CustomResource 
from gem5.simulate.simulator import Simulator
import argparse
from O3CPU_Config import *


cache_hierarchy = NoCache()

parser = argparse.ArgumentParser(description='Config For Simulation')
parser.add_argument("-f","--freq",type=str)
parser.add_argument("-b","--branchp",type=str)
parser.add_argument("-bs", "--blockSize",type=str)

args=parser.parse_args()

freq=args.freq
bp=args.branchp
blkS=args.blockSize
if bp=="T":
    processor=TournamentBP_O3Processor(8, 192, 256)
elif  bp=="L":
    processor=LOCALBP_O3Processor(8, 192, 256)
elif bp=="B":
    processor=BiMode_O3Processor(8, 192, 256)

memory = SingleChannelDDR3_1600("1GiB")


board = SimpleBoard(
	clk_freq=freq,
	processor=processor,
	memory=memory,
	cache_hierarchy=cache_hierarchy,

)

binary = CustomResource("../../Github/IITD_Learning/Architecture of HPC/LAB3/loadBinary")


board.set_se_binary_workload(binary)
board.processor.get_cores()[0].core.workload[0].cmd=["../../Github/IITD_Learning/Architecture of HPC/LAB3/loadBinary",blkS]

simulator = Simulator(board=board)
simulator.run()