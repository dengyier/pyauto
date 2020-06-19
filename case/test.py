import unittest
import HTMLTestRunner
import os
class Test(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def testSubtract(self):
        u'''测试减法'''
        result = 6-5
        hope = 1
        self.assertEqual(result,hope,msg='This is a good test_case')

if __name__ == '__main__':
    unittest.main()
    # suit = unittest.TestSuite()
    # suit.addTest(Test('testSubtract'))
    # report_path = os.path.join(os.getcwd(),"case")
    #
    # runner = unittest.TextTestRunner()
    # runner.run(suit)
