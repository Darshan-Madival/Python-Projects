a=int(input("enter First Subject Marks:"))
b=int(input("enter Second Subject Marks:"))
c=int(input("enter Third Subject Marks:"))

avg=(a+b+c)/3

if(a<33 or b<33 or c<33):
    print("fail")
elif(avg>40):
     print("pass")
else:
     print("you have fail due to overall percentage")