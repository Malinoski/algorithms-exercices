"""
Simple Recursion
"""

def sum(i) -> int:
    """
    Function to sum number, ex.: 
    3 -> 6 (1+2+3) or 
    4 -> 10 (1+2+3+4)
    """
    if i == 0:
        return 0
    return i + sum(i-1)

result = sum(4)
print(result)
