#making an X
n=int(input('Enter side length:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==i or j==n-i+1:
            print('O',end=' ')
        else:
            print(' ',end=' ')
    print()
        
