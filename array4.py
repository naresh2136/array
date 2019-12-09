
#in arrays axis=1 means rows (axis=1=rows)
#in arrays axis=0 means columns (axis=0=columns)

import numpy as np
a=np.array([[1,2,3,4],[4,5,6,7]])
print(sum(a))
print(a.sum(axis=0))#it gives sum of all colums values
print(a.sum(axis=1))# it gives sum of all rows values

print(np.sqrt(a))#it gives root value os each eliment in the array √
print(np.std(a))# it gives standard devision value of the array. mean value of the array

'============================='
a=np.array([(1,2,3),(3,4,5)])
b=np.array([(4,5,6),(7,8,9)])

print(a+b)
print(a-b)
print(a*b)
print(a/b)
'================================'
a=np.array([(1,2,3),(3,4,5)])
b=np.array([(4,5,6),(7,8,9)])

print(np.vstack((a,b)))#convert two arrays in vertically into single array
print(np.hstack((a,b)))#convert two arrays in horigentally into single array
print(a.ravel())#convert array (list of list) into single list

'''output:
G:\anaconda\python.exe G:/abc/arrays/array4.py
[ 5  7  9 11]
[ 5  7  9 11]
[10 22]
[[1.         1.41421356 1.73205081 2.        ]
 [2.         2.23606798 2.44948974 2.64575131]]
1.8708286933869707
[[ 5  7  9]
 [10 12 14]]
[[-3 -3 -3]
 [-4 -4 -4]]
[[ 4 10 18]
 [21 32 45]]
[[0.25       0.4        0.5       ]
 [0.42857143 0.5        0.55555556]]
[[1 2 3]
 [3 4 5]
 [4 5 6]
 [7 8 9]]
[[1 2 3 4 5 6]
 [3 4 5 7 8 9]]
[1 2 3 3 4 5]

Process finished with exit code 0
'''