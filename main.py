# TODO: character creation
# TODO: main menu

import json
import sys
from datetime import datetime
from PyQt5 import QtCore, QtWidgets

from core.game.utils import *
from core.game.conf import conf
from core.game.gui import Gui
from core.game.core import Core

from start import Ui_startInterface
from sold import Ui_Sold

randseed = conf.randseed
LevelUpTime = conf.LevelUpTime
GenerateName = conf.GenerateName

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
        self.race = None
        self.klass = None

        self.setupUi(self)
        self.RollEm()

        self.rollButton.clicked.connect(self.RerollClick)
        self.unrollButton.clicked.connect(self.UnrollClick)
        self.soldButton.clicked.connect(self.sold)
        self.cancelButton.clicked.connect(self.close)
        self.randomNameButton.clicked.connect(lambda: self.nameInput.setText(GenerateName()))

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

    def raceGroupClicked(self, button):
        self.race = button.text()

    def classGroupClicked(self, button):
        self.klass = button.text()

    def sold(self):
        self.stats["seed"] = list(self.stats["seed"])
        newguy = {
            "Traits": {},
            "dna": list(self.stats["seed"]),
            "seed": list(self.stats["seed"]),
            "birthday": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "birthstamp": datetime.timestamp(datetime.now()),
            "Stats": self.stats,
            "beststat": self.stats["best"] + " " + str(self.stats[self.stats["best"]]),
            "task": "",
            "tasks": 0,
            "elapsed": 0,
            "bestequip": "Sharp Rock",
            "Equips": {},
            "Inventory": [['Gold', 0]],
            "Spells": [],
            "act": 0,
            "bestplot": "Prologue",
            "Quests": [],
            "questmonster": "",
            "kill": "Loading....",
            "ExpBar": { "position": 0, "max": LevelUpTime(1) },
            "EncumBar": { "position": 0, "max": self.stats["STR"] + 10 },
            "PlotBar": { "position": 0, "max": 26 },
            "QuestBar": { "position": 0, "max": 1 },
            "TaskBar": { "position": 0, "max": 2000 },
            "queue": [
            'task|10|Experiencing an enigmatic and foreboding night vision',
            "task|6|Much is revealed about that wise old bastard you'd underestimated",
            'task|6|A shocking series of events leaves you alone and bewildered, but resolute',
            'task|4|Drawing upon an unrealized reserve of determination, you set out on a long and dangerous journey',
            'plot|2|Loading'
            ]
        };

        newguy["Traits"]["Name"] = self.nameInput.text();
        newguy["Traits"]["Race"] = self.race
        newguy["Traits"]["Class"] = self.klass
        newguy["Traits"]["Level"] = 1;

        newguy["date"] = newguy["birthday"];
        newguy["stamp"] = newguy["birthstamp"];

        for equip in K.Equips:
            newguy["Equips"][equip] = '';

        newguy["Equips"]["Weapon"] = newguy["bestequip"];
        newguy["Equips"]["Hauberk"] = "-3 Burlap";

        json.dump(newguy, open(newguy["Traits"]["Name"]+".json", "w"), indent=4)
        playWindow.startGame(newguy["Traits"]["Name"]+".json")

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

    