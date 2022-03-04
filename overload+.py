class Rectangle:
    def __init__(self, length, breadth):
        self.__length = length
        self.__breadth = breadth
    def __lt__(self, other):
        if self.__length*self.__breadth < other.__length*other.__breadth:
            print("Area of rectangle 1 is less than area of rectangle 2")
r1 = Rectangle(5,4)
r2 = Rectangle(5,5)
r1 < r2