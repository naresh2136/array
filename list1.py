
#[zip function only works one time for a file]

x = [1, 2, 3, 4, 5, 6]
y = [5, 6, 7, 8, 9, 0]
print((x) * 3)

#for x,y in zip(x,y):
#    print(x,y)

out = [(x, y) for x, y in zip(x, y)]
print(out)

'''
output:
G:\anaconda\python.exe G:/abc/arrays/list.py
[1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]
[(1, 5), (2, 6), (3, 7), (4, 8), (5, 9), (6, 0)]

Process finished with exit code 0
'''