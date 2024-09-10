"""3D Vector module."""

from dataclasses import dataclass
from math import sqrt


@dataclass(frozen=True, slots=True)
class Vector3:
    """Representation of a 3D Vector.

    Attributes:
        x: x distance
        y: y distance
        z: z distance
    """

    x: float
    y: float
    z: float

    def norm(self) -> "Vector3":
        """Return this Vector3, normalized.

        Returns:
            A normalized Vector3
        """
        magnitude = self.magnitude()
        return Vector3(*(dim / magnitude for dim in (self.x, self.y, self.z)))

    def magnitude(self) -> float:
        """Return the magnitude of this Vector3.

        Returns:
            The magnitude of this Vector3.
        """
        return sqrt(self.x**2 + self.y**2 + self.z**2)

    def dot(self, vector: "Vector3") -> float:
        """Return the dot product of this and another Vector3 object.

        Args:
            vector: other Vector3 object

        Returns:
           dot product of this and `vector`
        """
        return (self.x * vector.x) + (self.y * vector.y) + (self.z * vector.z)

    def cross(self, vector: "Vector3") -> "Vector3":
        """Return the cross product of this and another Vector3 object.

        Args:
            vector: other Vector3 object

        Returns:
            cross product of this and `vector`
        """
        x = (self.y * vector.z) - (self.z * vector.y)
        y = (self.z * vector.x) - (self.x * vector.z)
        z = (self.x * vector.y) - (self.y * vector.x)
        return Vector3(x, y, z)

    def __neg__(self) -> "Vector3":
        """Return the negative value of the Vector3 object.

        Returns:
            the negative vector
        """
        return Vector3(-self.x, -self.y, -self.z)

    def __add__(self, vector: "Vector3") -> "Vector3":
        """Return the sum of two vectors.

        Args:
            vector: Vector to add.

        Returns:
            the sum of this and another vector.
        """
        return Vector3(self.x + vector.x, self.y + vector.y, self.z + vector.z)

    def __sub__(self, vector: "Vector3") -> "Vector3":
        """Return the difference of two vectors.

        Args:
            vector: The vector to subtract

        Returns:
            the difference of this and another vector
        """
        return Vector3(self.x - vector.x, self.y - vector.y, self.z - vector.z)

    def __abs__(self) -> "Vector3":
        """Return the absolute value of the vector.

        Returns:
            the absolute value of the vector
        """
        return Vector3(abs(self.x), abs(self.y), abs(self.z))

    def __mul__(self, scalar: int | float) -> "Vector3":
        """Return the vector multiplied by a scalar.

        Args:
            scalar: scalar to multiply the vector by

        Returns:
            the vector multiplied by the scalar
        """
        return Vector3(self.x * scalar, self.y * scalar, self.z * scalar)

    def __truediv__(self, scalar: int | float) -> "Vector3":
        """Return the vector divided by a scalar.

        Args:
            scalar: value to divide by

        Returns:
            the vector divided by the scalar
        """
        return Vector3(self.x / scalar, self.y / scalar, self.z / scalar)


ORIGIN = Vector3(0, 0, 0)
RIGHT = Vector3(1, 0, 0)
LEFT = Vector3(-1, 0, 0)
UP = Vector3(0, 1, 0)
DOWN = Vector3(0, -1, 0)
BACK = Vector3(0, 0, 1)
FORWARD = Vector3(0, 0, -1)
