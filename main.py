from metadata import TestFile
from test import Test


if __name__ == '__main__':
	testfile = TestFile('test.yml')
	test = Test(testfile,'./drivers/chromedriver')
	test.apply_test_cases()