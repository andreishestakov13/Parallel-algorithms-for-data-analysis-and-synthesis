import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

class Multiplication:
    def __init__(self, n1, n2):
        self.multiplication = n1 * n2

object1 = list(range(101))
object2 = Multiplication(123, 456)
object3 = a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

list_of_objects = [object1, object2, object3]

if rank == 0:
    massage = list_of_objects
else:
    message = None


message = MPI.COMM_WORLD.scatter(data, root=0)
print("Rank ", rank, "shows message:\n", data, "\n")
