"""
Deque circular module.
Following the example [1,2,3,4,5], the front is right (5) and back is left (1)
"""


class DequeCircular:
    """
    Class Deque Circular
    """

    def __init__(self, capacity: int):
        """
        Deque Circular constructor
        """

        self.capacity = capacity
        self.quantity_elements = 0
        self.start_index = -1
        self.end_index = -1
        self.values = [None for _ in range(self.capacity)] # ex.: [None, None, None]

    def is_full(self) -> bool:
        """
        Check if is full
        """
        return self.quantity_elements == self.capacity

    def is_empty(self) -> bool:
        """
        Check if is empty
        """
        return self.quantity_elements == 0

    def insert_front(self, value):
        """
        Insert value at front of vector (right side)
        """

        # If is full
        if self.is_full():
            print("Is full!")
            return

        # Change index if empty
        if self.is_empty():
            self.start_index = self.end_index = 0

        # Increment index to 0 if index is in final
        elif self.start_index == self.capacity-1:
            self.start_index = 0

        # Just increment to right
        else:
            self.start_index += 1

        self.quantity_elements += 1
        self.values[self.start_index] = value
        print(f"Value {value} was inserted at position {self.start_index}. {self.values}")

    def insert_back(self, value):
        """
        Insert value at back of vector (left side)
        """

        # If is full
        if self.is_full():
            print("Is full!")
            return

        # Change index if empty
        if self.is_empty():
            self.start_index = self.end_index = 0

        # Increment index to last position if is in begining
        elif self.end_index == 0:
            self.end_index = self.capacity-1

        # Just decrement to left
        else:
            self.end_index -= 1

        self.quantity_elements += 1
        self.values[self.end_index] = value
        print(f"Value {value} was inserted at position {self.end_index}. {self.values}")


    def remove_front(self):
        """
        Remove element at front of vector (right side)
        """

        # If is empty
        if self.is_empty():
            print("Is empty!")
            return

        # Remove element
        temp_value = self.values[self.start_index]
        self.values[self.start_index] = None

        # Update start index
        temp_index = self.start_index
        if self.start_index == 0:
            self.start_index = self.capacity-1
        else:
            self.start_index -= 1
        
        # update quantity
        self.quantity_elements -= 1

        print(f"Value {temp_value} was removed at position {temp_index}. {self.values}")

    def remove_back(self):
        """
        Remove element at back of vector (left side)
        """

        # If is empty
        if self.is_empty():
            print("Is empty!")
            return

        # Remove element
        temp_value = self.values[self.end_index]
        self.values[self.end_index] = None

        # Update end index
        temp_index = self.end_index
        if self.end_index == self.capacity-1:
            self.end_index = 0
        else:
            self.end_index += 1

        # update quantity
        self.quantity_elements -= 1

        print(f"Value {temp_value} was removed at position {temp_index}. {self.values}")

deque = DequeCircular(5)

deque.insert_front(1)   # [1, None, None, None, None]
deque.insert_front(2)   # [1, 2, None, None, None]
deque.insert_back(3)    # [1, 2, None, None, 3]
deque.insert_back(4)    # [1, 2, None, 4, 3]
deque.insert_back(5)    # [1, 2, 5, 4, 3]
deque.insert_front(6)

deque.remove_front()    # [1, None, 5, 4, 3]
deque.remove_front()    # [None, None, 5, 4, 3]
deque.remove_front()    # [None, None, 5, 4, None]
deque.remove_front()    # [None, None, 5, None, None]
deque.remove_front()    # [None, None, None, None, None]

deque.insert_front(1)   # [1, None, None, None, None]
deque.insert_back(2)    # [1, None, None, None, 2]
deque.insert_front(3)   # [1, 3, None, None, 2]
deque.insert_back(4)    # [1, 3, None, 4, 2]
deque.insert_front(5)   # [1, 3, 5, 4, 2]
