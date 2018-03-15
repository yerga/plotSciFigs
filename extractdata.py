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
__date__ = "13/03/18"
__license__ = "GPLv3"
__program__ = "plotSciFigs"
__version__ = "0.0.1"

import os
import csv

class ExtractData:
    def __init__(self, plottype, filename, doubleaxis):
        filetype = self.get_filetype(filename)
        print(filetype)

        if filetype == ".csv":
            format = "CSV"
            csvfiles = CSVfiles(filename)
            print("getting CSV data")
            self.xdata, self.ydata, self.xdata2, self.ydata2 = csvfiles.get_data(plottype, doubleaxis)

    def get_data(self):
        return self.xdata, self.ydata, self.xdata2, self.ydata2


    def get_filetype(self, filename):
        name, extension = os.path.splitext(filename)
        return extension

class CSVfiles:
    def __init__(self, filename):
        self.datacsv = []
        #TODO: autodetect dots or commas
        dots = True
        if dots:
            self.dotsreplace1 = ''
            self.dotsreplace2 = ''
            self.dotsreplace3 = ','
        else:
            self.dotsreplace1 = ','
            self.dotsreplace2 = '.'
            self.dotsreplace3 = '.'

        # Open and read CSV file
        textfile = open(filename)
        reader = csv.reader(textfile, delimiter=';')
        for row in reader:
            self.datacsv.append(row)
        textfile.close()

        print ("datacsv: ", self.datacsv)
        self.numrows = len(self.datacsv)
        self.numcolumns = len(self.datacsv[1])
        self.xdata = []
        self.ydata = []
        self.xdata2 = []
        self.ydata2 = []

    def get_data(self, plottype, doubleaxis):

        plotlines = ["LinePlot"]

        if plottype in plotlines:
            self.getXYDataColumns(doubleaxis)

        return self.xdata, self.ydata, self.xdata2, self.ydata2

    def getXYDataColumns(self, doubleaxis):
        #col1: X, col2: Y; col3: X; col4: Y...
        #col1: X1; col2: Y1; col3: X2, col4: Y2...

        xdata = []
        ydata = []
        xdata = []
        ydata = []

        print("num columns: ", self.numcolumns)

        print("doubleaxis: ", doubleaxis)
        if doubleaxis:
            for i in range(0, self.numcolumns, 4):
                # FIXME: 2 plots ydata1, 1 plot ydata2
                print("getting data from column: ", i)
                xdata1 = self.get_column_data(i)
                ydata1 = self.get_column_data(i+1)
                self.xdata.append(xdata1)
                self.ydata.append(ydata1)
                if i+3 < self.numcolumns:
                    xdataB = self.get_column_data(i+2)
                    ydataB = self.get_column_data(i+3)
                    self.xdata2.append(xdataB)
                    self.ydata2.append(ydataB)
        else:
            for i in range(0, self.numcolumns, 2):
                print("getting data from column: ", i)
                xdata1 = self.get_column_data(i)
                self.xdata.append(xdata1)
                ydata1 = self.get_column_data(i + 1)
                self.ydata.append(ydata1)


    def get_column_data(self, numcol):
        datatotal = []
        print("numrows: ", self.numrows)
        for i in range(2, self.numrows - 1):
            #print("numrow: ", i)
            data = self.datacsv[i][numcol].replace(self.dotsreplace3, '').replace(self.dotsreplace1, self.dotsreplace2)
            if data != '':
                data = float(data)
                datatotal.append(data)
        return datatotal

