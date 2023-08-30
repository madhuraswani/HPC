import m5
from m5.objects import *
import argparse
from Cache import *

parser = argparse.ArgumentParser(description='Config For Simulation')
parser.add_argument("-f","--freq",type=str)
parser.add_argument("--l1Size",type=str)
parser.add_argument("--l2Ratio",type=float)
parser.add_argument("--l1assoc",type=int)
parser.add_argument("--l2assoc",type=int)
parser.add_argument("--blksize",type=str)
parser.add_argument("--l1Latency",type=int)
parser.add_argument("--l2Latency",type=int)






args=parser.parse_args()
size_l1=args.l1Size
l1s=int(size_l1[:-2])
l2s=l1s*args.l2Ratio
l2Size=str(int(l2s))+"kB"
system = System()
l1Icache=L1Cache(args.l1assoc,args.l1Latency,size='16kB')
l1Dcache=L1Cache(args.l1assoc,args.l1Latency,size=args.l1Size)
l2Cache=L2Cache(assoc=args.l2assoc,latency=args.l2Latency,size=l2Size)


system.clk_domain = SrcClockDomain()
system.clk_domain.clock = args.freq
system.clk_domain.voltage_domain = VoltageDomain()

system.mem_mode = 'timing'
system.mem_ranges = [AddrRange('1GB')]

system.cpu = X86TimingSimpleCPU()

system.cpu.icache = l1Icache
system.cpu.dcache = l1Dcache

system.cpu.icache.cpu_side=system.cpu.icache_port
system.cpu.dcache.cpu_side=system.cpu.dcache_port

system.l2bus = L2XBar()

system.cpu.icache.connectBus(system.l2bus)
system.cpu.dcache.connectBus(system.l2bus)

system.l2cache = l2Cache
system.l2cache.connectCPUSideBus(system.l2bus)
system.membus = SystemXBar()
system.l2cache.connectMemSideBus(system.membus)

system.cpu.createInterruptController()
system.cpu.interrupts[0].pio = system.membus.mem_side_ports
system.cpu.interrupts[0].int_requestor = system.membus.cpu_side_ports
system.cpu.interrupts[0].int_responder = system.membus.mem_side_ports

system.system_port = system.membus.cpu_side_ports

system.mem_ctrl = MemCtrl()
system.mem_ctrl.dram = DDR3_1600_8x8()
system.mem_ctrl.dram.range = system.mem_ranges[0]
system.mem_ctrl.port = system.membus.mem_side_ports

system.workload = SEWorkload.init_compatible("../../Github/IITD_Learning/Architecture of HPC/LAB2/loadBinary")

process = Process()
process.cmd=["../../Github/IITD_Learning/Architecture of HPC/LAB2/loadBinary",args.blksize]
system.cpu.workload = process
system.cpu.createThreads()
root = Root(full_system = False, system = system)
m5.instantiate()

print("Beginning simulation!")
exit_event = m5.simulate()

print('Exiting @ tick {} because {}'.format(m5.curTick(), exit_event.getCause()))


