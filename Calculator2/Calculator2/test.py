import unittest
import Calculator2
class TestCalculator(unittest.TestCase):


    def test_Add(self):
        self.assertEqual(Calculator2.add(1,1),2)
        with self.assertRaises(TypeError):
          Calculator2.add('1',1)
    def test_Div(self):
        #Calculator2.div(10,0)
        self.assertEqual(Calculator2.div(10,5),2)
        with self.assertRaises(ZeroDivisionError):
          Calculator2.div(10,0)

    def test_Sub(self):
        self.assertEqual(Calculator2.sub(4,2),2)
    def test_Mul(self):
        self.assertEqual(Calculator2.mul(2,2),4)
    def test_Operator(self):
        self.assertEqual(Calculator2.operator('+',13,11),24)
        self.assertEqual(Calculator2.operator('-',15,-10),25)
        self.assertEqual(Calculator2.operator('/',16,2),8)
        self.assertEqual(Calculator2.operator('*',7,-3),-21)
    
    
    
if __name__=="__main__":
    unittest.main()