# test_with_unittest.py

# this is directly within the class_6 folder...py

from unittest import TestCase

class TryTesting(TestCase):
    def test_always_passes(self):
        self.assertTrue(True)

    def test_always_fails(self):
        self.assertTrue(False)