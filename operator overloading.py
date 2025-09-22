
# Operator Overloading :-

class vacter:
    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k
    
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    
    def __add__(self,x):
        return vacter (self.i + x.i,self.j + x.j,self.k + x.k)
    
v1 = vacter(2,3,4)
print(v1)

v2 = vacter(6,7,8)
print(v2)

print(v1 + v2)

