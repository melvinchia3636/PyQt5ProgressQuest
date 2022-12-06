from PyQt5.QtWidgets import QTableWidget, QAbstractItemView, QTableWidgetItem


class TableBox(QTableWidget):
    def __init__(self, id, columns, fixedkeys=None):
        super(TableBox, self).__init__()
        self.id = id
        self.columns = columns
        self.fixedkeys = fixedkeys

        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.verticalHeader().setDefaultSectionSize(20)
        self.verticalHeader().setVisible(False)
        self.setShowGrid(False)
        self.setRowCount(0)
        self.setColumnCount(2)

    def ClearSelection(self):
        self.clearSelection()

    def PutUI(self, key, value):
        i = 0
        still = True
        if self.rowCount() == 0:
            self.insertRow(0)
            self.setItem(0, 0, QTableWidgetItem(key))
            self.setItem(0, 1, QTableWidgetItem(str(value)))
        else:
            for i in range(self.rowCount()):
                if self.item(i, 0).text() == key:
                    self.item(i, 1).setText(str(value))
                    still = False
                    break

            i += 1

            if still:
                self.insertRow(i)
                self.setItem(i, 0, QTableWidgetItem(key))
                self.setItem(i, 1, QTableWidgetItem(str(value)))

        self.selectRow(i)

    def scrollToTop(self):
        self.scrollTo(self.model().index(0, 0),
                      QAbstractItemView.PositionAtTop)

    def length(self):
        return len(self.fixedkeys or self.game[self.id])

    def remove0(self):
        if self.game[self.id]:
            self.game[self.id].pop(0)
            self.removeRow(0)

    def remove1(self):
        t = self.game[self.id].pop(0)
        self.game[self.id].pop(0)
        self.game[self.id].insert(0, t)
        self.removeRow(1)

    def load(self, game):
        self.game = game

        if type(self.game[self.id]) is list:
            for item in self.game[self.id]:
                self.PutUI(item[0], item[1])

        if type(self.game[self.id]) is dict:
            for key, value in self.game[self.id].items():
                if key != "seed":
                    self.PutUI(key, value)

    def label(self, n):
        return self.fixedkeys[n] if self.fixedkeys else self.game[self.id][n][0]
