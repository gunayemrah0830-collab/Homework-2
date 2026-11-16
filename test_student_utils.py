import unittest

from student_utils import (
    calculate_average,
    get_highest_score,
    get_lowest_score
)


class TestStudentUtils(unittest.TestCase):

    def test_calculate_average(self):
        self.assertEqual(
            calculate_average([90, 80, 70]),
            80.0
        )

    def test_get_highest_score(self):
        self.assertEqual(
            get_highest_score([90, 80, 70]),
            90
        )

    def test_get_lowest_score(self):
        self.assertEqual(
            get_lowest_score([90, 80, 70]),
            70
        )


if __name__== "__main__":
    unittest.main()
