#!/bin/bash
size=("64kB" "128kB")
ratio=(2 4 8)
l1assoc=(2 4)
blksize=(0 4 8)
l2assoc=(8 16)
l1Lat=(3 5)
l2Lat=(20 30)
for n in ${size[@]}; 
do
    for r in ${ratio[@]}
    do
        for a in ${l1assoc[@]}
        do
            for b in ${l2assoc[@]}
            do
                for l1 in ${l1Lat[@]}
                do
                    for l2 in ${l2Lat[@]}
                    do
                        for bl in ${blksize[@]}
                        do
                            ./build/X86/gem5.opt ../../Github/IITD_Learning/Architecture\ of\ HPC/LAB2/Config.py -f "600MHz" --l1Size $n --l2Ratio $r --l1assoc $a --l2assoc $b --blksize $bl --l1Latency $l1 --l2Latency $l2
                            cp m5out/stats.txt ../../Github/IITD_Learning/Architecture\ of\ HPC/LAB2/stats/stats_l1Size_$n-l1nl2ratio_$r-l1assoc_$a-l2assoc_$b-l1Latency_$l1-l2Latency_$l2-blkSize_$bl.txt
                        done
                    done
                done
            done
        done
    done
done
