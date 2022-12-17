#HW12-3, 12/2/2022
#Finding LCM
#****************************************
n1=int(input("Please enter a number: "))
n2=int(input("Please enter a number: "))
reminder=True
while reminder:
    for i in range (1,n2+1):
        if (n1*i)%n2 ==0:
            print(n1*i)
            reminder=False
            break

    