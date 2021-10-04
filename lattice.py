#!/usr/bin/python 

import sys
from string import *
import os
from subprocess import *
    
for i in range(0,23):
 temp=250+i*125
 fn="in."+str(temp)
 call("cat script_part1.txt >"+fn, shell=True)
 s="log log."+str(temp)+" "
 call("echo " +s+ ">>"+fn, shell=True)
 s="velocity all create " +str(float(temp))+ " 78621 dist gaussian"
 call("echo " +s+ ">>"+fn, shell=True)
 s="fix NPT all npt temp " +str(float(temp))+ " " +str(float(temp))+ " 0.005 iso 0.0 0.0 10.0 drag 0.2"
 call("echo " +s+ ">>"+fn, shell=True)
 s="thermo 10 "
 call("echo " +s+ ">>"+fn, shell=True)
 call("echo " +s+ ">>"+fn, shell=True)
 s="run 3000 "
 call("echo " +s+ ">>"+fn, shell=True)
 call("time mpirun -np 2 /usr/local/Cellar/lammps/2021-09-29/bin/lmp_mpi -sf opt < "+fn, shell=True)