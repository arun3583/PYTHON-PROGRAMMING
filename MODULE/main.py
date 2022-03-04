from graphics import circle
from graphics import rectangle
from graphics.subg import cuboid
from graphics.subg import sphere
r = int(input("Enter radius of circle: "))
l = int(input("Enter length of rectangle: "))
b = int(input("Enter breadth of rectangle: "))
lc = int(input("Enter length of cuboid: "))
wc = int(input("Enter width of cuboid: "))
hc = int(input("Enter height of cuboid: "))
rs = int(input("Enter radius of sphere: "))
print("Area of circle is ",circle.area(r))
print("perimeter of circle is ",circle.perimeter(r))
print("Area of rectangle is ",rectangle.area(l,b))
print("perimeter of rectangle is ",rectangle.perimeter(l,b))
print("Area of cuboid is ",cuboid.area(lc,wc,hc))
print("perimeter of cuboid is ",cuboid.perimeter(lc,wc,hc))
print("Area of sphere is ",sphere.area(rs))
print("perimeter of sphere is ",sphere.perimeter(rs))
