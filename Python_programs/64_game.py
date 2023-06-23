import random
  
  
def gamewin(comp,you):
    if(comp==you):
        return None
    elif(comp=="s"):
        if(you=="p"):
            return True
        else:(you=="k")
        return False
    elif(comp=="p"):
        if(you=="k"):
            return True
        else:(you=="s")
        return False
    elif(comp=="k"):
        if(you=="s"):
            return True
        else:(you=="p")
        return False
    
    
    


print("comp:stone(s),papper(p),scissors(k)?")

comp=random.randint(1,3)
if(comp==1):
    comp="s"
elif(comp==2):
    comp="p"
elif(comp==3):
    comp="k"

you=input("you:stone(s),papper(p),scissors(k)?")

a=gamewin(comp,you)

print("you choose",{you})
print("comp choose",{comp})

if(a==None):
    print("game tie")
elif a:
    print("you win")
else:
    print("you loose")