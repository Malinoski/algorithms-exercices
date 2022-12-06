"""
Merge Sort
"""


from typing import List


def merge_sort(values: List) -> List:
    """
    Merge Sort

    [6 5 3 1 8 7 2 4]                   divide
    [6 5 3 1] [8 7 2 4]                 divide
    [6 5] [3 1] [8 7] [2 4]             divide
    [6] [5] [3] [1] [8] [7] [2] [4]     return sigle element

    [5 6] [1 3] [7 8] [2 4]             sort
    """
    size = len(values)
    if size > 1:

        left: List =   merge_sort(values[0:size//2])
        right: List = merge_sort(values[size//2:size])

        sorted_list: List = []
        for l in left:
            for r in right:
                if l < r:
                    sorted_list.append(l)
                else:
                    sorted_list.append(r)

        return sorted_list

    return values


# [0 6] [1 3]