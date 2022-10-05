from math import log
import numpy as np
import matplotlib.pyplot as plt

# List with 100 number, from 1 to 10, where has same distance between then. Ex.:
# [1, 1.09, 1.18, ...., 9.81, 9.90, 10]
n = np.linspace(1, 10, 1000)

# labels for plot
labels = ["Constant", "Logarithmic", "Linear", "Log Linear", "Quadradic", "Cubic", "Exponential"]

# Data with different complex functions
big_o = [
    np.ones(n.shape),       # Contant: Create array with len 100 and 1s, ex.: [1,1, ..., 1, 1]
    np.log(n),              # Logarithmic: Create new array log(n)
    n,                      # Linear: Just same array
    n*np.log(n),            # Log Linear: Create array nlog(n)
    n**2,                   # Quadradic: Create array nˆ2
    n**3,                   # Cubic: Create array nˆ3
    2**n                    # Exponential: Create array 2ˆn (the worse of then)
]

# Plot the graphic
plt.figure(figsize=(10, 8))
plt.ylim(0, 100)
for i in range(len(big_o)):
    plt.plot(n, big_o[i], label=labels)
plt.legend()
plt.ylabel('Runtime')
plt.xlabel('n')
plt.show()