allname=[]
name1=input("Please enter a name: ")
allname.append(name1)
while True:
    lastCh= name1[-1]
    name2=input("Please enter a name: ")
    firstCh= name2[0]
    if lastCh==firstCh:
        allname.append(name2)
        print('OK')
    else:
        print(f"Please enter the name that saterts with {lastCh}")
    name1=input("Please enter a name: ")
