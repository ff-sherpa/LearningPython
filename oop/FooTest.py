import sys
import unittest

class FooTest(unittest.TestCase):
	"""Sample test case"""

	#@unittest.skip("Skipping over entire test routine")

	#preparing to test
	def setUp(self):
		"""Setting up for test case"""
		print "FooTest:setUp_:begin"
		
		## do something
		testName = self.shortDescription()
		if (testName == "Test Routine A"):
			print "Setting up for test A"
		elif (testName == "Test Routine B"):
			print "Setting up for test B"
		else:
			print "UNKNOWN TEST ROUTINE"

		print "FooTest:setUp_:end"

	#ending test
	def tearDown(self):
		"""Cleaing up for test case"""
		print "FooTest:tearDown_:begin"

		## do something
		testName = self.shortDescription()
		if (testName == "Test Routine A"):
			print "Cleaning up for test A"
		elif (testName == "Test Routine B"):
			print "Cleaning up for test B"
		else:
			print "UNKNOWN TEST ROUTINE"

		print "FooTest:tearDown_:end"

	#test routine A
	#@unittest.skipIf(mylib.__version__ > (1,3), "Skipping over entire test routine")
	def testA(self):
		"""Test routine A"""
		#self.skipTest("FooTest:test_A:skipped")
		print "FooTest:testA"

	#test routine B
	def testB(self):
		"""Test routine B"""
		fooA = 123
		fooB = 234
		self.assertEqual(fooA, fooB, "A is not equal to B")
		print "FooTest:testB"
	
	#test routine C
	def testC(self):
		"""Test routine C"""
		fooA = 123
		self.assertEqual(fooA, fooB, "A is not equal to B")
		print "FooTest:testC"
	
	#test routine D
	def testD(self):
		"""Test routine D"""
		self.fail("FooTest:test_D:fail_")
		print "FooTest:testD"
	

if __name__ == '__main__':
	unittest.main()
	#fooSuite = unittest.TestLoader().loadTestsFromTestCase(FooTest)
