"""
Module to recursive function to calculate the value of a base with a exponent
"""

def calc_exponent(base, exponent) -> int:
    """
    Function to cal exponent number, given a base and a exponent
    """
    if exponent == 0:
        return 1
    return base * calc_exponent(base, exponent-1)

print(calc_exponent(2, 2)) # 2ˆ2 = 4
print(calc_exponent(2, 3)) # 2ˆ3 = 8
print(calc_exponent(3, 3)) # 3ˆ3 = 27
