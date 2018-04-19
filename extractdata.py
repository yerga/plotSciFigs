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
__license__ = "GPLv3"
__program__ = "plotSciFigs"
__version__ = "0.0.1"

import os
import csv
import pandas as pd
import numpy as np

class ExtractData:
    def __init__(self, plottype, filename, doubleaxis, desvest):
        filetype = self.get_filetype(filename)
        print(filetype)

        if filetype == ".csv":
            format = "CSV"
            csvfiles = CSVfiles(filename)
            print("getting CSV data")
            self.xdata, self.ydata, self.xdata2, self.ydata2 = csvfiles.get_data(plottype, doubleaxis, desvest)
        elif filetype == ".xlsx" or filetype == ".xls":
            format = "Excel"
            excelfiles = EXCELfiles(filename)
            # self.xdata2 = desvstd
            self.xdata, self.ydata, self.xdata2, self.ydata2 = excelfiles.get_data()

    def get_data(self):
        return self.xdata, self.ydata, self.xdata2, self.ydata2

    def get_filetype(self, filename):
        name, extension = os.path.splitext(filename)
        return extension

class EXCELfiles:
    def __init__(self, filename):
        excelfile = pd.ExcelFile(filename)
        csvrows1 = excelfile.parse()
        self.csvrows = csvrows1.get_values()
        self.numrows = len(self.csvrows)
        self.numcolumns = len(self.csvrows[0])

        self.xdata = []
        self.ydata = []
        self.xdata2 = []
        self.ydata2 = []

    def get_data(self):
        # TODO: option for multiple calplots
        xdata = [item[0] for item in self.csvrows]
        self.xdata.append(xdata)


        medias = []
        desvstds = []
        for i in range(self.numrows):
            items = self.csvrows[i][1:self.numcolumns]
            media1 = np.nanmean(items)
            desvstd1 = np.nanstd(items)
            medias.append(media1)
            desvstds.append(desvstd1)

        self.ydata.append(medias)
        self.xdata2.append(desvstds)

        return self.xdata, self.ydata, self.xdata2, self.ydata2

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

    def get_data(self, plottype, doubleaxis, desvest):
        if plottype == "LinePlot":
            self.getXYDataColumns(doubleaxis)
        elif plottype == "DotPlot":
            self.getXYDotPlot(doubleaxis, desvest)

        return self.xdata, self.ydata, self.xdata2, self.ydata2

    def getXYDataColumns(self, doubleaxis):
        #col1: X, col2: Y; col3: X; col4: Y...
        #col1: X1; col2: Y1; col3: X2, col4: Y2...

        if doubleaxis:
            for i in range(0, self.numcolumns, 4):
                # FIXME: 2 plots ydata1, 1 plot ydata2, other options, etc
                print("getting data from column: ", i)
                self.xdata.append(self.get_column_data(i))
                self.ydata.append(self.get_column_data(i+1))
                if i+3 < self.numcolumns:
                    self.xdata2.append(self.get_column_data(i+2))
                    self.ydata2.append(self.get_column_data(i+3))
        else:
            for i in range(0, self.numcolumns, 2):
                print("getting data from column: ", i)
                self.xdata.append(self.get_column_data(i))
                self.ydata.append(self.get_column_data(i + 1))

    def getXYDotPlot(self, doubleaxis, desvest):
        if desvest:
            column_step = 3
        else:
            column_step = 2

        for i in range(0, self.numcolumns, column_step):
            print("getting data from column: ", i)
            self.xdata.append(self.get_column_data(i))
            self.ydata.append(self.get_column_data(i + 1))
            if desvest:
                self.xdata2.append(self.get_column_data(i + 2))

    def get_column_data(self, numcol):
        datatotal = []
        print("numrows: ", self.numrows)
        for i in range(2, self.numrows):
            #print("numrow: ", i)
            print ("numcol: ", numcol)
            print("sdatacsv: ", self.datacsv[i])
            data = self.datacsv[i][numcol].replace(self.dotsreplace3, '').replace(self.dotsreplace1, self.dotsreplace2)
            if data != '':
                data = float(data)
                datatotal.append(data)
        return datatotal

