from PyQt5 import QtCore, QtWidgets
from core.game.conf import conf

K = conf.K
RandomName = conf.GenerateName
Random = conf.Random

class Ui_Sold(object):
    def defineWidgets(self, Window):
        self.mainLayout = QtWidgets.QGridLayout(Window)

        self.raceGroup = QtWidgets.QGroupBox(Window)
        self.classGroup = QtWidgets.QGroupBox(Window)
        self.statsGroup = QtWidgets.QGroupBox(Window)

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()

        self.statsGroupLayout = QtWidgets.QGridLayout(self.statsGroup)
        self.raceGroupLayout = QtWidgets.QVBoxLayout(self.raceGroup)
        self.classGroupLayout = QtWidgets.QVBoxLayout(self.classGroup)

        self.nameInput = QtWidgets.QLineEdit(Window)
        self.totalInput = QtWidgets.QLineEdit(self.statsGroup)

        self.label = QtWidgets.QLabel(Window)
        self.totalInputLabel = QtWidgets.QLabel(self.statsGroup)

        self.randomNameButton = QtWidgets.QPushButton(Window)
        self.soldButton = QtWidgets.QPushButton(Window)
        self.cancelButton = QtWidgets.QPushButton(Window)
        self.rollButton = QtWidgets.QPushButton(self.statsGroup)
        self.unrollButton = QtWidgets.QPushButton(self.statsGroup)

        self.spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

    def addWidgets(self):
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout.addWidget(self.nameInput)
        self.mainLayout.addWidget(self.raceGroup, 1, 0, 2, 1)
        self.horizontalLayout.addWidget(self.randomNameButton)
        self.horizontalLayout_2.addItem(self.spacerItem)
        self.horizontalLayout_4.addWidget(self.soldButton)
        self.horizontalLayout_4.addWidget(self.cancelButton)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_4)
        self.mainLayout.addWidget(self.classGroup, 1, 1, 1, 1)
        self.mainLayout.addWidget(self.statsGroup, 1, 2, 1, 1)
        self.mainLayout.addLayout(self.verticalLayout, 0, 0, 1, 3)
        self.mainLayout.addLayout(self.horizontalLayout_2, 2, 1, 1, 2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        for index, stat in enumerate(K.PrimeStats):
            self.label_2 = QtWidgets.QLabel(self.statsGroup)
            self.label_2.setText(stat)
            self.statsGroupLayout.addWidget(self.label_2, index, 0, 1, 1)

            self.lineEdit = QtWidgets.QLineEdit(self.statsGroup)
            self.lineEdit.setText("0")
            self.lineEdit.setReadOnly(True)
            self.statsGroupLayout.addWidget(self.lineEdit, index, 1, 1, 1)
            self.lineEdit.setMaximumSize(QtCore.QSize(40, 16777215))
            self.lineEdit.setStyleSheet("background: transparent")
            self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
            self.lineEdit.setObjectName(stat)

        self.statsGroupLayout.addWidget(self.totalInputLabel, 6, 0, 1, 1)
        self.statsGroupLayout.addWidget(self.totalInput, 6, 1, 1, 1)
        self.statsGroupLayout.addWidget(self.rollButton, 7, 0, 1, 2)
        self.statsGroupLayout.addWidget(self.unrollButton, 8, 0, 1, 2)
        self.totalInput.setReadOnly(True)
        self.totalInput.setAlignment(QtCore.Qt.AlignCenter)

        n = Random(len(K.Races))
        for index, race in enumerate(K.Races):
            self.radioButton = QtWidgets.QRadioButton(self.raceGroup)
            self.radioButton.setText(race.split("|")[0])
            self.raceGroupLayout.addWidget(self.radioButton)
            self.radioButton.toggled.connect(lambda: self.raceGroupClicked(self.radioButton))
            if index == n:
                self.radioButton.setChecked(True)

        n = Random(len(K.Klasses))
        for index, klass in enumerate(K.Klasses):
            self.radioButton_2 = QtWidgets.QRadioButton(self.classGroup)
            self.radioButton_2.setText(klass.split("|")[0])
            self.classGroupLayout.addWidget(self.radioButton_2)
            self.radioButton_2.toggled.connect(lambda: self.classGroupClicked(self.radioButton_2))
            if index == n:
                self.radioButton_2.setChecked(True)

    def setSizesAndSpacing(self):
        self.verticalLayout.setSpacing(0)
        self.horizontalLayout.setSpacing(10)
        self.raceGroupLayout.setSpacing(10)
        self.horizontalLayout_4.setSpacing(10)
        
        self.soldButton.setMinimumSize(QtCore.QSize(100, 0))
        self.cancelButton.setMinimumSize(QtCore.QSize(100, 0))
        self.statsGroup.setMaximumSize(QtCore.QSize(120, 16777215))

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.unrollButton.sizePolicy().hasHeightForWidth())

        self.rollButton.setSizePolicy(sizePolicy)
        self.unrollButton.setSizePolicy(sizePolicy)

    def setWidgetText(self, Window):
        Window.setWindowTitle("New Character")

        self.raceGroup.setTitle("Race")
        self.classGroup.setTitle("Class")
        self.statsGroup.setTitle("Stats")

        self.label.setText("Name")
        self.randomNameButton.setText("?")

        self.totalInputLabel.setText("Total")
        self.rollButton.setText("Roll")
        self.unrollButton.setText("Unroll")
        self.soldButton.setText("Sold!")
        self.cancelButton.setText("Cancel")

        self.nameInput.setText(RandomName())
        

    def setupUi(self, Window):
        Window.setFixedSize(600, 580)

        self.defineWidgets(Window)
        self.addWidgets()
        self.setSizesAndSpacing()
        self.setWidgetText(Window)

        QtCore.QMetaObject.connectSlotsByName(Window)

        
