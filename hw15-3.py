#HW15-3, 12/16/2022
#Showing n prime numbers.
#*******************************
def prime(n):
    l=[]
    for i in range (1,n+1):
        if n%i==0:
            l.append(i)
    if len(l)==2:
        return n
    else:
        return 0
#*******************************
n=int(input("Please enter a number: "))
l=[]
count=2
while len(l)!=n:
    if prime(count) != 0:
        l.append(prime(count))
    count+=1
print(l)