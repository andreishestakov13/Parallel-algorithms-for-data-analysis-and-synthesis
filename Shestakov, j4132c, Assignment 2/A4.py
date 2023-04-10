import time
from mpi4py import MPI

def current_time():
    return time.asctime(time.localtime(time.time()))

def sleep_for(time = 10):
    time.sleep(time)

rank = MPI.COMM_WORLD.Get_rank()

if rank == 0:

    print(f"Master with rank {rank} sleeps in {current_time}.")

    sleep_for()

    print(f"Master with rank {rank} wakes up in {current_time}.")

    message = MPI.COMM_WORLD.recv(source = 1, tag = 0)

    print(f"Master with rank {rank} receives message {message} and that took {1000 * (time.time() - message):.4f} milliseconds")

if rank == 1:
    number_triangle = [
        "1",
        "1 2",
        "1 2 3",
        "1 2 3 4",
        "1 2 3 4 5",
        "1 2 3 4",
        "1 2 3",
        "1 2",
        "1"
    ]
    time1 = time.time()
    message = MPI.COMM_WORLD.isend(time1, dest = 0, tag = 0)
    for i in number_triangle:
        print(item)
        sleep_for(0.75)