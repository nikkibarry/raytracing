from raytracing.mathematics.ray import Ray
from raytracing.mathematics.vector3 import LEFT, ORIGIN, UP
from raytracing.shapes.hit import Hit


class TestHit:

    def test_normal(self):
        hit = Hit(ORIGIN, UP * 2, 2.0)
        assert hit.normal == UP

    def test_normal_ray(self):
        hit = Hit(ORIGIN, UP * 2.0, 2.0)
        expected_ray = Ray(ORIGIN, UP)
        assert hit.normal_ray() == expected_ray

    def test_eq_same_object_returns_true(self):
        hit = Hit(ORIGIN, UP, 2.0)
        assert hit == hit

    def test_eq_different_type_returns_false(self):
        assert Hit(ORIGIN, UP, 2.0) != UP

    def test_eq_identical_object_returns_true(self):
        hit_1 = Hit(ORIGIN, UP, 2.0)
        hit_2 = Hit(ORIGIN, UP, 2.0)
        assert hit_1 == hit_2

    def test_eq_different_origin_returns_false(self):
        hit_1 = Hit(ORIGIN, UP, 2.0)
        hit_2 = Hit(UP, UP, 2.0)
        assert hit_1 != hit_2

    def test_eq_different_normal_returns_false(self):
        hit_1 = Hit(ORIGIN, UP, 2.0)
        hit_2 = Hit(ORIGIN, LEFT, 2.0)
        assert hit_1 != hit_2

    def test_eq_different_distance_returns_false(self):
        hit_1 = Hit(ORIGIN, UP, 2.0)
        hit_2 = Hit(ORIGIN, UP, 1.0)
        assert hit_1 != hit_2

    def test_eq_different_normal_magnitudes_returns_true(self):
        hit_1 = Hit(ORIGIN, UP, 2.0)
        hit_2 = Hit(ORIGIN, UP * 2, 2.0)
        assert hit_1 == hit_2
