num=15#int(input("Enter yout number:"))
fib=0
if num ==1 or num==2:
    fib=1
else:
    for i in num:
        fib=fib(num-1)
