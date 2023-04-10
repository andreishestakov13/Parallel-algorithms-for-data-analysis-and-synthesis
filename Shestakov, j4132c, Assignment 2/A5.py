from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    first_vector = np.random.randint(100, size = 100000)
    second_vector = np.random.randint(100, size = 100000)
    first_message = np.array_split(first_vector, size - 1)
    second_message = np.array_split(second_vector, size - 1)

    for i in range(size - 1):
        first_req = MPI.COMM_WORLD.isend(first_message[i], dest = i + 1, tag = i + 1)
        second_req = MPI.COMM_WORLD.isend(second_message[i], dest = i + 1, tag = i + 1001)

    dot_product = 0

    for i in range(size - 1):
        dot_product += MPI.COMM_WORLD.recv(source = i + 1, tag = i + 2001)

    print(f"Total dot product is {dot_product}")

else:
    first_responce = MPI.COMM_WORLD.recv(source = 0, tag = rank)
    second_responce = MPI.COMM_WORLD.recv(source = 0, tag = rank + 1000)
    result = np.dot(first_responce, second_responce)
    print(f"Worker {rank} submitting sum is {result:.4f}")

    res = MPI.COMM_WORLD.isend(result, dest = 0, tag = rank + 2000)