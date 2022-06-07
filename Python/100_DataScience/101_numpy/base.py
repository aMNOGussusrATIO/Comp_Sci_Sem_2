import numpy as np
from numpy import random
size = int(input("Enter a size: "))
min1 = int(input("Enter the minimum: "))
max1 = int(input("Enter the maximum: "))

rndm = np.random.randint(min1, size, max1)

array = np.array(rndm)
print(array)