x=int(input("Enter x coordinate: "))
y=int(input("Enter y coordinate: "))
if x>0 and y>0:
    print("Point lies in the first quadrant")
elif x<0 and y>0:
    print("Point lies in the second quadrant")
elif x<0 and y<0:
    print("Point lies in the third quadrant")
elif x>0 and y<0:
    print("Point lies in the fourth quadrant")
else:
    print("Point is at the origin")