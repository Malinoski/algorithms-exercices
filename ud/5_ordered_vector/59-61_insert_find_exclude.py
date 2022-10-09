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
        if self.last_index == -1:
            print("Empty list")
        else:
            for index in range(self.last_index+1):
                print(f"{index} - {self.values[index]}")

    # O(n)
    def insert(self, new_value):

        # Check if vector is full (returning -1 if full) - O(1)
        if self.last_index == self.size:
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

    def exclude(self, value):
        
        # Find value's index
        index_value = self.find(value=value)

        if index_value == -1:
            return False
        
        # Reorder vaetor inside of index value
        for i in range(index_value, self.last_index):
            self.values[i] = self.values[i+1]
        
        # update last index
        self.last_index -=1
        return True


v = OrderedVector(size=10)

print("\nInsert 5 ...", v.insert(5))
v.print()

print("\nInsert 4 ...", v.insert(4))
v.print()

print("\nInsert 7 ...", v.insert(7))
v.print()

print("\nInsert 1 ...", v.insert(1))
v.print()

print("\nFind 4 ...", v.find(7))
print("\nFind 1 ...", v.find(1))
print("\nFind 9 ...", v.find(9))

print("\nExclude 10 ...", v.exclude(10))
v.print()
print("\nExclude 1 ...", v.exclude(1))
v.print()
print("\nExclude 7 ...", v.exclude(7))
v.print()
print("\nExclude 4 ...", v.exclude(4))
v.print()
print("\nExclude 5 ...", v.exclude(5))
v.print()
