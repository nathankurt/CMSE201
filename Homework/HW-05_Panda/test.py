import numpy as np


ls1 = [1,2,3,4,5,6]
ls2 = [1,2,3,4,5,6]

ls3 = map(lambda x,y: x+y, ls1,ls2)

print("normal python list", ls3)

npls1 = np.array(1,2,3,4,5,6)
npls2 = np.array(1,2,3,4,5,6)

npls3 = npls1 + npls2

print("Numpy list adding", npls3)