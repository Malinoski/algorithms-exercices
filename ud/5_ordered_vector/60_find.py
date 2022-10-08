import numpy

class OrderedVector:

    def __init__(self, size: int):
        self.size: int = size
        
        self.values: numpy.ndarray = numpy.empty(self.size, dtype=int)
        # self.values: list = [None for _ in range(self.size)] # you can use this instead

        self.last_index = -1
        print("Vector: ", type(self.values))

    # O(n)
    def print(self):
        print("\n## Print")
        if self.last_index == -1:
            print("Empty list")
        else:
            for index in range(self.last_index+1):
                print(f"{index} - {self.values[index]}")

    # O(n)
    def insert(self, new_value):

        # Check if vector is full (returning -1 if full) - O(1)
        if self.last_index == self.size:
            print("Vector is full")
            return -1

        # Search index to insert - for O(n)
        index_to_insert = 0 # Useful to insert the first value
        for i in range(self.last_index+1):
            if new_value<self.values[i]:
                index_to_insert = i
                break
            if i == self.last_index:
                index_to_insert = self.last_index+1
        
        # Reorder remainging elements, from end to index to insert - for O(n)
        for i in range(self.last_index+1, index_to_insert, -1):
            self.values[i] = self.values[i-1]
        
        # Update last index
        self.last_index += 1

        # Insert value at index - O(1)
        self.values[index_to_insert] = new_value
        return index_to_insert

    # O(n)
    def find(self, value):

        for i in range(self.last_index+1):
            if value < self.values[i]:
                # If less than first in an ordered vector, so the element do not exist
                return -1 
            if value == self.values[i]:
                # Found
                return i
        
        # Not found
        return -1

v = OrderedVector(size=10)
v.print()
v.insert(5)
v.print()
v.insert(4)
v.print()
v.insert(7)
v.print()
v.insert(1)
v.print()

print("Find: ", v.find(7))
print("Find: ", v.find(1))
print("Find: ", v.find(9))

