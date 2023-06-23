class programmer:
     company="okgoogle"
     def __init__(self,name,product,salary):
            self.name=name
            self.product=product
     def getInfo(self):
            print(f"The Programmer working in {self.company} company is {self.name} and his product name is {self.product} is {self.salary} ")  
harry=programmer("harry","pandu")
carry=programmer("carry","paper")
harry.getInfo()
carry.getInfo()