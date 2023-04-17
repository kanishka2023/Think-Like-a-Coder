#lock
from random import randint
l=[]
for i in range(100):
    l.append('Red')
a=randint(0,99)
l[a]='Green'
for i in range(100):
    print(i+1,'-->',l[i])

#key
for i in range(100):
    if l[i]=='Green':
        print('Angle = ',i+1,'*')
    
