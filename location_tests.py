import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")

        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("Paris", 48.9, 2.4)
        self.assertNotEqual(repr(loc1), loc2)

    def test_eq(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(loc.name, "SLO")
        self.assertEqual(loc.lat, 35.3)
        self.assertEqual(loc.lon, -120.7)

if __name__ == "__main__":
        unittest.main()
