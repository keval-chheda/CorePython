class Circle:
    def _init_(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius


circle = Circle(5)
area = circle.area()
perimeter = circle.perimeter()
print(area)
print(perimeter)