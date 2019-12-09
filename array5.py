x=[1,2,3,4,5,6,[1,2,3]]
print(x)
x=[j+2 for i in x  if type(i)==list for j in i]
print(x)

import numpy as np

x=np.array([[1,2,3,4],[3,4,5,6]])
print(x+2)

'''
output:
G:\anaconda\python.exe G:/abc/arrays/array5.py
[1, 2, 3, 4, 5, 6, [1, 2, 3]]
[3, 4, 5]
[[3 4 5 6]
 [5 6 7 8]]

Process finished with exit code 0
'''