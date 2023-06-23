def great(n1,n2,n3):
    if(n1>n2 and n1>n3):
        print("n1 is greater")
    elif(n2>n3 and n2>n1):
        print("n2 is greater")
    elif(n3>n1 and n3>n2) :
        print("n3 is greater")
       
a=int(input("enter the  number n1\n"))
b=int(input("enter the  number n2\n"))
c=int(input("enter the  number n3\n"))


great(a,b,c)

           
    