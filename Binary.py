def ConvertToBinary(n):
    e=''
    while n!= 0 :
        r=n%2
        e = str(r) +e
        n = n//2
    return e

print (ConvertToBinary (147))