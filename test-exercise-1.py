import unittest
from exercise_1 import replace_last


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

    def test_replace_last(self):
        self.assertEqual(replace_last([2, 3, 4, 1]),  [1, 2, 3, 4])
        self.assertEqual(replace_last([1, 2, 3, 4]),  [4, 1, 2, 3])
        self.assertEqual(replace_last([1]),  [1])
        self.assertEqual(replace_last([]), [])


if __name__ == '__main__':
    unittest.main()
