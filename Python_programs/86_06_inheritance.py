class animal:
    pass

class pets(animal):
    pass

class dog(pets):
    
    @staticmethod 
    def bark():
         print("bow bow bow pandu poude ")
         

v1=dog()
v1.bark()