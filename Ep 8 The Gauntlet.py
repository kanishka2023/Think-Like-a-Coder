#The GAUNTLET
#Concept of recurssion
def f():
    if artifact found:
        send signal to parent with the dirn. the bot itself had moved(L/R)
    elif path splits:
        send 2 new copies in 2 different directions (L & R)
        f()
    elif recieves a signal:
        transfer the signal to parent with dirn. the bot itself had moved (L/R)
f()

#dirn=direction





#ANOTHER METHOD

def dirn(a):
    d=input('Enter your own direction: ')
    if a==0:
        return None
    else:
        return (d+dirn(a-1))


while True:
    if artifact found:
        gen=int(input('Enter your Generation:'))
        print('Direction is ',dirn(gen)[::-1])
        break
    else:
        make 2 copies and sen in 2 diff dirns.
