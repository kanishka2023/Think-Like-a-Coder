def mxl (l,i):                        #mxl= maximum in left
    ll=l[0:i]
    ll.sort()
    return ll[len(ll)-1]
def mxr (l,i):                        #mxr= maximum in right
    lr=l[i+1:len(l)]
    lr.sort()
    return lr[len(lr)-1]

l=[8,4,2,10,11,8,9,12]               #heights of different set of blocks
e=0
for i in range(1,len(l)-1):
    if mxl(l,i)>=mxr(l,i):
        a=mxr(l,i)- l[i]
    else:
        a=mxl(l,i)- l[i]
    if a>0:
        e+=a
print('Total Energy level is ',e,'units')
