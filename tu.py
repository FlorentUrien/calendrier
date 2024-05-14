import unittest
import main


class MyTestCase(unittest.TestCase):
    def test_21(self):
        cubes = [[0, 1, 2, 4, 8, 9], [5, 3, 7, 6, 0, 1]]
        self.assertEqual(21, main.fin(cubes))

    def test_05(self):
        cubes = [[1, 2, 3, 4, 5, 7], [9, 0, 6, 8, 1, 5]]
        self.assertEqual(5, main.fin(cubes))


if __name__ == '__main__':
    unittest.main()
