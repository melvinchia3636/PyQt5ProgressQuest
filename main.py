import json
import sys
from PyQt5 import QtCore, QtWidgets

from core.game.utils import *
from core.game.conf import conf
from core.game.gui import Gui
from core.game.core import Core

from core.sold.gui import UISold
from core.sold.core import CoreSold

from start import UIStartInterface

randseed = conf.randseed
LevelUpTime = conf.LevelUpTime
GenerateName = conf.GenerateName

class StartMenu(QtWidgets.QWidget, UIStartInterface):
    def __init__(self):
        super(StartMenu, self).__init__()
        self.setupUi(self)

        self.newGameButton.clicked.connect(self.newGame)
        self.loadGameButton.clicked.connect(self.loadGame)
        self.exitButton.clicked.connect(self.close)

    def loadGame(self):
        savePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", "", "JSON Files (*.json)")
        if savePath:
            playWindow.startGame(savePath)

    def newGame(self):
        soldWindow.show()
        self.hide()

class SoldMenu(QtWidgets.QWidget, CoreSold, UISold):
    def __init__(self):
        super(SoldMenu, self).__init__()

        self.setupUi(self, playWindow)
        self.RollEm()

    def closeEvent(self, event):
        startWindow.show()
        event.accept()

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

        soldWindow.close()
        startWindow.close()
        self.show()

        self.lasttick = timeGetTime()

        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.Progress)
        timer.start(100)

    def closeEvent(self, event):
        self.SaveGame()
        QtWidgets.QMessageBox.information(self, "Saved", "Game saved as " + self.savePath)
        event.accept()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    playWindow = Main()
    soldWindow = SoldMenu()
    startWindow = StartMenu()
    startWindow.show()
    sys.exit(app.exec_())

    