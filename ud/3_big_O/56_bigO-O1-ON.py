import numpy

class NotOrderedVector:

    def __init__(self, size: int):
        self.size: int = size
        self.values: numpy.ndarray = numpy.empty(shape=self.size, dtype=int)
        self.last_index = -1
        print("Vector: ", type(self.values))
    
    # O(n)
    def print_vector(self):
        print("\n## Print")
        if self.last_index == -1:
            print("Empty list")
        else:
            for index in range(self.last_index+1):
                print(f"index {index}, value {self.values[index]}")
    
    # O(1)
    def insert_vector(self, value):
        if self.size -1 == self.last_index:
            print(f"Cant insert value '{value}', due list are full!")
        else:
            self.last_index += 1
            self.values[self.last_index] = value
            print("Inserted ", self.values[self.last_index])

    # O(n)
    def find_element_vector(self, target_value):
        print("\n# Find")
        for index in range(self.size):
            if target_value == self.values[index]:
                print(f"Element {target_value} found!")
                return index
        print(f"Element {target_value} not found!")
        return -1

    # O(n)
    def remove_element(self, target_value):
        print(f"\n## Remove {target_value}")
        index_target = self.find_element_vector(target_value)
        if index_target == -1:
            print(f"Cant remove element {target_value} (not found)")
        else:
            print(f"Removing {self.values[index_target]} ...")
            for index in range(index_target, self.size-1):
                self.values[index] = self.values[index+1]
        self.last_index -= 1


v = NotOrderedVector(size=5)

# Insert
v.print_vector()
v.insert_vector(1)
v.insert_vector(2)
v.insert_vector(3)
v.insert_vector(4)
v.insert_vector(5)
v.insert_vector(6)
v.print_vector()

# Find
v.find_element_vector(1)
v.find_element_vector(5)
v.find_element_vector(123)

# Remove
v.remove_element(3)
v.print_vector()

# Remove
v.remove_element(5)
v.print_vector()

# Remove
v.remove_element(4)
v.print_vector()

# Remove
v.remove_element(2)
v.print_vector()

# Remove
v.remove_element(1)
v.print_vector()