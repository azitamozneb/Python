#hw13-3, 12/9/2022
#Finding numbers which include two digits of 2.
#**************************************************************
print(list(i for i in range(1,10000) if str(i).count('2')==2))