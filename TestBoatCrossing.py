import unittest
from main import boat_crossing


class TestBoatCrossing(unittest.TestCase):

    def test_case_1(self):
        B, D, C = 2, 2, 2
        result = boat_crossing(B, D, C)
        expected_output = [(1, 1), (1, 0), (2, 0), (1, 0), (1, 1)]
        self.assertEqual(result, expected_output)

    def test_case_2(self):
        B, D, C = 3, 3, 2
        result = boat_crossing(B, D, C)
        expected_output = [(1, 1), (1, 0), (0, 2), (0, 1), (2, 0), (1, 1), (2, 0), (0, 1),(0,2),(1,0), (1, 1)]
        self.assertEqual(result, expected_output)

    def test_case_3(self):
        B, D, C = 3, 2, 3
        result = boat_crossing(B, D, C)
        expected_output = [(2, 1), (1, 0), (2, 1)]
        self.assertEqual(result, expected_output)

    def test_case_4(self):
        B, D, C = 4, 4, 2
        result = boat_crossing(B, D, C)
        expected_output = []  # No valid moves possible because capacity is 0
        self.assertEqual(result, expected_output)

    def test_case_5(self):
        B, D, C = 25, 25, 4
        result = boat_crossing(B, D, C)
        expected_output = [(1,1),(1,0),(0,4),(0,1),(4,0),(1,1),(2,2),(1,1),(2,2),(1,1),(2,2),(1,1),(2,2),(1,1),(2,2),(1,1),(2,2),(1,1),(2,2),(1,1),(2,2),(1,1),(2,2),(1,1),(2,2),(1,1),(2,2),(1,1),(2,2),(1,1),(2,2),(1,1),(2,2),(1,1),(2,2),(1,1),(2,2),(1,1),(2,2),(1,1),(2,2),(1,1),(2,2),(1,1),(2,2),(1,1),(2,2),]
        self.assertEqual(result, expected_output)

    def test_case_6(self):
        B, D, C = 50, 10, 4
        result = boat_crossing(B, D, C)
        expected_output = [(2,1),(1,0),(2,2),(0,1),(2,2),(1,0),(2,2),(0,1),(2,2),(1,0),(2,2),(0,1),(2,2),(1,0),(4,0),(1,0),(4,0),(1,0),(4,0),(1,0),(4,0),(1,0),(4,0),(1,0),(4,0),(1,0),(4,0),(1,0),(4,0),(1,0),(4,0),(1,0),(4,0),(1,0),(4,0),(1,0),(4,0),(1,0),(4,0)]
        self.assertEqual(result, expected_output)

    def test_case_7(self):
        B, D, C = 10, 10, 4
        result = boat_crossing(B, D, C)
        expected_output = [(1, 1), (1, 0), (0, 4),(0, 1),(4,0),(1,1),(2,2),(1,1),(2,2),(1,1),(2,2),(1,1),(2,2),(1,1),(2,2),(1,1),(2,2)]
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()
