def natural(n):
    if(n==0 or n==1):
       return 1
    a=n+natural(n-1)
    return a

print(natural(15))