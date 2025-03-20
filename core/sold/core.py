import json
from PyQt5 import QtWidgets
from datetime import datetime
import os
from core.game.conf import conf

with open('core/game/config.json', encoding='utf-8') as f:
    K = json.load(f)
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
        for this in K["PrimeStats"]:
            total += self.Roll(this)
            if best < self.stats[this]:
                best = self.stats[this]
                self.stats["best"] = this
            self.findChild(QtWidgets.QLineEdit, this).setText(str(self.stats[this]))
            
        self.stats['最大生命值'] = Random(8) + self.stats["体质"] // 6
        self.stats['最大魔法值'] = Random(8) + self.stats["智力"] // 6

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
            "特征": {},
            "dna": list(self.stats["seed"]),
            "seed": list(self.stats["seed"]),
            "birthday": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "birthstamp": datetime.timestamp(datetime.now()),
            "属性": self.stats,
            "beststat": self.stats["best"] + " " + str(self.stats[self.stats["best"]]),
            "task": "",
            "tasks": 0,
            "elapsed": 0,
            "bestequip": "锋利的石块",
            "装备": {},
            "Inventory": [['金币', 0]],
            "Spells": [],
            "章节": 0,
            "bestplot": "序言",
            "Quests": [],
            "questmonster": "",
            "kill": "加载中....",
            "ExpBar": { "position": 0, "max": LevelUpTime(1) },
            "EncumBar": { "position": 0, "max": self.stats["力量"] + 10 },
            "PlotBar": { "position": 0, "max": 26 },
            "QuestBar": { "position": 0, "max": 1 },
            "TaskBar": { "position": 0, "max": 2000 },
            "queue": [
            'task|10|经历着一段神秘莫测且令人心生恐惧的夜间幻象',
            "task|6|关于那个你曾低估了的聪明的老家伙，很多事情都真相大白了",
            'task|6|一连串令人震惊的事件让你陷入了孤立无援且困惑不已的境地，但你依然坚定不屈',
            'task|4|凭借着一股此前未曾发觉的坚定决心，你踏上了一段漫长而危险的旅程',
            'plot|2|加载中'
            ]
        };

        newguy["特征"]["名字"] = self.nameInput.text();
        newguy["特征"]["种族"] = self.race
        newguy["特征"]["职业"] = self.klass
        newguy["特征"]["等级"] = 1;

        newguy["date"] = newguy["birthday"];
        newguy["stamp"] = newguy["birthstamp"];

        for equip in K["装备"]:
            newguy["装备"][equip] = '';

        newguy["装备"]["武器"] = newguy["bestequip"];
        newguy["装备"]["铠甲"] = "-3 粗麻布衣";

        save_dir = 'save'
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        filename = newguy["特征"]["名字"]+".pq.json"
        save_path = os.path.join(save_dir, filename)
        json.dump(newguy, open(save_path, "w"), indent=4)
        playWindow.startGame(save_path)