#single inheritance
class employee:
    a=50
    
class programmer(employee):
    b=60
    
pr=programmer()
print(pr.a)
print(pr.b)
em=employee()
print(em.a)
print(em.b)#This throws an error