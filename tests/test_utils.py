# import certification_app
import unittest

def tambah(a,b):
    return a + b 

def kurang(a,b):
    return a - b

class Test_tambah(unittest.TestCase):
    
    def test_tambah(self):
        self.assertEqual(tambah(4, 4), 8)
        # self.assertEqual(tambah(4, 4), 15)
    def test_kurang(self):
        self.assertEqual(kurang(6,2), 4)
        
        
if __name__ == '__main__':
    unittest.main()