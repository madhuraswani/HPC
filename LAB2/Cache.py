from m5.objects import Cache

class L1Cache(Cache):
    assoc = 2
    data_latency = 2
    tag_latency = 2
    response_latency = 2
    mshrs = 4
    tgts_per_mshr = 20
    size='64kB'
    def __init__(self,assoc,latency,size):
        super(L1Cache, self).__init__()
        self.assoc=assoc
        self.data_latency=latency
        self.tag_latency=latency
        self.response_latency=latency
        self.size=size
    def connectBus(self, bus):
        self.mem_side = bus.cpu_side_ports


class L2Cache(Cache):
    assoc = 8
    tag_latency = 20
    data_latency = 20
    response_latency = 20
    mshrs = 20
    tgts_per_mshr = 12
    
    size='256kB'
    def __init__(self,assoc,latency,size):
        super(L2Cache, self).__init__()
        self.assoc=assoc
        self.data_latency=latency
        self.tag_latency=latency
        self.response_latency=latency
        self.size=size
    def connectCPUSideBus(self, bus):
        self.cpu_side = bus.mem_side_ports

    def connectMemSideBus(self, bus):
        self.mem_side = bus.cpu_side_ports