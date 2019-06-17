import unittest
from lab1 import *

class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        self.assertEqual(reverse_rec([10, 20, 30, 40]), [40, 30, 20, 10])
        tlist = None
        with self.assertRaises(ValueError): # checks for exception
            reverse_rec(tlist)

    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )
        self.assertEqual(bin_search(6, 0, len(list_val)-1, list_val), None )
        tlist = None
        with self.assertRaises(ValueError):  # checks for exception
            bin_search(4, 0, 100, tlist)

if __name__ == "__main__":
        unittest.main()

    
