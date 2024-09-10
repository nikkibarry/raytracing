from raytracing.mathematics.ray import Ray
from raytracing.mathematics.vector3 import DOWN, ORIGIN, RIGHT, UP


class TestRay:
    def test_direction(self):
        origin = ORIGIN
        direction = UP + RIGHT
        ray = Ray(origin, direction)
        expected_direction = direction.norm()
        assert ray.origin == origin
        assert ray.direction == expected_direction

    def test_eq_same_normalized_direction_returns_true(self):
        direction = UP + RIGHT
        ray_1 = Ray(ORIGIN, direction)
        ray_2 = Ray(ORIGIN, direction * 2)
        assert ray_1 == ray_2

    def test_eq_different_origin_returns_false(self):
        ray_1 = Ray(ORIGIN, UP)
        ray_2 = Ray(ORIGIN + UP, UP)
        assert ray_1 != ray_2

    def test_eq_different_direction_returns_false(self):
        assert Ray(ORIGIN, UP) != Ray(ORIGIN, DOWN)

    def test_eq_different_type_returns_false(self):
        assert Ray(ORIGIN, UP) != ORIGIN
