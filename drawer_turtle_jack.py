# Works by KC and Jack
import turtle
import my_enums
from tigr import AbstractDrawer


class DrawerTurtleJack(AbstractDrawer):

    def __init__(self, canvas):
        super().__init__(canvas)
        self.test_string = ""
        self.cursor = turtle.RawPen(self._canvas)
        self.penIsDown = True
        self.cursor.speed(1)

    def select_pen(self, pen_num):
        self.cursor.color(my_enums.Pen.colours[pen_num])
        print(f"Selected pen {pen_num}")

    def pen_down(self):
        self.penIsDown = True
        print("pen down")

    def pen_up(self):
        self.penIsDown = False
        print("pen up")

    def go_along(self, along):
        self.pen_up()
        self.cursor.setx(along - 250)
        print(f"GOTO X={along}")

    def go_down(self, down):
        self.pen_up()
        self.cursor.sety(down - 250)
        print(f"GOTO X={down}")

    def draw_line(self, direction, distance):
        if self.penIsDown:
            self.cursor.setheading(direction + 90)
            self.cursor.forward(distance)
            print(f"drawing line of length {distance} at {direction} degrees")
