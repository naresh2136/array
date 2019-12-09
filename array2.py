import numpy as np
import time
import sys


size=1000000

l1=range(size)
l2=range(size)

a1=list(np.arange(size))
a2=list(np.arange(size))

start=time.time()
resullt=a1+a2
result=[(x+y) for x,y in zip(l1,l2)]
print(time.time()-start)

starttime=time.time()
result=a1+a2
print(time.time()-starttime)