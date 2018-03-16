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

from colors import default_color_cycler as dcc
from matplotlib.ticker import MultipleLocator
from scipy import stats
import numpy as np

class CalPlot():
    def __init__(self, plotconfig):
        self.plottype, self.filename, self.xlabel1, self.ylabel1, self.ylabel2, self.legends, \
            self.xlimit, self.y1limit, self.y2limit, self.doubleaxis, self.legend1loc, self.legend2loc, \
            self.xaxislocator, self.y1axislocator, self.y2axislocator, self.converty, self.converty2, \
            self.normalized = plotconfig

    def plot(self, axis, plotdata):
        xdata1, ydata1, xdata2, ydata2 = plotdata

        if self.doubleaxis:
            if self.legends:
                legend1, legend2 = self.legends.split(";;")
                legend1 = legend1.split(";")
                legend2 = legend2.split(";")
            else:
                legend1 = [""]*len(xdata1)
                legend2 = [""]*len(xdata2)
        else:
            if self.legends:
                legend1 = self.legends.split(";")
            else:
                legend1 = [""]*len(xdata1)

        for i in range(len(ydata1)):
            scplot = axis.scatter(xdata1[0], ydata1[i])
            axis.errorbar(xdata1[0], ydata1[i], yerr=xdata2[i], fmt='o', ecolor='r', capsize=2, color='k')
            slope1, intercept1, r_value1, p_value1, std_err1 = stats.linregress(xdata1[0], ydata1[i])
            newx = np.linspace(xdata1[i][0], xdata1[i][len(xdata1[i]) - 1], 100)
            line1 = slope1 * np.array(newx) + intercept1
            axis.plot(newx, line1, ':')

        self.set_format(axis)

        # TODO: plot colors, plot style (dots, etc.)

        # if self.doubleaxis:
        #     axis2 = axis.twinx()
        #     for i in range(len(xdata2)):
        #         line2, = axis2.plot(xdata2[i], ydata2[i], lineformat, color=dcc._left[i+len(xdata1)]['color'], label=legend2[i])
        #
        #     self.set_format_double(axis2)

            # color=dcc._left[1]['color'], ls="-", label=legends[i+1])

    def set_format(self, axis):
        axis.set_xlabel(self.xlabel1)
        axis.set_ylabel(self.ylabel1)
        if self.xlimit:
            xlim1, xlim2 = self.xlimit.split(";")
            axis.set_xlim(float(xlim1), float(xlim2))
        if self.y1limit:
            ylim1, ylim2 = self.y1limit.split(";")
            axis.set_ylim(float(ylim1), float(ylim2))

        leg = axis.legend(loc=self.legend1loc, shadow=False)

        if self.xaxislocator:
            yml = MultipleLocator(float(self.xaxislocator))
            axis.xaxis.set_major_locator(yml)

        if self.y1axislocator:
            yml = MultipleLocator(float(self.y1axislocator))
            axis.yaxis.set_major_locator(yml)

            # if color:
            #     axis.set_ylabel("Abs / a.u.", color=dcc._left[0]['color'])
            #     axis.tick_params('y', colors=dcc._left[0]['color'])

            #TODO: minor locator
            #     minx = MultipleLocator(0.25)
            #     axis.xaxis.set_minor_locator(minx)

    def set_format_double(self, axis):
        axis.set_ylabel(self.ylabel2)
        axis.legend(loc=self.legend2loc, shadow=False)

        if self.y2limit:
            ylim1, ylim2 = self.y2limit.split(";")
            axis.set_ylim(float(ylim1), float(ylim2))

        if self.y2axislocator:
            yml = MultipleLocator(float(self.y2axislocator))
            axis.yaxis.set_major_locator(yml)

        #TODO: colors, annotations, etc.

        # TODO: minor locator
        #     minx = MultipleLocator(0.25)
        #     axis.xaxis.set_minor_locator(minx)

        #self.ax2.set_ylabel('Intensity / kcounts', color=dcc._left[1]['color'])
        #self.ax2.tick_params('y', colors='r')


        #plt.gcf().text(0.02, 0.98, "a)", fontsize=11, fontweight="bold")
        #plt.gcf().text(0.02, 0.5, "b)", fontsize=11, fontweight="bold")
