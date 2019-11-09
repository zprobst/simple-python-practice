import unittest


def add_list(num_list):
    """
    This function takes a list of numbers and adds them starting
    with a sum of zero.

    :param num_list: The list of numbers.
    :return: A number, the sum of the num_list
    """
    # TODO: Implement this method
    pass


class MathTestCases(unittest.TestCase):
    def test_zero_numbers(self):
        lst = []
        self.assertEqual(0, add_list(lst))

    def test_one_number(self):
        lst = [163]
        self.assertEqual(163, add_list(lst))

    def test_many_numbers(self):
        lst = [1, 3, 4, 12, -1, 0]
        self.assertEqual(19, add_list(lst))


if __name__ == '__main__':
    unittest.main()
