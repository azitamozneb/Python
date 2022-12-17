#hw13-2, 12/9/2022
#Findin perfect numbers by using a function.
#********************************************
def perfectNumber (num):
    l=[]
    for i in range (1,num):
        if num%i ==0:
            l.append(i)
    if sum(l)== num:
        return "yes"
    else:
        return "No"
        
#********************************************s
l=[]
for i in range (1,10000):
    if perfectNumber(i) == "yes":
        l.append(i)
print (l)