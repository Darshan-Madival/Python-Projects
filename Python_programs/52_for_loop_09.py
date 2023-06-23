a=int(input("enter the number"))

for i in range(1,a+1):
    print(" "*(a-i-1),end="")
    print("*"*(2*i+1),end="")
    print(" "*(a-i-1))