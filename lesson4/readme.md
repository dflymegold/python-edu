    Output:
    shape = Shape()
    square = Square(2, 5, 5)
    print(square.get_center()) # (2,5)
    square.move(10, 10) # (10,10)
    print(square.get_center()) # 25
    print(square.get_area()) # 78.53981633974483
    circle = Circle(10, 10, 5)
    print(circle.get_area())
    triangle = Triangle(10,3,5)
    print(shape.get_distance(square,triangle)) # 7.0
