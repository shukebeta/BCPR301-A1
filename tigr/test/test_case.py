import unittest
from tigr.drawer.tkinter_worker import TkinterWorker


class TestTkinterWorker(unittest.TestCase):

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
        self.assertTrue(not self.o._pendown)
        self.o.pendown()
        self.o.draw_line(90, 100)
        self.assertTrue(self.o._pendown)

if __name__ == '__main__':
    unittest.main()