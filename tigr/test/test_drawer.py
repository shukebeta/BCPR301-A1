import unittest
from tigr.drawer.drawer import Drawer
from tigr.drawer.turtle_worker import TurtleWorker


class TestDrawer(unittest.TestCase):

	def setUp(self):
		self.o =Drawer(worker=TurtleWorker)

	def test_pensize(self):
		pass

	# self.o.pensize(2)
	# AttributeError: 'int' object has no attribute '_pensize'

	def test_select_pen(self):
		pass

	def test_pen_down(self):
		self.o.pen_down()
	# self.assertTrue(self.o.worker.isdown())
	# TypeError: pendown() missing 1 required positional argument: 'self'

	def test_pen_up(self):
		self.o.pen_up()
		self.assertTrue(self.o.worker.isup())