class complex1:
    def __init__(self,r,i):
        self.real=r
        self.imaginary=i
    def __add__(self,c):
        return complex1(self.real+c.real,self.imaginary+c.imaginary)
    
    def __str__(self):
        return f"{self.real}+{self.imaginary}i"
    
    
    
c1=complex1(1,2)
c2=complex1(4,5)
print(c1+c2)