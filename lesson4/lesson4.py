import math
class Shape :
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @staticmethod
    def get_distance (figure1,figure2):
        rez = math.sqrt(math.pow(figure2.x-figure1.x,2)+math.pow(figure2.y-figure1.y,2))
        return rez

class Square (Shape):
    def __init__(self, x, y, a=1):
        self.a = a
        Shape.__init__(self, x, y)
    def get_center(self):
        center = (self.x, self.y)
        return center
    def move (self, x1, y1):
        self.x = x1
        self.y = y1
        return 0
    def get_area (self):
        area = self.a**2
        return area
    # def get_vertex (self):


class Triangle(Shape):
    def __init__(self, x, y, a=1):
            self.a = a
            Shape.__init__(self, x, y)

    def get_center(self):
            center = (self.x, self.y)
            return center

    def move(self, x1, y1):
            self.x = x1
            self.y = y1
            return 0

    def get_area(self):
            area = ((3 ** 0.5) / 4) * self.a
            return area

    # def get_vertex(self):


class Circle(Shape):
    def __init__(self, x, y, r=1):
            self.r = r
            Shape.__init__(self, x, y)

    def get_center(self):
            center = (self.x, self.y)
            return center

    def move(self, x1, y1):
            self.x = x1
            self.y = y1
            return 0

    def get_area(self):
            area = math.pi*self.r**2
            return area
    # def get_vertex(self):

def main ():
    shape = Shape()
    square = Square(2, 5, 5)
    print(square.get_center())
    square.move(10, 10)
    print(square.get_center())
    print(square.get_area())
    circle = Circle(10, 10, 5)
    print(circle.get_area())
    triangle = Triangle(10,3,5)
    print(shape.get_distance(square,triangle))

if __name__ == "__main__":
    main()
