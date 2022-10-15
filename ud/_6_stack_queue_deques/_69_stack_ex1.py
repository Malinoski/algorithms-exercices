"""
Stack module
"""

from xmlrpc.client import boolean


class Stack:
    """
    Slack class
    """

    def __init__(self, size: int):
        self.__size = size
        self.__index_top = -1
        self.__values = [None for _ in range(size)]

    def __is_full(self) -> int:
        if self.__index_top == self.__size-1:
            return True
        return False

    def stack(self, value):
        """
        Put value on top of stack
        """
        if self.__is_full():
            print("Full stack")
        else:
            self.__index_top += 1
            self.__values[self.__index_top] = value
            print("Value added: ", value)

    def unstack(self):
        """
        Remove value from top
        """
        if self.__index_top == -1:
            print("Stack is empty")

        self.__values[self.__index_top] = None
        self.__index_top -= 1
        print("Value removed")

    def get_top(self) -> int:
        """
        Show top of stack
        """
        if self.__index_top == -1:
            print("Stack is empty")
        else:
            return self.__values[self.__index_top]

    def check_expression(self, expression_value) -> boolean:
        """
        Check expression correctness (true of false).
        If openning sentences it will be stacked
        Otherwise, closing sentences will be checked with related openning at top of stack.
        In case of ok, it will be unstacked and go on. But in case of no match, it will return error

        :param int expression_value: expression value, like a{b{c}}
        :returns: boolean
        """

        index = -1  # Only to print index error
        for char in expression_value:
            index +=1
            if char in '{[(':
                self.stack(char)
            elif char in '}])':
                top_char = self.get_top()
                if (top_char == '{' and char == '}') or (top_char == '[' and char == ']') or (top_char == '(' and char == ')'):
                    self.unstack()
                    continue
                else:
                    print(f"Error at position {index}!")
                    return False
        if self.__index_top != -1:
            print("Error due incompleteness!")
            return False
        return True


# Input samples
# a{b}
# a{{b}
# a{b(c[d]e)f}
# a{b(c[d}e)f}
# a{b(c)(e)f}
# a{b(c)((e)f}

# Create stack
expression = input("Type expression: ")
stack: Stack = Stack(size=len(expression))

# Check expression
print(stack.check_expression(expression_value=expression))
