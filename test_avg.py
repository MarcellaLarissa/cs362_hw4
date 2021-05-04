import unittest
import avgElement

class TestCase(unittest.TestCase):
   
    def test_avg(self):
        listNums = [4, 7, 3, 3, 9]
        length = len(listNums)
        # test if return is not None
        self.assertIsNotNone(avgElement.findAvg(listNums, length))

    def test_avg_1(self):
        #test if list passed to function is not None
        listNums = []
        self.assertIsNotNone(avgElement.listNums)  
        
    def test_avg_2(self):
        # test if function returns a float
        listNums = [4, 7, 3, 3, 9]
        length = len(listNums)
        self.assertTrue(type(avgElement.findAvg(listNums, length)), float)
        
    
if __name__ == '__main__':
    unittest.main()