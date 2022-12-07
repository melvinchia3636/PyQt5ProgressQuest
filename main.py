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

from start import Ui_startInterface

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

    def startGame(self, path):
        self.savePath = path
        
        try:
            with open(path, "r") as f:
                content = json.load(f)
            
        except:
            QtWidgets.QMessageBox.critical(self, "Error", "Could not load game from " + path)
            startWindow.show()
            return

        self.LoadGame(content)

        self.lasttick = timeGetTime()

        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.Progress)
        timer.start(100)

        startWindow.close()
        self.show()

    def closeEvent(self, event):
        self.SaveGame()
        QtWidgets.QMessageBox.information(self, "Saved", "Game saved as " + self.savePath)
        event.accept()

class StartMenu(QtWidgets.QWidget, Ui_startInterface):
    def __init__(self):
        super(StartMenu, self).__init__()
        self.setupUi(self)

        self.loadGameButton.clicked.connect(self.loadGame)

    def loadGame(self):
        savePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", "", "JSON Files (*.json)")
        if savePath:
            playWindow.startGame(savePath)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    playWindow = Main()
    startWindow = StartMenu()
    startWindow.show()
    sys.exit(app.exec_())

    