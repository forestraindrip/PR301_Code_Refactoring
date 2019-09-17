# created by Kieran Jerry Jonathon
from TIGr import AbstractSourceReader


class MainTIGr(AbstractSourceReader):

    def go(self):
        global interface
        if config[2] == 'FrontEndKieran':
            from FrontEndKieran import TkinterInterface
            interface = TkinterInterface(self)
        elif config[2] == 'FrontEndJerry':
            from FrontEndJerry import GuiInterface
            interface = GuiInterface(self)
        interface.start()


if __name__ == '__main__':
    config = open('config.txt', "r+").read().splitlines()
    if config[0] == 'DrawerKieran':
        from DrawerKieran import Drawer
    elif config[0] == 'DrawerJack':
        from DrawerJack import Drawer
    elif config[0] == 'DrawerTurtleJack':
        from DrawerTurtleJack import Drawer

    if config[1] == 'ParserDang':
        from ParserDang import Parser
    elif config[1] == 'ParserJerry':
        from ParserJerry import Parser
    elif config[1] == 'ParserJonathanV2':
        from ParserJonathanV2 import Parser

    main = MainTIGr(Parser(Drawer()))
    main.go()
