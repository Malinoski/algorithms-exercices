from optparse import Values
import numpy

class NotOrderedVector:

    def __init__(self, size: int):
        self.size: int = size
        self.values: numpy.ndarray = numpy.empty(shape=self.size, dtype=int)
        self.index = -1
        print("Vector: ", type(self.values))
    
    def print_vector(self):
        if self.index == -1:
            print("Empty list")
        else:
            for value in range(self.values):
                print(value)

v = NotOrderedVector(size=5)
v.print_vector()
