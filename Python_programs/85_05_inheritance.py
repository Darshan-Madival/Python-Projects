class Vector2d:
    def __init__(self, i , j)-> None:
        self.i=i
        self.j=j 
        
    def darshan(self):
       return f"The vectors are {self.i}i+{self.j}j"
   
class Vector3d(Vector2d):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k
        
    def darshan(self):
        return f"The vectors are {self.i}i+{self.j}j+{self.k}k"
        


v2 = Vector2d(1, 5)
v3 = Vector3d(12, 5, 9)

print(v2.darshan())
print(v3.darshan())