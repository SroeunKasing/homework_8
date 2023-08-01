import unittest
from exercise_5 import reverse_ascending


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

    def test_reverse_ascending(self):
        self.assertEqual(reverse_ascending([1, 2, 3, 4, 5]),  [5, 4, 3, 2, 1])
        self.assertEqual(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3]),  [10, 7, 5, 4, 8, 7, 2, 3, 1])
        self.assertEqual(reverse_ascending([5, 4, 3, 2, 1]),  [5, 4, 3, 2, 1])
        self.assertEqual(reverse_ascending([1, 2, 1, 2, 1, 2, 1, 2]),  [2, 1, 2, 1, 2, 1, 2, 1])
        self.assertEqual(reverse_ascending([1,1,1,1,1,1,1,1,2]),  [1,1,1,1,1,1,1,2,1])
        self.assertEqual(reverse_ascending([1,1,1,1,1,1,1,1,2,2,2,2,2,2]),  [1,1,1,1,1,1,1,2,1,2,2,2,2,2])
        self.assertEqual(reverse_ascending([1,2]),  [2,1])
        self.assertEqual(reverse_ascending([1]),  [1])
        self.assertEqual(reverse_ascending([]),  [])


if __name__ == '__main__':
    unittest.main()
