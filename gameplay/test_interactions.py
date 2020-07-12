import unittest

class TestInteractions(unittest.TestCase):
    
    def test_case_1(self):
        self.assertEqual('test'.upper(), 'TEST')
        
if __name__ == '__main__':
    unittest.main()