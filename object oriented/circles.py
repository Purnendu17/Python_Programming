class Circle:
    pi = 3.14  # Class attribute for the value of pi

    @staticmethod
    def area(radius):
        return Circle.pi * (radius ** 2)


# Test:
radius = 5
print("The area of a circle with radius", radius , "is:" ,Circle.area(radius))
