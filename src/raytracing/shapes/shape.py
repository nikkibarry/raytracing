"""Shape module."""

from abc import ABC, abstractmethod

from raytracing.mathematics.ray import Ray
from raytracing.mathematics.vector3 import Vector3
from raytracing.shapes.hit import Hit


class Shape(ABC):
    """Shape abstract class."""

    @abstractmethod
    def hit(self, ray: Ray) -> Hit | None:
        """Determine ray-object intersection.

        Args:
            ray: ray to check intersection.

        Returns:
            None if no intersection.
            Hit with intersection details otherwise.
        """

    @abstractmethod
    def uv(self, point: Vector3) -> tuple[float, float]:
        """Return uv mapping at a given point on a shape.

        Args:
            point: point on the given shape.

        Returns:
            The uv mapping (as a tuple) at the point.
        """
