#TODO: multiplayer
#TODO: save/load
# TODO: character creation
# TODO: main menu

import json
import sys
from PyQt5 import QtCore, QtWidgets
from core.utils import *

from core.gui import Gui
from core.core import Core
class Main(QtWidgets.QWidget, Core, Gui):
    def __init__(self):
        super(Main, self).__init__()

        self.ExpBar = self.PlotBar = self.TaskBar = self.QuestBar = self.EncumBar = None
        self.Traits = self.Stats = self.Spells = self.Equips = self.Inventory = self.Plots = self.Quests = None
        self.Kill = None

        self.setupUi(self)

        self.AllBars = [self.ExpBar, self.PlotBar,
                        self.TaskBar, self.QuestBar, self.EncumBar]
        self.AllLists = [self.Traits, self.Stats, self.Spells,
                         self.Equips, self.Inventory, self.Plots, self.Quests]

        save = json.load(open("Upniem.json"))
        self.LoadGame(save)

        self.lasttick = timeGetTime()

        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.Progress)
        timer.start(100)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
