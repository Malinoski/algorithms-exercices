"""
Simple Recursion
"""

def print_n_times(i):
    """
    Simple recursion function where print N times
    """

    if i == 0:
        return
    print("Recursion")
    print_n_times(i-1)

print_n_times(5)