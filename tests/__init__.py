'''\
Tests for TinkerPy.
'''

def test_suite():
    import unittest, doctest
    import tinkerpy
    suite = unittest.TestSuite()
    suite.addTests(doctest.DocTestSuite(tinkerpy))
    return suite
