import unittest
from tigr.drawer.drawer import Drawer
from tigr.drawer.turtle_worker import TurtleWorker


class TestCaseDrawer(unittest.TestCase):

	def setUp(self):
		self.o = Drawer(worker=TurtleWorker())

	def test_pensize(self):
		self.o.pensize(2)
		self.assertEqual(self.o.pensize(), 2)
		self.o.pensize(4)
		self.assertEqual(self.o.pensize(), 4)

	def test_select_pen(self):
		self.o.select_pen(1)
		self.assertTrue(self.o.pencolor() == 'black')
		self.assertTrue(self.o.pensize() == 1)
		self.o.select_pen(2)
		self.assertTrue(self.o.pencolor() == 'black')
		self.assertTrue(self.o.pensize() == 2)
		r = self.o.select_pen(100)
		self.assertFalse(r)

	def test_pen_down(self):
		self.o.pen_down()
		self.assertTrue(self.o.isdown())

	def test_pen_up(self):
		self.o.pen_up()
		self.assertFalse(self.o.isdown())

	def test_pen_color(self):
		self.o.pencolor('blue')
		self.assertTrue(self.o.pencolor() == 'blue')

	def test_pen_size(self):
		self.o.pensize(5)
		self.assertTrue(self.o.pensize() == 5)

	def test_go_along(self):
		self.o.setposition(400, 300)
		self.o.setheading(90)
		self.o.go_along(100)
		self.assertTrue(self.o.pos() == (500, 300))

	def test_go_down(self):
		self.o.setposition(400, 300)
		self.o.go_down(100)
		self.assertTrue(self.o.pos() == (400, 200))

	def test_go_to(self):
		self.o.goto(400,200)
		self.assertTrue(self.o.pos() == (0, 100))
		self.o.goto(400,400)
		self.assertTrue(self.o.pos() == (0, -100))

	def test_forward(self):
		self.o.setposition(400, 300)
		self.o.setheading(0)
		self.o.forward(100)
		self.assertTrue(self.o.pos() == (500, 300))

	def test_draw_line(self):
		self.o.pen_up()
		self.o.draw_line(270, 100)
		self.assertTrue(self.o.isdown())
		self.o.pen_up()
		self.o.draw_line(90, 100)
		self.assertTrue(self.o.isdown())

	def test_reset(self):
		pass

	def test_bye(self):
		pass
