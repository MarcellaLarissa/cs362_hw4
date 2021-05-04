import unittest
import cube

class TestCase(unittest.TestCase):
    #test add function
    def test_cube(self):
        #testing for input 0
        self.assertEqual(cube.findVol(3), 0)

    def test_cube_1(self):
        #testing for input neg number
        self.assertGreater(cube.findVol(-3), 0)  
        
    def test_cube_2(self):
        #testing for return integer
        self.assertTrue(type(cube.findVol(3)), int)
        

    
if __name__ == '__main__':
    unittest.main()