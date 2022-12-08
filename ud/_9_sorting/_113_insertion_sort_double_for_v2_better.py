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

        target = values[i]
        for j in range(i, -1, -1):

            if (i!=j) and (target < values[j]):
                temp = values[j+1]
                values[j+1] = values[j]
                values[j] = temp
        print(*values, sep = " ")

    return values

print(insertion_sort([1,4,2,6,3,8,9,9,4]))
