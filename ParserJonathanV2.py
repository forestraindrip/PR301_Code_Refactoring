# created by Kieran Jerry Jonathon
from TIGr import AbstractParser
import re


class Parser(AbstractParser):
    def __init__(self, drawer):
        super().__init__(drawer)
        self.commandlist = {
            "P": "self.drawer.select_pen(self.data)",
            "D": "self.drawer.pen_down()",
            "N": "self.drawer.draw_line(0, self.data)",
            "E": "self.drawer.draw_line(90, self.data)",
            "S": "self.drawer.draw_line(180, self.data)",
            "W": "self.drawer.draw_line(270, self.data)",
            "X": "self.drawer.go_along(self.data)",
            "Y": "self.drawer.go_down(self.data)",
            "U": "self.drawer.pen_up()"
        }

    def parse(self, raw_source):
        """hard coded parsing like this is a Bad Thing!
            It is inflexible and has no error checking
        """
        # Jonathan Holdaway worked on this
        self.source = raw_source.splitlines()
        for line in self.source:
            inputs = re.findall("\w+", line)
            self.data = re.findall("\d+", line)
            self.command = inputs[0].upper()
            if len(self.data) > 0:
                self.data = int(float(self.data[0]))
            # if self.command[0] == 'P':
            #     self.drawer.select_pen(self.data)
            # if self.command[0] == 'D':
            #     self.drawer.pen_down()
            # if self.command[0] == 'N':
            #     self.drawer.draw_line(360, self.data)
            # if self.command[0] == 'E':
            #     self.drawer.draw_line(90, self.data)
            # if self.command[0] == 'S':
            #     self.drawer.draw_line(180, self.data)
            # if self.command[0] == 'W':
            #     self.drawer.draw_line(270, self.data)
            # if self.command[0] == 'X':
            #     self.drawer.go_along(self.data)
            # if self.command[0] == 'Y':
            #     self.drawer.go_down(self.data)
            # if self.command[0] == 'U':
            #     self.drawer.pen_up()
            if self.command[0] in self.commandlist:
                parsed_command = self.commandlist[self.command[0]]
                exec(parsed_command)
