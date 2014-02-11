#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2013 Jérémie DECOCK (http://www.jdhp.org)

# run:
#   mpirun python master.py
#     or
#   mpiexec python master.py

from mpi4py import MPI
import sys

comm = MPI.COMM_SELF.Spawn(sys.executable, args=['worker.py'], maxprocs=5)

result = comm.reduce(None, op=MPI.SUM, root=MPI.ROOT)

print "master:", result

comm.Disconnect()
