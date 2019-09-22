# created by Kieran Jerry Jonathon
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


class GuiInterface:
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

    def init_widgets(self):
        self.master.title("TkinterGUI")
        width = 1200
        height = 600
        screenwidth = self.master.winfo_screenwidth()
        screenheight = self.master.winfo_screenheight()
        center = "%dx%d+%d+%d" % (
            width,
            height,
            (screenwidth - 800) / 2,
            (screenheight - height) / 2,
        )
        self.master.geometry(center)
        self.master.draw_btn = Button(self.master, text="Draw", command=self.draw)
        self.master.draw_btn.pack(side="left", fill="both", expand="yes")
        self.master.import_btn = Button(
            self.master, text="import", command=self.to_import
        )
        self.master.import_btn.pack(side="left", fill="both", expand="yes")

        self.master.selectDrawer = tkinter.Label(self.master, text="Select Drawer")
        self.master.selectDrawer.pack(side="left", fill="both", expand="yes")

        self.master.comboDrawer = Combobox(
            self.master, values=["DrawerJack", "DrawerKieran", "DrawerTurtleJack"]
        )
        self.master.comboDrawer.set(self.config[0])
        self.master.comboDrawer.pack(side="left", fill="both", expand="yes")

        self.master.selectParser = tkinter.Label(self.master, text="Select Parser")
        self.master.selectParser.pack(side="left", fill="both", expand="yes")

        self.master.comboParser = Combobox(
            self.master, values=["ParserDang", "ParserJerry", "ParserJonathanV2"]
        )
        self.master.comboParser.set(self.config[1])
        self.master.comboParser.pack(side="left", fill="both", expand="yes")

        self.master.selectInterface = tkinter.Label(
            self.master, text="Select Interface"
        )
        self.master.selectInterface.pack(side="left", fill="both", expand="yes")

        self.master.comboInterface = Combobox(
            self.master, values=["FrontEndJerry", "FrontEndKieran"]
        )
        self.master.comboInterface.set(self.config[2])
        self.master.comboInterface.pack(side="left", fill="both", expand="yes")

        self.master.close_btn = Button(
            self.master, text="Restart", command=self.restart_program
        )
        self.master.close_btn.pack(side="left", fill="both", expand="yes")

        self.master.instruction = Label(
            self.master, text="Please enter command:", font=("serif", 18)
        )
        self.master.instruction.pack(side="left", fill="both", expand="yes")

        self.master.text = Text(self.master, height=27, width=32)
        self.master.text.pack(side="left", fill="both", expand="yes")

    def draw(self):  # TODO: Inappropriate Intimacy
        self.source_reader = SourceReader(self.parser, self.importedFile)
        self.source_reader.go()

    def restart_program(self):  # TODO: Duplicate code
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

    def insert_text(self, row_source):
        self.master.text.insert("0.0", row_source)

    def to_import(self):
        self.importedFile = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title="Select file",
            filetypes=(("txt files", "*.txt"), ("all files", "*.*")),
        )
        if self.importedFile is not "":
            self.insert_text(open(self.importedFile, "r+").read())

    def start(self):
        self.master.mainloop()
