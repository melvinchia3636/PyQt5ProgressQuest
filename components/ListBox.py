from PyQt5.QtWidgets import QListWidget, QListWidgetItem, QAbstractItemView
from PyQt5.QtCore import Qt

from core.utils import toRoman

class ListBox(QListWidget):
    def __init__(self, id, columns, fixedkeys=None):
        super(ListBox, self).__init__()
        self.id = id
        self.columns = columns
        self.fixedkeys = fixedkeys

    def AddUI(self, caption):
        item = QListWidgetItem(caption)
        item.setFlags(item.flags() & ~Qt.ItemIsSelectable)
        item.setCheckState(Qt.Unchecked)
        self.addItem(item)

        self.scrollToItem(item, QAbstractItemView.PositionAtBottom)

    def ClearSelection(self):
        self.clearSelection()

    def scrollToTop(self):
        self.scrollTo(self.model().index(0, 0), QAbstractItemView.PositionAtTop)

    def CheckAll(self, butlast=False):
        for i in range(self.count() - (1 if butlast else 0)):
            self.item(i).setCheckState(Qt.Checked)

    def length(self):
        return len(self.fixedkeys or self.game[self.id])

    def remove0(self):
        if self.game[self.id]:
            self.game[self.id].pop(0)

    def remove1(self):
        t = self.game[self.id].pop(0)
        self.game[self.id].pop(0)
        self.game[self.id].insert(0, t)

    def load(self, game):
        self.game = game

        if self.id == "Plots":
            for i in range(max([0, self.game["act"]-99]), self.game["act"] + 1):
                self.AddUI(('Act ' + toRoman(i)) if i else "Prologue")
        else:
            for item in self.game[self.id]:
                self.AddUI(item)

    def label(self, n):
        return self.fixedkeys[n] if self.fixedkeys else self.game[self.id][n][0]