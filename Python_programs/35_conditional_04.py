# a=input("enter your Text:\n")
# if("make a lot of money" in a):
#     print("this is span")
# elif("buy now"in a):
#     print("this is span")
# elif("subscribe" in a):
#     print("this is spam")
# else:
#     print("not spam")

# another method

a=input("enter your Text:\n")
if("make a lot of money" in a):
    spam=True
elif("buy now"in a):
    spam=True
elif("subscribe" in a):
    spam=True
elif("click here"in a):
    spam=True
else:
    spam=False
 
if(spam):
    print("This is a spam")
else:
    print("this is not spam")
        

