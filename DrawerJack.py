# Works by KC and Jack
import MyEnums
from TIGr import AbstractDrawer


class Drawer(AbstractDrawer):
    # config = open('config.txt', "r+").read().splitlines()
    # if config[2] == 'FrontEndKieran':
    #     from FrontEndKieran import TkinterInterface
    #     this_canvas = TkinterInterface.canvas
    # elif config[2] == 'FrontEndJerry':
    #     from FrontEndJerry import GuiInterface
    #     this_canvas = GuiInterface.canvas

    def __init__(self):
        self.colour = ''
        self.test_string = ''
        self.src_x = 0
        self.src_y = 0
        self.des_x = 0
        self.des_y = 0
        self.penIsDown = False

    def select_pen(self, pen_num):
        self.colour = MyEnums.Pen.colours[pen_num]
        print(f'Selected pen {pen_num}')

    def pen_down(self):
        self.penIsDown = True
        print('pen down')

    def pen_up(self):
        self.penIsDown = False
        print('pen up')

    def go_along(self, along):
        self.src_x = along
        print(f'GOTO X={along}')

    def go_down(self, down):
        self.src_y = down
        print(f'GOTO X={down}')

    def draw_line(self, direction, distance):
        if direction == 0:
            self.des_y = self.src_y - distance
            self.des_x = self.src_x
            # print("going UP " + str(distance))
        if direction == 180:
            self.des_y = self.src_y + distance
            self.des_x = self.src_x
            # print("going DOWN " + str(distance))
        if direction == 90:
            self.des_x = self.src_x + distance
            self.des_y = self.src_y
            # print("going RIGHT " + str(distance))
        if direction == 270:
            self.des_x = self.src_x - distance
            self.des_y = self.src_y
            # print("going LEFT  " + str(distance))

        if self.penIsDown:
            # print("src_x == " + str(self.src_x) + "/ src_y == " + str(self.src_y) + "des_x == " + str(
            # self.des_x) + "/ des_y == " + str(self.des_y))
            self.this_canvas.create_line(self.src_x, self.src_y, self.des_x, self.des_y, fill=self.colour)
            # self.test_string += f'drawing line of length {distance} at {direction} degrees'

        self.src_x, self.src_y = self.des_x, self.des_y
        # print("source_x == " + str(self.src_x) + "source_y == " + str(self.src_y))
        print(f'drawing line of length {distance} at {direction} degrees')
