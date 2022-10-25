"""
Module do bublle sort implementation
"""

from typing import List


def bubble_sort_with_for(list: List):
    """
    Bubble Sort Method
    """

    size = len(list)
    for i in range(size-1):
        for j in range(size-i-1):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    return list

def bubble_sort_with_while(list: List):
    """
    Bubble Sort Method
    """

    if list is not None:
        size = len(list)
        i = 0
        while i < size:
            j = 0
            while j < (size-i-1):
                if list[j] > list[j+1]:
                    temp = list[j]
                    list[j] = list[j+1]
                    list[j+1] = temp
                j += 1
            i += 1
        return list
    return list

print(bubble_sort_with_for([12,6,7,22,2]))
print(bubble_sort_with_for([3]))
print(bubble_sort_with_for([10,9,8,7,6,5,4,3,2,1,0]))
print(bubble_sort_with_for([]))

print(bubble_sort_with_while([12,6,7,22,2]))
print(bubble_sort_with_while([3]))
print(bubble_sort_with_while([10,9,8,7,6,5,4,3,2,1,0]))
print(bubble_sort_with_while([]))
