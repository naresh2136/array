print('{0:.2%},{0:.2}'.format(1 / 3, 1 / 3))

print(2 ** 4, 2 ** 4.0)

a = False
b = True
c = False

if a and not b and not c:
    print('cat')
elif a or not b and c:
    print('dog')
elif not a and b or c:
    print('fish')

else:
    print('parrot')

'''output:
G:\anaconda\python.exe G:/abc/arrays/list3.py
33.33%,0.33
16 16.0
fish

Process finished with exit code 0
'''