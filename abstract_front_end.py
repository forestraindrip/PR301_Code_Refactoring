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
        self.importedFile = None
        self.master = tkinter.Tk()
        self.config = open("config.txt", "r+").read().splitlines()
        self.canvas = tkinter.Canvas(self.master, bg="white", width=500, height=500)
        self.canvas.pack(side="bottom", fill="x", expand="yes")
        self.init_widgets()

        drawer = None
        if self.config[0] == "DrawerKieran":
            drawer = DrawerKieran(self.canvas)
        elif self.config[0] == "DrawerJack":
            drawer = DrawerJack(self.canvas)
        elif self.config[0] == "DrawerTurtleJack":
            drawer = DrawerTurtleJack(self.canvas)

        self.parser = None
        if self.config[1] == "ParserDang":
            self.parser = ParserDang(drawer)
        elif self.config[1] == "ParserJerry":
            self.parser = ParserJerry(drawer)
        elif self.config[1] == "ParserJonathanV2":
            self.parser = ParserJonathon(drawer)

        self.source_reader = None

    def start(self):
        self.master.mainloop()

    def init_widgets(self):
        pass

    def draw(self):
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
