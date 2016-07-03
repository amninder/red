import unittest
import red as sut


@unittest.skip("Don't forget to test!")
class RedTests(unittest.TestCase):

    def test_example_fail(self):
        result = sut.red_example()
        self.assertEqual("Happy Hacking", result)
