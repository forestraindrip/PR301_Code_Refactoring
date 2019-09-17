# created by Kieran Jerry Jonathon
import math

import MyEnums
from TIGr import AbstractDrawer


class Drawer(AbstractDrawer):
    x_pos = 0
    y_pos = 0

    # config = open('config.txt', "r+").read().splitlines()
    # if config[2] == 'FrontEndKieran':
    #     from FrontEndKieran import TkinterInterface
    #     this_canvas = TkinterInterface.canvas
    # elif config[2] == 'FrontEndJerry':
    #     from FrontEndJerry import GuiInterface
    #     this_canvas = GuiInterface.canvas

    def __init__(self):
        self.test_string = ''
        self.colour = ''
        self.can_draw = False

    def select_pen(self, pen_num):
        self.colour = MyEnums.Pen.colours[pen_num]
        print(f'Selected pen {pen_num}')

    def pen_down(self):
        self.can_draw = True
        print('pen down')

    def pen_up(self):
        self.can_draw = False
        print('pen up')

    def go_along(self, along):
        self.x_pos = along
        print(f'GOTO X={along}')

    def go_down(self, down):
        self.y_pos = down
        print(f'GOTO X={down}')

    def draw_line(self, direction, distance):
        if self.can_draw:
            if direction == 0:
                direction = 360
            # test a direction angle direction = 30 Angle direction needs to be converted a decimal and divided into
            # pie. This is required math.sin and math.cos
            direction = (math.pi * 2) / (360 / direction)
            new_x = distance * math.sin(direction)
            new_y = -distance * math.cos(direction)
            # self.this_canvas.create_line(self.x_pos, self.y_pos, self.x_pos + new_x, self.y_pos + new_y,
            #                              fill=self.colour)
            self.x_pos += new_x
            self.y_pos += new_y
            print(f'drawing line of length {distance} at {direction} degrees')
