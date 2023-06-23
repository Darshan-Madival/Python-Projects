class parent1:
    a=10
    def __init__(self):
        print("First")
    
class child1(parent1):
    b=20
    def __init__(self):
        super().__init__()
        print("second")
        
class child2(child1):
    c=30
    def __init__(self):
        super().__init__()
        print("Third")
    
ch=parent1()
print(ch.a)
        
        