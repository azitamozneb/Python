#HW12-2, 12/2/2022
#Function of finding the max of 3 numbers.
#****************************************
def findMax (n1,n2,n3):
    max=n1
    if max<n2:
        max=n2
    if max<n3:
        max=n3
    return n3
#****************************************
a=int(input("Please enter a number: "))
b=int(input("Please enter a number: "))
c=int(input("Please enter a number: "))
print("The max is: ",findMax(a,b,c))