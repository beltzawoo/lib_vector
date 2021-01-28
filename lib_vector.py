from math import sqrt

class GeometryObject():
    """A generic geometric object with x and y coordinates."""
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x}, {self.y})"

class Point(GeometryObject):
    """A point in a geometric space."""
    pass

class Vector(GeometryObject):
    """A vector in a geomtric space."""
    def norm(self) -> float:
        """Returns the vector's norm (length)."""
        return sqrt(self.x*self.x+ self.y*self.y)

def make_vector_from_points(a: Point, b: Point) -> Vector:
    """Creates a Vector() object from two points."""
    return Vector(b.x-a.x, b.y-a.y)

def det(a: Vector, b: Vector) -> float:
    """Calculates the determinator of two vectors."""
    return a.x*b.y - b.x*a.y

def are_vectors_colinear(a: Vector, b: Vector) -> bool:
    """Checks if two given vectors are colinear."""
    if det(a, b) == 0:
        return True
    else:
        return False

def apply_vector(point: Point, vector: Vector) -> Point:
    """Applies the translation of given vector to a Point() object."""
    return Point(point.x+vector.x, point.y+vector.y)

def add_vectors(a: Vector, b: Vector) -> Vector:
    """Returns a vector from the addition of two other vectors."""
    return Vector(a.x+b.x, a.y+b.y)
