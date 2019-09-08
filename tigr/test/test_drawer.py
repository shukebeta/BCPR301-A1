import unittest
from tigr.drawer.drawer import Drawer
from tigr.drawer.turtle_worker import TurtleWorker

class TestDrawer(unittest.TestCase):
	def setUp(self):
		self.o = Drawer(worker=TurtleWorker)


	def test_pensize(self):
		self.o.pensize(2)


	def test_select_pen(self):
		pass

	def test_pen_up(self):
		# self.o.pen_up()
		# # TypeError: penup()
		# # missing
		# # 1
		# # required
		# # positional
		# # argument: 'self'




































