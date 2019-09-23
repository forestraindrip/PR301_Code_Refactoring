# created by Kieran Jerry Jonathon
import os
import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox

from abstract_front_end import AbstractFrontEnd


class GuiInterface(AbstractFrontEnd):
    def __init__(self):
        super().__init__()
        self.master = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.master, bg="white", width=500, height=500)
        self.canvas.pack(side="bottom", fill="x", expand="yes")
        self.init_widgets()

    def importfile(self):
        self.importedFile = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title="Select file",
            filetypes=(("txt files", "*.txt"), ("all files", "*.*")),
        )
        if self.importedFile is not "":
            self._insert_text(open(self.importedFile, "r+").read())

    def init_widgets(self):
        self.__setup_title("TkinterGUI")
        center = self.__get_center_point(1200, 600)
        self.master.geometry(center)

        self.__create_draw_button()
        self.__setup_label("selectDrawer", "Select Drawer")
        self.__create_drawer_selection_input()

        self.__setup_label("selectParser", "Select Parser")
        self.__create_parser_selection_input()

        self.__setup_label("selectInterface", "Select Interface")
        self.__create_frontend_selection_input()

        self.__create_close_button()

        self.__setup_label("instruction", "Please enter command:")
        self.__create_instruction_input()

    def __setup_title(self, title):
        self.master.title(title)

    def __setup_label(self, target, text):
        self.master.target = tkinter.Label(self.master, text=text)
        self.master.target.pack(side="left", fill="both", expand="yes")

    def __create_drawer_selection_input(self):
        self.master.comboDrawer = Combobox(
            self.master, values=["DrawerJack", "DrawerKieran", "DrawerTurtleJack"]
        )
        self.master.comboDrawer.set(self.config[0])
        self.master.comboDrawer.pack(side="left", fill="both", expand="yes")

    def __create_frontend_selection_input(self):
        self.master.comboInterface = Combobox(
            self.master, values=["FrontEndJerry", "FrontEndKieran"]
        )
        self.master.comboInterface.set(self.config[2])
        self.master.comboInterface.pack(side="left", fill="both", expand="yes")

    def __create_parser_selection_input(self):
        self.master.comboParser = Combobox(
            self.master, values=["ParserDang", "ParserJerry", "ParserJonathanV2"]
        )
        self.master.comboParser.set(self.config[1])
        self.master.comboParser.pack(side="left", fill="both", expand="yes")

    def __create_draw_button(self):
        self.master.draw_btn = Button(self.master, text="Draw", command=self.draw)
        self.master.draw_btn.pack(side="left", fill="both", expand="yes")
        self.master.import_btn = Button(
            self.master, text="import", command=self.importfile
        )
        self.master.import_btn.pack(side="left", fill="both", expand="yes")

    def __create_instruction_input(self):
        self.master.text = Text(self.master, height=27, width=32)
        self.master.text.pack(side="left", fill="both", expand="yes")

    def __create_close_button(self):
        self.master.close_btn = Button(
            self.master, text="Restart", command=self.restart_program
        )
        self.master.close_btn.pack(side="left", fill="both", expand="yes")

    def __get_center_point(self, width, height):
        screenwidth = self.master.winfo_screenwidth()
        screenheight = self.master.winfo_screenheight()
        center = "%dx%d+%d+%d" % (
            width,
            height,
            (screenwidth - 800) / 2,
            (screenheight - height) / 2,
        )
        return center

    def _insert_text(self, row_source):
        self.master.text.insert("0.0", row_source)
