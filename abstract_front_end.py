import os
import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox

from drawer_jack import DrawerJack
from drawer_kieran import DrawerKieran
from drawer_turtle_jack import DrawerTurtleJack
from parser_dang import ParserDang
from parser_jerry import ParserJerry
from parser_jonathan_v2 import ParserJonathon
from source_reader import SourceReader


class AbstractFrontEnd:
    def __init__(self):
        self.master = None
        self.config = open("config.txt", "r+").read().splitlines()
        self.canvas = None
        self.importedFile = None
        self.drawer = None
        self.parser = None
        self.source_reader = None

    def start(self):
        self.master.mainloop()

    def init_widgets(self):
        pass

    def draw(self):
        self.drawer = self.construct_drawer()
        self.parser = self.construct_parser(self.drawer)
        self.source_reader = SourceReader(self.parser, self.importedFile)
        self.source_reader.go()

    def restart_program(self):
        file = open("config.txt", "w")
        file.write(
            self.master.comboDrawer.get()
            + "\n"
            + self.master.comboParser.get()
            + "\n"
            + self.master.comboInterface.get()
        )
        file.close()
        python = sys.executable
        os.execl(python, python, *sys.argv)

    def importfile(self):
        pass

    def construct_drawer(self):
        drawer = None
        if self.config[0] == "DrawerKieran":
            drawer = DrawerKieran(self.canvas)
        elif self.config[0] == "DrawerJack":
            drawer = DrawerJack(self.canvas)
        elif self.config[0] == "DrawerTurtleJack":
            drawer = DrawerTurtleJack(self.canvas)
        return drawer

    def construct_parser(self, drawer):
        parser = None
        if self.config[1] == "ParserDang":
            parser = ParserDang(drawer)
        elif self.config[1] == "ParserJerry":
            parser = ParserJerry(drawer)
        elif self.config[1] == "ParserJonathanV2":
            parser = ParserJonathon(drawer)
        return parser
