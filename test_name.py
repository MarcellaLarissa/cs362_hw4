import unittest
import name

class TestCase(unittest.TestCase):

    #test input is not none
    def test_name(self):
        fName = input("Please enter first name\n")
        lName = input("Please enter last name\n")
        self.assertIsNotNone(name.fullName(fName, lName))
        
        #test return is not empty
    def test_name_1(self):
        fName = input("Please enter first name\n")
        lName = input("Please enter last name\n")
        self.assertIsNotNone(name.fullName(fName, lName))        
        
    def test_name_2(self):
        #test that first name is part of full name
        fName = input("Please enter first name\n")
        lName = input("Please enter last name\n")
        self.assertIn(fName, name.fullName(fName, lName))
        
   
if __name__ == '__main__':
    unittest.main()