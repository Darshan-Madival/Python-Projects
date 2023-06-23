class calculator:
    def __init__(self,number):
        self.number=number
    @staticmethod
    def hello():
        print("Hello Sir")
    def square(self):
        print(f"square of {self.number} is {self.number*self.number}")
    def squareroot(self):
        print(f"squareroot of {self.number} is {self.number**0.5}")
    def cube(self):
        print(f"square of {self.number} is {self.number**self.number}")
        
a=calculator(3)
a.hello()
a.square()
a.squareroot()
a.cube()
