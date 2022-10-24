"""
Module for Linked List with Queue
"""

class Node:
    """"
    Class for Node
    """
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedListQueue:
    """
    Class for Linked List with Queue
    """

    def __init__(self):
        self.first: Node = None
        self.last: Node = None

    def queue(self, value):
        """
        Add value to end of queue
        """

        node: Node = Node(value=value)

        if self.is_empty():
            self.first = self.last = node
        else:
            self.last.next = node
            self.last = node

    def unqueue(self):
        """
        Remove first value from queue
        """

        if self.is_empty():
            print("Cant unqueue. Empty list")
        else:
            self.first = self.first.next

    def is_empty(self) -> bool:
        """
        check if queue is empty
        """
        return self.first is None

    def show_first(self):
        """
        Show first value element
        """

        if self.is_empty():
            print("Queue is empty.")
        else:
            print(self.first.value)

queue: LinkedListQueue = LinkedListQueue()
queue.show_first()

queue.queue(1)
queue.show_first()

queue.queue(2)
queue.show_first()

queue.queue(3)
queue.show_first()

queue.unqueue()
queue.show_first()

queue.unqueue()
queue.show_first()

queue.unqueue()
queue.show_first()