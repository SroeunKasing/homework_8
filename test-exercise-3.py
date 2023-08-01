import unittest
from exercise_3 import remove_all_after


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

    def test_remove_all_after(self):
        self.assertEqual(remove_all_after([1, 2, 3, 4, 5], 3),  [1, 2, 3])
        self.assertEqual(remove_all_after([1, 1, 2, 2, 3, 3], 2),  [1, 1, 2])
        self.assertEqual(remove_all_after([1, 1, 2, 2, 3, 3], 5),  [1, 1, 2, 2, 3, 3])
        self.assertEqual(remove_all_after([1], 1),  [1])
        self.assertEqual(remove_all_after([], 1),  [])


if __name__ == '__main__':
    unittest.main()
