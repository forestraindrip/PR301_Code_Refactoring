# created by Kieran Jerry Jonathon
from tigr import AbstractParser
import re
from drawer_kieran import DrawerKieran
import doctest


class ParserJerry(AbstractParser):
    def parse(self, raw_source):
        """
        >>> d = DrawerKieran()
        >>> d.can_draw = True
        >>> p = ParserJerry(d)
        >>> p.parse('X 100')
        GOTO X=100
        """
        """hard coded parsing like this is a Bad Thing!
            It is inflexible and has no error checking
        """
        self.source = raw_source
        if raw_source is not "":
            for line in raw_source:
                line = re.match(r"^\w*\s*\d*", line).group()
                direction = "".join(re.findall(r"[A-Z]", line))
                data = int("".join(re.findall(r"\d+", line)))  # TODO: Switch Statements
                try:
                    if direction == "P":
                        self.drawer.select_pen(data)
                    if direction == "G":
                        self.drawer.goto(data)
                    if direction == "N":
                        self.drawer.draw_line(0, data)
                    if direction == "E":
                        self.drawer.draw_line(90, data)
                    if direction == "S":
                        self.drawer.draw_line(180, data)
                    if direction == "W":
                        self.drawer.draw_line(270, data)
                    if direction == "X":
                        self.drawer.go_along(data)
                    if direction == "Y":
                        self.drawer.go_down(data)
                except ValueError:
                    if direction == "D":
                        self.drawer.pen_down()
                    if direction == "U":
                        self.drawer.pen_up()


if __name__ == "__main__":
    doctest.testmod()
