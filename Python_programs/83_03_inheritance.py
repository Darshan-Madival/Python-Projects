class parent1:
    a=90

class child1(parent1):
    b=91

class child2(child1):
    c=67
    
ch=child2()
r=parent1()
print(ch.a)
print(ch.b)
print(ch.c)
print(r.a)