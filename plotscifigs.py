#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Short description of this Python module.
Longer description of this module.

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.
This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
"""

__author__ = "Daniel Martin-Yerga"
__email__ = "dyerga@gmail.com"
__copyright__ = "Copyright 2018"
__date__ = "13 / 03 / 18"
__license__ = "GPLv3"
__version__ = "0.1"

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog
from ui_mainwindow import Ui_MainWindow
from ui_tabplotwidget import Ui_tabPlotWidget
from plotting import Plotting

class MainWindow (QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setupMainWindow()

    def setupMainWindow(self):
        self.tabWidget = self.ui.tabWidget
        self.tabConfig = self.ui.tabConfig
        self.tabplot1 = self.ui.tabPlot1
        self.tabplot2 = self.ui.tabPlot2
        self.tabplot3 = self.ui.tabPlot3
        self.tabplot4 = self.ui.tabPlot4


        self.tabplots = [self.tabplot1, self.tabplot2, self.tabplot3, self.tabplot4]
        self.tabtexts = []
        for i in range(1, 5):
            self.tabtexts.append(self.tabWidget.tabText(i))

        self.tabplotwidgets = []
        for tabplot in self.tabplots:
            newwidget = TabPlotWidget()
            self.tabplotwidgets.append(newwidget)
            tabplot.layout().addWidget(newwidget)

        self.tabplotting = self.ui.tabPlotting
        self.nextbutton = self.ui.nextButton
        self.nextbutton.clicked.connect(self.onNextButtonClicked)
        self.settingsButton = self.ui.settingsButton

        self.nplotspin = self.ui.nplotsSpin
        self.nplotspin.valueChanged.connect(self.nplotsChanged)
        self.nplots = int(self.nplotspin.value())

        self.combostyle = self.ui.comboStyle

        self.verticalRBtn = self.ui.verticalRBtn
        self.verticalRBtn.toggled.connect(self.aspectToggled)
        self.singleRBtn = self.ui.singleRBtn
        self.singleRBtn.toggled.connect(self.aspectToggled)

        self.plotbutton = self.ui.plotButton
        self.plotbutton.clicked.connect(self.plotFigure)

    def aspectToggled(self):
        #TODO: improve behaviour, show msg, if verticalplot -> single: True
        if self.verticalRBtn.isChecked():
            self.singleRBtn.setChecked(True)


    def onNextButtonClicked(self):
        index = self.tabWidget.currentIndex()
        numtabs = self.tabWidget.count()
        print(index, numtabs)
        if index < numtabs-1:
            self.tabWidget.setCurrentIndex(index+1)

    def nplotsChanged(self):
        newvalue = self.nplotspin.value()
        if self.nplots > newvalue:
            self.tabWidget.removeTab(self.nplots)
        else:
            tabtext = self.tabtexts[newvalue-1]
            newtab = self.tabplots[newvalue-1]
            self.tabWidget.insertTab(newvalue, newtab, tabtext)

        self.nplots = newvalue


    def plotFigure(self):
        config = self.getConfig()
        plotsconfig = self.getPlotsConfig()

        print("plotsconfig: ", plotsconfig)

        plotting = Plotting(config, plotsconfig)

    def getConfig(self):
        self.plotstyle = self.combostyle.currentText()

        self.singlecolumn = self.singleRBtn.isChecked()
        self.verticalplot = self.verticalRBtn.isChecked()

        return self.nplots, self.singlecolumn, self.verticalplot, self.plotstyle

    def getPlotsConfig(self):
        plotsconfig = []
        for i in range(self.nplots):
            widget = self.tabplotwidgets[i]
            widgetdata = widget.getData()
            plotsconfig.append(widgetdata)

        return plotsconfig


class TabPlotWidget (QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.ui = Ui_tabPlotWidget()
        self.ui.setupUi(self)
        self.setupTabPlotWidget()

    def setupTabPlotWidget(self):
        self.browseBtn = self.ui.browseBtn
        self.browseBtn.clicked.connect(self.browseDialog)

        self.filenameBox = self.ui.filenameBox
        self.typecombo = self.ui.comboType

        self.doubleaxisCB = self.ui.doubleCB

        self.xlabel1line = self.ui.xlabel1line
        self.ylabel1line = self.ui.ylabel1line
        self.ylabel2line = self.ui.ylabel2line
        self.legendsline = self.ui.legendline
        self.xlimitline = self.ui.xlimitline
        self.y1limitlne = self.ui.y1limitline
        self.y2limitline = self.ui.y2limitline

        self.legend1CB = self.ui.legend1CB
        self.legend2CB = self.ui.legend2CB

        self.xaxislocator = self.ui.xaxislocator
        self.y1axislocator = self.ui.y1axislocator
        self.y2axislocator = self.ui.y2axislocator

        self.convertyline = self.ui.convertYline
        self.converty2line = self.ui.convertY2line


    def browseDialog(self):
        filename, filter = QFileDialog.getOpenFileName(self, 'Select file')
        if filename:
            self.filenameBox.setText(filename)

    def getData(self):
        plottype = self.typecombo.currentText()
        filename = self.filenameBox.text()
        xlabel1 = self.xlabel1line.text()
        ylabel1 = self.ylabel1line.text()
        ylabel2 = self.ylabel2line.text()
        xlimit = self.xlimitline.text()
        y1limit = self.y1limitlne.text()
        y2limit = self.y2limitline.text()
        legends = self.legendsline.text()
        doubleaxis = self.doubleaxisCB.isChecked()
        legend1loc = self.legend1CB.currentText()
        legend2loc = self.legend2CB.currentText()
        xaxislocator = self.xaxislocator.text()
        y1axislocator = self.y1axislocator.text()
        y2axislocator = self.y2axislocator.text()
        converty = self.convertyline.text()
        converty2 = self.converty2line.text()

        return plottype, filename, xlabel1, ylabel1, ylabel2, legends, xlimit, y1limit, y2limit, \
               doubleaxis, legend1loc, legend2loc, xaxislocator, y1axislocator, y2axislocator, converty, converty2

if __name__ == "__main__":

    #QApplication.setDesktopSettingsAware(False)
    app = QApplication(sys.argv)
    app.setApplicationName("plotSciFigs")
    app.setApplicationVersion("0.1")

    appname = "org.dyerga.plotscifigs"

    window = MainWindow()
    window.setWindowTitle("plotSciFigs")
    window.show()

    sys.exit(app.exec_())