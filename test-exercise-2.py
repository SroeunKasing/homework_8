import unittest
from exercise_2 import index_power


class CodingRoomsUnitTests(unittest.TestCase):

    def setUp(self):
        # Setup code here (if required, replace the 'pass')
        pass

    def tearDown(self):
        # Teardown code here (if required, replace the 'pass')
        pass

    def test_default_case(self):
        # Your test case logic here (replace the example assertion below)
        # You may also rename this to any function in the form of 'test_your_test_name(self):'
        self.assertTrue(True)

    def test_index_power(self):
        self.assertEqual(index_power([1, 2, 3, 4], 0),  1)
        self.assertEqual(index_power([1, 2, 3, 4], 1),  2)
        self.assertEqual(index_power([1, 2, 3, 4], 2),  9)
        self.assertEqual(index_power([1, 2, 3, 4], 3),  64)
        self.assertEqual(index_power([1, 2, 3, 4], 4),  -1)
        self.assertEqual(index_power([1, 2, 3, 4], -4),  1)
        self.assertEqual(index_power([1, 3, 10, 100], 3),  1000000)
        self.assertEqual(index_power([0, 1], 0),  1)
        self.assertEqual(index_power([1, 2], 3),  -1)
        self.assertEqual(index_power([], 3),  -1)
        self.assertEqual(index_power([], -1),  -1)


if __name__ == '__main__':
    unittest.main()
