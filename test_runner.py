from tigr.test.test_drawer import TestCaseDrawer
from tigr.test.test_reader import TestCaseSourceReader
from tigr.test.test_turtle import TestCaseTurtleWorker
from tigr.test.test_tkinter import TestCaseTkinterWorker

import unittest

the_suite = unittest.TestSuite()

the_suite.addTest(unittest.makeSuite(TestCaseDrawer))
the_suite.addTest(unittest.makeSuite(TestCaseSourceReader))
the_suite.addTest(unittest.makeSuite(TestCaseTkinterWorker))
the_suite.addTest(unittest.makeSuite(TestCaseTurtleWorker))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(the_suite)


