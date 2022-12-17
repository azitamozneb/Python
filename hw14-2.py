#HW14-2, 12/10/2022
#Drawing H pattern.
#*******************************
for i in range (0,12):
    for j in range (0,12):
        if j==0 or j==11 or i==5:
            print('*',end=' ')
        else:
            print(end='  ')
    print('')