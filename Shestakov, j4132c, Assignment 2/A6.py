import time
from sys import getsizeof
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

N = 10

if rank == 0:

    for i in range(51):
        list1 = [12345] * (1000 * i + 1)
        L = getsizeof(list1)

        T = time.time()
        for j in range(N):
            MPI.COMM_WORLD.send(list1, dest = 1, tag = 1000 * i + j)
            resp = MPI.COMM_WORLD.recv(source = 1, tag = 1000 * i + j + 1)
        T = time.time() - T

        R = (2 * N * L) / T

        print(f"Iteration {i}. Object_size {L} (bytes): {R} (MB/s)")

elif rank == 1:
    for i in range(51):
        for j in range(N):
            message = MPI.COMM_WORLD.recv(source = 0, tag = 1000 * i + j)
            MPI.COMM_WORLD.send(message, dest = 0, tag = 1000 * i + j + 1)