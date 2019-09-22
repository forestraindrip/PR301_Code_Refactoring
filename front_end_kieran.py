# created by Kieran Jerry Jonathon
import os
import sys
import tkinter
from tkinter import filedialog
from tkinter.ttk import Combobox

from abstract_front_end import AbstractFrontEnd
from drawer_jack import DrawerJack
from drawer_kieran import DrawerKieran
from drawer_turtle_jack import DrawerTurtleJack
from parser_dang import ParserDang
from parser_jerry import ParserJerry
from parser_jonathan_v2 import ParserJonathon
from source_reader import SourceReader


class TkinterInterface(AbstractFrontEnd):
    def __init__(self):
        super().__init__()
        self.master = tkinter.Tk()
        self.windowCanvas = tkinter.Tk()
        self.windowCanvas.title("TK")
        self.canvas = tkinter.Canvas(self.windowCanvas, width=500, height=500)
        self.config = open("config.txt", "r+").read().splitlines()
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
        self.toDraw = "N 100 # then north 1cm"
        self.importedFile = "Input.txt"
        self.canvas.pack()

    def init_widgets(self):
        self.master.title("GUI")
        self.master.draw_btn = tkinter.Button(
            self.master, text="Draw", command=self.draw
        )
        self.master.draw_btn.grid(column=0, row=0)

        self.master.import_btn = tkinter.Button(
            self.master, text="Import new File to read", command=self.importfile
        )
        self.master.import_btn.grid(column=1, row=0)

        self.master.selectDrawer = tkinter.Label(self.master, text="Select Drawer")
        self.master.selectDrawer.grid(column=2, row=0)

        self.master.comboDrawer = Combobox(
            self.master, values=["DrawerJack", "DrawerKieran", "DrawerTurtleJack"]
        )
        self.master.comboDrawer.set(self.config[0])
        self.master.comboDrawer.grid(column=3, row=0)

        self.master.selectParser = tkinter.Label(self.master, text="Select Parser")
        self.master.selectParser.grid(column=4, row=0)

        self.master.comboParser = Combobox(
            self.master, values=["ParserDang", "ParserJerry", "ParserJonathanV2"]
        )
        self.master.comboParser.set(self.config[1])
        self.master.comboParser.grid(column=5, row=0)

        self.master.selectInterface = tkinter.Label(
            self.master, text="Select Interface"
        )
        self.master.selectInterface.grid(column=6, row=0)

        self.master.comboInterface = Combobox(
            self.master, values=["FrontEndJerry", "FrontEndKieran"]
        )
        self.master.comboInterface.set(self.config[2])
        self.master.comboInterface.grid(column=7, row=0)

        self.master.close_btn = tkinter.Button(
            self.master, text="Restart", command=self.restart_program
        )
        self.master.close_btn.grid(column=8, row=0)

        self.master.toDrawLabel = tkinter.Label(self.master, text=self.toDraw)
        self.master.toDrawLabel.grid(column=1, row=1, columnspan=8)

    def draw(self):
        super().draw()
        self.master.toDrawLabel.config(text=self.toDraw)

    def importfile(self):
        self.importedFile = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title="Select file",
            filetypes=(("txt files", "*.txt"), ("all files", "*.*")),
        )
        self.toDraw = open(self.importedFile, "r+").read()
