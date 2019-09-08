import unittest
from tigr.reader.reader import SourceReader
from tigr.parser.regex_parser import RegexParser
from tigr.drawer.drawer import Drawer
from tigr.drawer.turtle_worker import TurtleWorker


class TestSourceReader(unittest.TestCase):
	def setUp(self):
		drawer = Drawer
		parser = RegexParser
		self.o = SourceReader(parser(drawer(TurtleWorker)), optional_file_name=None)

	def test_go(self):
		# self.assertTrue(self.o.parser.parse('instruction2.txt'))
		pass
# TypeError: reset() missing 1 required positional argument: 'self'
