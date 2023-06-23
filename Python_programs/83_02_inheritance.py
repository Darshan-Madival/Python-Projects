#multiple inheritance
class parent1:
    a=45

class parent2:
    b=78

class child(parent1,parent2):
    c=56
    
ch=child()
prt=parent1()
print(ch.a)
print(ch.b)
print(ch.c)
print(prt.c)
print(ch.a)#throws an error