"""3D Ray module."""

from dataclasses import dataclass
from typing import override

from raytracing.mathematics.vector3 import Vector3


@dataclass(eq=False, frozen=True, slots=True)
class Ray:
    """3D ray representation.

    Attributes:
        origin: origin point of the ray
        _direction: direction of the ray
    """

    origin: Vector3
    _direction: Vector3

    @property
    def direction(self):
        """Return normalized direction of the ray.

        Returns:
            Normalized direction of the ray.
        """
        return self._direction.norm()

    @override
    def __eq__(self, obj: object):
        """Check if rays are equal based on origin and normalized direction.

        Args:
            ray: Ray to compare.

        Returns:
            True if rays are equal. False otherwise.
        """
        if not isinstance(obj, self.__class__):
            return False
        return (self.origin == obj.origin) and (
            self.direction == obj.direction
        )

    @override
    def __hash__(self) -> int:
        """Return hash value of this ray.

        Returns:
            the hash value of the ray.
        """
        return hash((self.origin, self.direction))
