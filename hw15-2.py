#HW15-2,12/16/2022
#Finding the sum of a series.
#*******************************************
n=int(print("Please enter a number: "))
print(sum((i*i)/(2*i-1) for i in range (n)))