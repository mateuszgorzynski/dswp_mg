# Zadanie 1


class Point:
    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y

    # Zadanie 2
    def __str__(self):
        return f"Point({self.x}, {self.y})"

    # Zadanie 3
    def __mul__(self, other):
        if isinstance(other, int):
            return Point(self.x * other, self.y * other)
        else:
            raise TypeError("Pomnożenie nie jest możliwe")

    # Zadanie 4
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return False


p = Point(3, 4)
print(p)
# [Out] Point(3, 4)
# p2 = p * 2.14 - TypeError
p2 = p * 2
print(p2)
print(p2 == p)  # False

# Zadanie 5


class Polygon:
    def __init__(self):
        self.points = []

    def add_point(self, point):
        if isinstance(point, Point):
            self.points.append(point)
        else:
            raise TypeError("Tylko obiekty Point mogą być dodane do obiektu Polygon")

    # Zadanie 6
    def __str__(self):
        points_str = ", ".join(str(point) for point in self.points)
        return f"Polygon[{points_str}]"

    # Zadanie 7
    def __getitem__(self, item):
        if isinstance(item, int):
            return self.points[item]
        elif isinstance(item, slice):
            return Polygon(self.points[item])
        else:
            raise TypeError("Musi być typ int lub slice")


poly = Polygon()
poly.add_point(p)
poly.add_point(p2)
print(poly)
print(poly[0])
print(poly[1])
