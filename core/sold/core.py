from core.game.conf import conf
from PyQt5 import QtWidgets
from datetime import datetime
import json

K = conf.K
randseed = conf.randseed
Random = conf.Random
LevelUpTime = conf.LevelUpTime

class CoreSold:
    def __init__(self):
        self.stats = {}
        self.seedHistory = []
        self.race = None
        self.klass = None

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

    def sold(self, playWindow):
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

        json.dump(newguy, open(newguy["Traits"]["Name"]+".pq.json", "w"), indent=4)
        playWindow.startGame(newguy["Traits"]["Name"]+".pq.json")