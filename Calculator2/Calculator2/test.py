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
        self.assertEqual(Calculator2.operator('a',7,7),None)
    def test_output(self):
        self.assertEqual(Calculator2.output(5,'*',5,25),'5 * 5 = 25')
    def test_op(self):
        self.assertEqual(Calculator2.inputop(self.mock_inputop),'+')
    def test_input1(self):
        self.assertEqual(Calculator2.input1(self.mock_input),1)
    def test_input2(self):
        self.assertEqual(Calculator2.input2(self.mock_input),1)
    def test_success(self):
        num1 = Calculator2.input1(self.mock_input)
        oper = Calculator2.inputop(self.mock_inputop)
        num2 = Calculator2.input2(self.mock_input)
        ans = Calculator2.operator(oper,num1,num2)
        final = Calculator2.output(num1,oper,num2,ans)
        self.assertEqual(final,'1 + 1 = 2')
        pass
    def mock_input(self,prompt):
        return 1
    def mock_inputop(self,prompt):
        return('+')

        
    
    
    
if __name__=="__main__":
    unittest.main()