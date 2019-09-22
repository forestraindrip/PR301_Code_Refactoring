# created by Kieran Jerry Jonathon
from front_end_kieran import TkinterInterface
from front_end_jerry import GuiInterface


class MainTIGr:
    def go(self):
        config = open("config.txt", "r+").read().splitlines()
        interface = None
        if config[2] == "FrontEndKieran":
            interface = TkinterInterface()
        elif config[2] == "FrontEndJerry":
            interface = GuiInterface()

        interface.start()


if __name__ == "__main__":
    main = MainTIGr()
    main.go()
