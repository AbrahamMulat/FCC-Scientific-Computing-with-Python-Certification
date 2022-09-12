class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return __class__.__name__ + "(width=" + str(self.width) + ", height=" + str(self.height) + ")"

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        star = '*' * self.width + '\n'
        star = star * self.height
        return star

    def get_amount_inside(self, shape):
        w = self.width // shape.width
        h = self.height // shape.height

        return w * h


# rectangle = Rectangle(4, 4)
# print(rectangle.get_picture())


class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        self.width = side
        self.height = side

    def __str__(self):
        return __class__.__name__ + "(side=" + str(self.width) + ")"

    def set_side(self, side):
        self.width = side
        self.height = side


