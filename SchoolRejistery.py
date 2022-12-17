student= dict()
Course=["cpp","java","python"]
studnumber=1
#**********************************
def Register(name,Lname,Pnumber):
    global studnumber
    info=[name,Lname,Pnumber]
    student[studnumber]= info
    studnumber +=1
#**********************************
def Search(nameOfCourse):
    if nameOfCourse in Course:
        return True
    else:
        return False
#**********************************
flag = True
while flag:
    c =int( input("1) Register 2)Search Course 3)Show Info 4)Exit: "))
    if c==1 :
        n=input("Please enter your name: ")
        l=input("Pleasae enter your last name: ")
        p=input("Please enter tour phone number: ")
        Register(n,l,p)
    elif c==2:
        sc= input("Please enter your course: ")
        print(Search(sc))
    elif c==3:
        print(student)
    else:
        flag = False