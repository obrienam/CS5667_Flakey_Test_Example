import unittest
import driver as driverClass
class Testing(unittest.TestCase):
    def test_flake(self):
        c=4
        test=driverClass.driver()
        o=test.getOutput()
        self.assertEqual(c,o)
    def test_notflake(self):
        c=4
        test=driverClass.driver()
        for i in range(5):
            o=test.getOutput()
            if(o==4):
                break
        self.assertEqual(c,o)
        
if __name__ == '__main__':
    unittest.main()