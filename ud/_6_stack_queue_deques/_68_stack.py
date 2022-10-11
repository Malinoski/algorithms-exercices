class Stack:
    
    def __init__(self, size: int):
        self.__size = size
        self.__index_top = -1
        self.__values = [None for _ in range(size)]

    def __is_full(self) -> int:
        if self.__index_top == self.__size-1:
            return True
        else:
            return False

    def stack(self, value):
        if self.__is_full():
            print("Full stack")
        else:
            self.__index_top += 1
            self.__values[self.__index_top] = value
            print("Value added: ", value)

    def unstack(self):
        if self.__index_top == -1:
            print("Stack is empty")
        else:
            self.__values[self.__index_top] = None
            self.__index_top -= 1
            print("Value removed")
    
    def show_top(self) -> int:
        if self.__index_top == -1:
            print("Stack is empty")
        else:
            return self.__values[self.__index_top]

stack: Stack = Stack(size=5)
print(stack.show_top())
stack.stack(1)
stack.stack(2)
stack.stack(3)
stack.stack(4)
stack.stack(5)
print(stack.show_top())
stack.stack(6)
