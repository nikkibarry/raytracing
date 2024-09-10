"""Ray-object intersection module."""

from dataclasses import dataclass
from typing import override

from raytracing.mathematics.ray import Ray
from raytracing.mathematics.vector3 import Vector3


@dataclass(frozen=True, slots=True, eq=False)
class Hit:
    """Class for ray-object intersection.

    Attributes:
        point: location of the hit
        _normal: normal of the hit
        distance: distance to the hit
    """

    point: Vector3
    _normal: Vector3
    distance: float

    @property
    def normal(self):
        """The normal property."""
        return self._normal.norm()

    @override
    def __eq__(self, obj: object):
        """Check if intersections are equal.

        Args:
            obj: object to compare.

        Returns:
            True if hits are equal. False otherwise.
        """
        if not isinstance(obj, self.__class__):
            return False
        return (
            (self.point == obj.point)
            and (self.normal == obj.normal)
            and (self.distance == obj.distance)
        )

    @override
    def __hash__(self) -> int:
        """Return hash value of this hit.

        Returns:
            the hash value of the hit.
        """
        return hash((self.point, self.normal, self.distance))

    def normal_ray(self) -> Ray:
        """Return the point and normal as a ray.

        Returns:
            the point and normal as a ray.
        """
        return Ray(self.point, self.normal)
