"""
Simple recursion module with factorial
m!=m⋅(m−1)⋅(m−2)⋅(m−3)...3⋅2⋅1, where m ≥ 2.

Definitions:
- 1! = 1 (fatorial of 1) - stop criterium
- 0! = 1 (fatorial of 0)

Samples:
- 3! = 3 . 2 . 1 = 6
- 4! = 4 . 3 . 2 . 1 = 24
- 6! = 6 . 5 . 4 . 3 . 2 . 1 = 720
"""

def factorial(i):
    """
    Function to calc factorial of a number (ex.: 3*2*1)
    """

    if i <= 1:
        return 1
    return i * factorial(i-1)

print(factorial(0))
print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(5))
