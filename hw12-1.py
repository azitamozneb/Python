#HW12-1, 12/2/2022
#Findiinf the prime numbers between two numbers.
#***********************************************
n1=int(input("Please enter a number: "))
n2=int(input("Please enter a number: "))
l=[]
prime=[]
for i in range (n1,n2+1):
    l.clear()
    for j in range(1,i+1):
        if i%j==0:
            l.append(j)
    if len(l)==2:
        prime.append(i)
print(prime)