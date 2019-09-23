# created by Kieran Jerry Jonathon
from tigr import AbstractParser
import re


class ParserJonathon(AbstractParser):
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
            "U": "self.drawer.pen_up()",
        }

    def parse(self, raw_source):
        self.source = raw_source
        for line in self.source:
            inputs = re.findall(r"\w+", line)
            self.data = re.findall(r"\d+", line)
            self.command = inputs[0].upper()
            if len(self.data) > 0:
                self.data = int(float(self.data[0]))
            if self.command[0] in self.commandlist:
                parsed_command = self.commandlist[self.command[0]]
                exec(parsed_command)
