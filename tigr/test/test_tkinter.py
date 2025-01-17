import unittest
from tigr.drawer.tkinter_worker import TkinterWorker


class TestCaseTkinterWorker(unittest.TestCase):

    def setUp(self):
        self.o = TkinterWorker(speed=8, pencolor='red', pensize=3)

    def test_pencolor(self):
        self.o.pencolor('red')
        self.assertEqual(self.o._pencolor, 'red')
        self.o.pencolor('black')
        self.assertEqual(self.o._pencolor, 'black')

    def test_pensize(self):
        self.o.pensize(4)
        self.assertEqual(self.o._pensize, 4)
        self.o.pensize(6)
        self.assertEqual(self.o._pensize, 6)

    def test_draw_line(self):
        self.o.penup()
        self.o.draw_line(45, 100)
        self.assertFalse(self.o._pendown)
        self.o.pendown()
        self.o.draw_line(90, 100)
        self.assertTrue(self.o._pendown)

    def test_goto(self):
        self.o.goto(200, 100)
        self.assertTrue(self.o.pos['x'] == 200)
        self.assertTrue(self.o.pos['y'] == 100)

    def test_reset(self):
        self.o.goto(*self.o.home_pos)
        self.o.setheading(0)
        self.o.forward(100)
        self.o.reset()
        self.assertTrue(self.o.pos['x'] == 400)
        self.assertTrue(self.o.pos['y'] == 300)

    def test_pendown(self):
        self.o.penup()
        self.assertFalse(self.o._pendown)
        self.o.pendown()
        self.assertTrue(self.o._pendown)

    def test_forward(self):
        self.o.goto(*self.o.home_pos)
        self.o.setheading(0)
        self.o.forward(100)
        self.assertTrue(int(self.o.pos['x']) == self.o.home_pos[0] + 100)
        self.o.setheading(90)
        self.o.forward(100)
        self.assertTrue(int(self.o.pos['y']) == self.o.home_pos[1] - 100)
        self.o.goto(*self.o.home_pos)
        self.o.penup()
        self.o.forward(-100)
        self.assertTrue(int(self.o.pos['y']) == self.o.home_pos[1] + 100)

    def test_setheading(self):
        self.o.setheading(100)
        self.assertTrue(self.o.heading == 100)

    def test_godown(self):
        self.o.goto(*self.o.home_pos)
        self.o.go_down(100)
        self.assertTrue(int(self.o.pos['y']) == self.o.home_pos[1] + 100)
        self.o.goto(*self.o.home_pos)
        self.o.go_down(-100)
        self.assertTrue(int(self.o.pos['y']) == self.o.home_pos[1] - 100)

    def test_speed(self):
        self.o.speed(3)
        wait_1 = self.o.wait
        self.o.speed(4)
        wait_2 = self.o.wait
        self.assertTrue(wait_1 > wait_2)

    def test_go_along(self):
        self.o.goto(*self.o.home_pos)
        self.o.go_along(100)
        self.assertTrue(tuple(self.o.pos.values()) == (500, 300))
        self.o.go_along(-100)
        self.assertTrue(tuple(self.o.pos.values()) == (400, 300))
