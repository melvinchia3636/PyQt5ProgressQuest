# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'start.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_startInterface(object):
    def setupUi(self, startInterface):
        startInterface.setObjectName("startInterface")
        startInterface.setWindowModality(QtCore.Qt.NonModal)
        startInterface.resize(521, 308)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(startInterface.sizePolicy().hasHeightForWidth())
        startInterface.setSizePolicy(sizePolicy)
        startInterface.setMaximumSize(QtCore.QSize(16777215, 536))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(startInterface)
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pqIcon = QtWidgets.QLabel(startInterface)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pqIcon.sizePolicy().hasHeightForWidth())
        self.pqIcon.setSizePolicy(sizePolicy)
        self.pqIcon.setMaximumSize(QtCore.QSize(256, 256))
        self.pqIcon.setText("")
        self.pqIcon.setPixmap(QtGui.QPixmap(":/pic/pq.png"))
        self.pqIcon.setScaledContents(True)
        self.pqIcon.setObjectName("pqIcon")
        self.horizontalLayout.addWidget(self.pqIcon)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.newGameSinglePlayerButton = QtWidgets.QPushButton(startInterface)
        self.newGameSinglePlayerButton.setObjectName("newGameSinglePlayerButton")
        self.verticalLayout.addWidget(self.newGameSinglePlayerButton)
        self.newGameMultiPlayerButton = QtWidgets.QPushButton(startInterface)
        self.newGameMultiPlayerButton.setObjectName("newGameMultiPlayerButton")
        self.verticalLayout.addWidget(self.newGameMultiPlayerButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.loadGameButton = QtWidgets.QPushButton(startInterface)
        self.loadGameButton.setObjectName("loadGameButton")
        self.verticalLayout.addWidget(self.loadGameButton)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.exitButton = QtWidgets.QPushButton(startInterface)
        self.exitButton.setObjectName("exitButton")
        self.verticalLayout.addWidget(self.exitButton)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.websiteLink = QtWidgets.QLabel(startInterface)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.websiteLink.setFont(font)
        self.websiteLink.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.websiteLink.setStyleSheet("color: blue")
        self.websiteLink.setAlignment(QtCore.Qt.AlignCenter)
        self.websiteLink.setOpenExternalLinks(True)
        self.websiteLink.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.websiteLink.setObjectName("websiteLink")
        self.verticalLayout.addWidget(self.websiteLink)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.projectInfoLabel = QtWidgets.QLabel(startInterface)
        self.projectInfoLabel.setStyleSheet("color:gray")
        self.projectInfoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.projectInfoLabel.setObjectName("projectInfoLabel")
        self.verticalLayout_2.addWidget(self.projectInfoLabel)

        self.retranslateUi(startInterface)
        QtCore.QMetaObject.connectSlotsByName(startInterface)

    def retranslateUi(self, startInterface):
        _translate = QtCore.QCoreApplication.translate
        startInterface.setWindowTitle(_translate("startInterface", "Progress Quest"))
        self.newGameSinglePlayerButton.setText(_translate("startInterface", "New Game (Single player)"))
        self.newGameMultiPlayerButton.setText(_translate("startInterface", "New Game (Multi player)"))
        self.loadGameButton.setText(_translate("startInterface", "Load Game"))
        self.exitButton.setText(_translate("startInterface", "Exit"))
        self.websiteLink.setText(_translate("startInterface", "https://progressquest.com"))
        self.projectInfoLabel.setText(_translate("startInterface", "Recreated by Melvin Chia using PyQt5. Project under MIT License."))

from assets import main_rc