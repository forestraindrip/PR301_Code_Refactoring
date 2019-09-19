# created by Kieran Jerry Jonathon
from tigr import AbstractSourceReader


class MainTIGr(AbstractSourceReader):  # TODO: this class should be in the front end
    def go(self):
        global interface  # TODO: Global
        if config[2] == "FrontEndKieran":
            from front_end_kieran import TkinterInterface

            interface = TkinterInterface(self)
        elif config[2] == "FrontEndJerry":
            from front_end_jerry import GuiInterface

            interface = GuiInterface(self)

        interface.start()


if __name__ == "__main__":
    config = open("config.txt", "r+").read().splitlines()
    if config[0] == "DrawerKieran":
        from drawer_kieran import Drawer
    elif config[0] == "DrawerJack":
        from drawer_jack import Drawer
    elif config[0] == "DrawerTurtleJack":
        from drawer_turtle_jack import Drawer

    if config[1] == "ParserDang":
        from parser_dang import Parser
    elif config[1] == "ParserJerry":
        from parser_jerry import Parser
    elif config[1] == "ParserJonathanV2":
        from parser_jonathan_v2 import Parser

    main = MainTIGr(Parser(Drawer()))
    main.go()