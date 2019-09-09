import unittest
import time
from tigr.drawer.turtle_worker import TurtleWorker


class TestCaseTurtleWorker(unittest.TestCase):

	def setUp(self):
		self.o = TurtleWorker(speed=6, pencolor='black', pensize=2)

	def test_go_down(self):
		self.o.setposition(400, 300)
		self.o.go_down(100)
		self.assertTrue(self.o.pos() == (400, 200))

	def test_go_along(self):
		self.o.setposition(400, 300)
		self.o.go_down(100)
		self.assertTrue(self.o.pos() == (400, 200))

	def test_draw_line(self):
		self.o.penup()
		self.o.draw_line(270, 100)
		self.assertTrue(self.o.isdown())
		self.o.penup()
		self.o.draw_line(90, 100)
		self.assertTrue(self.o.isdown())

	def test_goto(self):
		self.o.goto(400, 200)
		self.assertTrue(self.o.pos() == (0, 100))
		self.o.goto(400, 400)
		self.assertTrue(self.o.pos() == (0, -100))

	def test_speed(self):
		self.o.speed = 3
		self.assertEqual(self.o.speed, 3)

	def test_bye(self):
		pass


if __name__ == '__main__':
	unittest.main(verbosity=2)
