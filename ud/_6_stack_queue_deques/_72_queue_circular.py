"""
Circular queue module
"""
from xmlrpc.client import boolean


class CircularQueue:
    """
    Circular queue class
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.elements_number = 0
        self.start_index = -1
        self.end_index = -1
        self.values = [None for _ in range(capacity)]

    def is_full(self) -> boolean:
        """
        Return if queue is full
        """
        return self.elements_number == self.capacity

    def is_empty(self) -> boolean:
        """
        Return if queue is empty
        """
        return self.elements_number == 0

    def get_first(self):
        """
        Return first of queue
        """
        result = None
        if not self.is_empty():
            result = self.values[self.start_index]
        print(f"First of queue: {result}")
        return result

    def queue(self, value):
        """
        Insert a value at end from queue, where can be at rigth of at begin

        """
        if self.is_full():
            print("Queue is full!")
            return
        elif self.start_index == self.end_index == -1:
            # first element
            self.start_index = 0
            self.end_index = 0
        elif self.end_index == self.capacity-1:
            # last of array
            self.end_index = 0
        else: 
            # Middle of array
            self.end_index += 1

        self.values[self.end_index] = value
        self.elements_number += 1
        print(f"Value {value} was added at end of queue (position {self.end_index})! {self.values}")

    def unqueue(self):
        """
        Remove the first value from the queue
        """
        # To log at end
        original_position = self.start_index
        original_value = self.values[original_position]

        # Unqueue
        self.values[original_position] = None
        if self.start_index == self.capacity-1:
            self.start_index = 0
        else:
            self.start_index += 1

        self.elements_number -= 1
        print(f"Value {original_value} was removed from start of queue (position {original_position})! \{self.values}")

queue = CircularQueue(capacity=3)

# Queue
queue.queue(1)              # 1,null,null
queue.get_first()
queue.queue(2)              # 1,2, null
queue.get_first()
queue.queue(3)              # 1,2,3
queue.get_first()
queue.queue(4)              # Full!

# Unqueue
queue.unqueue()             # null,2,3
queue.unqueue()             # null,null,3

# Queue again
queue.get_first()
queue.queue(4)              # null,4,3
queue.get_first()
queue.queue(5)              # 5,4,3
queue.get_first()
