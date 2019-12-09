a=[[1,2],[3,4]]
a=[(1,2),(3,4)]
#a=[{1:2},{3:4}]#not support
#a=[{1,2,3,4},{5,6,7,8}]# not support
#print(sum(sum(a,{})))
#a=[{1:2},{3:4}]not works only list of list or list of tuple
#print(sum(sum(a,{})))not works only list of list or list of tuple
b=[1,2,3,4,5,6]
print(sum(b))

a=(1,2,3,4)
print(sum(a))
a=((1,2,3),(4,5,6))
print(sum(a,()))
print(sum(sum(a,())))
a=([1,2,3],[5,6,7])
print(sum(a,[]))
print(sum(sum(a,[])))

#a={4:3,2:5}}not support
#print(sum(a))}not support
#a={1,2,3,4,5}not support
#print(sum(a))not support

'output:'
'''G:\anaconda\python.exe G:/abc/arrays/list2.py
21
10
(1, 2, 3, 4, 5, 6)
21
[1, 2, 3, 5, 6, 7]
24

Process finished with exit code 0'''
