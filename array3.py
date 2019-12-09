import numpy as np
import time

a=np.array([(1,2,3,4),(4,5,6,7)])
print(a)
print(a.ndim)#dimentional
print(a.size)#nomber of eliments
print(a.itemsize)
print(a.dtype)#datatype
print(a.shape)#rows and columns
#a=a.reshape(4,2)
print(a)#reshape array
print(a[0,2])#take particular eliment
print(a[0:,3])#3index value in both rows
print(a[0:2,3]) #0:2 means untill 0,1rows not 2nd row 3means indexvaluof the both rows
a=np.linspace(1,3,5)# it gives 5 values bitween 1 to 3
print(a)
a=np.linspace(1,3,10)# it gives 10 values between 1 to 3
print(a)
a=np.array([(1,2,3,4),(4,5,6,7)])
print(a.max())# give maximum value
print(a.min())#gives minimum value
print(a.sum())#gives sum of array


'''output:
G:\anaconda\python.exe G:/abc/arrays/array3.py
[[1 2 3 4]
 [4 5 6 7]]
2
8
4
int32
(2, 4)
[[1 2 3 4]
 [4 5 6 7]]
3
[4 7]
[4 7]
[1.  1.5 2.  2.5 3. ]
[1.         1.22222222 1.44444444 1.66666667 1.88888889 2.11111111
 2.33333333 2.55555556 2.77777778 3.        ]
7
1
32

Process finished with exit code 0
'''