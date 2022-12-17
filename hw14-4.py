#HW14-4, 12/11/2022
#Determining if sum of digits is a prime number.
#*******************************
def prime(n):
    l=[]
    for i in range (1,n+1):
        if n%i==0:
            l.append(i)
    if len(l)==2:
        return 'y'
    else:
        return 'n'
#*******************************
l=[]
for i in range(1,10000):
    l=(list(str(i)))
    p=0
    print(l)
    for i in l:
        p=int(i)+p
    print(p)
    print(prime(p))
