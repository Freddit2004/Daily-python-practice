def TriangleArea(b,h):
    area=0.5*b*h
    return area
b=float(input( "Enter the base:"))
h=float(input("Enter the height:"))
print("The Area of the triangle is:",TriangleArea(b,h))