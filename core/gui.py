from components import ProgressBar, TableBox, ListBox
from PyQt5 import QtCore, QtGui, QtWidgets
from .conf import conf

K = conf.K

class Gui:
    def defineComponents(self, progressQuest):
        self.mainContainer = QtWidgets.QGridLayout(progressQuest)
        self.leftContainer = QtWidgets.QVBoxLayout()
        self.middleContainer = QtWidgets.QVBoxLayout()
        self.rightContainer = QtWidgets.QVBoxLayout()
        self.bottomContainer = QtWidgets.QVBoxLayout()

        self.charSheetLabel = QtWidgets.QLabel(progressQuest)
        self.equipmentLabel = QtWidgets.QLabel(progressQuest)
        self.plotDevLabel = QtWidgets.QLabel(progressQuest)
        self.ExpLabel = QtWidgets.QLabel(progressQuest)
        self.spellLabel = QtWidgets.QLabel(progressQuest)
        self.invLabel = QtWidgets.QLabel(progressQuest)
        self.encumbranceLabel = QtWidgets.QLabel(progressQuest)
        self.questsLabel = QtWidgets.QLabel(progressQuest)
        self.Kill = QtWidgets.QLabel(progressQuest)

        self.Traits = TableBox(
            "Traits", 2, K["Traits"])
        self.Stats = TableBox(
            "Stats", 2, K["Stats"])
        self.Spells = TableBox("Spells", 2)
        self.Equips = TableBox("Equips", 2, K["Equips"])
        self.Inventory = TableBox("Inventory", 2)

        self.Quests = ListBox("Quests", 1)
        self.Plots = ListBox("Plots", 1)

        self.ExpBar = ProgressBar(
            "ExpBar", "$remaining XP needed for next level")
        self.EncumBar = ProgressBar(
            "EncumBar", "$position/$max cubits")
        self.QuestBar = ProgressBar(
            "QuestBar", "$percent% complete")
        self.TaskBar = ProgressBar(
            "TaskBar", "$percent%")
        self.PlotBar = ProgressBar(
            "PlotBar", "$time remaining")

    def addWidgets(self):
        self.leftContainer.addWidget(self.charSheetLabel)
        self.leftContainer.addWidget(self.Traits)
        self.leftContainer.addWidget(self.Stats)
        self.leftContainer.addWidget(self.ExpLabel)
        self.leftContainer.addWidget(self.ExpBar)
        self.leftContainer.addWidget(self.spellLabel)
        self.leftContainer.addWidget(self.Spells)

        self.middleContainer.addWidget(self.equipmentLabel)
        self.middleContainer.addWidget(self.Equips)
        self.middleContainer.addWidget(self.invLabel)
        self.middleContainer.addWidget(self.Inventory)
        self.middleContainer.addWidget(self.encumbranceLabel)
        self.middleContainer.addWidget(self.EncumBar)

        self.rightContainer.addWidget(self.plotDevLabel)
        self.rightContainer.addWidget(self.Plots)
        self.rightContainer.addWidget(self.PlotBar)
        self.rightContainer.addWidget(self.questsLabel)
        self.rightContainer.addWidget(self.Quests)
        self.rightContainer.addWidget(self.QuestBar)

        self.bottomContainer.addWidget(self.Kill)
        self.bottomContainer.addWidget(self.TaskBar)

        self.mainContainer.addLayout(self.leftContainer, 0, 0, 1, 1)
        self.mainContainer.addLayout(self.middleContainer, 0, 1, 1, 1)
        self.mainContainer.addLayout(self.rightContainer, 0, 2, 1, 1)
        self.mainContainer.addLayout(self.bottomContainer, 1, 0, 1, 3)

    def setFontForLabels(self):
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)

        for widget in (
            self.charSheetLabel,
            self.spellLabel,
            self.ExpLabel,
            self.equipmentLabel,
            self.invLabel,
            self.encumbranceLabel,
            self.questsLabel,
            self.plotDevLabel
        ):
            widget.setFont(font)

    def setSizePolicies(self):
        for widgets in (
            self.Traits,
            self.Stats,
            self.Spells,
            self.Plots,
            self.Quests
        ):
            widgets.setSizePolicy(QtWidgets.QSizePolicy(
                QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding))

        self.Equips.setSizePolicy(QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed))

        for widgets in (self.ExpBar, self.PlotBar, self.QuestBar):
            widgets.setSizePolicy(QtWidgets.QSizePolicy(
                QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed))

    def setWidgetSizes(self):
        self.Traits.setMinimumSize(QtCore.QSize(240, 124))
        self.Traits.setMaximumSize(QtCore.QSize(240, 124))
        self.ExpBar.setMaximumSize(QtCore.QSize(240, 16777215))
        self.Spells.setMaximumSize(QtCore.QSize(240, 16777215))
        self.Stats.setMaximumSize(QtCore.QSize(240, 220))
        self.Stats.setMinimumSize(QtCore.QSize(240, 220))
        self.Equips.setMinimumSize(QtCore.QSize(0, 224))
        self.Equips.setMaximumSize(QtCore.QSize(16777215, 250))
        self.PlotBar.setMaximumSize(
            QtCore.QSize(250, 16777215))
        self.QuestBar.setMaximumSize(QtCore.QSize(250, 16777215))

    def setWidgetsText(self):
        item = self.Traits.horizontalHeaderItem(0)
        item.setText("Trait")
        item = self.Traits.horizontalHeaderItem(1)
        item.setText("Value")
        item = self.Stats.horizontalHeaderItem(0)
        item.setText("Stat")
        item = self.Stats.horizontalHeaderItem(1)
        item.setText("Value")
        item = self.Spells.horizontalHeaderItem(0)
        item.setText("Spell")
        item = self.Spells.horizontalHeaderItem(1)
        item.setText("Level")

        self.charSheetLabel.setText("Character Sheet")
        self.equipmentLabel.setText("Equipment")
        self.plotDevLabel.setText("Plot Development")
        self.ExpLabel.setText("Experience")
        self.spellLabel.setText("Spell Book")
        self.invLabel.setText("Inventory")
        self.encumbranceLabel.setText("Encumbrance")
        self.questsLabel.setText("Quests")

    def addHeaderToTable(self, table):
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)

        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        item.setFont(font)
        table.setHorizontalHeaderItem(0, item)

        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        item.setFont(font)
        table.setHorizontalHeaderItem(1, item)

    def configTable(self):
        self.addHeaderToTable(self.Traits)
        self.addHeaderToTable(self.Stats)
        self.addHeaderToTable(self.Spells)

        for table in (self.Traits, self.Stats):
            table.horizontalHeader().setDefaultSectionSize(60)
            table.horizontalHeader().setStretchLastSection(True)

        self.Equips.horizontalHeader().setStretchLastSection(True)

        self.Equips.horizontalHeader().setVisible(False)
        self.Inventory.horizontalHeader().setVisible(False)

        for table in (self.Inventory, self.Spells):
            table.horizontalHeader().setSectionResizeMode(
                0, QtWidgets.QHeaderView.Stretch)
            table.horizontalHeader().setSectionResizeMode(
                1, QtWidgets.QHeaderView.ResizeToContents)

    def setupUi(self, progressQuest):
        progressQuest.setWindowTitle("Progress Quest - Upniem")
        progressQuest.setWindowIcon(QtGui.QIcon("pq.png"))
        progressQuest.resize(1005, 596)

        self.defineComponents(progressQuest)
        self.setFontForLabels()
        self.setSizePolicies()
        self.setWidgetSizes()
        self.configTable()
        self.addWidgets()
        self.setWidgetsText()

        QtCore.QMetaObject.connectSlotsByName(progressQuest)