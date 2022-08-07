import random

import item as item

a=["rock","scicesor","paper"]
rand=random.choice(a)
print("***The computer has selected The option***")
print(a)
l=['/','@','#','$']

while(True):
 try:
  userinput = input(("It's your Turn to select the option: "))
  if any(char.isdigit() for char in userinput):
    print("Please do not include digits in your item.")
    continue
  print(f"the computer choose"" "+rand)  
  for i in l:
       if (userinput == i):
        print("invalid")
        break

  else:
   def function1(userinput):
    if (rand==userinput and userinput==rand):
        return 1
   def function2(userinput):
    if(userinput=="rock" and rand=="paper"):
        return True
    elif(userinput=="paper" and rand=="rock"):
        return False
    elif (userinput == "scicesor" and rand == "rock"):
        return False
    elif (userinput == "rock" and rand == "scicesor"):
        return True
    elif (userinput == "paper" and rand == "scicesor"):
        return False
    elif (userinput == "paper" and rand == "scicesor"):
        return False




   function1(userinput)
   function2(userinput)
   if(function1(userinput)==1):
      print("tie")
   elif(function2(userinput)==True):
      print("******YOU WON******")
   elif (function2(userinput) == False):
     print("******YOU LOOSE.BETTER LUCK NEXT TIME******")
   exit()

 except Exception as e:
     print(e)

