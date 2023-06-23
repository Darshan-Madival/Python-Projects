class calculator:
    def __init__(self,number):
        self.number=number
    def square(self):
        print(f"The square of {self.number} is {self.number*self.number}")
    def squareroot(self):
        print(f"The squareroot of {self.number} is {self.number**0.5}")
    def cube(self):
        print(f"The cube of {self.number} is {self.number**self.number}")
        
a=calculator(3)
a.square()
a.squareroot()
a.cube()
        