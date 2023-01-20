# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newInterfaceKyUfVT.ui'
##
## Created by: Qt User Interface Compiler version 5.15.7
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore

import ui.res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 300)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"border: none;")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.mainFrame = QFrame(self.centralwidget)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setStyleSheet(u"/*Globals*/\n"
"QLabel{\n"
"   font: 9pt \"JetBrains Mono\";\n"
"   color: grey;\n"
"}\n"
"\n"
"/*Frames*/\n"
"#mainFrame{\n"
"   font: 9pt \"JetBrains Mono\";\n"
"   background-color:  #2F343F;\n"
"}\n"
"\n"
"/*Objects*/\n"
"#searchBar{\n"
"   background-color: #262A32;\n"
"   border-radius: 5px;\n"
"   color:  #A0A0A0;\n"
"}\n"
"\n"
"#settingsBtn{\n"
"   image: url(:/Icons/icons/icon_settings.png);\n"
"   background-color: transparent;\n"
"   border: none;\n"
"}\n"
"\n"
"#clipsListWidget{\n"
"   background-color: transparent;\n"
"   color:  #A0A0A0;\n"
"}\\\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.mainFrame.setFrameShape(QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.mainFrame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.searchBarFrame = QFrame(self.mainFrame)
        self.searchBarFrame.setObjectName(u"searchBarFrame")
        self.searchBarFrame.setMinimumSize(QSize(0, 35))
        self.searchBarFrame.setMaximumSize(QSize(16777215, 35))
        self.searchBarFrame.setStyleSheet(u"#searchBarFrame{\n"
"   background-color: #536D79;\n"
"}")
        self.searchBarFrame.setFrameShape(QFrame.StyledPanel)
        self.searchBarFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.searchBarFrame)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(6, 0, 0, 0)
        self.magnifiyingGlassLabel = QLabel(self.searchBarFrame)
        self.magnifiyingGlassLabel.setObjectName(u"magnifiyingGlassLabel")
        self.magnifiyingGlassLabel.setMinimumSize(QSize(15, 0))
        self.magnifiyingGlassLabel.setMaximumSize(QSize(15, 16777215))
        self.magnifiyingGlassLabel.setStyleSheet(u"image: url(:/Icons/icons/icon_magnifying.png);\n"
"color: #E1E4E7;")

        self.horizontalLayout.addWidget(self.magnifiyingGlassLabel, 0, Qt.AlignLeft)

        self.searchBar = QLineEdit(self.searchBarFrame)
        self.searchBar.setObjectName(u"searchBar")
        self.searchBar.setMinimumSize(QSize(400, 28))
        self.searchBar.setMaximumSize(QSize(600, 28))
        self.searchBar.setStyleSheet(u"QLineEdit{\n"
"   background-color: transparent;\n"
"   selection-background-color: #4C566A;\n"
"   font: 9pt \"JetBrains Mono\";\n"
"}")
        self.searchBar.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.searchBar)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addWidget(self.searchBarFrame)

        self.displayFrame = QFrame(self.mainFrame)
        self.displayFrame.setObjectName(u"displayFrame")
        self.displayFrame.setFrameShape(QFrame.StyledPanel)
        self.displayFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.displayFrame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(6, 6, 6, 6)
        self.clipsListWidget = QListWidget(self.displayFrame)
        self.clipsListWidget.setObjectName(u"clipsListWidget")
        self.clipsListWidget.setMaximumSize(QSize(16777215, 16777215))
        self.clipsListWidget.setStyleSheet(u"QListView::item:selected{\n"
"   font: 9pt \"JetBrains Mono\";\n"
"   background-color:  rgba(76, 86, 106, 125);\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.clipsListWidget)


        self.verticalLayout_2.addWidget(self.displayFrame)


        self.verticalLayout.addWidget(self.mainFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.magnifiyingGlassLabel.setText("")
        self.searchBar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search...", None))
    # retranslateUi

