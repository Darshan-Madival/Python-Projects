a=int(input("enter the number:"))
limit=int(input("enter the ending number:"))

for i in range(limit,0,-1):
    print(str(a)+"X"+str(i)+"="+str(a*i))
    