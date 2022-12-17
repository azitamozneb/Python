#hw13-4, 12/9/2022
#Determining a complete prime number.
#****************************************
def prime(n):
    l=[]
    for i in range (1,n+1):
        if n%i==0:
            l.append(i)
    if len(l)==2:
        return 'y'
    else:
        return 'n'
#****************************************
def totallprime(n):
    s=list(str(n))
    print(s)
    answer=[]
    newN=''
    while len(s)>1:

        for i in s:
            newN=newN+str(i)

        answer.append(prime(int(newN)))
        s.pop()
        newN=''

    if 'n' not in answer:
        return "Yes"
    else:
        return "No"
#****************************************
n=int(input("Please enter a number: "))
print(totallprime(n))