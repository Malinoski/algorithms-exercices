"""
Insertion Sort
"""
from typing import List

def insertion_sort(values: List[int]):
    """
    Insertion Sort
    """
    size = len(values)
    if size <= 1:
        return values

    for i in range(1, size):

        mark = values[i]
        j = i -1
        while j >= 0 and mark < values[j]:
            values[j+1] = values[j]
            values[j] = mark
            j -= 1

    return values

print(insertion_sort([3,2,1]))
print(insertion_sort([1,4,2,6,3,8,9,9,4]))
