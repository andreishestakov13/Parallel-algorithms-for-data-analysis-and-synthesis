import time
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    for i in range(1, size):
        data = MPI.COMM_WORLD.recv(source = i, tag = i)
        print(f"Message '{data[0]}' from rank {i} took {1000 * (time.time() - data[1]):.4f} ms")
else:
    message = "Hello, world!"
    current_time = time.time()
    data = (message, current_time)
    MPI.COMM_WORLD.send(data, dest = 0, tag = rank)