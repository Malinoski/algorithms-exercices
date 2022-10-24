"""
Module for stack with simply linked list
"""


class Node:
    """
    Class for Node
    """

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedListStack:
    """
    Class for stack with simply linked list
    """

    def __init__(self):
        self.first = None

    def stack(self, value):
        """
        Add value at top
        """

        node: Node = Node(value=value)
        if self.is_empty():
            self.first = node
        else:
            node.next = self.first
            self.first = node

    def unstack(self):
        """
        Remove value from top
        """

        if self.is_empty():
            print("Can not unstack. Empty list")
        else:
            self.first = self.first.next


    def is_empty(self) -> bool:
        """
        Check if is stack is empty
        """

        return self.first is None

    def show_top(self):
        """
        Show value at top
        """

        if self.is_empty():
            print("Empty list")
        else:
            print(self.first.value)


stack: LinkedListStack = LinkedListStack()

stack.stack(1)
stack.show_top()

stack.stack(2)
stack.show_top()

stack.unstack()
stack.show_top()

stack.unstack()
stack.show_top()

stack.stack(1)
stack.stack(2)
stack.stack(3)
stack.stack(4)
stack.show_top()
