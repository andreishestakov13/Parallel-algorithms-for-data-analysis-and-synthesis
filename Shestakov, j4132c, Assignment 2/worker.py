import numpy
from mpi4py import MPI

comm = MPI.Comm.Get_parent()
rank = comm.Get_rank()

comm.send(rank, dest=0, tag=10)

print(f"Worker created with rank {rank}")

comm.Disconnect()