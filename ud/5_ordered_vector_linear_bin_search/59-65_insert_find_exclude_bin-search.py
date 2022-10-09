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
    def insert(self, value):

        # If full
        if self.last_index+1 == self.size:
            return -1 

        # Find position to insert
        position_insert = 0
        for i in range(self.last_index+1):
            if value < self.values[i]:
                position_insert = i
                break
            # include at last
            if i == self.last_index:
                position_insert = i+1
        
        # Relocate vector
        for i in range(self.last_index+1, position_insert, -1):
            self.values[i] = self.values[i-1]

        # Insert new value at position to insert
        self.values[position_insert] = value
        self.last_index += 1
        return position_insert
    
    # O(n)
    def find_linear(self, value):
        for i in range(self.last_index+1):
            if value < self.values[i]:
                # If less than first in an ordered vector, so the element do not exist
                return -1 
            if value == self.values[i]:
                # Found
                return i
        
        # Not found
        return -1

    # O(log n)
    def find_binary(self, value):

        start_index = 0
        end_index = self.last_index

        while(start_index <= end_index):

            middle_index = int((start_index + end_index) / 2)

            if self.values[middle_index] == value:
                # Found!
                return middle_index
            elif value < self.values[middle_index]:
                # Update indexes to LEFT
                end_index = middle_index-1
            else:
                # Update indexes to RIGHT
                start_index = middle_index+1
        
        # Not found
        return -1

    def exclude(self, value):
        
        # Find value's index
        index_value = self.find_linear(value=value)

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

print("\nInsert 2 ...", v.insert(2))
v.print()

print("\nInsert 11 ...", v.insert(11))
v.print()

print("\nInsert 6 ...", v.insert(6))
v.print()

print("\nFind lin 7 ...", v.find_linear(7))
print("Find lin 1 ...", v.find_linear(1))
print("Find lin 9 ...", v.find_linear(9))

print("Find bin 5 ...", v.find_binary(5))
print("Find bin 4 ...", v.find_binary(4))
print("Find bin 1 ...", v.find_binary(1))
print("Find bin 99 ...", v.find_binary(99))



# print("\nExclude 10 ...", v.exclude(10))
# v.print()
# print("\nExclude 1 ...", v.exclude(1))
# v.print()
# print("\nExclude 7 ...", v.exclude(7))
# v.print()
# print("\nExclude 4 ...", v.exclude(4))
# v.print()
# print("\nExclude 5 ...", v.exclude(5))
# v.print()
