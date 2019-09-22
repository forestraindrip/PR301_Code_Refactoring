# created by Kieran Jerry Jonathon
import os
import sys
import tkinter
from tkinter import filedialog
from tkinter.ttk import Combobox

from drawer_jack import DrawerJack
from drawer_kieran import DrawerKieran
from drawer_turtle_jack import DrawerTurtleJack
from parser_dang import ParserDang
from parser_jerry import ParserJerry
from parser_jonathan_v2 import ParserJonathon
from source_reader import SourceReader


class TkinterInterface:
    def __init__(self):
        self.window = tkinter.Tk()
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
        self.window.title("GUI")
        self.window.draw_btn = tkinter.Button(
            self.window, text="Draw", command=self.draw
        )
        self.window.draw_btn.grid(column=0, row=0)

        self.window.import_btn = tkinter.Button(
            self.window, text="Import new File to read", command=self.importfile
        )
        self.window.import_btn.grid(column=1, row=0)

        self.window.selectDrawer = tkinter.Label(self.window, text="Select Drawer")
        self.window.selectDrawer.grid(column=2, row=0)

        self.window.comboDrawer = Combobox(
            self.window, values=["DrawerJack", "DrawerKieran", "DrawerTurtleJack"]
        )
        self.window.comboDrawer.set(self.config[0])
        self.window.comboDrawer.grid(column=3, row=0)

        self.window.selectParser = tkinter.Label(self.window, text="Select Parser")
        self.window.selectParser.grid(column=4, row=0)

        self.window.comboParser = Combobox(
            self.window, values=["ParserDang", "ParserJerry", "ParserJonathanV2"]
        )
        self.window.comboParser.set(self.config[1])
        self.window.comboParser.grid(column=5, row=0)

        self.window.selectInterface = tkinter.Label(
            self.window, text="Select Interface"
        )
        self.window.selectInterface.grid(column=6, row=0)

        self.window.comboInterface = Combobox(
            self.window, values=["FrontEndJerry", "FrontEndKieran"]
        )
        self.window.comboInterface.set(self.config[2])
        self.window.comboInterface.grid(column=7, row=0)

        self.window.close_btn = tkinter.Button(
            self.window, text="Restart", command=self.restart_program
        )
        self.window.close_btn.grid(column=8, row=0)

        self.window.toDrawLabel = tkinter.Label(self.window, text=self.toDraw)
        self.window.toDrawLabel.grid(column=1, row=1, columnspan=8)

    def start(self):
        self.window.mainloop()

    def restart_program(self):  # TODO: Duplicate code
        """
        Restarts the current program.
        Note: this function does not return. Any cleanup action (like
        saving data) must be done before calling this function.
        """
        file = open("config.txt", "w")
        file.write(
            self.window.comboDrawer.get()
            + "\n"
            + self.window.comboParser.get()
            + "\n"
            + self.window.comboInterface.get()
        )
        file.close()
        python = sys.executable
        os.execl(python, python, *sys.argv)

    def draw(self):  # TODO: Inappropriate Intimacy
        self.source_reader = SourceReader(self.parser, self.importedFile)
        self.source_reader.go()
        self.window.toDrawLabel.config(text=self.toDraw)

    def importfile(self):
        self.importedFile = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title="Select file",
            filetypes=(("txt files", "*.txt"), ("all files", "*.*")),
        )
        self.toDraw = open(self.importedFile, "r+").read()
