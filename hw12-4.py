#HW12-4, 12/2/2022
#factorial Function.
#************************************
def factorial (n):
    fact=1
    for i in range(1,n+1):
        fact =fact *i
    return fact
#************************************
m=int(input("Please enter a number: "))
n=int(input("Please enter a number: "))
print(factorial(m)/((factorial(n)*factorial(m-n))))