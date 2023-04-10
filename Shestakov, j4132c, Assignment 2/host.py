import sys
from mpi4py import MPI

N = 3 #max number of processes

comm = MPI.COMM_WORLD.Spawn(sys.executable, args = ['worker.py'], maxprocs = N)

for i in range(N):
    data = comm.recv(source = MPI.ANY_SOURCE, tag = MPI.ANY_TAG)
    print(f"Received message '{data}' from worker {data}")

comm.Disconnect()