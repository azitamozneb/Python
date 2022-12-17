#HW15-4, 12/17/2022
#*******************************************
def prime(n):
    l=[]
    for i in range (1,n+1):
        if n%i==0:
            l.append(i)
    if len(l)==2:
        return 'y'
    else:
        return 'n'
#******************************************
n=int(input("Please enter a number: "))
n1=2
n2=3
while (n2-1)-n1 != n:
    if prime(n2) == 'y':
        n1=n2 
    n2+=1
for i in range(n1+1,n2):
    print(i,',',end='')
