import sys


l1=[1,2,3,4,5,6]
l2=[4,5,6,7,8,9]

result=[(x,y) for x,y in zip(l1,l2)]
print(result)


for l1,l2 in zip(l1,l2):

    print(f'{l1},{l2}')



'''output:
G:\anaconda\python.exe G:/abc/arrays/array6.py
[(1, 4), (2, 5), (3, 6), (4, 7), (5, 8), (6, 9)]
1,4
2,5
3,6
4,7
5,8
6,9

Process finished with exit code 0
'''