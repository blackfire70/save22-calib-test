import unittest
import Calculator2
class TestCalculator(unittest):


    def test_Add(self):
        self.assertEqual(Calculator2.add(','),2)

    if __name__=="__main_":
        unittest.main()