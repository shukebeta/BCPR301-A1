import unittest
from tigr.drawer.turtle_worker_factory import TurtleWorkerFactory


class TestCaseTurtleWorker(unittest.TestCase):

	def setUp(self):
		self.o = TurtleWorkerFactory().create_worker()
		self.o.speed(6)
		self.o.pencolor('black')
		self.o.pensize(2)

	def test_go_down(self):
		self.o.setposition(400, 300)
		self.o.go_down(100)
		self.assertTrue(self.o.pos() == (400, 200))
		self.o.go_down(-100)
		self.assertTrue(self.o.pos() == (400, 300))

	def test_go_along(self):
		self.o.setposition(400, 300)
		self.o.go_along(100)
		self.assertTrue(self.o.pos() == (500, 300))
		self.o.go_along(-100)
		self.assertTrue(self.o.pos() == (400, 300))

	def test_draw_line(self):
		self.o.pen_up()
		self.o.draw_line(270, 100)
		self.assertTrue(self.o.isdown())
		self.o.pen_up()
		self.o.draw_line(90, 100)
		self.assertTrue(self.o.isdown())

	def test_goto(self):
		self.o.pen_down()
		self.o.goto(400, 200)
		self.assertTrue(self.o.pos() == (0, 100))
		self.o.pen_up()
		self.o.goto(400, 400)
		self.assertTrue(self.o.pos() == (0, -100))

	def test_speed(self):
		self.o.speed(3)
		self.assertEqual(self.o.speed(), 3)
		self.o.speed(100)
		self.assertEqual(self.o.speed(), 0)
		self.o.speed(-100)
		self.assertEqual(self.o.speed(), 1)

	def test_bye(self):
		pass


