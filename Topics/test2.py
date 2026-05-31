import unittest
from Topics.testcaseadd import add
from Topics.testcaseadd import sub
class Test(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1,3),4)
    def test_sub(self):
        self.assertEqual(sub(3,2),1)
if __name__=="__main__":
    unittest.main()