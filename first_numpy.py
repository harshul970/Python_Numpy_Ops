import numpy as np

a1 = np.arange(20)          # Creating 1-D numpy array; This array will have elements from 0 to input number-1
print(a1)

L1 = [(1,3),(4,6),(8,12),(7,5)]
a2 = np.array(L1)           # Creating numpy array using list
print(a2)

l1 = [3,5,6,7,8,9]
l2 = [5,6,3,9,2,1]

npa1 = np.array(l1)
npa2 = np.array(l2)

result2 = npa1 + npa2       # Adding two numpy arrays

print (result2)

b = np.linspace(2,10,5)     # Creating array using linspace method. In this Example, '2' should be the starting number
                            # '10' should be the end number, 5 should be number of partitions
print(b)
