l=['a','c','b','a','c','d','d','r','w','r','w']  #elements are types of blocks
print(l)
while True:
    oc=0
    for i in l:
        c=0
        for j in range(len(l)):
            if l[j]==i:
                c+=1
        print(i,'-->',c)
        if c%2==1:
            oc+=1
    print('Odd Count=',oc)
    if oc<=1:
        print('Select this stack.')
        break
    else:
        continue #look for another stack
