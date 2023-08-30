#!/bin/bash
bp=("T" "L" "B")
freq=("600MHz" "800MHz" "1.0GHz" "1.2GHz" "1.4GHz" "1.8GHz" "2.0GHz" "2.4GHz" "3.0GHz")
blockSize=(0 2 4 8)
for n in ${bp[@]}; 
do
    for r in ${freq[@]}
    do
        for b in ${blockSize[@]}
        do
            ./build/X86/gem5.opt ../../Github/IITD_Learning/Architecture\ of\ HPC/LAB3/Config.py --freq $r --branchp $n --blockSize $b
            cp m5out/stats.txt ../../Github/IITD_Learning/Architecture\ of\ HPC/LAB3/stats/stats_$n-$r-$b.txt
        done
    done
done