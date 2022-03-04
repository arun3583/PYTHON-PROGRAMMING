class Rectangle:
    def __init__(self,length,breadth) :
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length*self.breadth)
    
a=int(input("Enter length of rectangle: "))
b=int(input("Enter breadth of rectangle: "))
rect = Rectangle(a,b)
print(rect.area())
print(rect.perimeter())
