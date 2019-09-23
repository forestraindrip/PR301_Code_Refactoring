# Works by KC and Jack
from tigr import AbstractParser, AbstractSourceReader
import re


class ParserDang(AbstractParser):
    def parse(self, raw_source):
        self.source = raw_source

        for command in self.source:
            command = self.__remove_comment(command)
            if re.search("^P|p", command):
                self.drawer.select_pen(int(re.search("[1-4]", command).group(0)))

            elif re.search("^X|x", command):
                self.drawer.go_along(int(re.search("[-+]?[0-9]+", command).group(0)))

            elif re.search("^Y|y", command):
                self.drawer.go_down(int(re.search("[-+]?[0-9]+", command).group(0)))

            elif re.search("^D|d", command):
                self.drawer.pen_down()

            elif re.search("^U|u", command):
                self.drawer.pen_up()

            elif re.search("^W|w", command):
                self.drawer.draw_line(
                    270, int(re.search("[-+]?[0-9]+", command).group(0))
                )

            elif re.search("^E|e", command):
                self.drawer.draw_line(
                    90, int(re.search("[-+]?[0-9]+", command).group(0))
                )

            elif re.search("^N|n", command):
                self.drawer.draw_line(
                    0, int(re.search("[-+]?[0-9]+", command).group(0))
                )

            elif re.search("^S|s", command):
                self.drawer.draw_line(
                    180, int(re.search("[-+]?[0-9]+", command).group(0))
                )

    def __remove_comment(self, command):
        command_tuple = command.partition("#")
        return command_tuple[0]
