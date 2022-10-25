"""
Module for selection sort
"""

from typing import List


def selection_sort(list: List):
    """
    Selectio Sort Method
    """

    size = len(list)

    for i in range(size):
        minimun = i # Save index to minimun

        # Search minimum
        for j in range(i+1, size):
            if list[j]<list[minimun]:
                minimun = j

        # Change left with minimum found
        if minimun != i:
            temp = list[i]
            list[i] = list[minimun]
            list[minimun] = temp

    return list

print(selection_sort([]))
print(selection_sort([3,2,1]))
print(selection_sort([1,2,3,4]))
print(selection_sort([30,2,10,13,33,1]))
