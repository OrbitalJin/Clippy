# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfacekgUhwq.ui'
##
## Created by: Qt User Interface Compiler version 5.15.5
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore

import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(480, 230)
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
"   color: grey;\n"
"}\n"
"\n"
"QFrame{\n"
"\n"
"}\n"
"\n"
"/*Frames*/\n"
"#mainFrame{\n"
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
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.searchBarFrame = QFrame(self.mainFrame)
        self.searchBarFrame.setObjectName(u"searchBarFrame")
        self.searchBarFrame.setMaximumSize(QSize(16777215, 50))
        self.searchBarFrame.setStyleSheet(u"")
        self.searchBarFrame.setFrameShape(QFrame.StyledPanel)
        self.searchBarFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.searchBarFrame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.searchBar = QLineEdit(self.searchBarFrame)
        self.searchBar.setObjectName(u"searchBar")
        self.searchBar.setMinimumSize(QSize(283, 28))
        self.searchBar.setMaximumSize(QSize(283, 28))
        self.searchBar.setStyleSheet(u"")
        self.searchBar.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.searchBar)


        self.verticalLayout_2.addWidget(self.searchBarFrame)

        self.displayFrame = QFrame(self.mainFrame)
        self.displayFrame.setObjectName(u"displayFrame")
        self.displayFrame.setFrameShape(QFrame.StyledPanel)
        self.displayFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.displayFrame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.clipsListWidget = QListWidget(self.displayFrame)
        QListWidgetItem(self.clipsListWidget)
        QListWidgetItem(self.clipsListWidget)
        QListWidgetItem(self.clipsListWidget)
        self.clipsListWidget.setObjectName(u"clipsListWidget")
        self.clipsListWidget.setMaximumSize(QSize(320, 16777215))
        self.clipsListWidget.setStyleSheet(u"QListWidget{\n"
"\n"
"border-right:  1px solid 4F576C;\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"background-color:  #495366;\n"
"}")

        self.horizontalLayout_3.addWidget(self.clipsListWidget)

        self.verticalSeparator = QFrame(self.displayFrame)
        self.verticalSeparator.setObjectName(u"verticalSeparator")
        self.verticalSeparator.setStyleSheet(u"")
        self.verticalSeparator.setFrameShape(QFrame.VLine)
        self.verticalSeparator.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.verticalSeparator)

        self.shortcutsFrame = QFrame(self.displayFrame)
        self.shortcutsFrame.setObjectName(u"shortcutsFrame")
        self.shortcutsFrame.setStyleSheet(u"")
        self.shortcutsFrame.setFrameShape(QFrame.StyledPanel)
        self.shortcutsFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.shortcutsFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.shortcutTitleLabel = QLabel(self.shortcutsFrame)
        self.shortcutTitleLabel.setObjectName(u"shortcutTitleLabel")
        self.shortcutTitleLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.shortcutTitleLabel)

        self.shortcutLabel1 = QLabel(self.shortcutsFrame)
        self.shortcutLabel1.setObjectName(u"shortcutLabel1")
        self.shortcutLabel1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.shortcutLabel1)

        self.shortcutLabel2 = QLabel(self.shortcutsFrame)
        self.shortcutLabel2.setObjectName(u"shortcutLabel2")
        self.shortcutLabel2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.shortcutLabel2)

        self.shortcutLabel3 = QLabel(self.shortcutsFrame)
        self.shortcutLabel3.setObjectName(u"shortcutLabel3")
        self.shortcutLabel3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.shortcutLabel3)

        self.shortcutLabel4 = QLabel(self.shortcutsFrame)
        self.shortcutLabel4.setObjectName(u"shortcutLabel4")
        self.shortcutLabel4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.shortcutLabel4)


        self.horizontalLayout_3.addWidget(self.shortcutsFrame)


        self.verticalLayout_2.addWidget(self.displayFrame)

        self.bottomFrame = QFrame(self.mainFrame)
        self.bottomFrame.setObjectName(u"bottomFrame")
        self.bottomFrame.setMinimumSize(QSize(25, 25))
        self.bottomFrame.setMaximumSize(QSize(1000000, 25))
        self.bottomFrame.setStyleSheet(u"")
        self.bottomFrame.setFrameShape(QFrame.StyledPanel)
        self.bottomFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.bottomFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.statusLabel = QLabel(self.bottomFrame)
        self.statusLabel.setObjectName(u"statusLabel")
        self.statusLabel.setStyleSheet(u"border: none;")

        self.horizontalLayout_2.addWidget(self.statusLabel)

        self.settingsBtn = QPushButton(self.bottomFrame)
        self.settingsBtn.setObjectName(u"settingsBtn")
        self.settingsBtn.setMinimumSize(QSize(20, 20))
        self.settingsBtn.setMaximumSize(QSize(20, 20))
        self.settingsBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.settingsBtn)


        self.verticalLayout_2.addWidget(self.bottomFrame)


        self.verticalLayout.addWidget(self.mainFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.searchBar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Clipboard History Filter", None))

        __sortingEnabled = self.clipsListWidget.isSortingEnabled()
        self.clipsListWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.clipsListWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"yo this is a test yo", None));
        ___qlistwidgetitem1 = self.clipsListWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"yo this is a test yosdf;lkjdsfkjsd", None));
        ___qlistwidgetitem2 = self.clipsListWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"sdfsdflkj kl112214234", None));
        self.clipsListWidget.setSortingEnabled(__sortingEnabled)

        self.shortcutTitleLabel.setText(QCoreApplication.translate("MainWindow", u"Shortcuts:", None))
        self.shortcutLabel1.setText(QCoreApplication.translate("MainWindow", u"Clear: ctrl+alt+c", None))
        self.shortcutLabel2.setText(QCoreApplication.translate("MainWindow", u"Clear: ctrl+alt+c", None))
        self.shortcutLabel3.setText(QCoreApplication.translate("MainWindow", u"Clear: ctrl+alt+c", None))
        self.shortcutLabel4.setText(QCoreApplication.translate("MainWindow", u"Clear: ctrl+alt+c", None))
        self.statusLabel.setText(QCoreApplication.translate("MainWindow", u"ClipPy v.0.1", None))
        self.settingsBtn.setText("")
    # retranslateUi

