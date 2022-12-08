import math
import json
from .utils import *
from .conf import conf
import requests

randseed = conf.randseed
LevelUpTime = conf.LevelUpTime


class Core:
    def __init__(self):
        self.game = {}
        self.lasttick = None

    def TaskDone(self):
        return self.TaskBar.done()

    def Dequeue(self):
        while (self.TaskDone()):
            if Split(self.game["task"], 0) == 'kill':
                if Split(self.game["task"], 3) == '*':
                    self.WinItem()
                elif Split(self.game["task"], 3):
                    self.Add(self.Inventory, (
                        Split(self.game["task"], 1) + ' ' + Split(self.game["task"], 3)).lower(), 1)
            elif self.game["task"] == 'buying':
                self.Add(self.Inventory, 'Gold', - self.EquipPrice())
                self.WinEquip()
            elif (self.game["task"] == 'market') or (self.game["task"] == 'sell'):
                if self.game["task"] == 'sell':
                    amt = self.GetI(self.Inventory, 1) * \
                        self.GetI(self.Traits, 'Level')
                    if Pos(' of ', self.Inventory.label(1)) > 0:
                        amt *= (1+RandomLow(10)) * \
                            (1+RandomLow(self.GetI(self.Traits, 'Level')))
                    self.Inventory.remove1()
                    self.Add(self.Inventory, 'Gold', amt)

                if self.Inventory.length() > 1:
                    self.Inventory.scrollToTop()
                    self.Task('Selling ' + Indefinite(self.Inventory.label(1), self.GetI(self.Inventory, 1)),
                              1 * 1000)
                    self.game["task"] = 'sell'
                    break

            old = self.game["task"]
            self.game["task"] = ''
            if len(self.game["queue"]) > 0:
                a = Split(self.game["queue"][0], 0)
                n = int(Split(self.game["queue"][0], 1))
                s = Split(self.game["queue"][0], 2)
                if a == 'task' or a == 'plot':
                    self.game["queue"].pop(0)
                    if a == 'plot':
                        self.CompleteAct()
                        s = 'Loading ' + self.game["bestplot"]
                    self.Task(s, n * 1000)
                else:
                    raise 'bah!' + a

            elif (self.EncumBar.done()):
                self.Task('Heading to market to sell loot', 4 * 1000)
                self.game["task"] = 'market'
            elif (Pos('kill|', old) <= 0) and (old != 'heading'):
                if self.GetI(self.Inventory, 'Gold') > self.EquipPrice():
                    self.Task(
                        'Negotiating purchase of better equipment', 5 * 1000)
                    self.game["task"] = 'buying'
                else:
                    self.Task('Heading to the killing fields', 4 * 1000)
                    self.game["task"] = 'heading'
            else:
                nn = self.GetI(self.Traits, 'Level')
                t = self.MonsterTask(nn)
                InventoryLabelAlsoGameStyleTag = 3
                nn = math.floor(
                    (2 * InventoryLabelAlsoGameStyleTag * t['level'] * 1000) / nn)
                self.Task('Executing ' + t['description'], nn)

    def Q(self, s):
        self.game['queue'].append(s)
        self.Dequeue()

    def InterplotCinematic(self):
        r = Random(3)

        if r == 0:
            self.Q("task|1|Exhausted, you arrive at a friendly oasis in a hostile land")
            self.Q("task|2|You greet old friends and meet allies")
            self.Q("task|2|You are privy to a council of powerful do-gooders")
            self.Q("task|1|There is much to be done. You are chosen!")

        if r == 1:
            self.Q("task|1|Your quarry is in sight, but a mighty enemy bars your path!")
            nemesis = NamedMonster(self.GetI(self.Traits, "Level") + 3)
            self.Q("task|4|A desperate struggle commences with " + nemesis)

            s = Random(3)
            for i in range(1, Random(1 + self.game["act"] + 1) + 1):
                s += 1 + Random(2)

                if s % 3 == 0:
                    self.Q("task|2|Locked in grim combat with " + nemesis)

                if s % 3 == 1:
                    self.Q("task|2|" + nemesis +
                           " seems to have the upper hand")

                if s % 3 == 2:
                    self.Q("task|2|You seem to gain the advantage over " + nemesis)

            self.Q(
                "task|3|Victory! " +
                nemesis +
                " is slain! Exhausted, you lose conciousness"
            )
            self.Q("task|2|You awake in a friendly place, but the road awaits")

        if r == 2:
            nemesis2 = ImpressiveGuy()
            self.Q(
                "task|2|Oh sweet relief! You've reached the protection of the good " +
                nemesis2
            )
            self.Q(
                "task|3|There is rejoicing, and an unnerving encouter with " +
                nemesis2 +
                " in private"
            )
            self.Q("task|2|You forget your " +
                   BoringItem() + " and go back to get it")
            self.Q("task|2|What's self!? You overhear something shocking!")
            self.Q("task|2|Could " + nemesis2 + " be a dirty double-dealer?")
            self.Q(
                "task|3|Who can possibly be trusted with self news!? ... Oh yes, of course"
            )

        self.Q("plot|1|Loading")

    def MonsterTask(self, level):
        definite = False
        for i in range(level, 0, -1):
            if Odds(2, 5):
                level += RandSign()

        if level < 1:
            level = 1

        monster = lev = None
        if Odds(1, 25):
            monster = " " + Split(Pick(K["Races"]), 0)
            if Odds(1, 2):
                monster = "passing" + monster + \
                    " " + Split(Pick(K["Klasses"]), 0)
            else:
                monster = PickLow(K["Titles"]) + " " + \
                    GenerateName() + " the" + monster
                definite = True
            lev = level
            monster = monster + "|" + str(level) + "|*"
        elif self.game["questmonster"] and Odds(1, 4):
            monster = K["Monsters"][self.game["questmonsterindex"]]
            lev = int(Split(monster, 1))
        else:
            monster = Pick(K["Monsters"])
            lev = int(Split(monster, 1))
            for _ in range(5):
                m1 = Pick(K["Monsters"])
                if abs(level - int(Split(m1, 1))) < abs(level - lev):
                    monster = m1
                    lev = int(Split(monster, 1))

        result = Split(monster, 0)
        self.game["task"] = "kill|" + monster

        qty = 1
        if level - lev > 10:
            qty = math.floor((level + Random(lev)) / max([lev, 1]))
            if qty < 1:
                qty = 1
            level = math.floor(level / qty)

        if level - lev <= -10:
            result = "imaginary " + result
        elif level - lev < -5:
            i = 10 + (level - lev)
            i = 5 - Random(i + 1)
            result = Sick(i, Young(lev - level - i, result))
        elif level - lev < 0 and Random(2) == 1:
            result = Sick(level - lev, result)
        elif level - lev < 0:
            result = Young(level - lev, result)
        elif level - lev >= 10:
            result = "messianic " + result
        elif level - lev > 5:
            i = 10 - (level - lev)
            i = 5 - Random(i + 1)
            result = Big(i, Special(level - lev - i, result))
        elif level - lev > 0 and Random(2) == 1:
            result = Big(level - lev, result)
        elif level - lev > 0:
            result = Special(level - lev, result)

        lev = level
        level = lev * qty

        if not definite:
            result = Indefinite(result, qty)
        return {"description": result, "level": level}

    def EquipPrice(self):
        return (
            5 * self.GetI(self.Traits, "Level") * self.GetI(self.Traits, "Level") +
            10 * self.GetI(self.Traits, "Level") +
            20
        )

    def Put(self, list, key, value):
        if type(key) is int:
            key = list.label(key)

        if list.fixedkeys:
            self.game[list.id][key] = value
        else:
            i = 0;
            while i < len(self.game[list.id]):

                if self.game[list.id][i][0] == key:
                    self.game[list.id][i][1] = value;
                    break;

                i += 1
                

            if i == len(self.game[list.id]):
                self.game[list.id].append([key,value]);

        list.PutUI(key, value)

        if key == "STR":
            self.EncumBar.reset(10 + value, self.EncumBar.Position())

        if (list == self.Inventory):
            cubits = 0
            for item in self.game["Inventory"][1:]:
                cubits += int(item[1])
            self.EncumBar.reposition(cubits)

    def WinSpell(self):
        self.AddR(
            self.Spells,
            K["Spells"][
                RandomLow(
                    min([self.GetI(self.Stats, "WIS") +
                        self.GetI(self.Traits, "Level"), len(K["Spells"])])
                )
            ],
            1
        )

    def WinEquip(self):
        posn = Random(self.Equips.length())

        if not posn:
            stuff = K["Weapons"]
            better = K["OffenseAttrib"]
            worse = K["OffenseBad"]
        else:
            better = K["DefenseAttrib"]
            worse = K["DefenseBad"]
            stuff = K["Shields"] if posn == 1 else K["Armors"]

        name = LPick(stuff, self.GetI(self.Traits, "Level"))
        qual = int(Split(name, 1))
        name = Split(name, 0)
        plus = self.GetI(self.Traits, "Level") - qual
        if plus < 0:
            better = worse
        count = 0
        while count < 2 and plus:
            modifier = Pick(better)
            qual = int(Split(modifier, 1))
            modifier = Split(modifier, 0)
            if Pos(modifier, name) > 0:
                break
            if abs(plus) < abs(qual):
                break
            name = modifier + " " + name
            plus -= qual
            ++count

        if plus:
            name = str(plus) + " " + name
        if plus > 0:
            name = "+" + name

        self.Put(self.Equips, posn, name)
        self.game["bestequip"] = name
        if posn > 1:
            self.game["bestequip"] += " " + self.Equips.label(posn)

    def WinStat(self):
        i = None
        if Odds(1, 2):
            i = Pick(K["Stats"])
        else:
            t = 0
            for key in K["Stats"]:
                s = self.GetI(self.Stats, key)
                t += s * s
            t = Random(t)
            for key in K["Stats"]:
                i = key
                s = self.GetI(self.Stats, key)
                t -= s * s
                if t < 0:
                    return False
        self.Add(self.Stats, i, 1)

    def WinItem(self):
        self.Add(self.Inventory, SpecialItem(), 1)

    def CompleteQuest(self):
        self.QuestBar.reset(50 + RandomLow(1000))
        if self.Quests.length:
            self.Quests.CheckAll()
            [self.WinSpell, self.WinEquip,
                self.WinStat, self.WinItem][Random(4)]()
        while self.Quests.length() > 99:
            self.Quests.remove0()

        self.game["questmonster"] = ""
        r = Random(5)

        if r == 0:
            level = self.GetI(self.Traits, "Level")
            lev = 0
            for i in range(1, 5):
                montag = Random(K["Monsters"].length)
                m = K["Monsters"][montag]
                l = int(Split(m, 1))
                if i == 1 or abs(l - level) < abs(lev - level):
                    lev = l
                    self.game["questmonster"] = m
                    self.game["questmonsterindex"] = montag

            caption = "Exterminate " + \
                Definite(Split(self.game["questmonster"], 0), 2)

        if r == 1:
            caption = "Seek " + Definite(InterestingItem(), 1)

        if r == 2:
            caption = "Deliver self " + BoringItem()

        if r == 3:
            caption = "Fetch me " + Indefinite(BoringItem(), 1)

        if r == 4:
            mlev = 0
            level = self.GetI(self.Traits, "Level")
            for ii in range(1, 3):
                montag = Random(K["Monsters"].length)
                m = K["Monsters"][montag]
                l = int(Split(m, 1))
                if ii == 1 or abs(l - level) < abs(mlev - level):
                    mlev = l
                    self.game["questmonster"] = m

            caption = "Placate " + \
                Definite(Split(self.game["questmonster"], 0), 2)
            self.game["questmonster"] = ""

        if not self.game["Quests"]:
            self.game["Quests"] = []
        while len(self.game["Quests"]) > 99:
            self.game["Quests"].pop(0)
        self.game["Quests"].append(caption)
        self.game["bestquest"] = caption
        self.Quests.AddUI(caption)

        self.SaveGame()

    def CompleteAct(self):
        self.Plots.CheckAll()
        self.game["act"] += 1
        self.PlotBar.reset(60 * 60 * (1 + 5 * self.game["act"]))
        self.game["bestplot"] = "Act " + toRoman(self.game["act"])
        self.Plots.AddUI(self.game["bestplot"])

        if self.game["act"] > 1:
            self.WinItem()
            self.WinEquip()
        
        self.SaveGame()

    def Task(self, caption, msec):
        self.game["kill"] = caption + "..."
        if self.Kill:
            self.Kill.setText(self.game["kill"])
        self.TaskBar.reset(msec)

    def Add(self, list, key, value=None):
        self.Put(list, key, value + self.GetI(list, key))

        if not value:
            return
        line = "Gained" if value > 0 else "Lost"
        if key == "Gold":
            key = "gold piece"
            line = "Got paid" if value > 0 else "Spent"
        if value < 0:
            value = -value
        line = line + " " + Indefinite(key, value)

    def AddR(self, list, key, value):
        self.Put(list, key, toRoman(value + toArabic(self.Get(list, key))))

    def Get(self, list, key):
        if list.fixedkeys:
            if type(key) is int:
                key = list.fixedkeys[key]
            return self.game[list.id][key]
        elif type(key) is int:
            if key < len(self.game[list.id]):
                return self.game[list.id][key][1]
            else:
                return ""
        else:
            for i in range(len(self.game[list.id])):
                if (self.game[list.id][i][0] == key):
                    return self.game[list.id][i][1]
            return ""

    def GetI(self, list, key):
        try:
            return int(self.Get(list, key))
        except:
            return 0

    def LevelUp(self):
        self.Add(self.Traits, "Level", 1)
        self.Add(self.Stats, "HP Max", self.GetI(
            self.Stats, "CON") // 3 + 1 + Random(4))
        self.Add(self.Stats, "MP Max", self.GetI(
            self.Stats, "INT") // 3 + 1 + Random(4))
        self.WinStat()
        self.WinStat()
        self.WinSpell()
        self.ExpBar.reset(LevelUpTime(self.GetI(self.Traits, "Level")))

        self.SaveGame()

    def ClearAllSelections(self):
        for item in self.AllLists:
            item.ClearSelection()

    def LoadGame(self, sheet):
        self.game = sheet

        randseed(self.game["seed"])
        [e.load(self.game) for e in (self.AllBars + self.AllLists)]

        if self.Kill:
            self.Kill.setText(self.game["kill"])
        self.ClearAllSelections()

        for i in [self.Plots, self.Quests]:
            i.CheckAll(True)

        self.setWindowTitle("Progress Quest - " + self.game["Traits"]["Name"])

    def Progress(self):
        if self.TaskBar.done():
            self.game["tasks"] += 1
            self.game["elapsed"] += self.TaskBar.Max() // 1000

            self.ClearAllSelections()

            if self.game["kill"] == "Loading....":
                self.TaskBar.reset(0)

            gain = Pos("kill|", self.game["task"]) == 1
            if gain:
                if self.ExpBar.done():
                    self.LevelUp()
                else:
                    self.ExpBar.increment(self.TaskBar.Max() / 1000)

            if gain and self.game["act"] >= 1:
                if self.QuestBar.done() or not self.Quests.length:
                    self.CompleteQuest()
                else:
                    self.QuestBar.increment(self.TaskBar.Max() / 1000)

            if gain or not self.game["act"]:
                if self.PlotBar.done():
                    self.InterplotCinematic()
                else:
                    self.PlotBar.increment(self.TaskBar.Max() / 1000)

            self.Dequeue()
        else:
            elapsed = timeGetTime() - self.lasttick
            if (elapsed > 100):
                elapsed = 100
            if (elapsed < 0):
                elapsed = 0
            self.TaskBar.increment(elapsed)

        self.lasttick = timeGetTime()

    def HotOrNot(self):
        if self.Spells.length():
            flat = 1
            best = 0

            for i in range(1, self.Spells.length()):
                if ((i+flat) * toArabic(self.Get(self.Spells, i)) >
                        (best+flat) * toArabic(self.Get(self.Spells, best))):
                    best = i

            self.game["bestspell"] = self.Spells.label(
                best) + ' ' + self.Get(self.Spells, best)
        else:
            self.game["bestspell"] = ''

    def SaveGame(self):
        self.HotOrNot()

        self.game["seed"] = list(randseed())
        json.dump(self.game, open(self.savePath, 'w'), indent=2)