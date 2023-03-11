# Basic Python Program

# Surface volume and area of Cylinder

r = float(input("Enter radius of Cylinder: "))
h = float(input("Enter height of Cylinder: "))

# pi = 3.14
Area = (2 * 3.14 * r * h) + (2 * 3.14 * (r * r))    # Formula of area of Cylinder

sv = 2 * 3.14 * r * (h + r)     # Formula of Surface volume of Cylinder

print("Area of Cylinder is: ", Area)
print("Surface volume of Cylinder is: ", sv)

