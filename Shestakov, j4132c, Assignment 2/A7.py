from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

n = 10
message = "Hello, world!"
cycle_list = list(range(n)) + [0]

for i in range(n + 1):
    if i == rank or i == rank + n:
        if i != 0:
            req = MPI.COMM_WORLD.irecv(source = cycle_list[i - 1], tag = i - 1)
            message = req.wait()
            print(f"Worker {rank} received message '{message}' from worker {cycle_list[i - 1]}")
        if i != n:
            MPI.COMM_WORLD.send(message, dest = cycle_list[i + 1], tag = i)
            print(f"Worker {rank} sent message to worker {cycle_list[i + 1]}")