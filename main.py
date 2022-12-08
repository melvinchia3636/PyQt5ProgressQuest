# TODO: character creation
# TODO: main menu

import json
import sys
from PyQt5 import QtCore, QtWidgets

from core.utils import *
from core.conf import conf
from core.gui import Gui
from core.core import Core

from start import Ui_startInterface
from sold import Ui_Sold

randseed = conf.randseed

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

class SoldMenu(QtWidgets.QWidget, Ui_Sold):
    def __init__(self):
        super(SoldMenu, self).__init__()
        self.stats = {}
        self.seedHistory = []

        self.setupUi(self)
        self.RollEm()

        

        self.cancelButton.clicked.connect(self.close)
        self.rollButton.clicked.connect(self.RerollClick)
        self.unrollButton.clicked.connect(self.UnrollClick)
    
    def RerollClick(self):
        self.seedHistory.append(self.stats["seed"]);
        self.RollEm();

    def UnrollClick(self):
        randseed(self.seedHistory.pop());
        self.RollEm();

    def Roll(self, stat):
        self.stats[stat] = 3 + Random(6) + Random(6) + Random(6)
        return self.stats[stat]

    def RollEm(self):
        self.stats["seed"] = randseed()
        total = 0
        best = -1
        for this in K.PrimeStats:
            total += self.Roll(this)
            if best < self.stats[this]:
                best = self.stats[this]
                self.stats["best"] = this
            self.findChild(QtWidgets.QLineEdit, this).setText(str(self.stats[this]))
            
        self.stats['HP Max'] = Random(8) + self.stats["CON"] // 6
        self.stats['MP Max'] = Random(8) + self.stats["INT"] // 6

        color = "red" if total >= (63+18) else "yellow" if total > (4 * 18) else "grey" if total <= (63-18) else "silver" if total < (3 * 18) else "white"
        self.totalInput.setText(str(total))
        self.totalInput.setStyleSheet("background: " + color)

        if self.seedHistory:
            self.unrollButton.setEnabled(True)
        else:
            self.unrollButton.setEnabled(False)

    def closeEvent(self, event):
        startWindow.show()
        event.accept()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    playWindow = Main()
    soldWindow = SoldMenu()
    startWindow = StartMenu()
    startWindow.show()
    sys.exit(app.exec_())

    