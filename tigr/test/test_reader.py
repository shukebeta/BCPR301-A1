import unittest
from tigr.reader.reader import SourceReader
from tigr.parser.regex_parser import RegexParser
from tigr.drawer.drawer import Drawer
from tigr.drawer.turtle_worker import TurtleWorker
import os.path


class TestCaseSourceReader(unittest.TestCase):

	def test_go(self):
		drawer = Drawer(TurtleWorker())
		parser = RegexParser
		file_name = os.path.join(os.path.dirname(__file__), 'instructions1.txt')
		self.o = SourceReader(parser(drawer), optional_file_name=file_name)
		self.o.go()
		self.assertGreater(len(self.o.source), 0)

	def test_go_fail(self):
		drawer = Drawer(TurtleWorker())
		parser = RegexParser
		self.assertRaises(Exception, SourceReader(parser(drawer), optional_file_name='IIIinstructions2.txt'))

