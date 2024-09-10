from math import sqrt

from raytracing.mathematics.vector3 import (
    BACK,
    DOWN,
    FORWARD,
    LEFT,
    RIGHT,
    UP,
    Vector3,
)


class TestVector3:
    def test_magnitude(self):
        test_vector = Vector3(1.0, 2.0, 3.0)
        assert test_vector.magnitude() == sqrt(14)

    def test_norm(self):
        test_vector = Vector3(1.0, 2.0, 3.0)
        expected_result = Vector3(
            1.0 / sqrt(14), 2.0 / sqrt(14), 3.0 / sqrt(14)
        )

        assert test_vector.norm() == expected_result

    def test_dot(self):
        vector_1 = Vector3(1.0, 2.0, 3.0)
        vector_2 = Vector3(4.0, 5.0, 6.0)

        expected_dot_product = 4 + 10 + 18
        assert vector_1.dot(vector_2) == expected_dot_product

    def test_cross_cardinal_directions(self):
        assert DOWN == RIGHT.cross(BACK)
        assert UP == RIGHT.cross(FORWARD)
        assert UP == LEFT.cross(BACK)
        assert DOWN == LEFT.cross(FORWARD)

        assert DOWN == FORWARD.cross(RIGHT)
        assert UP == BACK.cross(RIGHT)
        assert UP == FORWARD.cross(LEFT)
        assert DOWN == BACK.cross(LEFT)

        assert RIGHT == UP.cross(BACK)
        assert LEFT == UP.cross(FORWARD)
        assert LEFT == DOWN.cross(BACK)
        assert RIGHT == DOWN.cross(FORWARD)

        assert RIGHT == BACK.cross(DOWN)
        assert LEFT == FORWARD.cross(DOWN)
        assert LEFT == BACK.cross(UP)
        assert RIGHT == FORWARD.cross(UP)

        assert FORWARD == UP.cross(RIGHT)
        assert BACK == UP.cross(LEFT)
        assert BACK == DOWN.cross(RIGHT)
        assert FORWARD == DOWN.cross(LEFT)

        assert BACK == RIGHT.cross(UP)
        assert FORWARD == LEFT.cross(UP)
        assert FORWARD == RIGHT.cross(DOWN)
        assert BACK == LEFT.cross(DOWN)

    def test_cross_product(self):
        vector_1 = Vector3(1.0, 2.0, 3.0)
        vector_2 = Vector3(4.0, 5.0, 6.0)
        cross_1 = vector_1.cross(vector_2)
        cross_2 = vector_2.cross(vector_1)
        expected_cross_1 = Vector3(-3.0, 6.0, -3.0)
        expected_cross_2 = Vector3(3.0, -6.0, 3.0)
        assert cross_1 == expected_cross_1
        assert cross_2 == expected_cross_2

    def test_neg(self):
        vector = Vector3(1.0, 2.0, 3.0)
        expected_result = Vector3(-1.0, -2.0, -3.0)
        assert -vector == expected_result

    def test_abs(self):
        vector = Vector3(1.0, -2.0, -3.0)
        expected_result = Vector3(1.0, 2.0, 3.0)
        assert abs(vector) == expected_result

    def test_add(self):
        vector_1 = Vector3(1.0, 2.0, 3.0)
        vector_2 = Vector3(4.0, 5.0, 6.0)
        expected_result = Vector3(5.0, 7.0, 9.0)
        assert vector_1 + vector_2 == expected_result
        assert vector_2 + vector_1 == expected_result

    def test_sub(self):
        vector_1 = Vector3(1.0, 2.0, 3.0)
        vector_2 = Vector3(4.0, 5.0, 6.0)
        expected_result_1 = Vector3(-3.0, -3.0, -3.0)
        expected_result_2 = -expected_result_1
        assert vector_1 - vector_2 == expected_result_1
        assert vector_2 - vector_1 == expected_result_2

    def test_mul(self):
        vector = Vector3(1.0, 2.0, 3.0)
        scalar = 1.5
        expected_result = Vector3(1.5, 3.0, 4.5)
        assert vector * scalar == expected_result

    def test_div(self):
        vector = Vector3(3.0, 6.0, 9.0)
        scalar = 3.0
        expected_result = Vector3(1.0, 2.0, 3.0)
        assert vector / scalar == expected_result
