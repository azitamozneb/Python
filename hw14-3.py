#HW14-3, 12/10/2022
#Eliminating repeated letters.
#*******************************
text=input("Please enter a word: ")
newtext=text+' '
ltext=list(newtext)
for j in range(len(ltext)-1):
    while ltext[j]!=ltext[j+1]:
        print(ltext[j],end='')
        ltext[j]=ltext[j+1]

