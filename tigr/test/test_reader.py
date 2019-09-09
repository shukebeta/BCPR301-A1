import unittest
from tigr.reader.reader import SourceReader
from tigr.parser.regex_parser import RegexParser
from tigr.drawer.drawer import Drawer
from tigr.drawer.turtle_worker import TurtleWorker


class TestCaseSourceReader(unittest.TestCase):
	def setUp(self):
		drawer = Drawer(TurtleWorker())
		parser = RegexParser
		self.o = SourceReader(parser(drawer), optional_file_name=None)

	def test_go(self):
		self.assertFalse(self.o.parser.parse('instruction2.txt'))

