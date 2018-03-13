# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setMinimumSize(QtCore.QSize(0, 50))
        self.backButton.setObjectName("backButton")
        self.horizontalLayout.addWidget(self.backButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.settingsButton = QtWidgets.QPushButton(self.centralwidget)
        self.settingsButton.setMinimumSize(QtCore.QSize(0, 50))
        self.settingsButton.setObjectName("settingsButton")
        self.horizontalLayout.addWidget(self.settingsButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextButton.setMinimumSize(QtCore.QSize(0, 50))
        self.nextButton.setObjectName("nextButton")
        self.horizontalLayout.addWidget(self.nextButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 2, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tabConfig = QtWidgets.QWidget()
        self.tabConfig.setObjectName("tabConfig")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tabConfig)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.tabConfig)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalRBtn = QtWidgets.QRadioButton(self.groupBox)
        self.verticalRBtn.setChecked(True)
        self.verticalRBtn.setObjectName("verticalRBtn")
        self.horizontalLayout_4.addWidget(self.verticalRBtn)
        self.horizontalRBtn = QtWidgets.QRadioButton(self.groupBox)
        self.horizontalRBtn.setChecked(False)
        self.horizontalRBtn.setObjectName("horizontalRBtn")
        self.horizontalLayout_4.addWidget(self.horizontalRBtn)
        self.gridLayout_3.addWidget(self.groupBox, 2, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 2, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.tabConfig)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.nplotsSpin = QtWidgets.QSpinBox(self.tabConfig)
        self.nplotsSpin.setMinimum(1)
        self.nplotsSpin.setMaximum(4)
        self.nplotsSpin.setProperty("value", 4)
        self.nplotsSpin.setObjectName("nplotsSpin")
        self.horizontalLayout_3.addWidget(self.nplotsSpin)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_2.addItem(spacerItem3, 5, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.tabConfig)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.comboStyle = QtWidgets.QComboBox(self.tabConfig)
        self.comboStyle.setMinimumSize(QtCore.QSize(400, 50))
        self.comboStyle.setObjectName("comboStyle")
        self.comboStyle.addItem("")
        self.comboStyle.addItem("")
        self.comboStyle.addItem("")
        self.comboStyle.addItem("")
        self.comboStyle.addItem("")
        self.comboStyle.addItem("")
        self.horizontalLayout_2.addWidget(self.comboStyle)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 4, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_2.addItem(spacerItem4, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tabConfig)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_5.setContentsMargins(-1, 9, -1, -1)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.singleRBtn = QtWidgets.QRadioButton(self.groupBox_2)
        self.singleRBtn.setChecked(True)
        self.singleRBtn.setObjectName("singleRBtn")
        self.horizontalLayout_5.addWidget(self.singleRBtn)
        self.multipleRBtn = QtWidgets.QRadioButton(self.groupBox_2)
        self.multipleRBtn.setObjectName("multipleRBtn")
        self.horizontalLayout_5.addWidget(self.multipleRBtn)
        self.gridLayout_2.addWidget(self.groupBox_2, 3, 0, 1, 1)
        self.tabWidget.addTab(self.tabConfig, "")
        self.tabPlot1 = QtWidgets.QWidget()
        self.tabPlot1.setObjectName("tabPlot1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tabPlot1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.tabPlot1)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.tabWidget.addTab(self.tabPlot1, "")
        self.tabPlot2 = QtWidgets.QWidget()
        self.tabPlot2.setObjectName("tabPlot2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tabPlot2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.tabPlot2)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.tabWidget.addTab(self.tabPlot2, "")
        self.tabPlot3 = QtWidgets.QWidget()
        self.tabPlot3.setObjectName("tabPlot3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tabPlot3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.tabPlot3)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.tabWidget.addTab(self.tabPlot3, "")
        self.tabPlot4 = QtWidgets.QWidget()
        self.tabPlot4.setObjectName("tabPlot4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tabPlot4)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.tabPlot4)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_5.addWidget(self.label_6)
        self.tabWidget.addTab(self.tabPlot4, "")
        self.tabPlotting = QtWidgets.QWidget()
        self.tabPlotting.setObjectName("tabPlotting")
        self.plotButton = QtWidgets.QPushButton(self.tabPlotting)
        self.plotButton.setGeometry(QtCore.QRect(260, 170, 201, 91))
        self.plotButton.setObjectName("plotButton")
        self.tabWidget.addTab(self.tabPlotting, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionQuit)
        self.menuAbout.addAction(self.actionHelp)
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.backButton.setText(_translate("MainWindow", "Back"))
        self.settingsButton.setText(_translate("MainWindow", "Settings"))
        self.nextButton.setText(_translate("MainWindow", "Next"))
        self.groupBox.setTitle(_translate("MainWindow", "Aspect"))
        self.verticalRBtn.setText(_translate("MainWindow", "Vertical figure"))
        self.horizontalRBtn.setText(_translate("MainWindow", "Horizontal figure"))
        self.label_2.setText(_translate("MainWindow", "Number of plots"))
        self.label.setText(_translate("MainWindow", "Style"))
        self.comboStyle.setItemText(0, _translate("MainWindow", "ACS"))
        self.comboStyle.setItemText(1, _translate("MainWindow", "RSC"))
        self.comboStyle.setItemText(2, _translate("MainWindow", "Elsevier"))
        self.comboStyle.setItemText(3, _translate("MainWindow", "Wiley"))
        self.comboStyle.setItemText(4, _translate("MainWindow", "Web"))
        self.comboStyle.setItemText(5, _translate("MainWindow", "Presentation"))
        self.singleRBtn.setText(_translate("MainWindow", "Single column"))
        self.multipleRBtn.setText(_translate("MainWindow", "Multiple column"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabConfig), _translate("MainWindow", "Config"))
        self.label_3.setText(_translate("MainWindow", "plot1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabPlot1), _translate("MainWindow", "Plot1"))
        self.label_4.setText(_translate("MainWindow", "plot2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabPlot2), _translate("MainWindow", "Plot2"))
        self.label_5.setText(_translate("MainWindow", "plot3"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabPlot3), _translate("MainWindow", "Plot3"))
        self.label_6.setText(_translate("MainWindow", "plot4"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabPlot4), _translate("MainWindow", "Plot4"))
        self.plotButton.setText(_translate("MainWindow", "Plot Figure"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabPlotting), _translate("MainWindow", "Options"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionAbout.setText(_translate("MainWindow", "About plotSciFigs"))
        self.actionAbout.setToolTip(_translate("MainWindow", "About plotSciFigs"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
