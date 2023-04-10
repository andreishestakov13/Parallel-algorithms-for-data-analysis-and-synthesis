import time
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

def waiting(sleep_for = 25):
    spacing = int(sleep_for / 5)
    for i in range(spacing):
        time.sleep(5)
        print(f"waiting")

if rank == 0:
    message = "Hello, world!"
    MPI.COMM_WORLD.send(message, dest = 1, tag = 1)
    waiting()
    response = MPI.COMM_WORLD.recv(source = 1, tag = 1)
    print(f"Host {rank} received worker message '{response}'")

if rank == 1:
    req = MPI.COMM_WORLD.recv(source = 0, tag = 1)
    print(f"Worker {rank} received host message '{req}'")
    response = req + "is received. Sending backwards."
    MPI.COMM_WORLD.isend(response, dest = 0, tag = 1)
    print(f"Worker {rank} sent message '{response}' to host")