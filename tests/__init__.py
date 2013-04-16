'''\
Tests for TinkerPy.
'''

import unittest, doctest
import tinkerpy


class TinkerPyTests(unittest.TestCase):
    def test_tinkerpy(self):
        doctest.testmod(tinkerpy)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TinkerPyTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

