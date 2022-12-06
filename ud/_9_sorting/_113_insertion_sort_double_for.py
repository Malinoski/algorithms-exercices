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

    for i in range(size):

        temp_i = i
        for j in range(i-1, -1, -1):

            if values[temp_i] < values[j]:
                temp = values[j]
                values[j] = values[temp_i]
                values[temp_i] = temp
                temp_i = j

    return values

print(insertion_sort([1,4,2,6,3,8,9,9,4]))
