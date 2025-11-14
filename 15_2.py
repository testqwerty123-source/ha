class Shape:
    def perimeter(self):
        raise NotImplementedError

    def display_info(self):
        try:
            p = self.perimeter()
            print(f"Фігура: {self.__class__.__name__}")
            print(f"Периметр: {p}")
        except NotImplementedError:
            print(f"Фігура: {self.__class__.__name__}")

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def perimeter(self):
        return 4 * self.side

class Triangle(Shape):
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def perimeter(self):
        return self.side_a + self.side_b + self.side_c


square1 = Square(5)
triangle1 = Triangle(3, 4, 5)

print("--- Квадрат ---")
square1.display_info()

print("--- Трикутник ---")
triangle1.display_info()

print("--- Базовий клас ---")
Shape().display_info()
